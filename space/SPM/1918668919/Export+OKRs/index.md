# Export OKRs

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The export option helps you want to extract current OKRs from the OKR module to share with stakeholders, update progress reports, or integrate them into other tools for analysis and decision-making.

You can export OKRs from BigPicture using API endpoints. Visit the [BigPicture Developer Portal](https://developer.bigpicture.one/reference/fetchobjectivesbyids) for details.

## Permissions

Only [permitted users](/cms_trial/space/SPM/1918765815/OKR+module+permissions/) can add, edit, and delete OKR teams:

- Jira Admin
- In-module Admin
- Users in roles with granted **Data export** permission.

## Export OKRs to a CSV file

You can customize the export options, but we recommend keeping the default settings if you plan to import the file back to BigPicture later. Changing the defaults may require you to adjust the CSV file manually to import successfully.

See the **Exported CSV file** section for more.

You can export OKRs from a .csv file or through the API. This page focuses on the .csv method.

1. On the *Overview*/*Hierarchy*/*Progress Dashboard* page, click **Export**.

   ![Export icon highlighted.](/cms_trial/assets/6c4b3c93-f9f8-4028-ad4c-96ca16fc8d7c.png)

1. The **Export** screen with the default export options displays:

   ![Export screen with the default options checked.](/cms_trial/assets/61fdc5e7-0e3f-403e-9e31-377b402e61ba.png)

- **Show the visual hierarchy of OKRs**. Check whether you want the exported OKRs to retain their hierarchical structure (represented by indentations in the .csv file).
- **Add a hierarchy column (numbered levels)**. Check whether you want your exported file to include an OKR order column.
- **Export all columns**. Check if you have filters applied and want to export all OKRs.
- **Don’t include column headers**. Select this if you do not want column headers in your exported file.
- **Export text without text formatting**. With this option, the export does not save formatting (text only).
- **Force DD/MM/YYYY format for dates**. This option adds formats for OKR period dates.
- **File name**. Name your exported file. If you leave it blank, the file will be given the default `export.csv` name.

1. Click the **Export .csv file** button to finish the process.
2. You can find the exported file in the **Downloads** folder on your device (Mac/Win).

## Exported CSV file

When you click the **Export .csv file** button, the app will create a file containing data on your OKRs, with each OKR in its own column. When you want to export all data, your CSV file will contain all columns from the *OKR Overview* page based on the following setup:

![Export screen with the first three and last option checked.](/cms_trial/assets/b45aaf37-3f6f-40a5-9d57-aa76848722be.png)

Note that when you select the **Don’t include column headers** option or uncheck any of the default options, your file will be missing important pieces of data, rendering the exported file incompatible with the CSV import file requirements.

- Order
- Type
- Key (applicable only to the linked issues)
- Summary (OKR name)
- Period
- Owner
- Teams
- Labels
- OKR Type
- Progress
- Collaborators
- Stats
- Weight
- Latest update
- Days since last update
- Date of last update
- Expected start date
- Expected end date
- Grade
- Start Value
- Current Value
- Target Value
- Assignee