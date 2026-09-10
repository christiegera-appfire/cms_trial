# Formatters

Formatters for **JMCF for Jira Cloud** enable to to change the appearance of your custom fields. The formatting options available depend on the type of field. See the table below for details on which formatting options are available for which types of fields.

Formatting options are currently unavailable for scripted string collection fields and [Time in Status](/cms_trial/space/JMCFC/465633373/Time+in+Status/) custom fields.

**Note**: due to current Atlassian limitations, most formatting options are currently available only on the **issue view**. Formatting for list views is planned for a future release when Atlassian provides API access.

**Note**: Custom fields that have been migrated from Jira Data Center will not include the formatting options that were applied in Data Center - only the definition of the custom field will be migrated.

To apply formatting to a JMCF custom field:

1. Log into your Jira instance as an Administrator.
2. In the upper right corner, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand panel, click **Jira Misc Custom Fields**.
4. Click **My custom fields**.
5. Click the action menu ( [png icon] ) for the field you want to format and select **Edit Formatters**.
6. The Formatters window (Figure 1, right) opens. Set your formatting options and click **Save**.

## Formatters window

![Jira Misc Custom Fields (JMCF) Cloud formatters configuration page](/cms_trial/assets/0ffcf487-0f73-4524-b270-8a57e99dc510.png)

The Formatters window consists of two panels. Specific formatting options for the selected field type are on the left, with a preview of the selected formatting on the right. Additionally, you can preview how the field will display for a specific issue by entering an issue ID or key and clicking **Preview**.

## Formatting options

The formatting options available depend on the type of custom field. Refer to the table below for a quick reference on the formatting options available for each custom field type.

### Global formatters

The Global formatters section includes formatting options that are available for the custom field on every screen.

- **Prefix** - Include a string before the field’s value.
- **Suffix** - Include a string directly after the field’s value.
- **Capitalization** - *String fields only*. Set the capitalization for the entire string.

  - **Uppercase** - Display the string in all capital letters.
  - **Lowercase** - Display the string in all lowercase letters.
  - **Capitalize** - Display the string with normal capitalization formatting.
- **Decimals** - *Number fields only*. Specify the precision of the field, up to 10 decimal places.

### Issue view formatters

The issue view formatters section includes options specific to the issue view.

- **Background color** - Select the background color for the field.
- **Foreground color** - Select the font color for the field.
- **Heading style** - Alter the font size and weight for the field. Select which heading value (H1 through H6) should be applied.
- **Locale** - *Date and datetime fields only*. Select the locale formatting that should be applied to the field value.
- **Timezone** - *Date and datetime fields only*. Select which timezone the field will display.

  - **Show timezone** - Add the specific timezone code to the end of the field value.
- **Month format** - *Date and datetime fields only*. Select how to display month values.

  - **Numeric** - Display the month as a number.
  - **Long form** - Display the full month name.
  - **Short form** - Display the shortened month name (e.g. ‘Mar’ for March)
- **Weekday format** - *Date and datetime fields only*. Select how day values are displayed.

  - **Numeric** - Display the day as a number.
  - **Long form** - Display the full day name.
  - **Short form** - Display the shortened day name (e.g. ‘Wed’ for Wednesday)

You are viewing the documentation for **Jira Cloud**

|  | **String** | **Number** | **Date** | **Datetime** | **User/User collection** | **Duration** |
| --- | --- | --- | --- | --- | --- | --- |
| Capitalization | ✅ | N/A | N/A | N/A | ❌ | N/A |
| Prefix | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Suffix | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Background color\*** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| **Font color\*** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| **Heading style\*** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Decimals | N/A | ✅ | N/A | N/A | N/A | N/A |
| **Localization (country)\*** | N/A | N/A | ✅ | ✅ | N/A | N/A |
| **Timezone\*** | N/A | N/A | ✅ | ✅ | N/A | N/A |
| **Month/Weekday formats\*** | N/A | N/A | ✅ | ✅ | N/A | N/A |
| **Duration string format\*** | N/A | N/A | N/A | N/A | N/A | ✅ |
| **Duration rounding\*** | N/A | N/A | N/A | N/A | N/A | ✅ |
| **Duration unit display behavior\*** | N/A | N/A | N/A | N/A | N/A | ✅ |

**\*Issue view only**