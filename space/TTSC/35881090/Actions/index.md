# Actions

Use **Actions** to set up simple, built-in automations for your SLAs without configuring advanced Jira automation rules.

Actions define what happens when an SLA reaches a specific point or breaches. You can use them to notify people, trigger Jira automation, add comments, or update Jira work items.

For example, when an SLA is breached, you can change the priority, assign the work item to another user, and send a Slack message to your team.

## Video overview

## Why use SLA actions

SLA Actions give teams a simpler way to automate follow-up work around SLAs.

They’re useful when you want lightweight automation without building complex Jira automation rules from scratch. You can manage common SLA-related actions, such as notifications, comments, and work item updates, directly from one place.

Instead of opening each SLA configuration to check its notifications, you can use the *Actions* page to view and manage them from a single home page.

### Example use cases

- An action that sends a Slack message 30 minutes before an SLA breaches.
- An action that triggers a Jira automation rule when an SLA reaches a specific point.
- A combination of actions that changes the priority, assigns the work item to a senior team member, and sends an email when an SLA breaches.

## Where can you manage SLA actions

You can access SLA actions in two ways:

- From the top navigation, select **Actions** to view and manage all actions in one place.
- From a specific SLA configuration, click the **Actions** button to view and manage the actions related to that SLA.

In both cases, you’ll be taken to the *Actions* page. When you open Actions from a specific SLA configuration, the page shows the actions related to that SLA.

Users with the **SLA Configurations** permission can access the *Actions* page. This is the same permission that provides access to the **SLAs** page.

## Prerequisites

- For notification actions to work, make sure you have enabled **Outgoing Mail** in Jira. To do that, click the *cog* icon in the Jira top bar, and open **System** > **Outgoing Mail** > **Enable Outgoing Mail**.
- It is essential to have the related permissions before creating a TTS notification for a specific SLA. The person responsible for creating the notification must have the necessary authorization to access the relevant work items related to the scope of the selected SLA.

## Managing actions

![Actions page showing the list of SLA actions with search, filters, and execution history.](/cms_trial/assets/d7c6358e-e0f1-4b86-8f05-1906fab70e11.png)

The *Actions* page shows all actions in one place.

1. **Search and filter actions –** Use the search field and filters to find actions by keyword, SLA, or action type.

Default actions are created by the app once an SLA is created and are marked with a **DEFAULT** label. You can disable them when needed, but you can’t delete them.

1. **Show or hide disabled actions –** Select **Hide disabled** to remove disabled actions from the list. Clear the checkbox to view them again.
2. **Customize columns –** Use **Columns** to choose which table columns are shown on the page.
3. **Select actions for bulk updates –** Select one or more actions using the checkboxes. After selecting actions, users can perform bulk operations, such as disabling or deleting multiple actions at once.

   ![Multiple SLA actions selected, showing available bulk actions.](/cms_trial/assets/b03bd362-a206-40c2-9b05-e31e174cc305.png)

   This helps administrators quickly clean up, reorganize, or temporarily pause or disable SLA automations across projects.

Default actions can be disabled in bulk. However, they can’t be deleted in bulk or individually. If your bulk selection includes one or more default actions, you won’t be able to delete any of those.

For example, if you select 10 actions and 2 of them are default actions, you won’t be able to delete the selected actions. To use **Bulk delete**, select only non-default actions.

1. **View execution history –** Click **View logs** to check whether an action ran successfully, how long it took, and why it failed. The *Execution history* page opens. For more information, refer to the [section below](https://support.appfire.com/space/TTSC/35881090/Actions#Execution-history).
2. **Manage an individual action –** Open the **More actions** menu to manage a specific action. From here, you can access available options such as editing, disabling, enabling, or deleting the action.
3. **Create a new SLA action –** Click **SLA Action** to create a new action. Users can choose an action type, define when it should be triggered, and configure what happens when the SLA event occurs. For more information, refer to the [related page](https://support.appfire.com/space/TTSC/3308945429/Create+actions).
4. **Edit notification templates –** Open the page-level **More actions** menu to edit notification templates for Slack and email actions and preview them.

   ![SLA notification templates page with the option to edit Email and Slack templates.](/cms_trial/assets/ff29c08c-a09c-4478-865e-5ccc2d142b5c.png)

### Execution history

From this page, you can review each action execution and filter the results. Time to SLA keeps execution history for **up to 90 days**.

![Execution history page showing action execution results and available filters.](/cms_trial/assets/992fcf02-36ac-4c63-a2b3-bb107a9b9c66.png)

1. **Filters –** Use the filters to narrow down the execution history.

   - **Search by work item –** Search for executions by work item key.
   - **Time period –** Filter executions by time period. You can choose **Last 10 days**, **Last 30 days**, **Last 90 days**, or **Custom range**.
   - **Status –** Filter executions by status. Available statuses are **Success**, **Partially failed**, **Failed**, and **Retry in progress**.
   - **Clear –** Removes the selected filters.
2. **Execution list –** The execution list shows each time the action ran for a matching work item.

   - **Work Item Key –** Shows the work item the action ran for. Click the arrow next to the work item key to expand execution details. If an action fails, the expanded row shows which action type failed and the error message returned by Jira or the connected service.  
     -> For example, if an *Add comment* action fails because the request type can’t be accessed, the execution details show the failed action type and the related Jira error message.
   - **Date and Time –** Shows when the action ran.
   - **Execution ID –** Shows the unique ID of the execution. Share this ID with support if you need help understanding why an action failed, wasn’t sent, or didn’t run as expected.
   - **Total Time –** Shows how long the execution took.
   - **Status –** Shows the result of the execution.

     - **Success –** The action ran successfully.
     - **Partially failed –** Some action types ran successfully, but one or more action types failed.
     - **Failed –** The action didn’t run successfully. Expand the row to view the error details.
     - **Retry in progress –** The action couldn’t be completed and is being tried again. This is an intermediate status. For example, if an assignee couldn’t be changed, Time to SLA may retry the action.

If an action includes multiple action types, they are listed in the execution details in the same order as they appear in the action configuration. This order is for readability only. **It doesn’t define an execution sequence**. All action types are triggered at the same time.

If you need actions to run in a specific order, use [Jira automation](https://www.atlassian.com/software/jira/guides/automation/overview#what-is-automation).

1. **Refresh –** Click **Refresh** to update the execution history and see the latest execution results.