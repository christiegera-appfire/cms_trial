# Make bulk changes to Salesforce and Jira mapping configuration by editing JSON files

## Purpose

As seen in the image below, mapping each Reporter field(Jira) to Owner ID(Salesforce) can take a long time. You will have to configure each field one by one manually.

By exporting the existing mapping, you can extract the issue type ID and the Salesforce objects data into a .json file.

This guide will help you use the exported JSON file to map user related fields such as assignee and reporter with new values and reimport it back into the Salesforce configuration page.

## Answer

1. Go to **Apps** > **Salesforce**> **Bindings** > **Mapping** > click on **Export** on the top right button.
2. You can use any open source editor, for the example, the [Notepad++](https://notepad-plus-plus.org/downloads/) text editor is used.
3. Open the Notepad++ application > on the navigation bar, select **Plugins** > **Plugins Admin**. 

   ![plugins.png](/cms_trial/assets/f5c49ab7-9270-4dca-b521-b03bcb1c936a.png)
4. In the search box, type "*JSON*" and click **Next**.
5. Select "JSON Viewer" and click **Install**to install the latest JSON viewer available. You may be required to restart the application.
6. Open the unformatted .json file with the Notepad++ application. In the navigation bar, select **Plugins** > **JSON Viewer** >  **Format JSON**. 

   ![format JSON.png](/cms_trial/assets/78007ff9-201a-4055-b8b6-37ea77f5332a.png)
7. In the formatted .json file, search for the Jira Issue Type ID of the existing mapping.

   ![ID.png](/cms_trial/assets/91c12a92-71ea-4976-b672-6e3444c4547d.png)

How to get the Jira issue type ID:

Go to your **Project** > **Project settings** > **Issues** > **Types** > hover on the issue type link.

In the URL shown, the last numbers (ex, 10001) is the Jira issue type ID.

1. Once located, scroll until you find the assignee user ID with the Salesforce Owner ID value. 

   ![example.png](/cms_trial/assets/1357c43b-23d3-4d02-b657-97c56d070f5e.png)
2. Copy those lines to another issue type ID. With this, you can copy the user ID data within the file to other issue type IDs without the need to map them manually in the user interface.

Make sure the lines that are copied over have opening and closing brackets, else the file import will fail.

1. Once the file editing is complete, go to **Apps** > **Salesforce**> **Bindings** > **Mapping** > click on **Import** on the top right button and enter the file.

   ![result.png](/cms_trial/assets/cc236440-33eb-4561-8dca-c306e45e636a.png)