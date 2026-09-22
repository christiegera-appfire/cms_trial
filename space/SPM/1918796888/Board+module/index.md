# Board module

## Board module (old navigation)

Click to expand the guide

## About the Board module

The **Board** module is a powerful tool whose primary purpose is to visualize and highlight new feature delivery dates and cross-team dependencies. However, if you work in non-agile teams, you can plan your tasks and coordinate the work you plan with the other teams.

The Board module is very helpful during planning sessions (such as Program Increment (PI) Planning or Iteration planning) as it can show capacities across different teams. But there is much more the Board module can help you with. For example, it can boost the way you monitor [timebox](/cms_trial/space/SPM/1918766987/Timeboxes/) execution thanks to its built-in reporting features and various progress bars that will help you and your team stay on track.

![Main view of the Board module](/cms_trial/assets/4b3578de-725b-4444-84fa-646729c63d48.png)

The Board module also incorporates a timeline that shows important events or milestones. Plus, you can customize the task cards by using the [card view creator](/cms_trial/space/SPM/1918832263/Card+view+creator/).

![The Board module, The Essentials option chosen](/cms_trial/assets/d46e0d10-61e8-4421-99c4-2c47400fe107.png)

## Board hierarchy

The Board module utilizes the concept of the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/), which needs to be configured first in the Overview module. You can zoom in on three levels of boxes, for example:

- Program
- Program Increment
- Iteration

If you create multiple sub-boxes, the board can display up to two levels.

The data on the Board can be displayed at one or two levels, such as the iteration level only or the program increment and iteration levels.

## Main features

The table below describes the Board's main features:

| **Feature** | **Description** |
| --- | --- |
| [+Add task](/cms_trial/space/SPM/1918800322/Create+tasks/) | Use this option to add tasks by:   - Creating new tasks in the host platform (the host platform is the Jira instance you are currently using) - Creating basic tasks   Use this option to access the scope definition page:   - Manage [scope definition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918796888)  add-task.png |
| Swimlane picker | Display or hide swimlanes of various types. swimlane-picker.png |
| Timebox reports | Generate instant reports using charts for each timebox. tiembox-reports.png |
| View | Adjust the way cards are displayed or quickly collapse all the team swim lanes to get an overview of your teams' progress. View settings include the following features:   - **Layout**    - Compact   - Regular   - Wide - **Totals**    - Type      - None     - Work progress     - Capacity allocation   - Aggregate by      - Story points     - Original Estimates     - Remaining Estimates - [Task warnings](/cms_trial/space/SPM/1918636230/Task+warnings+(Board+module)/) - [Show objectives](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Add%20associated%20work%20to%20Objectives&linkCreation=true&fromPageId=1918796888)  Board module view options. |
| Dependencies | Expand or collapse the dependencies for better visibility. Option for expanding and collapsing dependencies in the board module. |
| Dependencies / Browse dependencies | Display different dependency types and resolve conflicts. Click **Browse dependencies** to open dependencies in the Infobar panel.   - Incorrect dependencies (red) - target tasks are planned in previous timeboxes. - Dependencies at risk (orange) - target tasks are planned in the same timeboxes. - Correct dependencies (green) - target tasks are planned in next timeboxes. - Dependencies out of view (purple) - target tasks are out of view.  board-module-link.png |
| Export | To unlock the export features, install the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview) PDF image export requires NodeJS installation.  You can Export the Board module data using the "**Export**" button: board-module-export-1.pngboard-module-export.png |
| Inline editable field | You can inline edit the text and number fields both on a task card and within the backlog.  Inline edit the **Summary** field: board-module-inline.pngcontentId-1918796888 Inline edit the **"Status"** field: inline-status.png |
| Card views | Change the layout of the task card and add different fields to provide the right level of information for your team. system-deafult.png |
| Capacity planning | Define the capacity of teams and team members. capacity-planning.png |
| Quick filters | Filter data using previously created JQL filters in program configuration. quick-filters.png |
| Show full scope | Load tasks from lower-level Boxes/hide tasks in lower level Boxes:   - When the filter button is pressed (dark grey background, white icon), only tasks planned on the level you currently see are visible. Tasks planned for lower-level Boxes are hidden. - All tasks are shown when the filter button is not pressed (light grey background, dark icon).   The button doesn't affect the backlog on the right because the backlog has its own separate show/hide lower-level tasks button. currently-all-tasks-2.png |
| Show tasks with dependencies | Hide tasks that don't have any dependencies:   - When the filter button (dark grey background, white icon) is pressed, only tasks with dependencies are visible. Tasks without dependencies are hidden. - All tasks are shown when the filter button is not pressed (light grey background, dark icon).   The button doesn't affect the backlog on the right - only task cards on the left are affected. all-tasks-dependencies.png |
| Search box | Quick search your tasks using:   - Task summary search - JQL search  search-field.png |
| Timebox info | Additional information about the selected Timebox, which includes the Timebox ID. timebox-edit.pngtimebox-edit-2.png |
| Full-screen mode | Use this mode to hide Jira's and shared App headers. fullscreen-mode.png |
| Timeline | Dynamic timeline with "Today" and "Zoom" buttons. Click on the timeline's arrows to navigate between Iteration and Program Increments or to add a marker or an important event. zoom-in-out.png |
| [Infobar](/cms_trial/space/SPM/1918633681/Infobar+(Board)/) | The **Infobar** in the Board module provides information on crucial box content aspects, including:   - Backlog - Dependencies - Warnings  backlog.png |
| Back to backlog | Right-click on a task and select **Back to backlog** to move a task to the backlog. back-to-backlog.png |
| Create a task-based objective | You can create a task-based objective directly in the Board module. Right-click on a task (Jira issue/basic task) and select **Create objective based on this task**. create-objectives.png A new objective is immediately visible in the [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918796888). objectives-modules.png |
| [Aggregate: Totals](/cms_trial/space/SPM/1918666880/Aggregations/) | Totals will help you plan and monitor the execution of your timeboxes (like PIs and Sprints). You can also use past data to analyze your teams' performance in depth. |
| [Live sync](/cms_trial/space/SPM/1918765626/Live+sync/) | Jira admins can enable the Live sync feature. When enabled, any change to the tasks and the scope of the box will be updated. |
| [Undo](/cms_trial/space/SPM/1918636457/Undo+operation+on+task/) | Undo the last action.  **Important:** Only a single action can be undone.  The Undo button is grayed out by default. It becomes available when the user performs an operation that can be undone. Performing an undo operation OR reloading the page makes the Undo button grayed out again. undo-button.png |
| [Task multiselect](/cms_trial/space/SPM/1918767649/Multiselect+(Board+module)/) | You can streamline your work by selecting and moving multiple tasks. |

