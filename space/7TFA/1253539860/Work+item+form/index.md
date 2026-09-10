# Work item form

7pace Timetracker's integration with Azure DevOps (ADO) lets you track time directly from a work item or backlog.

7pace Timetracker is fully integrated with your ADO Services account.

After clicking a work item ID or name, the work item form displays, defaulting to the **Details** tab. With 7pace Timetracker installed, an additional tab is available on the work item form, the *7pace Timetracker* tab. This tab shows the total time spent by you and your team members on that work item and all child items.

The **7pace Timetracker** tab also features an **Add Time** button that enables you to add time directly to a work item. This **Add Time** button can also be found on the *Monthly*, *Times Explorer*, and *Timesheet* pages.

On the *Times Explorer* page, a manager can add time on behalf of their team members.

To allow this:

1. Go to the *Settings* > *Editing Time.*
2. Turn on the option for **Allow time to be edited by role other than user**.
3. From the **Role that can edit time** dropdown, select the 7pace Timetracker user role that will have this ability.

If the **Allow time to be edited by role other than user** toggle button is turned off, the edit and delete icons associated with work logs that belong to other users on the **Times Explorer** page will be grayed out.

If an admin enables the Activity Types feature in **Settings > Activity Types**, the **7pace Timetracker** tab displays time tracked to work items assigned an activity category under the **Activities** section on the work item form.

![Settings page showing Activities.](/cms_trial/assets/c16936e0-190b-407a-9c64-69c1e08c2879.png)

## Work item in 7pace Timetracker

Here is a breakdown of the *7pace Timetracker* tab within a work item and its main features:

### Total

Total time (in hours) tracked for the work item, including time logged for all child items.

### Pace

The pace at which the task is performed. This number is calculated by dividing the tracked hours by the estimated effort. To learn more about enabling pace settings within Timetracker, refer to the [General settings](/cms_trial/space/7TFA/1253540033/General+Settings/) page.

### Add time

When clicked, displays the *Add time* dialog so you can add time directly to the work item. For more information, click [here](/cms_trial/space/7TFA/1253539860/Work+item+form/).

If a work item is in a closed or done state and **Prevent time entry (adding/editing/deleting worklogs) on closed items** is enabled under *Settings* > *Rules*, the **Add Time** button is grayed out on the *7pace Timetracker* tab.

### Workitem

In the lower left quadrant of the window, you'll see the work item, total time tracked for the parent and all child items. Clicking on the Open Details in Times Explorer icon opens that specific work item’s details in the [Times Explorer](/cms_trial/space/7TFA/1253540013/Times+Explorer/) page.

### Hours

The total time tracked for the specific work item.

### Pace

Pace is only displayed for the PBI work item type. To learn more about enabling pace settings within 7pace Timetracker, click [here](/cms_trial/space/7TFA/1253540033/General+Settings/).

### Team

In the lower right quadrant of the work item window, all users who tracked time on the work item display. If an admin has enabled the activity type feature in *Settings,* each user's activity type also displays. Hovering over each color in the bar shows a tooltip with the time tracked to that specific activity type.

### Activities

The time logged on each configured [activity type](/cms_trial/space/7TFA/1253540033/General+Settings/).

### Budgets

You can assign budgets to work items from the *7pace Timetracker* tab of the work item form. You can also view budget inheritance information. For more information, click [here](/cms_trial/space/7TFA/1253540085/Budgets/).

## Work items: Start Tracking and Add Time

After installing 7pace Timetracker, and clicking a work item in ADO, the **Start Tracking** and **Add Time** buttons display (see the screenshot below) on the resulting work item *Details* tab.

![Azure DevOps work item showing the Start Tracking and Add Time buttons.](/cms_trial/assets/20576ef8-b261-4024-a771-fa2acb01f663.png)

Click **Start Tracking** to track a work item in real-time. If the 7pace Timetracker desktop app for Windows or Mac is downloaded and paired from the *Apps* page, tracking commences on that app and also initiates tracking on the 7pace Timetracker web app (found at the top of every 7pace Timetracker page) for that work item.

Click **Add Time** to open the *Add time* dialog. The person selector defaults to the current user, and the ability to select someone other than yourself is based on permissions. The date defaults to the current date but can be edited, and the activity type is set to the default value. This value can also be edited.

If the work item is in a closed or done status, and the **Prevent time entry (adding/editing/deleting worklogs) on closed items** button  is enabled in *Settings* > *Rules*, the **Start Tracking** and **Add Time** buttons will be disabled on the *Details* tab.

## Backlog Start Tracking and Add Time buttons

In 7pace Timetracker, the **Start Tracking** and **Add Time** buttons are also available directly from the ADO backlog pages (Backlog, Queries, Boards, etc.) in the work item context menu.

If a work item is in a closed or done status and **Prevent Time Entry Against Closed Items** is enabled under *Settings* > *Rules*, **Start Tracking** and **Add Time** are disabled from the context menu.

From the *7pace Timetracker* menu, click **Start Tracking** to start time tracking throughout the app. You’ll see the results in the integrated web app, work item form, and the downloadable Windows or Mac apps.

![Work item context menu showing the Start Tracking and Add Time commands.](/cms_trial/assets/23d5fc8e-d7ec-4667-b3fa-9391c15ed8b6.png)

Click **Add Time** to open the *Add time* dialog. The person selector defaults to the current user, and the ability to select someone other than yourself is based on permissions. The date defaults to the current date but can be edited, and the activity type is set to the default value. This value can also be edited.