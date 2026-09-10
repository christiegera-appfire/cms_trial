# Event-based actions

An **Event-based action** is a series of one or more JMWE post functions that run when a change is made to an issue, such as when fields are modified, an issue is transitioned, or a comment is added.

Some examples of what can be achieved through Event-based Actions are:

- Synchronizing changes to a field with related issues such as sub-tasks, linked issues, epics, etc.
- Calculating the value of a field based on the values of another field. See [this post](https://appfire.com/resources/blog/mwe-cloud-guide-how-to-calculate-field-values) for a demonstration.
- Copying a comment added by a customer on a Service Management request to linked Jira Software issues.
- Validating data when a user edits an issue field on the issue view screen (as opposed to validating field values during a transition, for which you should use a [Validator](/cms_trial/space/JMWEC/465474068/Validators/)). See [this video](https://hub.appfire.com/guides/getting-started-with-jmwe-cloud-guide/how-to-validate-field-changes/) for a demonstration.

**Warning**: JMWE Event-based actions utilize webhooks to enable events to trigger the execution of the Action; **Atlassian has established a limit of 100** ***dynamic*** **webhooks per Connect app, per tenant** (there is no published limit on static webhooks). This means that you will be limited to 100 Event-based actions that utilize dynamic webhooks on your instance. Please refer to the **Events** section below to determine if the events you need to monitor use static or dynamic webhooks.

This is an Atlassian limitation and cannot be overridden by Appfire.

## Events

Nearly any issue event can trigger an Event-based Action; the Event configurations determine which specific event will trigger the action.

**Note**: All Event-based actions run JMWE post functions which need at least one issue on which to operate. In the case of events not related to issues (for example, Project Created), the issues against which the post functions will run need to be the result of a JQL query. Due to Atlassian’s Cloud API there is no way to bypass this requirement.

**Warning**: Currently, only one event can be selected for an Event-based Action. If you need to trigger the same sequence of post functions for multiple events, it is recommended that you do the following:

1. Create a [Shared Action](/cms_trial/space/JMWEC/466288975/Shared+actions/) for the sequence of post functions that should run after the event.
2. Create an **Event-based Action** for the first event that should trigger the action.
3. In the **Post-functions** configuration for the action, use the [Shared Action post function](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/) to add the sequence of post functions you created in Step 1.
4. Duplicate the **Event-based Action** for each of the events needed.

When you create an Event-based Action in this way it makes some edits or updates easier. If you need to modify the post functions that run during the event (e.g. change the configuration of an existing post function or add a new post function), you can edit the **Shared Action**, and those changes will be applied to all of the actions that utilize that Shared Action.

The following events are able to trigger an Event-based Action:

Issue-related events

| **Event** | **Dynamic** 🌊  **or Static** ⛰️ | **Notes** |
| --- | --- | --- |
| Issue Created | 🌊 |  |
| Issue Updated | 🌊 |  |
| Issue Deleted | 🌊 | Post functions that modify the current issue will fail, as the issue is already deleted by the time the event is received. |
| Issue Commented | 🌊 |  |
| Comment Updated | 🌊 |  |
| Comment Deleted | 🌊 |  |
| Issue Transitioned | 🌊 | Can be set to specific transitions, or all transitions. |
| Issue Field Value Changed | 🌊 | Configured to monitor specific fields. |
| Attachment Created | ⛰️ |  |
| Attachment Deleted | ⛰️ |  |
| Issue Link Added | ⛰️ | Post functions configured are run on issues based on the direction of the associated issue link type. **See below**. |
| Issue Link Deleted | ⛰️ |
| Work Log Created | ⛰️ |  |
| Work Log Updated | ⛰️ |  |
| Work Log Deleted | ⛰️ |  |
| Work Started On Issue | ⛰️ |  |
| Work Stopped On Issue | ⛰️ |  |
| Issue Assigned | 🌊 |  |
| Issue Resolved | 🌊 |  |
| Issue Closed | 🌊 |  |
| Issue Reopened | 🌊 |  |
| Issue Moved | 🌊 |  |

Project-related events

| **Event** | **Dynamic** 🌊 **or Static** ⛰️ | **Notes** |
| --- | --- | --- |
| Project Created | ⛰️ |  |
| Project Updated | ⛰️ |  |
| Project Deleted | ⛰️ |  |
| Project Restored (from Delete) | ⛰️ |  |
| Project Archived | ⛰️ |  |
| Project Restored (from Archived) | ⛰️ |  |

Sprint-related events

| **Event** | **Dynamic** 🌊 **or Static** ⛰️ | **Notes** |
| --- | --- | --- |
| Sprint Created | ⛰️ |  |
| Sprint Updated | ⛰️ |  |
| Sprint Deleted | ⛰️ |  |
| Sprint Started | ⛰️ |  |
| Sprint Closed | ⛰️ |  |

Version-related events

| **Event** | **Dynamic** 🌊 **or Static** ⛰️ | **Notes** |
| --- | --- | --- |
| Version Created | ⛰️ |  |
| Version Updated | ⛰️ |  |
| Version Deleted | ⛰️ |  |
| Version Merged | ⛰️ |  |
| Version Moved | ⛰️ |  |
| Version Released | ⛰️ |  |
| Version Unreleased | ⛰️ |  |

User-related events

| **Event** | **Dynamic** 🌊 **or Static** ⛰️ | **Notes** |
| --- | --- | --- |
| User Created | ⛰️ |  |
| User Updated | ⛰️ |  |
| User Deleted | ⛰️ |  |

- **Issue Link Added**, **Issue Link Deleted**: When you select one of these events, the **Post-functions** configured are run on issues based on the direction of the associated issue link type. For example, when the issue link type between a *Dev* task and *Testing* task is *Dev* `is blocked by` *Testing*, the post function is run on the *Testing* task.

## Administration

![Administration page for managing Event-based actions](/cms_trial/assets/24f11012-6a08-4c3e-94bc-b2997d58ecf9.png)

To access **Event-based Actions**:

1. Log into your Jira instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **Apps**.
3. Under *JIRA MISC WORKFLOW EXTENSIONS* in the left-hand panel, click **Event-based Actions**.

The Event-based Actions page (Figure 1, above) lists all Event-based Actions that have been created, as well as the following:

- **Search** - Filter the list of Event-based actions by action ID.
- **Create new action** - Click to create a new Event-based Action.
- **Shared action list** - A list of all Event-based Actions for the instance. The list includes the following information:

  - **Enabled** - Status of an Event-based Action. *By default, a newly created Event-based Action is enabled.*
  - **Action Name** - The name of the Event-based Action. Click the name to edit the Event-based Action.
  - **Event(s)** - The event or events that will trigger the action.
  - **Projects** - The number of projects to which the Event-based Action has been applied.  
    [note icon] **Hold the pointer over the badge to see a list of projects in which the Event-based Action is used.**
  - **By** - The user who created the action, or the last user to edit or enable/disable the action.
  - **Last modified** - When the action was last modified (edited or enabled/disabled).
  - **Post-functions** - The number of post functions included in the Event-based Action.   
    [note icon] **Hold the pointer over the badge to see a list of the post functions included in the Event-based Action.**
  - **Action menu** - Click to open a menu with specific actions for the Event-based Action:

    - **Duplicate** - Create a copy of the Event-based Action. The new action will have the same name as the original, with “- copy” appended.
    - **View Summary** - Open the Summary window (Figure 2, below), listing the triggering event for the action, the projects and issues included in the action, and the Post functions that will run in the Event-based Action.
    - **ID** - The Jira ID of the Event-based Action. Click the menu option to copy the ID value to your clipboard. This value can be used in the [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/) page to filter the logs by **Action ID**.
    - **Delete** - Permanently delete the Event-based Action.

![admin-EventBasedActionSummary.png](/cms_trial/assets/28176901-38f2-427e-b6bc-3e8b0c18e263.png)

In the event that an Event-based Action encounters a serious issue, it may be disabled by Appfire. In these circumstances, the **Enabled** column will show as either **Disabled** or **Blocked** with the message “This event-based action was disabled/blocked by Appfire. Please [contact Appfire support](http://appf.re/support) for details”.

## Show obsolete only

As noted in [Deprecated post functions](/cms_trial/space/JMWEC/542803231/Deprecated+post+functions/), changes to Atlassian’s infrastructure require that deprecated JMWE post functions be **completely removed by the end of September 2025**. Please review the documentation on how this impacts your automations and how to update your workflows and Actions to the current versions of each deprecated post function.

Check this box to filter the display of Event-based actions to only display actions that include deprecated post functions. The checkbox includes a number indicating how many deprecated post functions exist across all Event-based actions.

## Filter and Sort

Nearly every column in the table of actions includes tools for sorting the list (ascending or descending for the selected column) and filtering the list. The following tools are available:

- **Filter** - Filter the column based on the possible values. For example, you can filter the list for enabled or disabled actions using the **Enabled** column, filter the actions by the Projects in which they are included (**Project** column), or the post-functions they include (**Post-functions** column).
- **Sort** - Sort the column ascending or descending based on the column values.

**Note**: Due to restrictions on sorting by generic user names, the **By** column does not include the option to sort.

## Configure an Event-based action

For more information on configuring Event-based actions, see [this page](/cms_trial/space/JMWEC/1793852536/Configure+an+Event-based+action/).