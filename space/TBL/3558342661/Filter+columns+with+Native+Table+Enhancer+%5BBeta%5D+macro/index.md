# Filter columns with Native Table Enhancer [Beta] macro

The Native Table Enhancer macro provides the column filtering table property to filter table data based on values in specific columns.

- You can configure the column filtering property for each column in the macro setup mode.
- Once filters are configured for columns, you can filter the column data in **View** mode of the Confluence page.
- Filtering only narrows down how data is displayed—it does not alter the actual content in the table.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

## Configure and apply column filters

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the setup mode.

**Column filtering** is OFF by default. To enable column filtering:

1. Edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).
2. Enable the **Column filtering** (▢).
3. Once you enable column filtering, the **Column filters** feature panel appears on the right side of the configuration screen.

   ![Enable column filtering in Native Table Enhancer macro](/cms_trial/assets/a4ac2276-b07a-42b2-b281-5609eac26c8c.png)
4. Turn on the **Column filters** toggle. You will see a list of column names, with filter options for each column. You can select the filter types for each column and save the changes.

   ![Select column filters for each column](/cms_trial/assets/ca96dd9e-302f-4d71-a90f-2795da052297.png)

- To disable column filtering, click the column filtering icon(▢).
- To disable the column filter for any specific configured field, set the filter to **None**.

[Unmapped macro: refined-tab — no content to fall back on]

- The column filters available are based on the column datatype and value.

  ![Column filter datatypes](/cms_trial/assets/09bb2e98-64cd-4fc7-bc5d-aa4f2c7501ed.png)
- The available column filters are:

| **Column filter type** | **Description** |
| --- | --- |
| **Dropdown filter** | Displays a list of all unique values found in the selected column, allowing users to select a value to filter by. The dropdown filter is available for all data types. |
| **Free text filter** | Provides a text input box to enter text or numeric values to filter column data. This can be applied to columns containing text, numeric data, and special characters. |
| **Number filter** | Available only for columns containing numeric values. The number filter provides a free-text input box to enter only numeric values. |
| **Date range filter** | Available only for columns containing dates. Enables filtering of table data between two date ranges. |
| **None** | Disables filtering for the selected column. |

[Unmapped macro: refined-tab — no content to fall back on]

1. To apply column filters, select the appropriate filter type for each column based on the datatype it contains.
2. When you apply column filters, the column name with the chosen filter option displays just above the table.  
   For example:

   - The **Category** and **Supplier** fieldsdisplay the dropdown filter with unique values.
   - The **Product Name** displays an input box for free text.
   - The **Reorder Level** column displays the input box for a numeric value.
   - The **Last Restocked** column displays the **From** and **To** date fields.
3. Apply filters, and the table updates dynamically to show only the matching rows. For example, the table data is filtered by the **Category** and **Last Restocked** column filters.

   ![Apply filters in Native Table Enhancer macro](/cms_trial/assets/1b1ea543-98b3-43e9-8d4e-616a0335599b.png)

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

  ![Date filter formats](/cms_trial/assets/892a3057-4f32-4c70-97f4-f5c9324f4fcd.png)
- To filter the table data, enter the date range in the **From** and **To** fields in the chosen format, and the table filters dynamically.

  ![Enter the from and to date fields to filter table](/cms_trial/assets/6e82e6c6-66e3-4b13-9d39-89c1515a43e7.png)