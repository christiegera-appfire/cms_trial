# Create actions

SLA actions let you automate what happens when an SLA starts, is met, or reaches a specific milestone, such as when it is close to breaching, has breached, or has stopped.

Each action has two parts:

- **When the action runs** — the SLA, goals, and trigger event.
- **What the action does** — one or more action types, such as sending an email, adding a comment, changing the assignee, triggering Jira automation, and more.

## Create an action

To create an action:

1. Go to **Time to SLA** > **Actions**.
2. Select **+ SLA Action**.

   ![Actions page showing the SLA Action button used to create a new SLA action.](/cms_trial/assets/8ee1ee9e-a978-469a-94c9-317e868f1ddc.png)
3. Use the fields on the right side of the page to define the scope and trigger for the action.

| **Field** | **Description** |
| --- | --- |
| **Description** | Enter a name or short explanation to help you identify the action. |
| **Apply to** | Choose whether the action applies to a single SLA or all SLAs (global). |
| **Select an SLA** | Select the SLA this action applies to. This field is shown when you choose **Single SLA**. |
| **Applied goals** | Select the SLA goals this action applies to. This field is shown when you choose **Single SLA**.  If an SLA has multiple goals, you can use this feature to configure different notifications for each goal. This flexibility lets you tailor notifications based on specific requirements, such as priority or response time.  **Example**  Imagine you have an SLA with the following goals:   - **High-priority work items**: 1 hour - **Low-priority work items**: 24 hours   In this scenario, you may want to send notifications more frequently for critical work items and notify different users based on the work item’s priority.  This feature makes this possible by allowing you to link specific SLA goals to different notifications, ensuring the right information reaches the right people at the right time.  Goals may not always have names, so use the goal details that appear when you hover over a goal to identify and select the right one. Applied goals selector showing available SLA goals for a Single SLA action. |
| **Trigger when SLA** | Choose the SLA event that runs the action. Available trigger options include:   - **is breached** - **will be breached in** - **has been breached for** - **percentage is reached** - **is over (SLA has stopped) –** Runs the action when the SLA finishes, regardless of whether the SLA was met or breached. Use **is met** instead when you want the action to run only when the SLA finishes successfully. - **is started –** Runs the action when the SLA starts for the first time. If the SLA is reset and starts again, the action does not run again.  If the SLA has multiple start conditions connected by **All of the following**, the action runs only after all required conditions are met and the SLA timer enters the running state. - **is met –** Runs the action when the SLA finishes successfully within its goal. The action does not run when the SLA finishes after breaching its goal. To run an action when an SLA breaches, use the is breached trigger.   Depending on the trigger you select, additional fields may appear. For example, if you select **will be breached in**, you’ll need to define how much time before the breach the action should run. |
| **Activate notifications from a specific date** | By default, notifications are sent for all matching work items, including past and future matches. Enable **Activate notifications from a specific date** if you only want notifications to start from a certain date. Once selected, the **Effective From** date picker appears, allowing you to choose the date when notifications should start.  Use this option if you don’t want the action to run for older matching work items. Activate notifications from a specific date option with the Effective From date picker. |
| **Repeat this action** | Run the action more than once, when supported. For example, enter `8h` to repeat the action every 8 hours. You can also choose when the action should stop repeating:   - After a certain number of notifications have been sent - After a certain percentage of the SLA goal has passed - After a certain duration has passed   Assignee, priority, and Jira field updates can’t be repeated. |
| **Run with permissions of** (*This field is available only when you edit an action*.) | SLA actions run with the Jira permissions of the user who configured the SLA action. This means an action can only perform operations that this user is allowed to perform in Jira.  For example, an action may fail if that user:   - is inactive or no longer exists, - doesn’t have permission to view/update the project or work item, - doesn’t have permission to add comments or change fields.   To avoid permission-related failures, you can edit the action and use **Run with permissions of** to choose a user who has the required permissions for the projects and work items where the action will run. Run with permissions of field for selecting the Jira user whose permissions the action uses. |

1. Use the action type gallery on the left side of the page to choose what should happen when the action runs.

After you select an action type, it appears in the **Actions** section below the gallery. You can expand, collapse, configure, or delete each selected action type.

![Action gallery showing selected action types added to the Actions section for configuration.](/cms_trial/assets/e896a178-4818-4d73-ac6f-28b92c47c771.gif)

| **Action type** | **What it does** |
| --- | --- |
| **Send an email** | Sends an email notification. |
| **Send a Slack message** | Sends a Slack message using a webhook URL. |
| **Trigger Jira automation** | Triggers a Jira automation rule using a webhook URL. |
| **Change assignee** | Use **Change assignee** to assign the Jira work item to another user when the action runs. For example, when an escalation SLA is met, you can reassign the work item from an escalation manager to its original support team. |
| **Add comment** | Adds a comment to the Jira work item. |
| **Set Jira field** | Use **Set Jira field** to update a Jira work item field. For example, select the **is met** trigger and use **Set Jira field** to update a text field named **SLA Indicator** to `MET`. |
| **Change priority** | Changes the priority of the Jira work item. |
| ***Change status*** | *Not available yet.* |

### Use dynamic parameters

Some action types support dynamic parameters. Dynamic parameters let you include SLA or Jira work item details in messages, comments, and notification content.

You can use dynamic parameters in:

- Email subjects and bodies
- Slack messages
- Comments

To add a dynamic parameter, type **$** or select one of the available parameter chips. For the full list of parameters, refer to [this page](/cms_trial/space/TTSC/35881100/Action+parameters/).