## Constraints

**A task must be in the scope of a Box**  
Tasks based on external sources (Jira) have to be added to the scope of a box. The scope of a box can be changed in the scope definition section (Box configuration).

[Unmapped block: nestedExpand]

**To be visible as a card on the Board**

[Unmapped block: nestedExpand]

## Board module (new navigation)

Click to expand the guide

## About the Board module

The **Board** module is a powerful tool whose primary purpose is to visualize and highlight new feature delivery dates and cross-team dependencies. However, if you work in non-agile teams, you can plan your tasks and coordinate the work you plan with the other teams.

The Board module is very helpful during planning sessions (such as Program Increment (PI) Planning or Iteration planning) as it can show capacities across different teams. But there is much more the Board module can help you with. For example, it can boost the way you monitor [timebox](/cms_trial/space/SPM/1918766987/Timeboxes/) execution thanks to its built-in reporting features and various progress bars that will help you and your team stay on track.

![Screenshot of the Board module in BigPicture.](/cms_trial/assets/e5bfa0b0-53e5-4e4c-9c25-84a67c58c993.png)

The Board module also includes a timeline that highlights key events and milestones. Plus, you can customize the task cards by using the [card view creator](/cms_trial/space/SPM/1918832263/Card+view+creator/).

![Screenshot of the Board module with the Current view menu expanded.](/cms_trial/assets/2ea4ac59-b262-44b9-8123-7d2779962198.png)

## Board hierarchy

The Board module utilizes the concept of the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/), which needs to be configured first in the Overview module. You can zoom in on three levels of boxes, for example:

- Program
- Program Increment
- Iteration

If you create multiple sub-boxes, the board can display up to two levels.

The data on the Board can be displayed at one or two levels, such as the iteration level only or the program increment and iteration levels.

## Main features

The table below describes the Board's main features:

