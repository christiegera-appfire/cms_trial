# Set up the Native Table Enhancer [Beta] macro features

The Native Table Enhancer macro setup mode enables you to configure macro features. The full-screen setup view provides better visibility into your table data and a smoother configuration experience for table display options.

- The macro provides column filtering, row styling, column grouping, search, row numbering, sorting, pagination, download, and column and group calculations. You can configure these features and access them in Confluence page view mode.
- The macro currently supports only plain text in table cells and only the first native Confluence table content from the macro body.
- The macro enables the search and sort features by default when you insert it for the first time.
- Pagination turns on automatically if the table has more than 10 rows, displaying 10 rows per page by default.
- The features configured in macro setup mode are saved as the default for each Confluence page refresh.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

[Unmapped macro: refined-tab — no content to fall back on]

To configure the features, navigate to the macro’s setup mode. Only users with edit permissions can access it.

1. Open the Confluence page containing the Native Table Enhancer macro.
2. Edit the Confluence page.
3. Edit the Native Table Enhancer macro to open the setup mode.

   ![Edit the Native Table Enhancer macro](/cms_trial/assets/f1b4df4d-ca1a-4567-9436-21456920caa1.png)

1. The macro setup mode opens in full-screen view.

   - The left panel displays a preview of the table data.
   - The right panel displays the available feature configurations.
   - To enable or disable a feature, click the specific icon.

     ![Native Table Enhancer macro setup mode](/cms_trial/assets/286ce41f-946d-4d4d-9326-276f48323d26.png)
2. The feature configurations are available at the table and column level. Refer to the Table and column properties section.

[Unmapped macro: refined-tab — no content to fall back on]

- The right panel toolbar displays the available feature configuration at the table level.
- The table properties apply to the entire table, affecting all columns and rows within a single macro.
- In the right panel, you can enable or disable the macro table features.

| **Table properties** | **Description** | **Default value** | **Read more** |
| --- | --- | --- | --- |
| Column filtering  (▢ ) | Configure column filters for individual columns and filter table data based on specific column values. | OFF | [Filter columns with Native Table Enhancer macro](/cms_trial/space/TBL/3558342661/Filter+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Row styling  (▢ ) | Apply row colors and highlight table rows using the row styling feature. | OFF | [Row styling with Native Table Enhancer macro](/cms_trial/space/TBL/3539308932/Row+styling+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Grouping  (▢ ) | Interactively group and organize your table data on the Confluence page, with support for nested grouping across multiple columns. | OFF | [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Search  (▢ ) | Perform a dynamic search on the table data. The search feature is enabled by default. | ON | [Search with Native Table Enhancer macro](/cms_trial/space/TBL/3549431418/Search+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Row numbering  (▢ ) | Display a column with row numbers. | OFF | - |
| Sort  (▢ ) | Sort the column values in ascending and descending order. | ON | [Sorting with Native Table Enhancer macro](/cms_trial/space/TBL/3551428609/Sorting+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Pagination  (▢ ) | - Navigate large datasets efficiently on the Confluence page using the previous, next, and direct page number controls. - Displays the current row range and total row count (for example, showing 1–10 of 55 rows). - Set the number of rows displayed per page using the **Rows per page** option. | ON if the table consists of more than 10 rows per page | - |
| Download  (▢ ) | - Download the table data as a CSV file. - When enabled, the download button is displayed at the top right of the table in the Confluence page view mode. - When you click **Download**▢, the file gets downloaded to your local file system. | OFF | - |

[Unmapped macro: refined-tab — no content to fall back on]

- The column features apply specifically to the table columns.
- The macro offers **column** and **group calculations**. To set up the column properties for a specific column, click *Edit column* (▢ ).

  ![Click Edit column for column and group calculation](/cms_trial/assets/ea19c827-62e5-4954-ab29-f39646c2c455.png)

| **Column properties** | **Description** | **Default value** | **Read more…** |
| --- | --- | --- | --- |
| Edit column calculation | Perform column-level calculations and display the Sum, Average, Minimum, Maximum, Count, and Distinct for column values. | None | [Column calculation with Native Table Enhancer macro](/cms_trial/space/TBL/3565584387/Column+calculation+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |
| Edit group calculation | Perform group calculations such as Sum, Average, Minimum, Maximum, Count, and Distinct and display summarized values at each level of the nested group. | None | [Column group calculation with Native Table Enhancer macro](/cms_trial/space/TBL/3567878145/Column+group+calculation+with+Native+Table+Enhancer+%5BBeta%5D+macro/) |