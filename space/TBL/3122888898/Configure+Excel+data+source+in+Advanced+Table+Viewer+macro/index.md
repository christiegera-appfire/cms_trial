# Configure Excel data source in Advanced Table Viewer macro

The Advanced Table Viewer macro lets you import Excel data using the **Excel** data connector. It supports `.xls/.xlsx` Excel file formats up to 10 MB.

You can import Excel data using the following data source types:

- [Upload file](#)
- [Attachment](#)
- [URL](#)

## Watch the video to quickly create your project portfolio health report in Confluence using an Excel data source

---

This page details how to configure the Advanced Table Viewer macro for an Excel data source.

## Insert the macro

Insert the macro in a Confluence page editor using the macro browser or the macro shortcut (/).

![Advanced Table Viewer_Insert_macro](/cms_trial/assets/69035acd-a7f4-4c89-b2d0-57f983740bdd.jpg)

## **Connect data source**

- On the initial setup screen, click **Connect Data Source**.

  ![connect datasource](/cms_trial/assets/3a603b52-b705-4bc8-b0f8-8ca1a44bddc8.jpg)
- The *Select* *data source* dialog opens.
- To configure the Excel data connector, select **Excel** from the *Select data connector* dropdown. By default, the CSV data connector is selected.

  ![Advanced Table Viewer _Select Excel data connector](/cms_trial/assets/e0631076-82b4-4580-8361-0b2d9ac8c9ea.jpg)
- For the Excel data connector, choose how you want to provide your Excel data. By default, **Upload file** is selected. Refer to [Configure the Excel data source](#Configure-the-Excel-data-source).

  - **Upload file**: Upload an Excel file from your computer.
  - **Attachment**: Use an Excel file attached to the current Confluence page.
  - **URL**: Provide a direct URL to your Excel file.

## Configure the Excel data source

[Unmapped macro: refined-tab — no content to fall back on]

The **Upload file** option lets you to use an Excel file from your computer.

- Once you select **Upload file,** the macro displays the **Upload a file** field.
- To upload an Excel file, click **Browse**.

  ![ATV_Excel_Upload file_Browse](/cms_trial/assets/32718b22-cc20-4ea7-a5bf-fee537be227c.jpg)
- Select an Excel file not exceeding 10 MB from your computer.

  ![ATV_Excel_Upload_select file](/cms_trial/assets/2b48cb58-f6d0-4fec-b21c-1e76f849f846.jpg)
- Once you choose a file, the macro automatically fetches the first sheet and first table and displays the sheet name and column names:

  - The **Select sheet** displays the list of sheets from the Excel file. By default, it displays the name of the first sheet.
  - To choose a different sheet, click the drop-down and select the required sheet. You can select only one sheet per macro instance.

    ![ATV_Excel_Upload_Select sheet](/cms_trial/assets/bd67497d-75df-43bc-aa1f-59a01d6c0437.jpg)
  - The **Select columns** field displays the list of column names available from the selected sheet. By default, it displays the column names from the first sheet.

    ![ATV_Excel_Upload file_Select Columns](/cms_trial/assets/b969d812-1783-4772-b525-1cba0723b286.jpg)
  - As you change the sheet selection, the **Select columns** field fetches the corresponding column names and updates accordingly.
- For further configuration, proceed to the **Select and order columns** section on this page.

If the Excel file contains errors or exceeds 10 MB, the macro displays an error message.

[Unmapped macro: refined-tab — no content to fall back on]

The Attachment option lets you to use an Excel file attached to the current Confluence page as your data source.

- Once you select **Attachment,** the macro displays the **Select page attachment** dropdown.
- The **Select page attachment** dropdown lists the Excel files attached to the current page. Select the Excel file you want to use as your data source.

  ![ATV_Excel_Select attachments](/cms_trial/assets/bb1795e5-b859-4a76-9afc-18d1c445a6e6.jpg)
- Once you choose an Excel attachment, the macro automatically fetches the first sheet and first table and displays the sheet name and column names:

  - The **Select sheet** displays the list of sheets from the Excel file. By default, it displays the name of the first sheet.
  - To choose a different sheet, click the drop-down and select the required sheet. You can select only one sheet per macro instance.

    ![ATV_Excel_Attachment_Select sheet](/cms_trial/assets/756e9134-e418-4075-958e-42baf2ee30d0.jpg)
  - The **Select columns** field displays the list of column names available from the chosen sheet. By default, it displays the column names from the first sheet.

    ![ATV_Excel_Attachment_Select columns](/cms_trial/assets/1df60677-1502-414d-a0d8-fbe0f9b3c209.jpg)
  - As you change the sheet selection, the **Select columns** field fetches the corresponding column names and updates accordingly.
- For further configuration, proceed to the **Select and order columns** section on this page.

If the Excel file contains errors or exceeds 10 MB, the macro displays an error message.

[Unmapped macro: refined-tab — no content to fall back on]

The URL option lets you use an Excel file’s direct URL as your data source.

- Once you select the **URL** option, the macro displays the **Paste file URL** field.
- In the **Paste file URL** field, paste the direct URL to your Excel file and click **Import data**.

  ![ATV_URL_Import Data](/cms_trial/assets/bd00332e-3eb6-4095-ad14-be255db033b7.jpg)

The macro supports only a direct link to an .xls or .xlsx file up to 10 MB.

✅ <https://abc.example.com/../Product_Inventory.xlsx>

❌ [https://abc.example.com/…/Product\_Inventory\_download](https://abc.example.com/taxables_download)

- Once you click Import data, the macro automatically fetches the first sheet and first table and displays the sheet name and column names:

  - The **Select sheet** displays the list of sheets from the Excel file. By default, it displays the name of the first sheet.
  - To choose a different sheet, click the drop-down and select the required sheet. You can select only one sheet per macro instance.

    ![ATV_URL_Select Sheets](/cms_trial/assets/2178b40c-cd95-4732-936b-3cefd94b38ed.jpg)

The **Select columns** field displays the list of column names available from the selected sheet. By default, it displays the column names from the first sheet.

- - ![ATV_ExcelURL_Select Columns](/cms_trial/assets/6ae6d5f5-68d1-44e3-8bf7-a1416fad6208.jpg)
- As you change the sheet selection, the **Select columns** field fetches the corresponding column names and updates accordingly.
- For further configuration, proceed to the **Select and order columns** section on this page.

If the Excel URL is invalid, or the file contains errors, or exceeds 10 MB, the macro displays an error message.

[Unmapped macro: refined-tab — no content to fall back on]

The **Select columns** field displays the column names available to display in the table.

You can remove, select, and reorder the column names as needed. The column names appear in the Confluence table in the order you select them.

- **To clear all selected columns**

  - To remove all column selections at once, click Clear All ([cross circle icon] ). After clearing, click the field and re-select column names in the required order.

    ![ATV_Excel_Select columns_clearAll](/cms_trial/assets/be1665a2-3436-40f6-9fc3-b8d1a08dc68d.jpg)
- **To remove a specific column**

  - Next to the column name, click [cross circle icon] to remove it from the selection.

    ![ATV_Excel_SelectColumns_clear a column](/cms_trial/assets/a540169b-9ddd-4aa9-8bb4-34d848f40a69.jpg)
- **To select columns**

  - Click the **Select columns** field and choose the column names from the dropdown. The order you select determines the column order in the table.

    ![ATV_Excel_Select columns_select](/cms_trial/assets/d013d8ee-eb9d-4ba6-9d2b-0b921977f2fd.jpg)

The order in which you select the column names determines the column order displayed in the Confluence table.

Once you have selected the required columns, proceed to the **Save and publish** section.

[Unmapped macro: refined-tab — no content to fall back on]

- In the *Select data source* dialog, click **Save**.

  ![ATV_ExcelURL_Select Columns](/cms_trial/assets/6ae6d5f5-68d1-44e3-8bf7-a1416fad6208.jpg)
- The macro opens in setup mode, displaying the table with the selected column names and data.
- In setup mode, you can configure various available features, such as column filtering, row styling, search, row numbering, sorting, download, and sum-up. Refer to [Setup the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![ATV_Excel_source_setup mode](/cms_trial/assets/394e9604-6be2-4337-88c2-b717011cf27e.jpg)
- To apply the configurations, click **Save**.
- The configured table appears on the Confluence page in edit mode.

  ![ATV_Excel_source_data imported_page edit mode](/cms_trial/assets/a229a00f-d84a-42ae-b165-c788b1754ab2.jpg)
- **Publish** the page to view the table in the page view mode.

  ![ATV_Excel_data_page viewmode](/cms_trial/assets/57fea1af-63e4-4453-8b52-ab581a92a84a.jpg)
- Your Excel data is now ready to view and analyze directly within Confluence. The full-screen view opens as an overlay on the Confluence page to provide a maximized view of data.

To know about the various terms used in the macro, refer to the [Advanced Table Viewer macro glossary](/cms_trial/space/TBL/1765245023/Advanced+Table+Viewer+macro+glossary/).