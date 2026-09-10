# Shared actions

**Shared actions** are a series of one or more post functions, run in sequence, that can be reused across numerous workflow transitions. A Shared Action can then be updated in one place - the Shared Actions Editor page - and it will update everywhere that it is used. Adding a Shared Action to a transition only requires using the [Shared Action](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/) post-function.

To access **Shared actions**:

1. Log in to your Jira instance as an administrator.
2. Click the **Settings** icon ⚙️ in the upper right corner and select **Apps**.
3. Under *Jira MISC WORKFLOW EXTENSIONS* in the left-hand panel, click **Shared actions**.

![admin-SharedActions.png](/cms_trial/assets/ce82d90e-9fba-498e-8510-c0ac4b3131a9.png)

The Shared Actions page (Figure 1, right) lists all Shared Actions that have been created and includes the following:

- **Search** - Filter the list of Shared actions by action name.
- **Create new action** - Click to create a new Shared Action.
- **Shared action list** - A list of all Shared Actions for the instance. The list includes the following information:

  - **Action name** - The action name and description (if any). Click the name to edit the Shared action.
  - **Used in** - A badge indicating the number of places the Shared Action is used in your instance.   
    [note icon] **Hover over the badge to see a detailed list of where the Shared Action is used.**
  - **By** - The user who created the action, or the last user to edit or enable/disable the action.
  - **Last modified** - When the action was last modified (edited or enabled/disabled).
  - **Post-functions** - The number of post-functions included in the Shared Action.   
    [note icon] **Hover over the badge to see a list of the post-functions included in the Shared Action.**
  - **Action menu** - Click to open a menu with specific actions for the Shared Action:

    - **Duplicate** - Create a copy of the Shared Action. The new Shared Action will have the same name as the original, with “- copy” appended.
    - **View Summary** - Open the Summary window (Figure 2, right), listing the Post-functions included in the Shared Action and where the Shared Action is currently being used.
    - **ID** - The Jira ID of the Shared Action. Click the menu option to copy the ID value to your clipboard. This value can be used in the [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/) page to filter the logs by **Action ID**.
    - **Delete** - Permanently delete the Shared Action.   
      ⚠️ **You cannot delete a Shared action when it is used in any workflow transitions. You need to remove it from all workflows before trying to delete it.**

**Note**: You can click the **Used in** and **Post-functions** badges to open the Shared Action Editor!

![Modal window displaying summary of a Shared Action](/cms_trial/assets/913fa939-9b3b-45d6-95fa-6657e1b8b0fe.png)

See the video to learn more.

## Show obsolete only

As noted in [Deprecated post functions](/cms_trial/space/JMWEC/542803231/Deprecated+post+functions/), changes to Atlassian’s infrastructure require that deprecated JMWE post functions be **completely removed by the end of September 2025**. Please review the documentation on how this impacts your automations and how to update your workflows and Actions to the current versions of each deprecated post function.

Check this box to filter the display of Shared actions to only display actions that include deprecated post functions. The checkbox includes a number indicating how many deprecated post functions exist across all Shared actions.

## Filter and Sort

Nearly every column in the table of actions includes tools for sorting the list (ascending or descending for the selected column) and filtering the list. The following tools are available:

- **Filter** - Filter the column based on the possible values. For example, you can filter the list for enabled or disabled actions using the **Enabled** column, filter the actions by the Projects in which they are included (**Project** column), or the post-functions they include (**Post-functions** column).
- **Sort** - Sort the column ascending or descending based on the column values.

**Note**: Due to restrictions on sorting by generic user names, the **By** column does not include the option to sort.

## Configure a Shared Action

![Shared Action Editor screen](/cms_trial/assets/9849e0ae-b24c-44b9-bb40-97c531417be6.png)

When you create or edit a Shared Action, the Shared Action Editor will open (Figure 3, right). The Shared Action Editor uses the [JMWE Automation Rule Builder](/cms_trial/space/JMWEC/768573574/JMWE+Automation+Rule+Builder/), consisting of two side-by-side panels; the left panel has buttons for selecting each configuration category (e.g. **What** for the post-functions to be included in the Shared Action), and the right panel includes specific configuration options for the selected category.

To configure a Shared Action set the following configurations:

1. **Action name** (**Point 1**, **Figure 3**, right) - *Required*. Click the name to edit. Enter a meaningful name and hit Enter, or click the check button, to save.
2. **Description** (**Point 1**, **Figure 3**, right) - Click *Add a description* to edit the Shared Action description. Enter a detailed explanation of the action and click the check button to save.
3. **What/Post-functions** (**Point 2**, **Figure 3**, right) - Click the **What** header or the **Post-functions** button. In the right panel, select a post-function from the list to add the first post-function, or click **Add post-function** (**Point 2**, **Figure 3**, right) to add additional post-functions. See **Post-functions**, below for more information.
4. **Where/Used in** (**Point 4**, **Figure 3**, right) - *Read-only*. Click the **Where** header or the **Used in** button to view the list of places your Shared Action is being used. You can search the list of locations using the search box, and filter using the **Type** pulldown menu. See Shared Actions for details on how to add a Shared Action to a workflow transition or other action.
5. Click **Save** to save the Shared Action.

