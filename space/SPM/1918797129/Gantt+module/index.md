# Gantt module

## Gantt module (old navigation)

Click to expand the guide

## An overview of the Gantt module

The Gantt module is your go-to module for managing projects and portfolios. Use it to plan and visualize project schedules and roadmaps, monitor and control their execution, and generate data exports showing data that meets your business needs.

The Gantt module includes four key elements:

- (**A**) Customizable [task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) that presents almost any Jira or built-in [fields](/cms_trial/space/SPM/1918635376/Fields/) as columns with [aggregated data](/cms_trial/space/SPM/1918636993/Column+data+aggregation+methods/).
- (**B**) [Timeline](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) with taskbars and dependencies that visualize and auto-schedule your work items.
- (**C**) [Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) that highlights the most important information related to your project, such as overdue tasks, critical path, dependencies, milestones, and change history.
- (**D**) [Resources panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) that shows your resources’ workload.

Image — asset pipeline pending  
Gantt module featuring WBS, Gantt chart, and Infobar.

## Main features

The table below lists the main features of the Gantt module:

| **Feature** | **Description** |
| --- | --- |
| [Scenario mode](/cms_trial/space/SPM/1918634045/Scenarios/) | Try different variants of your plan, compare the results, and find the best one. |
| [Add task](/cms_trial/space/SPM/1918800322/Create+tasks/) (+) | Use this option to:   - Create new tasks and subtasks as Jira issues and [basic tasks](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297702042). - Import tasks from a file (requires the BigTemplate app). - Clone the existing scope. - Access the *Manage scope definition* page. |
| Data | Add the following features to all tasks within the box scope:   - [Organize tasks](/cms_trial/space/SPM/1918667546/Organize+tasks%2F+Default+task+order/) - changes the order of the tasks in all the users' views in an ascending (A-Z) or descending way (Z-A), based on the fields added as columns in the current column view. - [Scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) - enables auto-scheduling or manual planning. - [Baselines](/cms_trial/space/SPM/1918404564/Baselines/) - creates and displays schedule baselines under your tasks. - [Group tasks](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Group%20tasks%20%28Gantt%20and%20Scope%20modules%29&linkCreation=true&fromPageId=1673560464) - groups tasks by one or multiple active columns and counts them in each group. - [Resynchronization](/cms_trial/space/SPM/1918404058/Data+synchronization+with+connected+tools/) - triggers an incremental sync of the box (requires [Box Admin or Box Editor](/cms_trial/space/SPM/1918668158/Box+security+roles/) security role). |
| Sort by | Sort your task tree in an ascending (A-Z) or descending (Z-A) order based on the fields added as columns in the current column view. Unlike the [Organize tasks](/cms_trial/space/SPM/1918667546/Organize+tasks%2F+Default+task+order/) option, sorting does not affect other users' views. |
| View | Customize the look of the WBS and Gantt chart and add extra details to your Gantt chart view:   - Layout - adjusts the row height (compact, regular, wide) so that you can fit more or fewer tasks on your screen; also adds and removes horizontal and vertical lines. - Baselines - displays schedule baselines under tasks to compare initial and actual schedules. - Critical path - highlights tasks on the critical path that determine project duration. - Period warning - shows the position of parent tasks calculated in relation to their children. - Progress - shows task progress directly on the taskbar. |
| Taskbar | Show task information using labels added to the task on the timeline or change the task colors based on status or manually:   - Task information - determines what task details are shown on the Gantt chart and their position. - Other scope info - shows/hides an icon indicating that a given task is in the scope of multiple boxes. - Task color - changes the color of the taskbar based on the status of the user’s choice of color. |
| [Dependencies](/cms_trial/space/SPM/1918536086/Dependencies/) | Visualize two types of dependencies on the Gantt chart:   - Strong dependencies. - Soft dependencies. |
| [Show/Hide Resources](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) | Use the Resources panel to see the workload of each resource (assignee). When enabled, an additional icon with **Resources settings** will appear next to the Show/Hide Resources button:  Effort modes:   - Original estimate. - Remaining estimate.   Aggregations:   - Daily. - Weekly. - Monthly. |
| Switch to Resources | Once the Resources panel is enabled, you can click **Switch to Resources** to be redirected to the Resources module. |
| [Export](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Export%20in%20Gantt%20module&linkCreation=true&fromPageId=1918797129) | Export data to a specified file type:   - MPP, XML, MPX - XLSX - CSV - PDF image |
| [Column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/) | Column view displays field-based data for your project in a clear, tabular format. Under the **Column Views** button, you can find:   - Current view - indicates the active column view. - Available section - lists available views you can select. - Star (icon) - marks a column view as a favorite. - Manage column view - takes you to the box configuration page, where you can manage your column views.   Click **More actions** (**…**) on the selected column for column configuration options. (The available options vary depending on the column type):   - Pin column - pins the column on the left or the right side of your column view. - Sort tasks - sorts tasks A-Z or Z-A. - Customize - if the data cannot be aggregated, it provides options for customizing the way the data in the column is displayed (icon and name; icon; name). If the data can be aggregated, it provides a list of aggregation methods. - Column info - displays the field name the column is based on and indicates where the given field is mapped in the [field mapping](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297635027) settings. - Resize all columns to fit - resizes all columns in the view to fit the screen. - Delete - removes the column from the column view.   Double-click the column edge to fit the column width to its content. |
| [Undo](/cms_trial/space/SPM/1918636457/Undo+operation+on+task/) | The **Undo** button reverses a single, most recent action. It becomes available when you take the following actions:   - Resize a taskbar on the Gantt chart (live and scenario mode) - Move a taskbar on the Gantt chart (live and scenario mode) |
| [Filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Add your favorite filters to the header and filter the list of tasks to see only the items that you are interested in. There are two types of filters:   - Quick Filters - narrows down the visible scope based on JQL statements. - Date range - narrows down the visible scope to the defined period. |
| Search box | Use the search box to filter out unwanted information. Choose between two modes:   - Text search. - JQL. |
| Filter options | Apply additional filtering options to Quick Filters and Date range. |
| [Timeline](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) zoom | Zoom in and out, move to the current date, or scale to fit all your tasks on the timeline. |
| Timeline settings | Show additional elements on the timeline:   - Markers. - Timeboxes. - Week numbers. |
| [Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) | You can manually indent and outdent your tasks or move them up and down the task hierarchy. The [manual task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/) might conflict with the active structure builders, in which case a warning will be displayed. |
| [Delete task](/cms_trial/space/SPM/1918406592/Delete+task/) | You can delete tasks from the list, in which case they will also be removed from the Host and External platforms (in case of connecting with other External Platforms such as Trello or other Jira instances). |
| [Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) | Show more information about your tasks:   - Change history - Critical path - Dependencies - Milestones - Overdue tasks - Bulk change |
| Mini-map | Enable a mini-map to navigate through the whole timeline with a single click. |

### Context menu

**Right-click** on a task in the task structure or on a taskbar on a Gantt timeline (anywhere but the Key field) to prompt a context menu. This menu displays the same options as the editor slider.

Select **Edit** from the menu.

Image — asset pipeline pending  
Context menu on a task in the Gantt module.

When you click **Edit**, a Jira issue screen appears, allowing you to modify the selected task.

If the task is based on a Jira issue, you will see the **Configure Fields** button in the upper-right corner. Click it to manage issue fields. Other items (such as sprints or components) cannot be edited in this way.

Image — asset pipeline pending  
Edit task details Jira issue screen.

The task details screen looks different for a basic task. On that screen, you can update only the task summary and (optionally) start/end dates.

Image — asset pipeline pending  
Update basic task details screen.

### Editor slider

1. Left-click on a task or taskbar to select it.  
   The task is now highlighted in blue and the editor slider appears in between the work breakdown structure and the Gantt timeline.
2. Click the **three dots**.
3. Click **Edit**.

Image — asset pipeline pending  
Taskbar with the Editor slider selected.

### Redirection to a connected tool

When you click the Jira issue **Key** (either in the column view or on a Gantt timeline), you will be taken to the connected tool (for Jira, it will be the Jira issue detail screen).

Image — asset pipeline pending  
Jira issue key on a task and taskbar.

#### Limitations

- Basic tasks do not exist in any connected tool, so their Key does not function as a link.
- For a Project, the Key will take you to the Project screen.
- For a Sprint, the Key will take you to the Issue search, displaying all the sprint issues.

## Gantt module (new navigation)

Click to expand the guide

## An overview of the Gantt module

The Gantt module is your go-to module for managing projects and portfolios. Use it to plan and visualize project schedules and roadmaps, monitor and control their execution, and generate data exports showing data that meets your business needs.

The Gantt module includes four key elements:

- (**A**) Customizable [task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) that presents almost any Jira or built-in [fields](/cms_trial/space/SPM/1918635376/Fields/) as columns with [aggregated data](/cms_trial/space/SPM/1918636993/Column+data+aggregation+methods/).
- (**B**) [Timeline](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) with taskbars and dependencies that visualize and auto-schedule your work items.
- (**C**) [Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) that highlights the most important information related to your project, such as overdue tasks, critical path, dependencies, milestones, and change history.
- (**D**) [Resource panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) that shows your resources’ workload.

![Screenshot of the Gantt module.](/cms_trial/assets/4f0f133c-0294-4e75-a990-29a3a528b74d.png)

See the video to learn more.

## Main features

The table below lists the main features of the Gantt module:

| **Feature** | **Description** |
| --- | --- |
| [Scenario mode](/cms_trial/space/SPM/1918634045/Scenarios/) | Try different variants of your plan, compare the results, and find the best one. |
| [Tasks](/cms_trial/space/SPM/1918800322/Create+tasks/) | Under the **Tasks** menu, you’ll find the following features:   - Create Jira work item - Create BigPicture task - Create BigPicture task from template    - Manage templates (opens a [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page with [task templates](/cms_trial/space/SPM/1918702714/Task+template/)) - [Add work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) (opens a modal where you can configure the scope for the current box) - [Import tasks from file](/cms_trial/space/SPM/1918800781/Import+from+file/) (import your task templates from tools like MS Project, MS Excel, CSV, or OpenDocument files)   The import and export features are available with the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview)   - [Clone from another box](/cms_trial/space/SPM/1918636677/Clone+tasks+%2F+Clone+from+another+box/) (clones the existing scope from one box to another) - [Set scheduling mode for all tasks](/cms_trial/space/SPM/1918831395/Scheduling+mode/) (overwrites the scheduling mode for all tasks in a box) - [Resynchronize](/cms_trial/space/SPM/1918404058/Data+synchronization+with+connected+tools/) (triggers box data resynchronization with Jira/another connected tool) |
| View | Under the View menu, you’ll find the following features:   - Expand by levels:    - Expand n-th level (you can expand the task structure to any level. The number of available levels depends on the number of nestings present in the structure)   - Expand all (expands the entire task structure)   - Collapse all (collapses the entire task structure)   Alternatively, click **More actions** (**…**) on the **Summary** column (or the column set as the tree root in the [column view configuration](/cms_trial/space/SPM/1918668503/Column+view+creator/)) and mouse over the **Expand / collapse levels** option.   - Task structure - redirects to the [Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) page in the box configuration - [Group tasks](/cms_trial/space/SPM/1918830289/Group+tasks/) (groups tasks by one or multiple columns present in the current [column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/)) - Sort    - This option sorts data locally (only your view is affected), and the action can be reversed. The sorting criteria depend on the active columns in the current column view.  Alternatively, you can click the column header to sort data on it A-Z/ Z-A. - [Default task order](/cms_trial/space/SPM/1918667546/Organize+tasks%2F+Default+task+order/) A-Z/ Z-A (applies a global and irreversible work item sort in your view and in the view of other users)    - Restore Jira tasks order - Layout (customize the column view layout)    - Row height      - Compact     - Regular     - Wide   - Grid line (turn on/ turn off the grid lines on the Gantt timeline)      - Horizontal     - Vertical   - WBS lines (turn on/ turn off the grid lines in the column view)      - Horizontal     - Vertical - Task labels:    - Label position (determines where the task summary will be positioned on the taskbar)      - Hidden     - On taskbar     - Next to taskbar     - Smart labeling (displays summary on or next to the taskbar depending on whether the summary exceeds the taskbar length)   - Show (adds more info on/next to the taskbar)      - Key     - Summary     - Other scope info     - Dates     - Assignee     - Priority     - Scheduling mode     - Notes   - [Task color](/cms_trial/space/SPM/1918636160/Task+color/)      - Status (colors taskbars by their status)     - Manual (colors taskbars by manually selected colors) - Dependencies    - Category      - Strong     - Soft   - Display      - Expanded     - Collapsed   - Browse dependencies (open the **Dependencies** tab in the [**Infobar**](/cms_trial/space/SPM/1918800450/Dependencies+(Infobar)/)) - [Editor slider](/cms_trial/space/SPM/1918635307/Editor+slider/) - [Resource panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) |
| Indicators | Under the Indicators menu, you’ll find the following features:   - [Baselines](/cms_trial/space/SPM/1918404564/Baselines/) (baselines management)    - New baseline   - Save to version history   - Delete   - Manage baselines - [Markers](/cms_trial/space/SPM/1918699490/Markers/) - Timeboxes (Sprints, PIs) - Week numbers - [Parent task conflicts](/cms_trial/space/SPM/1918832897/Period+warnings+%2F+Parent+task+conflicts/) - Progress - [Critical path](/cms_trial/space/SPM/1918405060/Critical+path/) - [Overdue tasks](/cms_trial/space/SPM/1918537803/Overdue+tasks/) |
| [Dependencies](/cms_trial/space/SPM/1918536086/Dependencies/) | Visualize two types of dependencies on the Gantt chart:   - Strong dependencies. - Soft dependencies. |
| [Resource panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) | Use the Resources panel to see the workload of each resource (assignee). When enabled, an additional icon with **Resources settings** will appear next to the Show/Hide Resources button:  Effort modes:   - Original estimate. - Remaining estimate.   Aggregations:   - Daily. - Weekly. - Monthly. |
| Switch to Resources | Once the Resources panel is enabled, you can click **Switch to Resources** to be redirected to the Resources module. |
| [Export](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Export%20in%20Gantt%20module&linkCreation=true&fromPageId=1918797129) | The import and export features are available with the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview)  Export data to a specified file type:   - MPP, XML, MPX - XLSX - CSV - PDF image |
| [Column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/) | Column view displays field-based data for your project in a clear, tabular format. Under the **Column Views** button, you can find:   - Current view - indicates the active column view. - Available section - lists available views you can select. - Star (icon) - marks a column view as a favorite. - Manage column view - takes you to the box configuration page, where you can manage your column views.   Click **More actions** (**…**) on the selected column for column configuration options. (The available options vary depending on the column type):   - Pin column - pins the column on the left or the right side of your column view. - Sort tasks - sorts tasks A-Z or Z-A. - Customize - if the data cannot be aggregated, it provides options for customizing the way the data in the column is displayed (icon and name; icon; name). If the data can be aggregated, it provides a list of aggregation methods. - Column info - displays the field name the column is based on and indicates where the given field is mapped in the [field mapping](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297635027) settings. - Resize all columns to fit - resizes all columns in the view to fit the screen. - Delete - removes the column from the column view.   Double-click the column edge to fit the column width to its content. |
| [Undo](/cms_trial/space/SPM/1918636457/Undo+operation+on+task/) | The **Undo** button reverses a single, most recent action. It becomes available when you take the following actions:   - Resize a taskbar on the Gantt chart (live and scenario mode) - Move a taskbar on the Gantt chart (live and scenario mode) |
| [Filters](/cms_trial/space/SPM/1918503449/Filters+and+search/) | Add your favorite filters to the header and filter the list of tasks to see only the items that you are interested in. There are two types of filters:   - Quick Filters - narrows down the visible scope based on JQL statements. - Date range - narrows down the visible scope to the defined period. |
| Search box | Use the search box to filter out unwanted information. Choose between two modes:   - Text search. - JQL. |
| Filter options | Apply additional filtering options to Quick Filters and Date range. |
| [Timeline](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) zoom | Zoom in and out, move to the current date, or scale to fit all your tasks on the timeline. |
| Timeline settings | Show additional elements on the timeline:   - Markers. - Timeboxes. - Week numbers. |
| [Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) | You can manually indent and outdent your tasks or move them up and down the task hierarchy. The [manual task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/) might conflict with the active structure builders, in which case a warning will be displayed. |
| [Delete task](/cms_trial/space/SPM/1918406592/Delete+task/) | You can delete tasks from the list, in which case they will also be removed from the Host and External platforms (in case of connecting with other External Platforms such as Trello or other Jira instances). |
| [Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) | Show more information about your tasks:   - Dependencies - Overdue tasks - Milestones - Critical path - Change history - Bulk change - Reports |
| Mini-map | Enable a mini-map to navigate through the whole timeline with a single click. |
| Editor slider | The **editor slider** provides similar options to the right-click contextual menu. It appears at the border between the task structure and Gantt timeline sections.  See more on the [Editor slider](/cms_trial/space/SPM/1918635307/Editor+slider/) page. |

