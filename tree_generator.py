import pandas as pd
import json
import os
from jinja2 import Template

EXCEL_FILE = 'Department_Map.xlsx'
TEMPLATE_FILE = 'template.html'
OUTPUT_FILE = 'Dashboard.html'

def generate_tree():
    if not os.path.exists(EXCEL_FILE):
        print(f"Error: {EXCEL_FILE} not found.")
        return

    df = pd.read_excel(EXCEL_FILE)
    df = df.fillna('')

    df['Name'] = df['Name'].astype(str).str.strip()
    df['Parent'] = df['Parent'].astype(str).str.strip()

    def build_node(name, depth=0):
        node_row = df[df['Name'] == name]
        notes = node_row['Notes'].values[0] if not node_row.empty else ""
        link  = node_row['Link'].values[0]  if not node_row.empty and 'Link' in df.columns else ""

        # Fix: handle both literal \n and real newlines
        notes_str = str(notes).replace('\\n', '\n')
        formatted_notes = [line.strip() for line in notes_str.split('\n') if line.strip()]

        # Clean link — treat NaN / 'nan' / whitespace as empty
        link_str = str(link).strip() if link and str(link).strip().lower() not in ('nan','none','') else ""

        node = {
            "id": f"{name}__{depth}",   # Fix: unique key prevents D3 duplicate-name bug
            "name": name,
            "notes": formatted_notes,
            "link": link_str,
            "children": []
        }

        children_names = df[df['Parent'] == name]['Name'].tolist()
        for child_name in children_names:
            node['children'].append(build_node(child_name, depth + 1))

        return node

    root_node_name = df[df['Parent'] == '']['Name'].values[0]
    tree_data = build_node(root_node_name)

    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: {TEMPLATE_FILE} not found.")
        return

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template_html = f.read()

    template = Template(template_html)
    rendered_html = template.render(data=json.dumps(tree_data))

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_tree()
