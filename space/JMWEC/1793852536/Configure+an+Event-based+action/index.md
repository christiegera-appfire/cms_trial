# Configure an Event-based action

When you create or edit an Event-based Action, the Event-based Action Editor will open (Figure 1, right). The Event-based Action Editor uses the [JMWE Automation Rule Builder](/cms_trial/space/JMWEC/768573574/JMWE+Automation+Rule+Builder/), consisting of two side-by-side panels; the left panel has buttons for selecting each configuration category (e.g. **When** for the event that triggers the action), and the right panel includes specific configuration options for the selected category.

![JMWE for Jira Cloud eventbased action editor with configuration options and settings](/cms_trial/assets/ba3c4c94-43f7-40a6-925f-40052b223cd4.png)

To configure an Event-based action, set the following configurations:

1. **Action name** (**Point 1**, **Figure 1**, right) - *Required*. Click the name to edit. Enter a meaningful name and hit Enter, or click the check button to save.
2. **Description** (**Point 1**, **Figure 1**, right) - Click *Add a description* to edit the Scheduled Action description. Enter a detailed explanation of the action and click the check button to save.
3. **When/Event** (**Point 2**, **Figure 1**, right) - Click the **When** header or the **Event** button. In the right panel, select the event that will trigger the action. See the **Events** section of [Event-based Actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/) for more information.

   1. **Ignore events caused by JMWE post-functions and actions** - Check this box to prevent the Event-based action from triggering when another JMWE post-function or action runs.
   2. **Ignore events caused by Jira Automation and other apps** - Check this box to prevent the Event-based action from triggering when the event is caused by a native Jira Automation or other app.
4. **If Scope/Projects** (**Point 3**, **Figure 1**, right) - Click the **If Scope** header or the **Projects** button to configure which projects will trigger the Event-based Action; only events on issues within the selected projects will trigger the action. See **Projects and Issue Types**, below, for more information.   
   [note icon] If you do not select a specific project(s), **issues from all projects** will trigger the action.
5. **Issue Types** (**Point 4**, **Figure 1**, right) - Click the **Issue Types** button to configure which issue types will trigger the Event-based Action. See **Projects and Issue Types**, below, for more information.  
   [note icon] If you do not select specific issue type(s), **all issue types** will trigger the action.

   1. **Only apply to issues that match a JQL filter** - Check this box to use a JQL query to filter the issues that should trigger the action.
   2. **Only apply to issues that match a Nunjucks condition** - Check this box to use a Nunjucks condition to filter the issues that should trigger the action.
6. **Then/Post-functions** (**Point 5**, **Figure 1**, right) - Click the **Then** header or the **Post-functions** button. In the right panel, select a post-function from the list to add the first post-function, or click **Add post-function** to add additional post-functions. See **Post functions**, below for more information.

   1. **Skip subsequent post-functions if a post-function encounters an error** - Check this box to stop the execution of the Event-based Action if any of it’s post-functions encounter an error.

**Please note**: for the **Ignore events caused by Jira Automation and other apps** setting:

- Events triggered by actions that are run using impersonation (the automation's "actor" setting) are **not ignored**.
- This option is disabled when one of the following events is selected:

  - **Attachment Deleted**
  - **Issue Link Added**
  - **Issue Link Deleted**
  - **Work Log Updated**
  - **Work log Deleted**

## Projects and Issue Types

Configuring which projects and issue types will trigger your Event-based Action, both work the same way. You can use the pull-down menu at the top of their list to browse the list or start typing to search for specific projects and issue types. Check the box next to the project or issue type to add it; click the **X** next to its name in the list to remove it.

Alternately, you can click **Select Projects/Select Issue Types** to open a window listing all of your Jira projects or issue types (Figure 2, right). Select or deselect the projects or issue types and click **Add**.

You can further filter the issue types that will trigger your action by using the JQL and Nunjucks filters. When either of these boxes are checked, a newfield will appear - **JQL** or **Nunjucks**. Click these fields to open the **JQL Filter/Nunjucks expression** window, where you can enter the query or template and preview its results. Click **Save** to save the query or template and apply it to the action.

For more information on using JQL queries, see [Using Jira Expressions](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).

For more information on using Nunjucks, see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).

![JMWE for Jira Cloud eventbased action issue type selection interface](/cms_trial/assets/e4d32afb-d1d3-4694-98ef-eeda4646436b.png)

