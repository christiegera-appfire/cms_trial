# Last Time an Issue was Flagged

## Scenario

You require a field that displays the date and time for when an issue was most recently flagged.

## Resolution

This solution uses the **Last Field Change Time** custom field type which displays the date and time an issue field was last changed.

You are viewing the documentation for **Jira Cloud**.

### On This Page

## Steps to Create

### 1. Create a *Last Field Change Time* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Last Field Change Time** and click **Next**.
7. Select the screens to which the new custom field should be added. Click **Next**.
8. Configure the field (Figure 1, right) by setting **Field to watch** to `Flagged`.
9. Click **Save**.

![Jira Misc Custom Fields (JMCF) Cloud last flagged field configuration](/cms_trial/assets/90ed909e-bd9e-4e66-a5a0-117de8f9a277.png)

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

![Jira Misc Custom Fields (JMCF) Cloud custom field context modification dialog](/cms_trial/assets/38bd22a4-d746-44f8-947a-85887611c80c.png)