# Filter columns with Advanced Table Viewer macro

The Advanced Table Viewer macro provides the column filtering table property to filter table data based on values in specific columns.

- You can configure the column filtering property for each column in the macro setup mode.
- Once filters are configured for columns, you can filter the column data in both the **Edit** and **View** modes of the Confluence page.
- Filtering only narrows down how data is displayed—it does not alter the actual content in the table.

## **Watch the video to** filter Confluence table data fast with the Advanced Table Viewer macro

## Configure and apply column filters

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the setup mode.

**Column filtering** is OFF by default. To enable column filtering:

1. Edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
2. Enable the **Column filtering** (▢).
3. Once you enable the column filtering, the **Column filters** feature panel appears on the right side of the configuration screen.

   ![Advanced Table Viewer - Enable column filtering](/cms_trial/assets/edf02908-8d5d-4ee7-9f52-2e2bdc5ca5a4.jpg)
4. Turn on the **Column filters** toggle. You will see a list of column names, with filter options for each column. You can select the filter types for each column and **Save** the changes.

   ![Table Viewer showing the column filter options.](/cms_trial/assets/353350dc-0360-4b94-99e6-b5b68fe3b87e.jpg)

To disable column filtering, click the column filtering icon(▢).

[Unmapped macro: refined-tab — no content to fall back on]

- The column filters available are based on the column datatype and value.

  ![Filters with number](/cms_trial/assets/c53030aa-e990-4502-8d14-4435a819a378.jpg)
- The available column filters are:

| **Column filter type** | **Description** |
| --- | --- |
| **Dropdown filter** | Displays a list of all unique values found in the selected column, allowing users to select a value to filter by. The dropdown filter is available for all data types. |
| **Free text filter** | Provides a text input box to enter text or numeric values to filter column data. This can be applied to columns containing text, numeric data, and special characters. |
| **Number filter** | Available only for columns containing numeric values. The number filter provides a free-text input box to enter only numeric values. |
| **Date range filter** | Available only for columns containing dates. Enables filtering of table data between two date ranges. |
| **None** | Disables filtering for the selected column. |

[Unmapped macro: refined-tab — no content to fall back on]

1. To apply column filters, select the appropriate filter type for each column based on the data type it contains.
2. When you apply column filters, the column name with the chosen filter option displays just above the table.  
   For example:

   - The **First Name**, **Sex**, and **Job Title** fieldsdisplay the dropdown filter with unique values.
   - The **Last Name** displays an input box for free text.
   - The **Rating** column displays the input box for a numeric value.
   - The **Date of birth** displays the **From** and **To** date fields.
3. Apply filters, and the table updates dynamically to show only the matching rows. For example, the table data is filtered by the **Sex** and **Date of Birth** column values.

   ![Advanced Tables filtered table data with multiple column filters](/cms_trial/assets/c7fcc0b4-23ad-4da1-b851-6edf9f7fbae6.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The date range filter is available only for columns containing dates. This enables filtering of table data between date ranges.

- The macro supports the following date formats to import from external data sources:

  - YYYY-MM-DD
  - YYYYMMDD
  - MM-DD-YYYY
  - MM/DD/YYYY
  - DD-MM-YYYY
  - DD/MM/YYYY
- Once you select the **Date range** filter:

  - The macro displays the **From** and **To** date fields above the table.
  - The **Date format** drop-down displays the formats that you can use to filter the dates.
- Select the required **Date format** to filter the dates. The chosen format is displayed in the **From** and **To** date fields.

  ![Advanced Tables date format dropdown in filter settings](/cms_trial/assets/c6d48c6a-3c50-4f90-ad53-35572eefb106.jpg)
- To filter the table data, enter the date range in the **From** and **To** fields in the chosen format, and the table filters dynamically.

  ![Advanced Tables table data filtered by date range](/cms_trial/assets/9d9e9b92-c9f2-4a7e-9651-8b6724b7fb91.jpg)