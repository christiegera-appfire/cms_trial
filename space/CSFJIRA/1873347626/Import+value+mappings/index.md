# Import value mappings

This page helps you understand how to value mappings from the CSV file imported from your local computer.

The following are the limitations of this feature:

- [Cascading field mapping](/cms_trial/space/CSFJIRA/1873413246/Configuring+Jira+cascading+fields+to+work+with+Salesforce+dependent+fields/) is not supported.
- File upload limitations:

  - Only CSV format files can be uploaded.
  - Maximum file size of 50kb.
  - Maximum of 200 rows per CSV file.
  - Minimum of 2 columns per CSV file.
- The Jira users imported from the CSV file are shown only as user IDs. The name of the user is not shown in the value mappings table.

  - Refer to [Export users from a site | Atlassian Support](https://support.atlassian.com/organization-administration/docs/export-users-from-a-site/) to get the list of users with the corresponding user ID.

## Guide

1. Go to **Apps** > *Connector for Salesforce*, and select **Bindings** from the side navigation bar.
2. Click **Mappings** on the bindings of your choice.
3. In the pop-up, click **Configure** on a field, then click **Import**.

   ![contentId-1873347626](/cms_trial/assets/cd41d93c-8ec3-4bff-b318-60804b3c10a4.png)
4. In the **Upload file** phase, click **Upload a file** or drag and drop to upload the CSV file.  
   The CSV file must be in format similar to the one shown.  
   *Jira Data* | *Salesforce Data*  
   *value 1* | *new value 1*  
   *value 2* | *new value 2*

   ![value-mapping-csv.png](/cms_trial/assets/e56ede48-7fc7-4992-9f90-36658dad0d3e.png)
5. Click **Next** when you see the *File uploaded successfully!* message.
6. Map the **CSV field** values to the existing **Value mapping field**, then click **Next**.

   ![contentId-1873347626](/cms_trial/assets/a3692518-ccf7-4ad1-9a90-b67fc2446d72.png)
7. In the **Summary** phase, go through the uploaded field data and verify them. Once verified, click **Import**.

   ![contentId-1873347626](/cms_trial/assets/e864cd19-9351-40bb-927e-77b589f55eda.png)

   ℹ️ Toggling **Only show rows with problems** only shows you the fields uploaded that are flagged due to formatting issues or duplicate values.

When the value mapping import is successful, the *Entity Mapping updated successfully* message appears.