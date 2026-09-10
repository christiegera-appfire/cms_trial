# Display the Sprint End Date

## Scenario

You require a field that displays the date the issue’s Sprint ends.

## Resolution

This solution uses the **Scripted Datetime** custom field type which displays the end date of the issue’s Sprint. The custom field is also configured to use the **Sprint** value as a dependency - if that value is changed, the custom field will automatically be recalculated!

**Note**: the configuration detailed below uses the **Sprint** field as both a dependency and within the script itself; however, in order to access the field value within the script, you must reference the field by the field name (e.g. `customfield_10020` in this instance) instead of its label (“Sprint”). To find the field name, check the **Dependencies** field where the **Sprint** field is listed with its field name in parentheses (Figure 1, below). You need to use this value in the script!

![Field name is included in parentheses](/cms_trial/assets/fa6aff7f-981b-40fb-8f69-37f4a43b4784.png)

You are viewing the documentation for **Jira Cloud**.

| On This Page  - [Scenario](#scenario) - [Resolution](#resolution) - [On This Page](#on-this-page) - [Watch the Video](#watch-the-video) - [Follow the Steps](#follow-the-steps) - [1. Create a Scripted datetime custom field](#1-create-a-scripted-datetime-custom-field) - [2. Configure Custom Field Context (Optional)](#2-configure-custom-field-context-optional) |
| --- |

## Watch the Video

## Follow the Steps

### 1. Create a *Scripted datetime* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Scripted datetime** and click **Next**.
7. Select the screens to which the new custom field should be added. Click **Next**.
8. Configure the field (Figure 2, right):

   1. In the script editor, enter the following:

      ```text
      // identify the sprints to which this issue is assigned (or an empty list if not assigned)
      const sprints = (await api.issue.getField(issue, "customfield_10020")) || []

      // write the returned sprints to the console for debugging
      console.log("sprints:",JSON.stringify(sprints,null,2))

      // locate the first active sprint
      const activeSprint = sprints.find((sprint)=>sprint.state==='active')

      // report the end date of the active sprint (if found, null otherwise)
      return activeSprint?.endDate
      ```
   2. In the **Dependencies on other fields** field, select `Sprint`.
9. Optionally, you can test the results of the script by entering an issue ID in the **Test with issue** field and clicking **Test**.
10. Click **Save**.

![sprintEndDate-FieldConfiguration.png](/cms_trial/assets/9aee37b5-b595-4432-9926-5a2228fa2aa0.png)

### 2. Configure Custom Field Context (Optional)

When a custom field is created, it is added to the selected screens, but it is also added to *every issue type* and *every project*. If a custom field should only be added to specific issue types and/or projects, you need to edit the custom field context.

1. Open the custom field configuration:

   1. From the My Custom Fields page, click the **Contexts** link for the new custom field.
   2. Through the native Jira menus:

      1. In the upper right corner of the Jira window, click **Settings** ( ⚙️ ) and select **Issues**.
      2. In the left-hand panel, click **Custom fields**.
      3. Locate your new custom field in the list and click **Action** at the far right. Select **Contexts and default value**.
2. Update the context for your custom field as necessary:

   1. To add a new context, click **Add new context**.
   2. To update the existing context, click **Edit context** or **Edit Configuration**.
   3. For specific steps on modifying contexts, see this page: <https://support.atlassian.com/jira-cloud-administration/docs/edit-a-custom-field-context/>

![contentId-861896776](/cms_trial/assets/ddb900c6-0346-40c0-9613-b3fc942c9b94.png)