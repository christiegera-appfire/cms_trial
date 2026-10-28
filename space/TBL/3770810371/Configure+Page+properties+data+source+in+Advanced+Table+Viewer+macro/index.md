# Configure Page properties data source in Advanced Table Viewer macro

The Advanced Table Viewer macro can import **Page properties** data from pages that have any of the specified labels in a single space on the current Confluence site.

- Pages can have different property headers in the Page properties macro. The macro combines the properties from all matching pages into one set of table columns.
- The table includes a link to each page title.
- The macro can display Page properties data for up to 200 pages. If more than 200 pages match the specified labels, the table shows the first 200.

**Prerequisites**

- Add the Page properties macro, with the metadata you need, to each page.
- Add the page labels that you want to specify in the Advanced Table Viewer macro.

- The macro displays only the Page properties of pages for which you have view permission.
- The macro supports importing Page properties data only from a single space of the current Confluence site.

---

## Configure the Page properties data source in the Advanced Table Viewer macro

### Insert macro and configure Page properties data source

- In the Confluence page edit mode, insert the Advanced Table Viewer macro using the macro browser or the macro shortcut (Type / followed by the macro name).

  ![Insert Advanced Table Viewer macro from macro browser](/cms_trial/assets/b1846584-cd70-4e5c-af70-06e1b3f8a1a8.png)
- On the initial setup screen, click **Connect Data Source**.

  ![connect datasource](/cms_trial/assets/ed90c2eb-1bc1-449b-bb29-d9218affcb72.jpg)
- The *Select* *data source* dialog opens.

  ![ATV_select data source dialog.png](/cms_trial/assets/2c77a38f-70fc-488f-8ece-0a675e50795c.png)
- To configure the Page properties data source, select **Page properties** from the *Select data connector* drop-down. By default, the CSV data connector is selected.
- Once you choose **Page properties**, the dialog displays the following fields.

  - **Select space**: The drop-down displays a list of spaces from the current Confluence site. By default, it selects the current space. Select the required space from which you want to import Page properties data.
  - **Select page labels**:

    - By default, this field displays the list of available labels from the chosen space.
    - You can select the labels you want and clear the ones you don't need. You must select at least one label.
    - If no labels are found, then the drop-down displays a message: *No matching labels in this space*.
  - **Search pages**:

    - To find pages that have the matching labels and contain the Page properties macro, click **Search pages**. A page can contain one or more matching labels.
    - If you change labels after you run a search, you will see the message: *Page labels changed. Search again to update the results.*

      ![ATV_Page properties_Search pages.png](/cms_trial/assets/9d823ffd-a55c-4901-8985-be3ca9743e8d.png)

- - - The macro performs the search and loads the count of pages found that contain the Page properties macro.

      ![ATV_Page properties_page found message.png](/cms_trial/assets/9d7be67d-738b-43b2-8e50-652138452627.png)

- If the matching pages do not contain any Page properties data or if you do not have the required permissions, the macro displays an error.

  ![ATV_Page properties_No page properties data found.png](/cms_trial/assets/65671db6-0e2f-42d0-ba2c-78d43c3686a2.png)
- If you do not have the permissions to view to the configured Page properties data in a Confluence page, the page view mode displays an access-restricted message.

  ![image-20261028-093003.png](/cms_trial/assets/253c1958-db5e-4305-b44e-b6567c556b27.png)
- If you don't specify any labels and run a search, the macro displays an error.

  ![ATV_Page Prop_Add atleast one label.png](/cms_trial/assets/fc96851e-081f-48a4-945b-ac7958e8945e.png)
- If you change the labels after running a search, a message appears, and the **Save** button is disabled. Run the search again to enable it.

  ![image-20261028-091953.png](/cms_trial/assets/9d6d05c1-82bd-4892-a8aa-654d4d3201bb.png)
- If a page in the search has no readable properties, the macro excludes it, so the table can show fewer than 200 rows.
- If the search returns properties for more than 200 pages, the macro displays a message to narrow the search to view page properties for specific labels.

  ![ATV_Page prop_more than 200.png](/cms_trial/assets/44a7deb2-6f40-4d66-8264-21069ecf14c9.png)

- **Select columns**: This field displays the list of aggregated properties found on the matching pages as table columns. It also includes the page title as the first column. You can select, clear, and reorder column names. For details, see the [**Select and order columns**](#Select-and-order-columns) section.

  ![ATV_Page Prop_Select column with properties.png](/cms_trial/assets/205ce05e-3bb3-4c66-ac73-feae74a080e5.png)

### Select and order columns

You can remove, select, and reorder the column names as needed.

- Clear all selected columns

  - To remove all default column selections at once, click clear all (▢). After clearing, click the field and re-select column names in the required order.

    ![ATV_clear all columns.png](/cms_trial/assets/c342736d-3a9e-4b00-8959-e1961771cc9d.png)
- Remove a specific column

  - Next to the column name, click clear (▢) to remove it from the selection.

    ![ATV_clear specific column.png](/cms_trial/assets/6d39a894-5bcf-4802-a8c5-9436665f591d.png)
- Select columns

  - Click the **Select columns** field and choose the column names from the list.

    ![ATV_Page properties_select columns.png](/cms_trial/assets/ff8821e0-0942-4e64-b8bc-3f421e05e734.png)
  - After you select the required columns, save the changes.

The order in which you select the column names determines the column order displayed in the Confluence table. You can further reorder columns using [drag and drop](/cms_trial/space/TBL/3398172705/Column+drag+and+drop+with+Advanced+Table+Viewer+macro/) feature in macro setup mode.

### Save and publish

- In the *Select data source* dialog, click **Save**.

  ![ATV_PAge prop_Save.png](/cms_trial/assets/d308b006-e3f9-4277-92a1-99d79346b1ca.png)
- The macro opens in setup mode and displays the table with the page title, selected column names, and values.
- The first column is **Page title**, and the title links to the page. The rows are sorted by page title until the user sets another sort.
- In setup mode, you can also configure macro features such as column filtering, grouping, column calculations, reordering columns, row styling, search, row numbering, sorting, and download. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![ATV_page properties_edit macro.png](/cms_trial/assets/5193ba5b-9399-4caa-ad0d-fb08c6a09dbc.png)
- To apply the configurations, click **Save**.
- The configured table appears in the Confluence page edit mode.

  ![ATV_Page properties_page edit mode.png](/cms_trial/assets/b2e2a694-181e-4fa0-9b8e-805b3c681087.png)
- **Publish** the page to view the table in the Confluence page view mode.

  ![ATV_Page properties_page view mode.png](/cms_trial/assets/b0d2b65a-35a7-489a-99c5-019d1b4c1c85.png)
- Your Page properties data is now ready to view and analyze directly within Confluence.

- The macro refreshes the table data on every page load.
- If you want to do a manual refresh for the latest changes, click **Sync** ( ▢ ).
- You can sync the table in setup mode, Confluence page edit mode, and Confluence page view mode.