# Concept of a field

BigPicture visualizes information based on the integrations with other tools you have set up. Field values in Jira, Trello, etc., must be mapped to the App's available fields. Information about the data source can be listed in the “origin” column and shown as an appropriate icon.

There are two possible field options:

- **Native external tool fields** - they display the value from an external platform; if the value is unavailable, it is left empty (if a column is supposed to display Jira “Start Date,” nothing can be displayed for a Trello task - the task doesn’t exist in Jira, so the App can’t find a value for it)
- [**Built-in fields**](/cms_trial/space/SPM/1918832240/Built-in+fields/) **-** can take information from various external platforms and map it to a built-in field, effectively letting you see a single column showing values for multiple task types coming from many external platforms and native BigPicture elements.

When adding a column, the icon on the right indicates what data will be shown—whether it will be based on a value of a Jira field, Trello field, or a built-in field.

![image-20250403-112339.png](/cms_trial/assets/364e5887-4bbd-4c53-b97c-bb279823a451.png)

The Jira icon column displays values from Jira only. This means that nothing is displayed for Trello cards and Basic tasks.

The Trello icon column displays values coming from Trello only. This means that nothing is displayed for Jira issues and basic tasks.

The Built-in icon column displays all values; it finds the appropriate field value in both Jira and Trello and displays it. Native BigPicture Basic tasks are also included.

## How to check the field type

**Method 1:**

Hover your cursor over any field value to see the present setup of the column.

![image-20250403-112703.png](/cms_trial/assets/55406d77-0d62-4944-b8c8-b79bc713d09c.png)

**Method 2:**

1. Click **… More actions** next to the column.
2. Click **Column info**.

![image-20250403-113006.png](/cms_trial/assets/94b3b251-5363-4957-9e29-57f641c22971.png)

## Custom fields created at the BigPicture installation

When you install BigPicture, the App will automatically create the following custom fields, as explained in the table below:

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| **Baseline end date** | Date Picker | Baseline end date field used in BigPicture |
| **Baseline start date** | Date Picker | Baseline start date field used in BigPicture |
| **End date** | Date Picker | End date field used in BigPicture |
| **Progress** | Number Field | Progress field used in BigPicture |
| **Start date** | Date Picker | Start date field used in BigPicture |
| **Task mode** | Select List (single choice) | Task mode field used in BigPicture |
| **Task progress** | Number Field | Progress field used in BigPicture |
| **Risk consequence** | Select List (single choice) | Risk Consequence field used in BigPicture (only issues with both Risk Probability and Risk Consequence values selected will appear in the Risk Matrix) |
| **Risk probability** | Select List (single choice) | Risk Probability field used in BigPicture (only issues with both Risk Probability and Risk Consequence values selected will appear in the Risk Matrix) |
| **Program Increment** | Text Field (single line) | Program Increment field created by BigPicture |

You can check these fields by navigating to **Jira administration (cog icon)** > **Work items** > **Fields** and searching by SoftwarePlant or BigPicture.

## Custom fields from third-party Jira apps in BigPicture

Depending on the functionality of a given plugin, custom fields based on third-party Jira apps may have limited or different functionality in the Cloud version of the product. For example, **Traffic Lights** can be displayed only as a text field.

### JMCF duration field

[Jira Misc Custom Fields](https://marketplace.atlassian.com/apps/27136/jira-misc-custom-fields-jmcf?tab=overview&hosting=datacenter) (duration field) is visible in available fields for [column views](/cms_trial/space/SPM/1918404907/Column+views/)/[card views](/cms_trial/space/SPM/1918536034/Card+views/).

- The JMCF Duration is displayed in 24h mode
- The JMCF Duration is blocked for inline editing even though it is mapped to the Estimation Data Type, which allows for inline editing. This is due to the fact that the JMCF Duration field is a scripted field, which means that it displays the results of calculations involving other fields.

## Built-in fields

See the [Built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/) page to learn more about built-in fields.