# First Approver or Approvers of Issue

## Scenario

You require a field that displays the Jira user or users who first approved an issue.

In this example, the workflow is configured so that an issue is approved when it is moved into the **Approved** status. In your Jira instance, the status that represents an issue’s approval may be different - just substitute your status value in the steps below!

## Resolution

Depending on whether your approval process requires a single user or multiple users, the custom field type will change. For a single approver, this solution uses the **Transitioned by User** custom field type. For multiple approvers, you can use the **Transitioned by Users** . This custom field creates a User field that, when calculated, displays the profile photo and user name of a Jira user; hovering over the field value will open a pop-up window displaying more details on that user, including their email address.

You are viewing the documentation for **Jira Cloud**.

### On This Page

## Steps to Create

### 1. Create a *Transitioned by User* or *Transitioned by Users* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Transitioned by User** (for a single approver) or **Transitioned by Users** (for multiple approvers) and click **Next**.
7. Select the screens to which the new custom field should be added (Figure 1, right). Click **Next**.
8. Configure the field:

   1. From the **Transition From Status** pulldown menu, select `Any` (or select the status that immediately precedes your approval status).
   2. From the **To Status** pulldown menu, select `Approved`.
   3. For **Which Change?** select `Earliest`.
9. Click **Save**.

![Jira Misc Custom Fields (JMCF) Cloud first approver screen association](/cms_trial/assets/9b9ca55a-e934-4d9a-b354-e404fc26e86a.png)

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

![Jira Misc Custom Fields (JMCF) Cloud custom field context modification dialog](/cms_trial/assets/1cb60ac6-6146-43e0-bcdc-fd54a97dd69f.png)