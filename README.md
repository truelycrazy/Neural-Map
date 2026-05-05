# Neural Map: Dynamic Visualization

This project turns a standard Excel spreadsheet into an interactive, high-tech **Cybersecurity Neural Tree**. It creates a visual "map" of departments,
attack path representation, work tracker etc. Featuring a dark "cyber" theme with glowing nodes and smooth animations.


## Main Features

 **Auto-Builds from Excel**: Just update `ANY_Excel_File.xlsx` and the tree updates itself.
 **Neural Look**: The map has a dark background with moving particles and hexagonal nodes that pulse when you click them.
 **Interactive Info**: 
    *   **Left-Click**: Expand or collapse different branches.
    *   **Right-Click**: Opens a card with specific notes and direct links to SharePoint(*SEE EDITS*) or other sites.
 **Search**: A search bar at the top lets you jump straight to any department, even if it’s currently hidden.

---

## How to Use It

1.  **Fill the Excel**: Open `ANY_Excel_File.xlsx` and add your data.Excel file can be named anything to maintain multiple files
  as per requirement with different names for different maps. The column names are to be maintained the same and there must be only 1 file in tool folder 
  to be created dashboard on.
2.  **Install Python tools**: You'll need these libraries:

   bash
    ```
  pip install pandas openpyxl jinja2
    ```

    
3.  **Update the Map**: **You must run the update script the first time to generate your `Dashboard.html` file**.
      Every time you modify/update the exccel file you run **RUN_UPDATE.bat/update.sh** after it to update the dashboard.
    *   **Windows**: Run `RUN_UPDATE_windowuse.bat`.
    *   **Linux**: Run `Update_linuxuse.sh`.
  
**Note**
**RUN** 
`chmod +x Update_linuxuse.sh` *(To provide permission to shell file to run)*     
Now you can freely use Update(linuxuse).sh file 


4.  **Open**: Double-click the newly created `Dashboard.html` to see your map.

## EDITS
  ** Direct Link Button**: Direct link button can be edited and changed to anything else too as per use in overall map. Follow the instructions below to do so:

  In the **template.html** file, between lines 160 to 170 you will onserve the below given line:

  ```
    <a id="note-sp-btn" target="_blank" rel="noopener noreferrer">SHAREPOINT ↗</a>
```
The "SHAREPOINT" can be changed to the required name of button.

## File List

  **`ANY_Excel_File.xlsx`**: The main data file where you list names, parents, notes, and links. Excel file can be named anything to maintain multiple files
  as per requirement with different names for different maps. The column names are to be maintained the same and there must be only 1 file in tool folder 
  to be created dashboard on.
  **`tree_generator.py`**: The script that reads your Excel file and builds the map.
  **`template.html`**: The design file that tells the map how to look and behave.
  **`Dashboard.html`**: The final result you open in your browser. **Note: This file is created only after you run the update script for the first time**.
  **`UPDATE_windowuse.bat`**: A quick shortcut for Windows users to refresh the map.
  **`UPDATE_linuxuse.sh`**: A quick shortcut for Linux users to refresh the map.

---

## Built With
*   **Backend**: Python (Pandas & Jinja2).
*   **Frontend**: HTML5, CSS3, and D3.js.
```