### Context menu

**Right-click** on a task in the task structure or on a taskbar on a Gantt timeline (anywhere but the Key field) to prompt a context menu. This menu displays the same options as the editor slider.

Select **Edit** from the menu.

![Screenshot of the context menu in the Gantt module.](/cms_trial/assets/c8050fd8-a5be-46a7-bd0a-a19c522272c6.png)

When you click **Edit**, a Jira work item screen appears, allowing you to modify the selected task.

If the task is based on a Jira work item, you will see the **Configure Fields** button in the upper-right corner. Click it to manage work item fields. Other items (such as sprints or components) cannot be edited in this way.

The task details screen looks different for a BigPicture task. On that screen, you can update only the task summary and (optionally) start/end dates.

![Screenshot of the details window for a BigPicture task in the Gantt module.](/cms_trial/assets/6ed72179-91e5-4be2-9f9d-ab96973fdbf6.png)

### Redirection to a connected tool

When you click the Jira work item **Key** (either in the column view or on a Gantt timeline), you will be taken to the connected tool (for Jira, it will be the Jira work item detail screen).

![Screenshot of the work item Key in the Gantt module.](/cms_trial/assets/0c30f507-98b9-4a1e-b7df-9a48e2ea69b5.png)

#### Limitations

- BigPicture tasks do not exist in any connected tool, so their Key does not function as a link.
- For a space, the Key will take you to the space screen.
- For a sprint, the Key will take you to the work item search, displaying all the sprint work items.