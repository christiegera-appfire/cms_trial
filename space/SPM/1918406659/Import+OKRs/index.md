# Import OKRs

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The import option lets you import Objectives and Key Results directly from external sources into the OKR module, making tracking and alignment easier.

You can import OKRs to BigPicture using API endpoints. Visit the [BigPicture Developer Portal](https://developer.bigpicture.one/reference/fetchobjectivesbyids) for details.

## Permissions

Only [permitted users](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918505859) can import OKRs:

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
| **Order\*** | **Type\*** | **Summary\*** | **Status\*** | **Period\*** | **Owner\*** | **Weight** | **OKR type** | **Labels** | **Teams** | **Expected start date** | **Expected end date\*** | **Start value\*** | **Current value\*** | **Target value\*** | **Description** |
| 1 | Objective | Strategic theme/ Objective name | On track | Q4 Y2025 | Agnette Smith |  | Strategic theme |  |  |  |  | 0 | 0 | 10 |  |
| 1.1 | Objective | Sub-theme name | not Started | Q3 Y2025 | Agnette Smith |  | Company |  | Alpha, Beta |  |  | 0 | 0 | 10 |  |
| 1.2 | Objective | Sub-objective name | AT RISK | Q3 Y2025 | agnette.smith@appfire.com |  | Team |  | Alpha |  |  | 0 | 0 | 20 |  |
| 1.2.1 | Milestone | Milestone name |  |  |  |  |  |  |  |  | 11/03/2025 |  |  | 35% |  |
| 1.2.2 | Key result | KR name | On track | Y2025 | Andrea Xu |  |  |  |  |  |  | 0 | 0 | 15 |  |

### Required CSV fields

Ensure that none of the following headers and data under those headers are missing in your file:

- **Order**—Each OKR is assigned a unique numeric identifier. Top-level objectives usually begin with whole numbers (e.g., 1, 2), while sub-themes, sub-objectives, Key Results, Jira work items, and OKR milestones use decimal numbers (e.g., 1.1, 1.2.2) to show their connection to the parent.
- **Type** - Specify whether the row represents an Objective, a Key Result, a Jira work item, or a milestone. Call Strategic themes and sub-objectives “Objectives” in the import file. This field is case-sensitive.

The **Type** column in the CSV file is not the same as the **OKR Type**. These are two separate columns.

| **Order** | **Type** | **Description** |
| --- | --- | --- |
| 1 | Objective | Top-level Strategic theme/Objective |
| 1.1 | Objective | Sub objective/Sub-theme |
| 1.2 | Objective | Sub-objective |
| 1.2.1 | Objective | Sub-objective |
| 1.2.1.1 | Key result | Manual Key Result |
| 1.2.1.2 | Auto key result | Automatic Key Result |
| 1.2.1.2.1 | Issue | Jira work item linked to a Key Result |
| 1.2 | Objective | Sub-objective |
| 1.2.1 | [Milestone](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=OKR%20milestones&linkCreation=true&fromPageId=1918406659) | Sub-objective’s milestone |

- **Period** - The timeframe for the OKR. It must match an existing period in the OKR module. (This does not apply to OKR milestones.)
- **Owner** - The OKR owner's username or email address. The username and email must match the Jira user added to the app. (This does not apply to OKR milestones.)
- **Expected end date** (milestone) - The milestone due date.
- **Status** - The current status of the OKR. The status must match the built-in statuses in the OKR module. This field is not case-sensitive. The OKR milestone status is calculated dynamically. The app ignores any entries in the CSV.
- **Start value** (Key Result) - The initial value of the Key Result.
- **Current value** (Key Result) - The current value of the Key Result.
- **Target value** (Key Result, milestone) - The target value for the Key Result and milestone.

- The start/current/target values for the KRs are required since KRs are imported as [manual KRs](/cms_trial/space/SPM/1918702967/Manual+KR/). By default, the **Measure** **as** unit for these values is **Numeric**. When the OKRs are imported, you can change the progress settings (values and units) for the imported KRs or convert them to [auto-KRs](/cms_trial/space/SPM/1918670238/Auto-KR/).

### Optional CSV fields

The following fields are optional for OKRs and do not apply to milestones (except for the Expected End Date).

- **Expected Start/End Date** - If the OKR's start and end dates (format: DD/MM/YYYY) are missing, they will be set based on the period. Milestones do not fall under the OKR period, so they must have an Expected End Date (due date).
- **Description:** A detailed explanation of the OKR.
- **OKR type:** The type of OKR (for example, Personal, Team, or Organizational).
- **Teams:** A multi-value field to indicate which teams are involved with this OKR.
- **Labels:** A multi-value field to assign labels to OKRs for easy categorization.
- **Weight:** Represents the OKR’s significance.

### Pre-existing data in the OKR module

You cannot import data that is not in the OKR module. If your .csv file does not have the following columns:

- Owners (users)
- Teams
- Labels
- OKR types (Note that you do not need to add the **Strategic theme** as a type in the module settings)
- Periods

—the import will fail.

- Status - The status must match the built-in statuses in the OKR module.
- Custom field - The custom field name must match the field name configured in the OKR Settings exactly.

### CSV file weight and encoding

- Ensure your .csv file is under 10 MB and saved in the .csv format.
- UTF-8 encoding is supported, but avoid using UTF-8 with BOM (Byte Order Mark). This specific encoding can cause import errors.

## Import OKRs from a CSV file

1. On the *Overview*/*Hierarchy*/*Progress Dashboard* page, select **Import**.

   ![The import icon is highlighted.](/cms_trial/assets/009ac181-fdff-41b4-9d9e-72743f38b98b.png)
2. On the **Import OKR file** screen, click **+ Select file**.

   ![Import OKR file modal.](/cms_trial/assets/7393ef0f-bd6d-446f-9c5b-d902c57de7b3.png)
3. Locate the .csv file on your device.
4. Click **Confirm** to finish the upload.
5. Wait till your OKRs are added.
6. Click **Finish import.** This will reset the screen to its initial state and let you to attach a new file.

When the import is complete, you will receive an email confirming that your OKRs imported successfully. If the import fails, you will also be notified.

## Failed to import OKRs (screen)

If there is at least one error, the import will fail, and no OKRs will be added to the module. You may see a screen similar to the one below.

![OKR import error screen.](/cms_trial/assets/51df6492-f130-4fd1-ba3d-70432ded9a70.png)

- **Duplicate order numbers** - Each order number should appear only once.
- **Incorrect type** - Ensure the type entries are either “Objective” or “Key result” (case-sensitive).
- **Period mismatch**: Check if the "Period" in your .csv file matches an existing period in the OKR module.
- **Invalid owner**: Use a valid Jira username or email address.
- **Symbols in summary**: You may experience issues with UTF-8 encoding with BOM. While English text typically works fine, entering alphabetic symbols may cause failures.
- **Missing KR values**: Key Results require start, current, and target values.

Correct your data and click the **Finish import** button before you upload your CSV file again.