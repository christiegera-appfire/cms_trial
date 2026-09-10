# Configure CSV data source in Advanced Table Viewer macro

The Advanced Table Viewer macro supports importing data from the **CSV** data connector. The supported CSV file size is up to 10 MB.

You can import CSV data using the following data source types:

- [Upload file](#Configure-the-data-source)
- [Attachment](#Configure-the-data-source)
- [URL](#Configure-the-data-source)
- [Insert CSV](#Configure-the-data-source)
- [Profiles](#Configure-the-data-source)

Watch this video to see how quickly you can upload a CSV file and import data as a structured table — with sorting, column filter, and sum for numeric column enabled.

This page details how to connect to a CSV data source and configure the Advanced Table Viewer macro.

## Insert the macro

Insert the macro in a Confluence page using the macro browser or the macro shortcut (/).

![Advanced Tables macro shortcut for inserting Advanced Table Viewer](/cms_trial/assets/cdeeb383-c9b9-4b40-8624-350573a05ebb.jpg)

## **Connect data source**

- On the initial setup screen, click **Connect Data Source**.

![connect datasource](/cms_trial/assets/6a37d824-bd7d-4142-a374-04aafcd19a9b.jpg)

- The *Select* *data source* dialog opens. By default, the CSV data connector is selected.

  ![ATV_CSV_Upload file](/cms_trial/assets/0da6a8bb-9c57-464c-a83d-0707a3e6dff3.jpg)
- For the CSV data connector, choose how you want to provide your CSV data. By default, **Upload file** is selected. Refer to [Configure the data source](#Configure-the-data-source).

  - **Upload file**: Upload a CSV file from your computer.
  - **Attachment**: Use a CSV file attached to the current Confluence page.
  - **URL**: Provide a URL to your CSV file.
  - **Insert CSV**: Type or paste CSV code directly into the macro.
  - **Profiles**: Select a predefined profile for the CSV file.

## Configure the data source

[Unmapped macro: refined-tab — no content to fall back on]

The **Upload file** option lets you to use a CSV file from your computer.

- Once you select **Upload file,** the macro displays the **Upload a file** field.
- To upload a CSV file, click **Browse**.

  ![ATV_CSV_Upload file_click browse](/cms_trial/assets/bc48bf97-947f-460f-97ec-7ccf945e2ab6.jpg)
- Select a CSV file not exceeding 10 MB from your computer.

  ![Advanced Tables Choose file dialog for selecting a CSV file](/cms_trial/assets/32c73c18-6073-47e8-b69c-3877fd5f340b.jpg)
- The **Select Columns** field displays the list of column names available from the CSV file.

  ![Advanced Tables CSV upload file source with Select Columns settings](/cms_trial/assets/46b71175-b645-4b98-b44c-6f975cebd8c7.jpg)

If the CSV file contains formatting errors or size exceeds 10 MB, the macro displays an error message. To learn about CSV file formats, refer to [The comma-separated value (CSV) File Format](https://www.creativyst.com/Doc/Articles/CSV/CSV01.shtml).

- For further configuration, proceed to the **Select and order columns** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

The Attachment option lets you to use a CSV file attached to the current Confluence page as your data source.

- Once you select **Attachment,** the macro displays the **Select page attachment** dropdown.
- The **Select page attachment** dropdown lists the CSV files attached to the current page. Select the CSV file you want to use as your data source.

  ![Advanced Tables CSV page attachment data source selection](/cms_trial/assets/4813892c-a3d9-4c4e-9817-41279fa9eb76.jpg)
- The **Select Columns** field displays the list of column names available from the CSV file.

  ![Advanced Tables CSV attachment source with Select Columns settings](/cms_trial/assets/19b3f00e-abfa-43ec-9f59-4a1b63be37f0.jpg)
- For further configuration, proceed to the **Select and order columns** section on this page.

If the CSV file contains formatting errors or size exceeds 10 MB, the macro displays an error message. To learn about CSV file formats, refer to [The comma-separated value (CSV) File Format](https://www.creativyst.com/Doc/Articles/CSV/CSV01.shtml).

[Unmapped macro: refined-tab — no content to fall back on]

The URL option lets you use a CSV file URL as your data source.

- Once you select the **URL** option, the macro displays the **Paste file URL** field.
- In the **Paste file URL** field, type or paste the direct URL to your CSV file and click **Import data**.

  ![Advanced Tables CSV URL source with Import Data button](/cms_trial/assets/7f6e005a-595b-4ec4-ba72-c6aea3321b70.jpg)

The macro supports only a direct link to a .csv file.

✅ <https://abc.example.com/taxables.csv>

❌ <https://abc.example.com/taxables_download>

- The **Select Columns** field displays the list of column names available from the CSV URL.

  ![Advanced Tables CSV URL source with Select Columns settings](/cms_trial/assets/7a2a36e4-682b-469a-9d71-f4f92ee98ab0.jpg)
- For further configuration, proceed to the **Select and order columns** section on this page.

If the URL is invalid, or the CSV file contains formatting errors, or the file size exceeds 10 MB, the macro displays an error message. To learn about CSV file formats, refer to [The comma-separated value (CSV) File Format](https://www.creativyst.com/Doc/Articles/CSV/CSV01.shtml).

[Unmapped macro: refined-tab — no content to fall back on]

The Insert CSV option lets you use the CSV code directly in the macro.

Inserting a large amount of CSV code can affect the performance of your Confluence page. For large datasets, use the Upload file, Attachment, or URL option instead.

- Once you select **Insert CSV,** the macro displays the **Add your CSV** box.
- In the **Add your CSV** box, enter or paste the CSV code and click **Save**.

  ![Advanced Tables Insert CSV text data source configuration](/cms_trial/assets/f71b24e5-40f1-4cdf-ad38-fadb237d9b52.jpg)

If the CSV code contains errors, the macro displays an error message. To learn about CSV file formats, refer to [The comma-separated value (CSV) File Format](https://www.creativyst.com/Doc/Articles/CSV/CSV01.shtml).

- For further configuration, proceed to the **Save and publish** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

The Profiles option lets you use a predefined profile for your CSV file. Administrators can configure Profiles in the Global Configuration.

**Pre-requisite:** Make sure you have access to the required profiles, or contact your Administrator to define them. To configure profiles, refer to [Configuration-Cloud](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/).

- Once you select **Profiles**, the macro displays the **Select a Profile** dropdown.
- The **Select a Profile** dropdown lists the available profiles. Select the profile from which you want to import the data as a Confluence table.

  ![ATV_CSV_Select a Profile](/cms_trial/assets/ecfa4b83-35b5-43f6-8309-135e98d846cd.jpg)

If data cannot be retrieved from the selected profile, the macro displays an error message.

- The **Select Columns** field displays the list of column names from the profile. For further configuration, proceed to the **Select and order columns** section on this page.

  ![Advanced Tables CSV profile source with Select Columns settings](/cms_trial/assets/ae6e8383-1073-428f-9bf1-6beeea5bc374.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The **Select Columns** field displays the column names available to display in the table.

You can remove, select, and reorder the column names as needed. The column names appear in the Confluence table in the order you select them.

- **To clear all selected columns**

  - To remove all column selections at once, click Clear All ([cross circle icon] ). After clearing, click the field and re-select column names in the required order.

    ![Advanced Tables Select Columns panel with Clear all option](/cms_trial/assets/273194f8-07f6-45a5-87f3-b6a0bd01ebc7.jpg)
- **To remove a specific column**

  - Next to the column name, click [cross circle icon] to remove it from the selection.

    ![Advanced Tables Select Columns panel with one column cleared](/cms_trial/assets/2e153615-bb03-4db7-8735-d049c26923ba.jpg)
- **To select columns**

  - Click the **Select Columns** field and choose the column names from the dropdown. The order you select determines the column order in the table.

    ![Advanced Tables Select Columns dropdown for table fields](/cms_trial/assets/ac8c3401-07c9-4a1d-8152-3c5e695248fe.jpg)

The order in which you select the column names determines the column order displayed in the Confluence table.

Once you have selected the required columns, proceed to **Save and publish** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

- In the *Select data source* dialog, click **Save**.

  ![Advanced Tables data source selection with Save button](/cms_trial/assets/7a1cc538-cdbc-4ae1-9563-5ec983773222.jpg)
- The macro opens in setup mode, displaying the table with the selected column names and data.
- In setup mode, you can configure various available features, such as column filtering, row styling, search, row numbering, sorting, download, and sum-up. Refer to [Setup the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![Advanced Tables Advanced Table Viewer macro in setup mode](/cms_trial/assets/39c03198-ca15-463c-a0c1-b2381bd0b1c3.jpg)
- To apply the configurations, click **Save**.
- The configured table appears on the Confluence page in edit mode.

  ![Advanced Tables CSV source shown on a Confluence page in edit mode](/cms_trial/assets/c8d82bc2-49ec-4b16-addb-f8fe43eee489.jpg)
- **Publish** the page to view the table in the page view mode.

  ![Advanced Tables CSV source table shown on a Confluence page in view mode](/cms_trial/assets/139ccc25-5592-43e7-9fc9-26d497073a6b.jpg)

Your CSV data is now ready to view and analyse directly within Confluence.

To know about the various terms used in the macro, refer to the [Advanced Table Viewer macro glossary](/cms_trial/space/TBL/1765245023/Advanced+Table+Viewer+macro+glossary/).