## Post functions

For each issue included in the Event-based Action (see **Projects and Issues**, above), the configured post functions will run *in the order in which they are listed*.

When editing an existing Event-based action, the right-hand panel for Post functions includes several buttons for working with the post functions within the action:

- **Filter** ▢ - Filter the list of post functions by type.
- **Advanced view/Simple view** ▢ - Switch between views. See **Post function views** below for more information.
- **Expand all** ▢ **/ Collapse all** ▢ - *Only available in* ***Advanced view****.* Expand or collapse all post function tiles.

### Add a post function

To add a post function to your Action:

1. For the first post function added to an Event-based action, simply click the post function in the list to add it.
2. Alternately, in the right panel, click **Add Post-function** at the top of the panel. Select a post function from the list and click **Add**. You can search for the post function by name using the Search field at the top of the list.
3. The post function configuration window will open. Configure the selected post function as needed, then click **Save**. See [Post functions](/cms_trial/space/JMWEC/465242045/Post+functions/) for more details on all of the available post functions.

### Modify or delete a post function

The steps to modify or delete a post function depend on the post function view you are using. See **Post function views** directly below for more information.

### Play the Arcade

<https://app.arcade.software/flows/s6qp6PJa99D7JlfiyxGp/view>

## Post function views

The post function panel of the Automation Rule Builder includes two different ways of viewing the post functions that are included in your action; you can switch between views using the **Switch view** button near the top of the panel.

### Simple view

Image — asset pipeline pending  
JMWE for Jira Cloud rule builder post function interface in simple view mode

The simple view (Figure, right) of your action's post functions includes an expandable tile for each post function. You can reorder them using the **Up** ▢ and **Down** ▢ buttons to the left of the tile. You can edit, delete, or duplicate any of them by expanding the tile using the arrow to the right.

The expanded tile includes:

