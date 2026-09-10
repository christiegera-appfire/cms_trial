# Configure a Scheduled action

## Configure a Scheduled Action

![Scheduled Action Editor configuration screen](/cms_trial/assets/d2c64aef-b352-45a1-82be-35154db68578.png)

When you create or edit a Scheduled Action, the Scheduled Action Editor will open (Figure 3, right). The Scheduled Action Editor uses the [JMWE Automation Rule Builder](/cms_trial/space/JMWEC/768573574/JMWE+Automation+Rule+Builder/), consisting of two side-by-side panels; the left panel has buttons for selecting each configuration category (e.g. **When** for the Scheduled Action schedule), and the right panel includes specific configuration options for the selected category.

To configure a Scheduled Action set the following configurations:

1. **Action name** (**Point 1**, **Figure 3**, right) - *Required*. Click the name to edit. Enter a meaningful name and hit Enter, or click the check button, to save.
2. **Description** (**Point 1**, **Figure 3**, right) - Click *Add a description* to edit the Scheduled Action description. Enter a detailed explanation of the action and click the check button to save.
3. **When/Schedule** (**Point 2**, **Figure 3**, right) - Click the **When** header or the **Schedule** button. In the right panel, click each field to set the schedule for the action. See **Schedule**, below for more information.
4. **If Scope/Target Issues** (**Point 3**, **Figure 3**, right) - Click the **If Scope** header or the **Target Issues** button to configure the JQL query that will return the issues for the Scheduled Action; set **Max Issues** to limit the number of issues for the action. You can test your query and preview the results by clicking the **Search** button. See **Target Issues**, below, for more information.
5. **Who** (**Point 4**, **Figure 3**, right) -
6. **Then/Post-functions** (**Point 5**, **Figure 3**, right) - Click the **Then** header or the **Post-functions** button. In the right panel, select a post function from the list to add the first post function, or click **Add post-function** to add additional post functions. See **Post-functions**, below for more information.

   1. **Skip subsequent post-functions if a post-function encounters an error** - Check this box to stop the execution of the Event-based Action if any of it’s post functions encounter an error.
7. Click **Save** to save the Shared Action.

## Schedule

The Schedule configuration determines how often the action will run. Every time the action runs, that action’s JQL search will run, and the post functions included in the action will run *on each issue returned by the search*, both in order of the issues returned by the JQL query **and** the order of the post functions within the Scheduled Action.

**Please note** the following limitations on Scheduled Actions:

- You cannot run a scheduled action *more than once every 10 minutes* and running scheduled actions too often will have an impact on the performance and responsiveness of your Jira instance.
- In general, there will be a difference of a few minutes in the configured scheduled time and the actual execution time of the action. For example. if you configure a Comment issue post function in the scheduled action to run every hour, then the comment might be added at 10:02 AM and then at 11:01 AM and then at 12:02 AM, etc.
- The greater the number of actions that are scheduled, the more the actual execution time will vary. Actual execution time and execution duration depend on how many scheduled actions are running at the same time.

### Configure a schedule

You can run the Scheduled Action at nearly any interval ranging from every hour to every year at specific times.

Note that the schedule is expressed in **UTC time**.

The available values for the **Schedule** will change based on the increment that is initially selected. To set the schedule for an action set each of the available fields:

1. **Increment** - Set the overall increment. Available options are **hour**, **day**, **week**, **month**, or **year**.   
   ⚠️ *The other values for schedule will change based on this selection.*
2. **Hour** and/or **Minute** - *All increments allow for the Scheduled Action to run at a specific time of day.*

   1. Hours are set using a 24 hour clock.
   2. Multiple hours or minute values can be selected. For example, to run an action every day at 6 AM and 3 PM every day, set the field as pictured below.

      ![JMWE for Jira Cloud scheduled action time configuration with hour settings](/cms_trial/assets/e0a36c49-39c1-4cb3-9f3a-c4da3ae36f8a.png)
3. **Day of the Week** - *Available when the increment is set to* ***week****.* Set the day or days of the week (Monday through Sunday) when the action will run.
4. **Day of the Month** - *Available when the increment is set to* ***month*** *or* ***year****.* Set the date or dates of the month when the action will run.   
   ⚠️ **Please note**, the default value for this field is ‘Every day of the month’. To set this field back to the default value, deselect all of the specific dates.
