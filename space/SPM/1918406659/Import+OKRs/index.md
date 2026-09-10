# Import OKRs

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The import option lets you import Objectives and Key Results directly from external sources into the OKR module, making tracking and alignment easier.

You can import OKRs to BigPicture using API endpoints. Visit the [BigPicture Developer Portal](https://developer.bigpicture.one/reference/fetchobjectivesbyids) for details.

## Permissions

Only [permitted users](/cms_trial/space/SPM/1918505859/Priorities+module+permissions/) can import OKRs:

- Jira Admin
- In-module Admin
- Users granted the **Create new OKRs** basic permission
- Users in roles with the **Create OKRs** advanced permission.

## Prepare the CSV file

You can import OKRs from a .csv file. Before importing your OKRs, ensure the data in the .csv file is properly structured.

### Sample CSV file structure

The following table shows an example of the correct data structure used in the .csv file. The cells marked with an asterisk (\*) indicate the required fields.

If you want to import Strategic themes, set the Type to “Objective” and the OKR **Type** to “Strategic theme.”

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Order\*** | **Type\*** | **Summary\*** | **Status\*** | **Period\*** | **Owner\*** | **Weight** | **OKR type** | **Labels** | **Teams** | **Expected start date** | **Expected end date** | **Start value\*** | **Current value\*** | **Target value\*** | **Description** |
| 1 | Objective | Establish world-class… | On track |  | Agnette Smith | 1 | Strategic theme |  |  |  |  | 0 | 0 | 10 |  |
| 1.1 | Objective | Increase ARR from… | not Started | Q3 Y2025 | Agnette Smith | 1 | Company |  | Alpha, Beta |  |  | 0 | 0 | 10 |  |
| 1.2 | Objective | Optimize sales processes… | AT RISK | Q3 Y2025 | agnette.smith@appfire.com |  | Team |  | Alpha |  |  | 0 | 0 | 20 |  |
| 1.2.1 | Key result | Increase sales from… | On track | Y2025 | Andreas Coppola | 1 |  |  |  | 01/01/2025 |  | 0 | 0 | 15 |  |

### Required CSV fields

Ensure that none of the following headers and data under those headers are missing in your file:

- **Order**—Each OKR is assigned a unique numeric identifier. Top-level objectives usually begin with whole numbers (e.g., 1, 2), while sub-themes, sub-objectives, Key Results, and Jira work items use decimal numbers (e.g., 1.1, 1.2.2) to show their connection to the parent.
- **Type** - Specify whether the row represents an Objective, a Key Result, or a Jira work item. Call Strategic themes and sub-objectives “Objectives” in the import file. This field is case-sensitive.

| **Order** | **Type** | **Description** |
| --- | --- | --- |
| 1 | Objective | Top-level Strategic theme |
| 1.1 | Objective | First sub-objective under the Strategic theme |
| 1.2 | Objective | Second sub-objective under the Strategic theme |
| 1.2.1 | Objective | Sub-objective |
| 1.2.1.1 | Key result | Sub-objective’s manual Key Result |
| 1.2.1.2 | Auto key result | Sub-objective’s automatic Key Result |
| 1.2.1.2.1 | Issue | Jira work item linked to a Key Result |

- **Period** - The timeframe for the OKR. It must match an existing period in the OKR module.
- **Owner** - The OKR owner's username or email address. The username and email must match the Jira user added to the app.
- **Status** - The current status of the OKR. The status must match the built-in statuses in the OKR module. This field is not case-sensitive.
- **Start value** (Key Result) - The initial value of the Key Result.
- **Current value** (Key Result) - The current value of the Key Result.
- **Target value** (Key Result) - The target value of the Key Result.

The start/current/target values for the KRs are required since KRs are imported as [manual KRs](/cms_trial/space/SPM/1918702967/Manual+KR/). By default, the **Measure** **as** unit for these values is **Numeric**. When the OKRs are imported, you can change the progress settings (values and units) for the imported KRs or convert them to [auto-KRs](/cms_trial/space/SPM/1918670238/Auto-KR/).

### Optional CSV fields

- **Expected Start/End Date** - If the OKR's start and end dates (format: DD/MM/YYYY) are missing, they will be set based on the period.
- **Description:** A detailed explanation of the OKR.
- **OKR type:** The type of OKR (for example, Personal, Team, or Organizational).
- **Teams:** A multi-value field to indicate which teams are involved with this OKR.
- **Labels:** A multi-value field to assign labels to OKRs for easy categorization.
- **Weight:** Represents the OKR’s significance.

### Pre-existing data in the OKR module

You cannot import data that does not appear in the OKR module. If your .csv file does not have the following columns:

- Owners (users)
- Teams
- Labels
- OKR types (Note that you do not need to add the **Strategic theme** as a type)
- Periods

—the import will fail.

- Status - The status must match the built-in statuses in the OKR module.
- Custom field - The custom field name must match the field name configured in the OKR Settings exactly.

### CSV file weight and encoding

- Ensure your .csv file is under 10 MB and saved in the .csv format.
- UTF-8 encoding is supported, but avoid using UTF-8 with BOM (Byte Order Mark). This specific encoding can cause import errors.

## Import OKRs from a CSV file

1. On the *Overview*/*Hierarchy*/*Progress Dashboard* page, select **Import**.

   ![The import icon is highlighted.](/cms_trial/assets/7ff84f5b-2420-40f8-87d4-52a9e1228fba.png)
2. On the **Import OKR file** screen, click **+ Select file**.

   ![Import OKR file modal.](/cms_trial/assets/d0e52f3e-d1bf-4099-89b0-24fd31defeb6.png)
3. Locate the .csv file on your device.
4. Click **Confirm** to finish the upload.
5. Wait till your OKRs are added.
6. Click **Finish import.** This will reset the screen to its initial state and let you to attach a new file.

When the import is complete, you will receive an email confirming that your OKRs imported successfully. If the import fails, you will also be notified.

## Fai.ed to import OKRs (screen)

If there is at least one error, the import will fail, and no OKRs will be added to the module. You may see a screen similar to the one below.

![OKR import error screen.](/cms_trial/assets/0d63c7bd-9113-435c-8bb5-98f99b2fc998.png)

- **Duplicate order numbers** - Each order number should appear only once.
- **Incorrect type** - Ensure the type entries are either “Objective” or “Key result” (case-sensitive).
- **Period mismatch**: Check if the "Period" in your .csv file matches an existing period in the OKR module.
- **Invalid owner**: Use a valid Jira username or email address.
- **Symbols in summary**: You may experience issues with UTF-8 encoding with BOM. While English text typically works fine, entering alphabetic symbols may cause failures.
- **Missing KR values**: Key Results require start, current, and target values.

Correct your data and click the **Finish import** button before you upload your CSV file again.