- the post-function name
- the post-function ID (this can be used in the [JMWE Logs](https://appfire-sandbox-774.atlassian.net/wiki/spaces/JMWEC/pages/428709194) Administration page to filter the logs for the post-function)
- a brief description of the configuration.

The bottom of the expanded tile includes action buttons:

1. To enable or disable a post-function, use the **Enabled/Disabled** toggle.
2. To edit the selected post-function, click **Edit** ▢.
3. To remove the post-function, click **Delete** ▢.
4. To copy the post-function, click **Duplicate** ▢

### Advanced view

The advanced view adds the **Post function details** section to the **bottom** of the Automation Rule builder page. This list includes all of the configuration details of each post function in an expanded format, making the full configuration of your action easier to browse. Each post function listed includes the same tools available in the Simple view - a toggle to enable or disable the post function, buttons for moving the post function up or down in the order, and commands to duplicate, edit, or delete the post function.

It also switches the right-hand panel to a condensed list (Figure, right) of the included post functions, with a handle for reordering them, an edit button for quick access to the post function configuration, and an action button that includes the options to duplicate, delete, or disable the post function.

Image — asset pipeline pending  
JMWE for Jira Cloud rule builder post function interface in advanced view mode

## Pass variables within a sequence

It is possible to pass data from one post function to all subsequent post functions within an Event-based Action by using the `{% setContextVar %}` Nunjucks tag. When using a Build-your-own (scripted) post function, the variable can be set anywhere within your script; when using other post functions, the most common place to set a variable is in the **Conditional Execution** configuration.

- **context:** Holds all the *context variables* added in the current post function. For example, if you create a context variable `myVar` in the first post-function of the sequence:

  ```javascript
  {% setContextVar myVar = "a value" %}
  ```

  This variable will then be available to all its subsequent post functions as:

  ```javascript
  {{ context.myVar }}
  ```

**Please note**: a variable created in a post-function will not be available in the Nunjucks tester if you are attempting to test additional post-functions that are to be added after the one where the variable was originally created.

**Variables specific to the Create Issue post-function**

- `newIssueKey:`Stores the issue key of the *last* issue created by a [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function in the action. You can access it as:

  ```javascript
  {{ context.newIssueKey }}
  ```
- `newIssueKeys:`Stores an array of the keys of all the issues created by any [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function in the action. You can access the created issues from

  ```javascript
  {{ context.newIssueKeys }}
  ```

  For example: to add a comment on the current issue with the keys of the issue created

  ```javascript
  Issues created are:
  {{ context.newIssueKeys | join(",") }}
  ```

You can access the information of a specific issue using the [issue](/cms_trial/space/JMWEC/465373638/Custom+filters/) filter. For example: To get the assignee of the issue created by the [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function

```javascript
{{ context.newIssueKey | issue("assignee") | field("fields.assignee.displayName") }}
```

## Pass context variables to an Event-based action

### Variables specific to the current transition

If a post-function for the acton is run during a transition, information about the transition is accessible.

Note that for Event-based Actions listening to the *Issue Transitioned* event, only the `from_status`, and `to_status` fields are available.

Access these variables using the prefix `context.`. For example:

```javascript
{{ context.transition.transitionId }}
```

This returns *ID* of a transition. The following information is available:

- `transition.transitionId`: Stores the ID of the transition.
- `transition.transitionName`: Stores the name of the transition.
- `transition.from_status`: The status from which the current transition starts.
- `transition.to_status`: The status to which the current transition leads.
- `transition.workflowName`: The name of the workflow to which the transition belongs.
- `transition.workflowID`: The ID of the workflow to which the transition belongs.

### Variables specific to Comments

If the post-function is run during a transition, any comment that was entered on the transition screen is available.

Access to the following data requires that the post-function is put *after* the **Add a comment to an issue if one is entered during a transition** built-in post-function.

The newly created comment is available if the post-function is run during an action triggered by an *Issue Commented* event.

- `context.comment.body`: The body of the comment, as text with wiki markup.
- `context.comment.created`: The date/time the comment was created.
- `context.comment.author.accountID`: The account ID of the author of the comment.
- `context.comment.author.displayName`: The display name of the author of the comment.
- `context.comment.jsdPublic`: Determines if the comment is shared with Customers (for Jira Service Management projects).

### **Variables specific to Attachments**

If the post-function runs as part of an Event-based Action listening to the `attachment_created` or `attachment_deleted` event, the attachment added or deleted is available through the `context.attachment` variable.

Access these variables using the prefix `context.`. For example:

```javascript
{{ context.attachment.id }}
```

This returns *ID* of an attachment. The following information is available:

- `attachment.filename`: Stores the filename of the attachment.
- `attachment.id`: Stores ID of the attachment.
- `attachment.created`: The date/time the attachment was created.
- `attachment.size`: The size of the attachment.
- `attachment.mimeType`: The mime-type of the attachment.
- `attachment.author.accountId`: The account ID of the user adding the attachment.
- `attachment.author.displayName`: The display name of the user adding the attachment.

### **Variables specific to Issue Links**

If the post-function runs as part of an Event-based Action listening to the `issue_link_created` or `issue_link_deleted` event, the issue link added or deleted is available through the `context.issueLink` variable.

Access these variables using the prefix `context.`. For example:

```javascript
{{ context.issueLink.issueLinkType.name }}
```

This returns the issue link type of the link being added. The following information is available:

- `issueLink.sourceIssueId`: The issue ID of the *source* issue of the issue link being added or deleted.
- `issueLink.destinationIssueId`: The issue ID of the *destination* issue of the issue link being added or deleted.
- `issueLink.issueLinkType.name`: The issue link type of the issue link being added or deleted.

- When an issue link is added, the source issue is always the issue on which the link name appears as the *Outward* link name (e.g. "blocks"), regardless of the issue from which the link was created.
- When an issue link is added, the destination issue is always the issue on which the link name appears as the *Inward* link name (e.g. "is blocked by"), regardless of the issue from which the link was created.

### **Variables specific to Work Log Links**

If the post-function runs as part of an Event-based action listening to the worklog\_created, worklog\_updated, or worklog\_deleted event, the worklog data is available through the `context.worklog` variable.

Access these variables using the prefix `context.`. For example:

```javascript
{{ context.worklog.created }}
```

This returns the date and time of when the worklog was created. The following information is available:

- `worklog.timeSpent`: Work Log string added/updated/deleted.
- `worklog.timeSpentSeconds`: Work Log in seconds added/updated/deleted
- `worklog.comment`: Comment added/updated with the Work Log.
- `worklog.created`: The date/time the worklog was created.
- `worklog.updated`: The date/time the worklog was updated.
- `worklog.started`: The date/time the worklog was started.
- `worklog.author.accountId`: The accountID of the user adding the worklog.
- `worklog.author.displayName`: The display name of the user adding the worklog.