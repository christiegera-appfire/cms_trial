# Set up the Advanced Table Viewer macro features

The Advanced Table Viewer macro setup mode enables you to configure macro features. It is a full-screen view to provide data visibility and a smoother configuration experience of data source and table display options.

- The macro provides column filtering, row styling, column drag-and-drop, column grouping, search, row numbering, sorting, pagination, download, rename heading, and column and group calculation. You can configure these features and access them in both Confluence page view and edit mode.
- The macro enables the search and sort feature by default when you insert it for the first time.
- Pagination turns on automatically if the table has more than 10 rows, displaying 10 rows per page by default.
- The features configured in macro setup mode are saved as the default for every refresh of the Confluence page.

[Unmapped macro: refined-tab — no content to fall back on]

To configure the features, navigate to the macro’s setup mode. Only users with edit permissions can access it.

- When you insert and configure the Advanced Table Viewer macro, you will navigate to the setup mode before saving the macro.
- To know about the various terms and modes used in the macro, refer to the [Advanced Table Viewer macro glossary](/cms_trial/space/TBL/1765245023/Advanced+Table+Viewer+macro+glossary/).

1. Open the Confluence page containing the Advanced Table Viewer macro.
2. Edit the Confluence page.
3. Edit the Advanced Table Viewer macro to open the setup mode.

![Advanced Tables Advanced Table Viewer macro edit screen](/cms_trial/assets/23396cb4-d722-4fc1-87cc-f6c793eba31d.jpg)

1. The macro setup mode opens in full-screen view.

   - The left panel displays a preview of the data imported from the data source.
   - The right panel displays the available feature configurations.
   - To enable or disable a feature, click the specific icon.![Advanced Tables Advanced Table Viewer macro setup screen](/cms_trial/assets/44eaa434-916a-4d7c-929a-dd662ced93b4.jpg)
2. The feature configurations are available at the table and column level. Refer to the Table and column properties section.

To configure the Advanced Table Viewer macro for CSV and Excel data sources, refer to:

- [Configure CSV data source in Advanced Table Viewer macro](/cms_trial/space/TBL/1782972884/Configure+CSV+data+source+in+Advanced+Table+Viewer+macro/)
- [Configure Excel data source in Advanced Table Viewer macro](/cms_trial/space/TBL/3122888898/Configure+Excel+data+source+in+Advanced+Table+Viewer+macro/)

[Unmapped macro: refined-tab — no content to fall back on]

- The right panel toolbar displays the available feature configuration at the table level.
- The table properties apply to the entire table, affecting all columns and rows within a single macro.
- In the right panel, you can enable or disable the macro table features.

| **Table properties** | **Description** | **Default value** | **Read more** |
| --- | --- | --- | --- |
| Column filtering  (▢ ) | Configure column filters for individual columns and filter table data based on specific column values. | OFF | [Filter columns with Advanced Table Viewer macro](/cms_trial/space/TBL/2001437596/Filter+columns+with+Advanced+Table+Viewer+macro/) |
| Row styling  (▢ ) | Apply row colors and highlight table rows using the row styling feature. | OFF | [Row styling with Advanced Table Viewer macro](/cms_trial/space/TBL/1864990849/Row+styling+with+Advanced+Table+Viewer+macro/) |
| Grouping  (▢ ) | Interactively group and organize your table data on the Confluence page, with support for nested grouping across multiple columns. | OFF | [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/) |
| Search  (▢ ) | Perform a dynamic search on the imported table data. The search feature is enabled by default. | ON | [Search with Advanced Table Viewer macro](/cms_trial/space/TBL/1764920560/Search+with+Advanced+Table+Viewer+macro/) |
| Row numbering  (▢ ) | Display a column with row numbers. | OFF | - |
| Sort  (▢ ) | Sort the column values in ascending and descending order. | ON | [Sorting with Advanced Table Viewer macro](/cms_trial/space/TBL/1540654640/Sorting+with+Advanced+Table+Viewer+macro/) |
| Download  (▢ ) | - Download the table data as a CSV file. - When enabled, the download button is displayed at the top right of the table in the Confluence view and edit page mode. - On clicking **Download**▢, the file gets downloaded to your local file system. | OFF | - |
| Pagination  (▢ ) | - Navigate large datasets efficiently on the Confluence page using the previous, next, and direct page number controls. - Displays the current row range and total row count (for example, showing 1–10 of 55 rows). - Set the number of rows displayed per page using the **Rows per page** option. | ON if the table consists of more than 10 rows per page | - |

To edit the Data Source in the setup mode, click **Edit Data Source** on the right panel. The *Data Source* dialog opens. For more information, refer to [Advanced Table Viewer macro](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/).

![Advanced Tables Edit Data Source screen in Advanced Table Viewer](/cms_trial/assets/207b50cc-3961-476c-833d-3b8192bc55c4.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

- The column features apply specifically to the configured table columns.
- The macro offers **Rename heading,** **column calculation,** and **group calculation**. To set up the column properties for a specific column, click *Edit column* (▢ ).

  ![Advanced Tables Column properties screen in Advanced Table Viewer](/cms_trial/assets/9f7e9d6f-fa8b-4a37-8a48-fa4d8f1c07b4.jpg)

| **Column properties** | **Description** | **Default value** | **Read more…** |
| --- | --- | --- | --- |
| Rename heading | Rename the column header. | - | [Rename the table column name with Advanced Table Viewer macro](/cms_trial/space/TBL/1940817034/Rename+the+table+column+name+with+Advanced+Table+Viewer+macro/) |
| Edit column calculation | Perform column-level calculation and display the Sum, Average, Minimum, Maximum, Count, and Distinct for column values. | None | [Column calculation with Advanced Table Viewer macro](/cms_trial/space/TBL/1540654683/Column+calculation+with+Advanced+Table+Viewer+macro/) |
| Edit group calculation | Perform column calculations and display summarized values at each level of the nested group. | None | [Column group calculation with Advanced Table Viewer macro](/cms_trial/space/TBL/3219587079/Column+group+calculation+with+Advanced+Table+Viewer+macro/) |
| Column drag-and-drop  (▢ ) | Reorganize table columns using drag-and-drop in macro setup mode. | - | [Column drag-and-drop with Advanced Table Viewer macro](/cms_trial/space/TBL/3398172705/Column+drag+and+drop+with+Advanced+Table+Viewer+macro/) |