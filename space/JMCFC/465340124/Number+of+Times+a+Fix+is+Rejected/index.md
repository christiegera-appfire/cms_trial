# Number of Times a Fix is Rejected

## Scenario

You require a field that displays the number of times an issue resolution has been rejected.

In this example, the workflow is configured so that an issue fix is rejected when it is moved into the **Rejected** status. In your Jira instance, the status that represents the rejection of a fix may be different - just substitute your status value in the steps below!

## Resolution

This solution uses the **Transition Count** custom field type. This custom field creates a number field that, when calculated, displays the number of times an issue has been transitioned *into* a status - in this example, the **Rejected** status.

You are viewing the documentation for **Jira Cloud**.

### On This Page

## Steps to Create

### 1. Create a *Transition Count* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Transition Count** and click **Next**.
7. Select the screens to which the new custom field should be added (Figure 1, right). Click **Next**.
8. Configure the field:

   1. From the **Transition From Status** pulldown menu, select `Any` (or select the status that immediately precedes your rejection status).
   2. From the **To Status** pulldown menu, select `Rejected`.
9. Click **Save**.

![Jira Misc Custom Fields (JMCF) Cloud times rejected field screen association](/cms_trial/assets/327de402-0de6-4a37-b20b-fb8d09546614.png)

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

![Jira Misc Custom Fields (JMCF) Cloud custom field context modification dialog](/cms_trial/assets/bcb2668a-011c-4f37-86a5-779678737ed4.png)