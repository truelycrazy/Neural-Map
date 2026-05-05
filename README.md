# Neural Map: Dynamic Visualization

This project turns a standard Excel spreadsheet into an interactive, high-tech **Cybersecurity Neural Tree**. It creates a visual "map" of departments,
attack path representation, work tracker etc. Featuring a dark "cyber" theme with glowing nodes and smooth animations.


## Main Features

 **Auto-Builds from Excel**: Just update `Department_Map.xlsx` and the tree updates itself.
 **Neural Look**: The map has a dark background with moving particles and hexagonal nodes that pulse when you click them.
 **Interactive Info**: 
    *   **Left-Click**: Expand or collapse different branches.
    *   **Right-Click**: Opens a card with specific notes and direct links to SharePoint or other sites.
 **Search**: A search bar at the top lets you jump straight to any department, even if it’s currently hidden.

---

## File List

  **`Department_Map.xlsx`**: The main data file where you list names, parents, notes, and links.
  **`tree_generator.py`**: The script that reads your Excel file and builds the map.
  **`template.html`**: The design file that tells the map how to look and behave.
  **`Dashboard.html`**: The final result you open in your browser. **Note: This file is created only after you run the update script for the first time**.
  **`RUN_UPDATE.bat`**: A quick shortcut for Windows users to refresh the map.

---

## How to Use It

1.  **Fill the Excel**: Open `Department_Map.xlsx` and add your data.
2.  **Install Python tools**: You'll need these libraries:

   bash
    ```
  pip install pandas openpyxl jinja2
    ```

    
3.  **Update the Map**: **You must run the update script the first time to generate your `Dashboard.html` file**.
      Every time you modify/update the exccel file you run **RUN_UPDATE.bat/update.sh** after it to update the dashboard.
    *   **Windows**: Double-click `RUN_UPDATE.bat`.
    *   **Linux**: Create a file named `update.sh`, paste the content below, and run it:
  
  bash      
```
        #!/bin/bash
        echo "Updating Cybersecurity Neural Tree..."
        python3 tree_generator.py
```

4.  **Open**: Double-click the newly created `Dashboard.html` to see your map.



## Built With
*   **Backend**: Python (Pandas & Jinja2).
*   **Frontend**: HTML5, CSS3, and D3.js.
```