You can use the **View Summary** button at the bottom of the Rule Builder to view a complete list of post-functions used in your Shared Action!

**Where is a Shared Action used? Where can I use a Shared Action?**

Shared Actions are a powerful tool for minimizing the maintenance overhead of your Jira automations; anywhere you need to use a repeatable series of post-functions is a candidate for Shared Actions. However, for larger Jira instances the number of Shared Actions, and where those actions are utilized, could be difficult to track.

The **Used in** panel is an excellent resource for determining where a Shared Action is currently being utilized; open the Shared Action for editing and select **Used in** in the left panel. The right panel will list all of the places a Shared Action is currently being used! This list can be filtered by **Type** using the pulldown menu, or searched using the **Search** field at the top of the list.

If a Shared Action is not currently being used, the right panel will display options for where the action can be used, including:

- Workflow transitions
- Scheduled Actions
- Event-based Actions
- Other Shared Actions

All of the above scenarios involve using the [Shared Action post-function](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/).

## Post-functions

When you first create a new Shared Action, it will not include any post functions; select the first post function from the list in the right panel to add it. You can add subsequent post functions to the sequence by clicking **Add Post-function** in the upper-right corner of the panel, and then select the post function you need in the window that opens.

The configured post functions will run in the order in which they are listed.

### Add a post function

1. In the right panel, click **Add post function** at the top of the panel.
2. Select a post-function from the list and click **Add**. You can search for the post-function by name, and filter by type using the fields at the top of the window.
3. The post-function configuration window will open. Configure the selected post-function as needed, then click **Save**. See [Post-functions](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Post-functions&linkCreation=true&fromPageId=466288975) for more details on all of the available post-functions.

### Modify or delete a post function

The steps to modify or delete a post function depend on the post function view you are using. See **Post function views** directly below for more information.

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

![admin-EventBasedActionPostFunctionsSimpleView.png](/cms_trial/assets/c1dfa3d7-0a9b-4d18-ac58-12fa61b9639c.png)![admin-EventBasedActionPostFunctionsAdvancedView.png](/cms_trial/assets/fb2df4ea-c03b-4947-b8e1-119781921cae.png)

### Post-function errors

![A list of Post-functions showing error icons](/cms_trial/assets/7b579f2d-41ee-48d5-86f0-73ffdbdc6f05.png)

When a Shared Action post-function encounters an error, an error icon will be displayed on the post-function tile (Figure 6, right). Hover over the icon to see additional details on the error. Click the error icon to open the [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/) Administration page; the logs will be filtered automatically for the post-function that encountered the error.

## Passing variables within a sequence

It is possible to pass data from one post-function to all subsequent post-functions within a Shared Action by using the `{% setContextVar %}` Nunjucks tag. When using a [Build-your-own (scripted) post-function](/cms_trial/space/JMWEC/466289991/Build-your-own+(Nunjucks+scripted)+Post+function/), the variable can be set anywhere within your script; when using other post-functions, the most common place to set a variable is in the **Conditional Execution** configuration.

- **context:** Holds all the *context variables* added in the current post-function. For example, if you create a context variable `myVar` in the first post-function of the sequence:

  ```javascript
  {% setContextVar myVar = "a value" %}
  ```

  This variable will then be available to subsequent post-functions as:

  ```javascript
  {{ context.myVar }}
  ```

**Please note**: a variable created in a post-function will not be available in the Nunjucks tester if you are attempting to test additional post-functions that are to be added after the one where the variable was originally created.

### **Variables specific to the Create Issue post-function**

- `newIssueKey:`Stores the issue key of the *last* issue created by a [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function in the action. You can access it as:

  ```javascript
  {{ context.newIssueKey }}
  ```
- `newIssueKeys:`Stores an array of the keys of all the issues created by any [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function in the action. You can access the created issues from:

  ```javascript
  {{ context.newIssueKeys }}
  ```

  For example: to add a comment on the current issue with the keys of the issues created previously:

  ```javascript
  Issues created are:
  {{ context.newIssueKeys | join(",") }}
  ```

You can access the information of a specific issue using the [issue](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=MWECS&title=Custom%20Filters&linkCreation=true&fromPageId=449806450) filter. For example: To get the assignee of the issue created by the [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function:

```javascript
{{ context.newIssueKey | issue("assignee") | field("fields.assignee.displayName") }}
```