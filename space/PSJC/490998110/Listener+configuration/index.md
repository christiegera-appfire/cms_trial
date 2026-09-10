# Listener configuration

This page covers how to create, configure, and manage your SIL Listeners, including understanding the events they can respond to. You'll learn the essential steps to get your listeners up and running effectively.

**Prerequisite:**

You must have Jira administrator permissions to create and manage SIL listeners.

## How to access the SIL Listeners configuration page

To open the SIL Listeners configuration page:

- Go to **Apps** > **Manage apps** > **Power Scripts**> **Configurations** > **Automations** > **Listeners**. If you haven’t configured any listeners yet, the configuration page will be empty.

![Power Scripts for Jira Cloud listeners configuration panel](/cms_trial/assets/0b0f507b-43f0-4bb5-acad-337675d16cf5.png)

The listeners page shows all configured listeners in a table with the following columns:

| **Column** | **Description** |
| --- | --- |
| **Script** | - Shows the script file path. - Click to access the file in the SIL Manager. |
| **User** | - The user account under which the script executes. - Shows the specific user if one was selected, or `[caller]` if the script runs as the user who triggered the event. |
| **Events** | - Lists the events that trigger the listener. - You can configure multiple events with the same script. |
| **Filters** | - If applicable for the selected events, shows which projects and/or issue types the listener is configured for. - This is optional, and if left unset, the listener will trigger for all projects and issue types. |
| **Execution** | - Shows whether execution is synchronous or asynchronous, as well as if the listener is enabled. - Disabled listeners display a corresponding label in this column. |
| **Operations** | **Edit** and **Delete** buttons for managing the listener. |

---

## How to create a SIL Listener

Each SIL Listener entry represents a script that runs for an event. To create a new SIL Listener:

1. Navigate to the SIL Listeners configuration page and click **Add listener**.

![Power Scripts for Jira Cloud add SIL listener dialog](/cms_trial/assets/1b469dbe-0f22-406c-a09e-d5194ffb1471.png)

1. Configure the listener by providing the following settings:

| **Setting** | **Descritption** |
| --- | --- |
| **Choose the script** | Select the SIL script file that will execute when the event occurs. You can browse and select from existing scripts in your SIL Manager. |
| **Enabled** | You can easily enable or disable listeners without deleting them.   - Leave checked to activate the listener. - When unchecked, the listener won’t execute. |
| **Asynchronous** | Determine how Power Scripts processes the listener execution:   - When checked for asynchronous execution (recommended for Cloud), the listener's script is scheduled for execution on a separate thread immediately. This means it runs independently and won't block the core Jira event, optimizing performance in the Cloud environment. - Leave unchecked for synchronous execution. While Power Scripts attempts to execute these in sequence, all communication with Jira Cloud remains asynchronous. Use this setting primarily when the internal execution order of multiple listeners on the same event is critical and your script has a very short runtime.   See [Understanding Listener execution](/cms_trial/space/PSJC/513278324/Understanding+listener+execution/) for guidance on choosing the right mode. |
| **If you want to run the script as a user, select one** | Define the Jira user account to impersonate when the script runs. If this field is left blank, the script will execute with the permissions of the user who triggered the event (indicated as `[caller]` in the **User** column).  This setting is crucial for scripts that require elevated permissions or need to operate under a specific user's context. |
| **Select the events you want to react to** | Choose one or more events from the dropdown that will trigger this listener.  For a detailed list of supported events, see [this section](/cms_trial/space/PSJC/490998110/Listener+configuration/).  To understand what data and functions are available for each event type, see [Understanding listener script context](/cms_trial/space/PSJC/490998238/Understanding+listener+script+context/).  While you can configure multiple listeners for the same event, this is not recommended for optimal performance. For configuration best practices and execution details, see [Best Practices for listener configuration](/cms_trial/space/PSJC/490998110/Listener+configuration/). |
| **Projects & issue types for which this listener is applicable** | (Appears for issue-related events) When you select issue-related events, additional filtering options become available:   - **Select projects**: (Optional) Limit the listener to specific projects. Leave blank to trigger for all projects. - **Select issue types**: (Optional) Limit the listener to specific issue types. Leave blank to trigger for all issues.   Issue types can only be selected in correlation with projects. |

1. Click **Add**.

---

## How to manage SIL Listeners

You manage your listeners from the SIL Listeners configuration page.

| **To…** | **Do this…** |
| --- | --- |
| Edit a listener | 1. To modify an existing listener's settings, click the **Edit** icon in the *Operations* column on the **SIL Listeners** page. 2. Make your updates, then click **Save**. |
| Delete a listener | - To remove a SIL Listener, click the **Delete** icon in the *Operations* column on the **SIL Listeners** page and confirm your action. |
| Enable or disable a listener | 1. Click the **Edit** icon in the *Operations* column for the listener you want to enable or disable. 2. Check or clear the **Enabled** setting to activate or deactivate the listener, respectively. 3. Click **Save**. |
| Switch between synchronous and asynchronous execution modes | 1. Click the **Edit** icon in the *Operations* column for the listener you want to modify. 2. Check or clear the **Asynchronous** setting:     - Check the box to set the listener to **Asynchronous** execution.    - Clear the box to set the listener to **Synchronous** execution. 3. Click **Save**. |

---

## Supported events

Power Scripts can respond to these Jira events:

| **Event Type** | **Events** | **When they trigger** |
| --- | --- | --- |
| Attachments | - Attachment Added - Attachment Removed | When files are attached or removed from issues. |
| Boards | - Board Created - Board Updated - Board Deleted - Board Config Updated | When Scrum boards are modified. |
| Filters | - Filters Created - Filters Updated - Filters Deleted | When saved filters change. |
| Issue | - Issue Created - Issue Updated - Issue Deleted | When an issue is created, modified, or deleted. |
| Issue comments | - Issue Commented - Issue Comment Edited - Issue Comment Deleted | When issue comments are added, modified, or removed. |
| Issue links | - Issue Link Added - Issue Link Deleted - Issue Link Updated | When issue relationships change. |
| Project | - Project Created - Project Updated - Project Deleted - Project Soft Deleted | When projects are created, modified, removed, or moved to trash. The soft-deleted event is triggered when a project is moved to trash, and the deleted event is triggered when the project is permanently removed. |
| Sprint | - Sprint Created - Sprint Updated - Sprint Deleted - Sprint Started - Sprint Closed | When Scrum sprints change status. |
| Version | - Version Created - Version Updated - Version Deleted - Version Released - Version Unreleased - Version Moved | When project versions change. |
| User | - User Created - User Updated - User Deleted | When users are created, their profiles are updated, or they are removed from the system. |

---

## Best practices for listener configuration

Following these guidelines will help you create better listener configurations that are easier to manage and work more reliably.

- **Multiple Listeners per Event**: You can configure multiple listener entries for the same event. While it's possible to define an execution order for synchronous listeners, this is generally not recommended for optimal performance and maintainability.

For technical details about execution order, see [Execution order and multiple Listeners](/cms_trial/space/PSJC/513278324/Understanding+listener+execution/).

- **Multiple Events per Listener**: A single listener entry can be mapped to multiple events, making the same script react to various triggers.
- **Recommended approach**: It is almost always best practice to have one comprehensive script per event. This centralizes all logic for a given event into a single file, simplifying maintenance, improving readability, and generally providing optimal performance by minimizing overhead.