| **Feature** | **Description** |
| --- | --- |
| [Tasks](/cms_trial/space/SPM/1918800322/Create+tasks/) | Use this option to add tasks by:   - Creating new Jira work items in the host platform (the host platform is the Jira instance you are currently using). - Creating BigPicture tasks.   Use this option to access the [Add work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918796888) page: Screenshot of the Tasks menu in the Board module. |
| Swimlane picker | Display or hide swimlanes of various types. Screenshot of the swimlane picker in the Board module. |
| Timebox reports | Generate instant reports using charts for each timebox. Screenshot of the Reports view in the Board module. |
| View | Adjust the way cards are displayed or quickly collapse all the team swim lanes to get an overview of your teams' progress. View settings include the following features:   - **Dependencies**    - Expand dependencies   - Collapse dependencies - **Sort A-Z/Z-A by**    - Priority, Icon, Key, Summary, Status, Reporter, Assignee - **Layout**    - Compact, Regular, Wide - [**Aggregation**](/cms_trial/space/SPM/1918666880/Aggregations/)    - Type      - None, Work progress, Capacity allocation   - Aggregate by      - Story points, Original Estimates, Remaining Estimates - [**Task warnings**](/cms_trial/space/SPM/1918636230/Task+warnings+(Board+module)/) - [**Objectives**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Add%20associated%20work%20to%20Objectives&linkCreation=true&fromPageId=1918796888)  Screenshot of the View menu in the Board module. |
| Dependencies / Expand dependencies | Display different dependency types and resolve conflicts.  Click **View** > **Dependencies** > **Expand dependencies** > **Browse dependencies** to open dependencies in the Infobar panel.   - Incorrect dependencies (red) - target tasks are planned in previous timeboxes. - Dependencies at risk (orange) - target tasks are planned in the same timeboxes. - Correct dependencies (green) - target tasks are planned in the next timeboxes. - Dependencies out of view (purple) - target tasks are out of view.  Screenshot of the Browse dependencies button in the View menu in the Board module. |
| Export | To unlock the export features, install the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview) PDF image export requires NodeJS installation.  You can export the Board module data using the **Export** button. Screenshot of the Export button in the Board module. |
| Inline editable field | You can inline edit the text and number fields both on a task card and within the backlog.  Inline edit the **Summary** field: Screenshot of the Summary field inline edited in the Board module.Screenshot of the Summary field inline edited in the Board module. Inline edit the **Status** field: Screenshot of the Status field inline edited in the Board module. |
| Card views | Change the layout of the task card and add different fields to provide the right level of information for your team. Screenshot of the Current view menu in the Board module. |
| Capacity planning | Define the capacity of teams and team members. Screenshot of the Capacity planning view in the Board module. |
| Filters | Filter data using previously created JQL filters in program configuration. Screenshot of the Filters button in the Board module. |
| Show full scope / Show only tasks not planned on a lower level | Load tasks from lower-level boxes/hide tasks in lower-level boxes:   - When the filter button is checked, only tasks planned on the level you currently see are visible. Tasks planned for lower-level boxes are hidden. - All tasks are shown when the filter button is unchecked.   This doesn't affect the backlog on the right - only task cards on the left are affected. Screenshot of the Filter options in the Board module. |
| Show tasks with dependencies | Hide tasks that don't have any dependencies:   - When the filter button is checked, only tasks with dependencies are visible. Tasks without dependencies are hidden. - All tasks are shown when the filter button is unchecked.   This doesn't affect the backlog on the right - only task cards on the left are affected. Screenshot of the Filter options in the Board module. |
| Search box | Quickly search your tasks using:   - Task summary search - JQL search  Screenshot of the search box in the Board module. |
| Timebox info | Additional information about the selected timebox, which includes the timebox ID. Screenshot of the timebox info in the Board module. |
| Timeline | Dynamic timeline with Today and Zoom buttons.  Click the timeline's arrows to navigate between iterations and program increments or to add a marker or an important event. Screenshot of the timeline buttons. |
| [Infobar](/cms_trial/space/SPM/1918633681/Infobar+(Board)/) | The **Infobar** in the Board module provides information on crucial box content aspects, including:   - Backlog - Dependencies - Warnings - [Reports](/cms_trial/space/SPM/2481848664/Contextual+reports/)  Screenshot of the Infobar panel in the Board module. |
| Back to backlog | Right-click a task and select **Back to backlog** to move it to the backlog. back-to-backlog.png |
| Create a task-based objective | You can create a task-based objective directly in the Board module. Right-click on a task (Jira work item/BigPicture task) and select **Create objective based on this task**. create-objectives.png A new objective is immediately visible in the [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918796888). objectives-modules.png |
| [Live sync](/cms_trial/space/SPM/1918765626/Live+sync/) | Jira admins can enable the Live sync feature. When enabled, any change to the tasks and the scope of the box will be updated. |
| [Undo](/cms_trial/space/SPM/1918636457/Undo+operation+on+task/) | Undo the last action.  **Important:** Only a single action can be undone.  The Undo button is grayed out by default. It becomes available when the user performs an operation that can be undone. Performing an undo operation OR reloading the page makes the Undo button grayed out again. |
| [Task multiselect](/cms_trial/space/SPM/1918767649/Multiselect+(Board+module)/) | You can streamline your work by selecting and moving multiple tasks. |

## Constraints

**A work item must be in the scope of a box**  
Jira work items have to be added to the scope of a box. The scope of a box can be changed on the [Work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918796888) page (box configuration).

**To be visible as a card on the Board**

[Unmapped block: nestedExpand]