1. Select one or more action types.
2. Configure the selected action types.
3. Select **Save**.

## Action types

You can add more than one action type. For example, one combination of actions can send an email, add a comment, and change the priority when an SLA breaches.

The order of action types does not matter. All selected action types are triggered at the same time. If you need staged changes, such as gradually increasing the priority over time, refer to the [Jira automation documentation](http://atlassian.com/software/jira/guides/automation/overview).

Some action types can only be added once. For example, a work item can only have one assignee and one priority at a time, so Time to SLA prevents adding multiple assignee or priority updates to the same action to prevent conflicting updates.

### Send an email

Use **Send an email** to notify users, groups, or fields when the action runs.

![Send an email action configuration with fields for recipients, subject, and email body.](/cms_trial/assets/cb49c3c7-600f-44fc-a45a-0d6e84ec4b76.png)

Configure the following fields:

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Subject** | Enter the email subject. You can use dynamic parameters. |
| **Body** | Enter the email body. You can use dynamic parameters. |
| **Recipients** | Choose who should receive the email, then select **Add**. |

If needed, you can click **Preview** to review the email message.

### Send a Slack message

Use **Send a Slack message** to send a Slack notification when the action runs. Configure the following fields:

![Slack message action configuration showing the webhook URL and message fields.](/cms_trial/assets/ef8d51b8-8331-4077-8dcc-a5bfd4737aaa.png)

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Slack webhook URL** | Enter the Slack webhook URL that should receive the message. To find or create a Slack channel webhook URL, follow these steps:   1. **Create a Slack app**:     - Navigate to the [Slack API: Your Apps](https://api.slack.com/apps) page.    - Click **Create an App**, and select **From scratch**.    - Provide a name for your app, and select the workspace where you want to post messages. 2. **Enable Incoming Webhooks**:     - Go to the **Incoming Webhooks** in your app's settings.    - Toggle the **Activate Incoming Webhooks** switch to **ON**. 3. **Generate a Webhook URL for a channel**:     - Click **Add New Webhook to Workspace**.    - Select the channel where the app will post messages.    - Click **Allow** to authorize.    - After authorization, you'll receive a unique webhook URL in the format `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX` that you can copy and paste into the Slack message field in TTS.   For more details, refer to [Slack’s Incoming Webhooks documentation](https://api.slack.com/messaging/webhooks#create_a_webhook). |
| **Body** | Enter the Slack message. You can use dynamic parameters. |

If needed, you can click **Preview** to review the Slack message and the parameters.

### Trigger Jira automation

Use **Trigger Jira automation** to run a Jira automation rule when the action runs.

![Trigger Jira automation action showing webhook URL and optional webhook secret fields.](/cms_trial/assets/430863ca-38a1-48f2-a6aa-b0088d1efe36.png)

Configure the following fields:

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Automation webhook URL** | Enter the webhook URL from your Jira automation rule. For more information, refer to the [documentation](/cms_trial/space/TTSC/1464075666/Use+SLA+actions+with+Jira+automation/). |
| **Automation webhook secret** | Enter the webhook secret, if your automation rule requires one. |

### Change assignee

Use **Change** **assignee** to assign the Jira work item to another user when the action runs. Search for and select the user who should become the assignee.

You can add this action type only once because a Jira work item can have only one assignee at a time. After you add it, the option to add another assignee action is disabled.

### Add comment

Use **Add comment** to add a comment to the Jira work item when the action runs.

Configure the following fields:

![Add comment action configuration with comment text and comment visibility options.](/cms_trial/assets/9f0cde3e-6302-45cf-85e2-7f061691286d.png)

|  |  |
| --- | --- |
| **Field** | **Description** |
| **Comment** | Enter the comment text. You can use dynamic parameters. |
| **Comment visibility** | For Jira Service Management requests, choose whether the comment is internal or shared with the customer. For other project types, comments are always public. |

For Jira Service Management requests, you can choose the comment visibility. For other project types, comments are always public.

If needed, you can click **Preview** to review the comment.

### Set Jira field

Use **Set Jira field** to update a Jira work item field.

**Supported fields include:**

- Labels
- Components
- Priority
- Text fields (single line)
- User pickers (single and multi-select)
- Select lists (single and multiple choice)
- Radio buttons

This feature excludes custom fields supplied by third-party vendors. Don't see a custom field you need? [Let us know](https://appfire.atlassian.net/servicedesk/customer/portals) what's missing so we can prioritize it in a future update.

Select the field you want to update from the **Jira work item field** dropdown. The options you see depend on the field you select.

For example, if you select a date field, a date picker appears so you can choose the date to set. If you select a multi-value field, you can choose how the selected value should be applied:

| **Option** | **Description** |
| --- | --- |
| **Replace value** | Replaces the current field value with the value you enter. |
| **Add to current value** | Adds the value you enter to the existing field value. |

For example, you can update the **Components** field when an SLA breaches. Select **Components**, select the component you want to add, and choose **Add to current**. When the action runs, Time to SLA adds the selected component to the work item without removing the existing components. If you choose **Replace value** instead, the existing components are removed and replaced with the component you selected.

![Set Jira field action showing the Components field with the Add to current option selected.](/cms_trial/assets/8701f0b9-58d5-4be8-b580-0b33ca8d5b4a.png)

### Change priority

Use **Change** **priority** to update the priority of the Jira work item when the action runs. Select the priority from the dropdown.

You can add this action type only once because a Jira work item can have only one priority at a time. After you add it, the option to add another priority action is disabled. If you need to change priority in stages, use Jira automation.