# Time Spent in 'Blocked' Status

## Scenario

You require a field that displays the amount of time an issue has spent in the “Blocked” status.

In this example, the workflow is configured so that an issue that is blocked uses a status of **Blocked**. In your Jira instance, the status that represents that an issue cannot proceed due to external issues may be different - just substitute your status value in the steps below!

## Resolution

This solution uses the **Time in Status** custom field type which displays the total time an issue has spent with a specific status value.

You are viewing the documentation for **Jira Cloud**.

### On This Page

## Steps to Create

### 1. Create a *Time in Status* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Time in Status** and click **Next**.
7. Select the screens to which the new custom field should be added. Click **Next**.
8. Configure the field (Figure 1, right). Set the **Status(es) to aggregate** pulldown menu to `Blocked` (or select the status that represents an issue that cannot progress due to external issues).
9. Click **Save**.

![Jira Misc Custom Fields (JMCF) Cloud time blocked field configuration](/cms_trial/assets/30ae9ab9-837a-4b06-ad32-0e1b74cf9eb0.png)

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

![Jira Misc Custom Fields (JMCF) Cloud custom field context modification dialog](/cms_trial/assets/d1b63137-b3b8-42d6-9e6b-144a4d4af073.png)