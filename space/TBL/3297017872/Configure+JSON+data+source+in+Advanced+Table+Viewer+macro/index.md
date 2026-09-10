# Configure JSON data source in Advanced Table Viewer macro

The Advanced Table Viewer macro supports importing data from the **JSON** data connector. The supported JSON file size is up to 10 MB.

You can import JSON data using the following data source types:

- [Upload file](#)
- [Attachment](#)
- [URL](#)
- [Insert JSON](#)

## Watch the video to quickly build reports in Confluence with **JSON data sources using the Advanced Table Viewer macro**

Video transcript

IT Operations Manager Alex has been flagged—the engineering team is facing a major deployment stall due to a critical resource shortage.

To fix this, he needs to quickly build a global asset report for stakeholders.

In this video, see how Alex uses the Advanced Table Viewer macro to consolidate data from separate **JSON** data sources into a single Confluence dashboard, exposing resource gaps and unblocking the deployment.

Alex first starts with the regional laptop stock report.

He inserts the Advanced Table Viewer macro, clicks **Connect Data Source**, and selects **JSON**.

For the **JSON** data source, you can either upload a file, select an attachment, use a **JSON** file **U.R.L,** or **insert** **JSON** code in the macro.

Alex uploads the local inventory file sent over by the North American IT team.

He specifies the **Row data path** to import the Laptop inventory, and clicks **Save**.

The macro opens setup mode, a full-screen experience designed for easy configuration.

He enables **Column Grouping** and groups the table by the Status column to track laptop availability.

He clicks Column properties for the **Asset Value** and applies a **SUM** group calculation to display total asset values at both the group and column levels.

**Save** the macro configuration.

Next, Alex needs to evaluate server capacity. He inserts the macro again, and this time he selects the Attachment option.

The global cloud infrastructure team has already attached their master server logs to this Confluence page.

He specifies the Row data path, de selects the columns not needed, and clicks Save to enter setup mode.

Alex enables **Column Grouping** and groups the table data by the **Status** column to view offline nodes.

He clicks the **CPU Cores** column properties and applies a SUM group calculation to track total global processing capacity at a glance.

**Save** the macro configuration.

Alex knows that the software resource gap can stall the engineers, and stakeholders need a current view of the application data.

He inserts the macro again — this time selects the **U.R.L.** option — and pastes a direct link to the **Software License registry** file hosted on Git Hub.

Clicks Import data, and the macro fetches data from the URL.

To extract the software license details, he specifies the Row data path and clicks **Save**.

The macro opens setup mode.

The table displays the Used Seats right next to Total Seats. He clicks the Cost column properties and applies the SUM calculation to total the monthly license expenditure to keep budgeting transparent for stakeholders.

**Save** the macro configuration.

Finally, Alex needs to account for any ongoing system maintenance windows that can cause operational friction.

He inserts the macro, selects the Insert JSON option this time, and pastes the standard raw JSON directly into the macro.

He specifies the Row data path for active infrastructure updates and **saves** the macro.

In setup mode, Alex enables **Column Grouping**, and for the Estimated Duration Hours column, he applies a **Sum** column calculation to show stakeholders the cumulative scheduled downtime.

Once all reports are complete, publish the page.

The Confluence page is now the single source of truth with all resource reports ready to present to stakeholders.

By showcasing unassigned **in-stock** laptops, he plans to free up idle hardware to be instantly deployed to blocked engineers.

He exposes a server distribution gap and proposes temporarily shifting the workload to an underutilized European server while the Singapore server is repaired.

He highlights maxed-out software seats to prove that a budget expansion is required to unblock critical deployment tools.

By revealing 60 hours of overlapping downtime, he proposes rescheduling updates to give engineers a safer launch window.

Data-driven reports—customized within Confluence for smarter business decisions.

---

This page details how to connect to a JSON data source and configure the Advanced Table Viewer macro.

## Insert the macro

Insert the macro in a Confluence page using the macro browser or the macro shortcut (/).

![Advanced Tables macro shortcut for inserting Advanced Table Viewer](/cms_trial/assets/f7ceae17-ace1-496a-a35f-c7591fd7e928.jpg)

## **Connect data source**

- On the initial setup screen, click **Connect Data Source**.

![connect datasource](/cms_trial/assets/f3d0c47f-e753-4c17-baf7-c5559bf71de3.jpg)

- The *Select* *data source* dialog opens. By default, the CSV data connector is selected.

  ![Advanced Tables Select JSON data source dialog](/cms_trial/assets/b65e6bd2-e495-42eb-920e-9e511cf94f63.jpg)
- For the JSON data connector, choose how you want to provide your JSON data. By default, **Upload file** is selected. Refer to [Configure the JSON data source](#Configure-the-JSON-data-source).

  - **Upload file**: Upload a JSON file from your computer.
  - **Attachment**: Use a JSON file attached to the current Confluence page.
  - **URL**: Provide a URL to your JSON file.
  - **Insert JSON**: Type or paste JSON code directly into the macro.

## Configure the JSON data source

[Unmapped macro: refined-tab — no content to fall back on]

The **Upload file** option lets you to use a JSON file from your computer.

- Once you select **Upload file,** the macro displays the **Upload a file** field.
- To upload a JSON file, click **Browse**.

  ![Advanced Tables JSON upload file source with Browse button](/cms_trial/assets/0feeb6be-b74b-458a-910a-eddf5daf7a7e.jpg)
- Select a JSON file not exceeding 10 MB from your computer.

  ![Advanced Tables file picker for selecting a JSON file](/cms_trial/assets/d2053545-0245-451a-a1c3-1f119d9ff022.jpg)
- Once you choose the file, the **Row data path** field appears.

  - Specify the JSON path to import data and generate a table. The path is case sensitive.
  - The path can be a dot-separated path to the target field in the JSON string. For example: *Hardware.Storage*
  - The data at this path will populate the table rows. [Learn more about JSON path syntax.﻿](https://goessner.net/articles/JsonPath/)

    ![Advanced Tables JSON configuration with Row data path field](/cms_trial/assets/ccd13ac3-3fe1-4457-b29b-ddd68338a1e6.jpg)

If the JSON file contains formatting errors or exceeds 10 MB, the macro displays an error message.

- Once you specify the **Row data path**, the **Select columns** field displays the list of field names available at the specified path. For further configuration, proceed to the **Select and order columns** section on this page.

  ![Advanced Tables JSON upload file source with Row data path and selected columns](/cms_trial/assets/55dfbd0f-fa54-4849-8c4a-e822e6205389.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The Attachment option lets you to use a JSON file attached to the current Confluence page as your data source.

- Once you select **Attachment,** the macro displays the **Select page attachment** dropdown.
- The **Select page attachment** dropdown lists the JSON files attached to the current page. Select the JSON file you want to use as your data source.

  ![Advanced Tables JSON page attachment data source selection](/cms_trial/assets/7cc5f294-9c2f-4a33-9110-7b706bd469d8.jpg)
- Once you choose the file, the **Row data path** field appears.

  - Specify the JSON path to import data and generate a table. The path is case sensitive.
  - The path can be a dot-separated path to the target field in the JSON string. For example: *Hardware.Storage*
  - The data at this path will populate the table rows. [Learn more about JSON path syntax.﻿](https://goessner.net/articles/JsonPath/)

    ![Advanced Tables JSON attachment source with Row data path field](/cms_trial/assets/580ab098-6bc5-44e4-bfc2-1f720f7378c8.jpg)

If the JSON file contains formatting errors or exceeds 10 MB, the macro displays an error message.

- Once you specify the **Row data path**, the **Select columns** field displays the list of field names available at the specified path. For further configuration, proceed to the **Select and order columns** section on this page.

  ![Advanced Tables JSON Row data path and column selection settings](/cms_trial/assets/b76989ac-90f7-448e-b966-d2d395c81a64.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The URL option lets you use a JSON file URL as your data source.

- Once you select the **URL** option, the macro displays the **Paste file URL** field.
- In the **Paste file URL** field, type or paste the direct URL to your JSON file and click **Import data**.

  ![Advanced Tables JSON URL source with Import Data button](/cms_trial/assets/bd164a01-c769-4358-822f-fa332da38a82.jpg)

The macro supports only a direct link to a JSON file.

✅ <https://abc.example.com/taxables.JSON>

❌ <https://abc.example.com/taxables_download>

- Once you click **Import data** and the file downloads successfully, the **Row data path** field appears.

  - Specify the JSON path to import data and generate a table. The path is case sensitive.
  - The path can be a dot-separated path to the target field in the JSON string. For example: *Hardware.Storage.*
  - The data at this path will populate the table rows. [Learn more about JSON path syntax.﻿](https://goessner.net/articles/JsonPath/)

    ![Advanced Tables JSON URL source with Import Data button](/cms_trial/assets/bd164a01-c769-4358-822f-fa332da38a82.jpg)

If the URL is invalid, or the JSON file contains formatting errors, or the file size exceeds 10 MB, the macro displays an error message.

- Once you specify the Row data path, the **Select columns** field displays the list of field names available at the specified path. For further configuration, proceed to the **Select and order columns** section on this page.

  ![Advanced Tables JSON URL source with Row data path settings](/cms_trial/assets/d27b1ace-4068-4294-958f-9540dfb19f54.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The Insert JSON option lets you use the JSON code directly in the macro.

Inserting a large amount of JSON code can affect the performance of your Confluence page. For large datasets, use the Upload file, Attachment, or URL option instead.

- Once you select **Insert JSON,** the macro displays the **Insert JSON text** field.
- In the **Insert JSON text** field, enter or paste the JSON code.

  ![Advanced Tables Insert JSON text data source configuration](/cms_trial/assets/e92c5e61-0984-48fe-919c-ff53bcbc2903.jpg)
- Once you insert the JSON text, the **Row data path** field appears.

  - Specify the JSON path to import data and generate a table. The path is case sensitive.
  - The path can be a dot-separated path to the target field in the JSON string. For example: *Hardware.Storage.*
  - The data at this path will populate the table rows. [Learn more about JSON path syntax.﻿](https://goessner.net/articles/JsonPath/)

If the JSON code contains errors, the macro displays an error message.

- Once you specify the Row data path, the **Select columns** field displays the list of field names available at the specified path. For further configuration, proceed to the **Select and order columns** section on this page.

  ![Advanced Tables Insert JSON source with Row data path settings](/cms_trial/assets/3512277c-ff83-4063-93b7-bb02224211ad.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

The **Select Columns** field displays the column names available to display in the table.

You can remove, select, and reorder the column names as needed. The column names appear in the Confluence table in the order you select them.

- **To clear all selected columns**

  - To remove all column selections at once, click Clear All ([cross circle icon] ). After clearing, click the field and re-select column names in the required order.

    ![Advanced Tables JSON Select Columns panel with Clear all option](/cms_trial/assets/b748c921-e0f7-4673-9bcd-22693ce4c168.jpg)
- **To remove a specific column**

  - Next to the column name, click [cross circle icon] to remove it from the selection.

    ![Advanced Tables JSON Select Columns panel with one field cleared](/cms_trial/assets/a95a2bc2-ac95-4341-897d-01984ed4f2bf.jpg)
- **To select columns**

  - Click the **Select Columns** field and choose the column names from the dropdown. The order you select determines the column order in the table.

    ![Advanced Tables Select Column dropdown for JSON fields](/cms_trial/assets/d02b70bd-cba4-4dee-9b68-1ea7480783bd.jpg)

The order in which you select the column names determines the column order displayed in the Confluence table.

Once you have selected the required columns, proceed to the **Save and publish** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

- In the *Select data source* dialog, click **Save**.

  ![Advanced Tables JSON data source settings with Save button](/cms_trial/assets/52116710-d085-4229-ac88-6c4148083b48.jpg)
- The macro opens in setup mode, displaying the table with the selected column names and data.
- In setup mode, you can configure various features, such as column filtering, row styling, column grouping, search, row numbering, sorting, pagination, download, rename heading, and column and group calculations. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![Advanced Tables JSON source in setup mode with Save button](/cms_trial/assets/fd3e5e62-d1d3-4b5c-9bff-5ddcf1afe44e.jpg)
- To apply the configurations, click **Save**.
- The configured table appears on the Confluence page in edit mode.

  ![Advanced Tables JSON source shown on a Confluence page in edit mode](/cms_trial/assets/45606958-cb0d-465f-ac3b-bbb9bd9f2ae8.jpg)
- **Publish** the page to view the table in the page view mode.

  ![Advanced Tables JSON source table shown on a Confluence page in view mode](/cms_trial/assets/ff30ef6c-693a-4bea-a9b7-74118c3e8afe.jpg)

Your JSON data is now ready to view and analyse directly within Confluence.

To know about the various terms used in the macro, refer to the [Advanced Table Viewer macro glossary](/cms_trial/space/TBL/1765245023/Advanced+Table+Viewer+macro+glossary/).