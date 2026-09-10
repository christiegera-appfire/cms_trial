# Date of Initial Fix

## Scenario

You require a field that displays the date and time when an issue was initially marked as fixed or resolved.

In this example, the workflow is configured so that an issue is fixed/resolved when it is moved into the **Closed** status. In your Jira instance, the status that represents that an issue has been fixed may be different - just substitute your status value in the steps below!

An interactive walkthrough of this solution is now available! [Play the Arcade!](#Play-the-Arcade)

## Resolution

This solution uses the **Transition Time** custom field type which displays the date and time an issue was transitioned to a specific status.

You are viewing the documentation for **Jira Cloud**.

| **On This Page**   - [Scenario](#scenario) - [Resolution](#resolution) - [Steps to Create](#steps-to-create) - [1. Create a Transition Time custom field](#1-create-a-transition-time-custom-field) - [2. Configure Custom Field Context (Optional)](#2-configure-custom-field-context-optional) - [Play the Arcade](#play-the-arcade) |
| --- |

## Steps to Create

### 1. Create a *Transition Time* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Transition Time** and click **Next**.
7. Select the screens to which the new custom field should be added. Click **Next**.
8. Configure the field (Figure 1, right):

   1. From the **Transition From Status** pulldown menu, select `Any` (or select the status that immediately precedes your resolved status).
   2. From the **To Status** pulldown menu, select `Resolved` (or whichever status represents that issue being fixed).
   3. For **Which Change?** select `Earliest`.
9. Click **Save**.

![contentId-465240183](/cms_trial/assets/6ca68cac-6527-4a25-a2c9-fbe9d57b5725.png)

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

![contentId-465240183](/cms_trial/assets/4e116a2f-75ce-45a9-affa-454038599a96.png)

## Play the Arcade

<https://app.arcade.software/share/LZcOfYT2VW5uWZYeqRT8?ref=share-link>