5. **Month of the Year** - *Available when the increment is set to* ***year***. Set the month or months when the action will run.   
   ⚠️ **Please note**, the default value for this field is ‘every month’. To set this field back to the default value, deselect all of the specific months

## Target issues

![Scheduled Action Target Issues configuration screen](/cms_trial/assets/0192703c-3b8e-4ec7-81c7-821f5d9c9eff.png)

Target issues for the Scheduled Action are determined by a JQL search that returns the issue or issues on which the action should run. For more information on creating JQL queries, see [Constructing JQL Queries](https://support.atlassian.com/jira-software-cloud/docs/what-is-advanced-searching-in-jira-cloud/#Advancedsearching-ConstructingJQLqueries).

To input a JQL query:

1. From the **Scheduled Action Editor**, select **If Scope** or **Target Issues** in the left-hand panel.
2. In the right-hand panel (Figure 4, right), input a JQL expression that will return the issues on which the post functions should be run. For example:

   ```sql
   project =  TEST and issuetype = Bug
   ```
3. Click **Search** (**Figure 4**, **Point 1**, right) to run the query and preview the issues that will be returned. It is recommended to check the results to avoid invalid JQL.
4. Set **Max issues** (**Figure 4**, **Point 2**, right) to limit the number of issues the query should return.

**Please note** that a query cannot return more than `1000`issues.

If the scheduled action runs *more than once per hour*, the number of issues is limited to `1000 * {lowest interval in minutes} / 60`. For example, if your scheduled action runs:

- Every hour then the maximum number of issues returned will be: `1000`
- Every 30 minutes then the maximum number of issues returned will be:   
  `1000 * 30 / 60` or `500` issues
- Every hour at 10 and 30 minutes past the hour, then the maximum number of issues returned will be:   
  `1000 * 20 / 60` or `333` issues (where 20 minutes is the lowest interval within the hour)
- Every hour at 0, 10 and 30 minutes past the hour then the maximum number of issues returned will be:   
  `1000 * 10 / 60` or `167` issues (where 10 minutes is the lowest interval within the hour)

## Run as user

Select one of the following to set the creator of the issue:

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## Post-functions

![JMWE for Jira Cloud scheduled action post functions configuration panel](/cms_trial/assets/c77b58bb-76bc-4edb-8cc0-d8c1da4fec50.png)

For each issue returned by the JQL search (detailed above), the configured post functions will run *in the order in which they are listed*.

### Add a post function

1. In the right panel, click **Add post function** at the top of the panel.
2. Select a post function from the list and click **Add**. You can search for the post function by name using the Search field at the top of the list.
3. The post function configuration window will open. Configure the selected post function as needed, then click **Save**. See [Post functions](/cms_trial/space/JMWEC/465242045/Post+functions/) for more details on all of the available post functions.

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

## Error handling

When a Scheduled Action encounters and error - in either it’s JQL query or in the included post functions - it will be indicated in two places:

1. The **Executions** column of the Scheduled Action list will display an error icon
2. The Scheduled Action Editor will include a banner at the top of the editor with details of the errors

Within the Scheduled Action Editor, you can view the details of any errors by expanding the banner using the **Down** ( [caret down icon] ) button to the right. The banner is divided into two columns:

- **Errors/Warnings** on the left will display any errors or warnings related to the action (e.g. a JQL query error)
- **Post-functions** on the right will display any specific errors for the included post functions

You can mark errors are resolved for each column; individual errors can be marked using the link to the right of the error message and all errors for the column can be marked resolved using the link at the top of the list. When all errors have been marked as resolved <what happens?>

**Note**: If one of the post functions fails with an error, the remaining post functions in the sequence will still run. To stop the execution of subsequent post functions after an error occurs, select the option “Skip subsequent post functions if a post function encounters an error” under **Then** in the left-hand panel.

![JMWE for Jira Cloud eventbased action post functions in simple view mode](/cms_trial/assets/3f8a2404-78fc-4aaa-b0a7-82a4538a82d5.png)![JMWE for Jira Cloud eventbased action post functions in advanced view mode](/cms_trial/assets/ca5ed103-2bd6-46c3-bc50-c9e06abedbef.png)