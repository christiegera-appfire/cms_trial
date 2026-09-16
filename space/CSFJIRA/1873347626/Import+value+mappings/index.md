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

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/cfc208de-f5be-4d59-bba0-b102debe6b0a.png)
3. Select your **Binding**, then click **Menu** (▢) > **Edit**.
4. Select the entity mapping.
5. In the *Field mappings* section, click **Menu** (▢) > **Configure** for a selected field mapping.

   ![Configure field mappings](/cms_trial/assets/6c60fdbc-1fd1-4b6e-b428-6209027b8a3f.png)
6. Click **Import**.

   ![image-20260915-112311.png](/cms_trial/assets/f4159daa-e089-4c27-a75b-980cc541315b.png)
7. In the **Upload file** phase, click **Upload a file** or drag and drop to upload the CSV file.

   ![image-20260915-112501.png](/cms_trial/assets/4f9c036f-d1df-4cba-bcec-81dca61e9bcf.png)

   The CSV file must be in format similar to the one shown.  
   *Jira Data* | *Salesforce Data*  
   *value 1* | *new value 1*  
   *value 2* | *new value 2*

   ![value-mapping-csv.png](/cms_trial/assets/e56ede48-7fc7-4992-9f90-36658dad0d3e.png)
8. Click **Next** when you see the *File uploaded successfully!* message.
9. Map the **CSV field** values to the existing **Value mapping field**, then click **Next**.

   ![contentId-1873347626](/cms_trial/assets/a3692518-ccf7-4ad1-9a90-b67fc2446d72.png)
10. In the **Summary** phase, go through the uploaded field data and verify them. Once verified, click **Import**.

    ![contentId-1873347626](/cms_trial/assets/e864cd19-9351-40bb-927e-77b589f55eda.png)

    ℹ️ Toggling **Only show rows with problems** only shows you the fields uploaded that are flagged due to formatting issues or duplicate values.

When the value mapping import is successful, the *Entity Mapping updated successfully* message appears.