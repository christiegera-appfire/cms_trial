# Navigation and interface (Gantt module)

## Navigation and interface - Gantt module (old navigation)

Click to expand the guide

The Gantt module consists of four main sections:

- Task structure (Work Breakdown Structure)
- Gantt chart (Timeline with tasks represented as taskbars)
- Infobar
- Resources panel (Shows workload and capacity of the resources assigned to the box)

![Gantt module full view.](/cms_trial/assets/602cbb1f-4c1b-4ad8-a740-cd9a01b2be57.png)

## Main sections

### Task structure (Work Breakdown Structure)

The upper-left section features a [task structure](/cms_trial/space/SPM/1918832018/Task+structure/) that represents the scope of the box. You can [automatically arrange](/cms_trial/space/SPM/1918832018/Task+structure/) the box contents into a specific hierarchy. You can also create the hierarchy for your work items [manually](/cms_trial/space/SPM/1918669003/Manual+task+structure/), or combine a manual and automatic approach.

The work items arrange into columns, forming a [column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/). Most of the columns can be [aggregated](/cms_trial/space/SPM/1918636993/Column+data+aggregation+methods/), and the custom views can be saved.

### Gantt chart (Gantt timeline)

A [Gantt chart](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) visualizes the work items (tasks, milestones, epics, etc.) listed on the task structure side as [taskbars](/cms_trial/space/SPM/1918637856/Taskbar/). These taskbars are put on the timeline based on their start and/or end dates. Taskbars are interactive, that is, they can be:

- Moved (actions will reschedule the item)
- Stretched (action will change the item’s period)

Work items can be connected with [dependencies](/cms_trial/space/SPM/1918536086/Dependencies/) and are subject to other automatic [scheduling](/cms_trial/space/SPM/1918535176/Automations/) rules.

### Infobar

[Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) is a contextual sidebar that provides comprehensive information about the contents of the current box. It consists of the following tabs:

- [Dependencies](/cms_trial/space/SPM/1918800450/Dependencies+(Infobar)/)
- [Overdue tasks](/cms_trial/space/SPM/1918834482/Overdue+tasks+(Infobar)/)
- [Milestones](/cms_trial/space/SPM/1918537479/Milestones/)
- [Critical path](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918833710)
- [Change history](/cms_trial/space/SPM/1918503025/Change+history/)
- [Bulk change](/cms_trial/space/SPM/1918506627/Bulk+change/)
- [Reports](/cms_trial/space/SPM/2481848664/Contextual+reports/)

### Resources panel

You can open the [Resources panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) using the **Show/Hide Resources** button.

The panel shows all the resources assigned to the box and displays their total workload. In addition, the [Workload Details](/cms_trial/space/SPM/1918864229/Workload+details/) dialog lists all the tasks the resource is currently assigned to and shows the remaining capacity of that resource.

## View adjustment and actions

You can customize the view on the task structure and Gantt timeline sides using the options in the upper menu. Some of these options also let you carry out specific actions associated with the Gantt module.

![Gant module view adjustment options.](/cms_trial/assets/436a629a-51d5-458c-9313-e1f2b3eb4e0e.png)

### [+Add new](/cms_trial/space/SPM/1918800322/Create+tasks/)

The **+Add new** button is responsible for actions related to work items and scope:

- Create task (Jira issue or a basic task)
- Create sub-task (Jira issue or a basic task)
- Manage templates (opens a [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page with [task templates](/cms_trial/space/SPM/1918702714/Task+template/))
- Manage [scope definition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918699591) (opens a modal where you can configure the scope for the current box)
- [Import tasks from file](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Import%20from%20a%20file&linkCreation=true&fromPageId=1918699591) (import your task templates from tools like MS Project, MS Excel, CSV, or OpenDocument files)
- [Clone existing scope](/cms_trial/space/SPM/1918636677/Clone+tasks+%2F+Clone+from+another+box/) (clones the existing scope from one box to another)

### Data

The **Data** button expands the dropdown with the following actions:

- [Organize tasks](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Organize%20tasks&linkCreation=true&fromPageId=1918699591) A-Z/ Z-A (applies a global and irreversible work item sort in your view and in the view of other users)
- Restore Jira tasks order
- [Scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) (overwrites the scheduling mode for all tasks in a box)
- [Baselines](/cms_trial/space/SPM/1918404564/Baselines/) (baselines management)

  - New baseline
  - Save to version history
  - Delete
  - Manage baselines
- [Group tasks](/cms_trial/space/SPM/1918830289/Group+tasks/) (groups tasks by one or multiple columns present in the current [column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/))
- [Resynchronize](/cms_trial/space/SPM/1918404058/Data+synchronization+with+connected+tools/) (triggers box data resynchronization with Jira/another connected tool)

### Sort by

The **Sort by** button sorts column data by one of the available criteria. This option sorts data locally (only your view is affected), and the action can be reversed. The sorting criteria depend on the active columns in the current column view.

Alternatively, you can click the column header to sort data on it A-Z/ Z-A.

### View

The **View** options control the settings dedicated to the task structure and Gantt timeline:

- Expand / Collapse level

  - Expand n-th level (you can expand the task structure to any level. The number of available levels depends on the number of nestings present in the structure)
  - Expand all (expands the entire task structure)
  - Collapse all (collapses the entire task structure)

Alternatively, click **More actions** (**…**) on the **Summary** column (or the column set as the tree root in the [column view configuration](/cms_trial/space/SPM/1918668503/Column+view+creator/)) and mouse over the **Expand / collapse all** option.

![Expand collapse all view option in the gantt module.](/cms_trial/assets/53116f4c-22eb-4b30-9a28-2beb96cc49d9.png)

- Layout (customize the column view layout)

  - Row height

    - Compact
    - Regular
    - Wide
  - Grid line (turn on/ turn off the grid lines on the Gantt timeline)

    - Horizontal
    - Vertical
  - WBS lines (turn on/ turn off the grid lines in the column view)

    - Horizontal
    - Vertical
- Show (adds/overlays additional info to the Gantt timeline)

  - [Baselines](/cms_trial/space/SPM/1918404564/Baselines/)
  - [Period warnings](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Period%20warnings&linkCreation=true&fromPageId=1918699591)
  - Progress
  - [Critical path](/cms_trial/space/SPM/1918405060/Critical+path/)
  - [Overdue](/cms_trial/space/SPM/1918537803/Overdue+tasks/)
  - [Editor slider](/cms_trial/space/SPM/1918635307/Editor+slider/)

### Taskbar

The **Taskbar** button expands the dropdown with options dedicated to the Gantt timeline view adjustment:

- Label position (determines where the task summary will be positioned on the taskbar)

  - Hidden
  - On taskbar
  - Next to taskbar
  - Smart labeling (displays summary on or next to the taskbar depending on whether the summary exceeds the taskbar length)
- Show (adds more info on/next to the taskbar)

  - Key
  - Summary
  - Other scope info
  - Dates
  - Assignee
  - Scheduling mode
- [Task color](/cms_trial/space/SPM/1918636160/Task+color/)

  - Status (colors taskbars by their status)
  - Manual (colors taskbars by manually selected colors)

### Dependencies

The **Dependencies** button controls the visibility of the dependency links on your Gantt timeline. Check the box next to the dependency type you want to see:

- Category

  - Strong
  - Soft
- Display

  - Expanded
  - Collapsed
- Browse dependencies (open the **Dependencies** tab in the [**Infobar**](/cms_trial/space/SPM/1918800450/Dependencies+(Infobar)/))

### Hide/Show Resources

Click the **Hide/Show Resources** button to open the Resources panel. When the panel is enabled, the button with additional options appears next to it:

- [Effort mode](/cms_trial/space/SPM/1918764313/Effort+modes/) (set the effort mode for your resources)

  - Original Estimate
  - Remaining Estimate
  - Story Points
- Aggregation (sums the data by the selected period)

  - Daily
  - Weekly
  - Monthly

### Export

Click the **Export** button to export the current view to one of the available formats:

- PDF image
- CSV
- XLSX (MS Excel)
- MPP, MPX, PDF, XML (MS Project)

### Current view

The **current view** button shows the currently applied column setup (view). Click to open the dropdown and switch to another view.

### Save

If you introduce any changes to the current view, click the **Save** button to save it. To configure the view column, the Jira/App/Box Admin [permission](/cms_trial/space/SPM/1918829579/Permissions/) is required.

### Undo

The **Undo** button becomes active when you move or stretch (resize) the taskbar. You can reverse only the most recent action.

### Filters and search

Search the box using text and JQL-based queries. In addition, you can use the quick and date range filters to narrow down the scope of visible work items.

### Scenario mode

The scenario mode provides a safe space for you to test different “what-if” cases related to the project schedule and resources. You can create an unlimited number of scenarios, compare them, and, when you are happy with the outcome, merge them with the live version of the project.

### Editor slider

The **editor slider** provides additional options for the task structure and Gantt timeline. To use it, you must first enable it in the **View** options.

## Navigation and interface - Gantt module (new navigation)

Click to expand the guide

The Gantt module consists of four main sections:

- Task structure (Work breakdown structure)
- Gantt chart (Timeline with tasks represented as taskbars)
- Infobar
- Resource panel (Shows workload and capacity of the resources assigned to the box)

![Screenshot of the Gantt module.](/cms_trial/assets/f4bc83b0-4215-4788-aa4d-982be113230b.png)

## Main sections

### Task structure (Work Breakdown Structure)

The upper-left section features a [task structure](/cms_trial/space/SPM/1918832018/Task+structure/) that represents the scope of the box. You can [automatically arrange](/cms_trial/space/SPM/1918832018/Task+structure/) the box contents into a specific hierarchy. You can also create the hierarchy for your work items [manually](/cms_trial/space/SPM/1918669003/Manual+task+structure/), or combine a manual and automatic approach.

The work items are arranged into columns, forming a [column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/). Most of the columns can be [aggregated](/cms_trial/space/SPM/1918636993/Column+data+aggregation+methods/), and the custom views can be saved.

### Gantt chart (Gantt timeline)

A [Gantt chart](/cms_trial/space/SPM/1918701893/Timeline+(Gantt+chart)/) visualizes the work items (tasks, milestones, epics, etc.) listed on the task structure side as [taskbars](/cms_trial/space/SPM/1918637856/Taskbar/). These taskbars are put on the timeline based on their start and/or end dates. Taskbars are interactive, that is, they can be:

- Moved (actions will reschedule the item)
- Stretched (action will change the item’s period)

Work items can be connected with [dependencies](/cms_trial/space/SPM/1918536086/Dependencies/) and are subject to other automatic [scheduling](/cms_trial/space/SPM/1918535176/Automations/) rules.

### Infobar

[Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/) is a contextual sidebar that provides comprehensive information about the contents of the current box. It consists of the following tabs:

- [Dependencies](/cms_trial/space/SPM/1918800450/Dependencies+(Infobar)/)
- [Overdue tasks](/cms_trial/space/SPM/1918834482/Overdue+tasks+(Infobar)/)
- [Milestones](/cms_trial/space/SPM/1918537479/Milestones/)
- [Critical path](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918833710)
- [Change history](/cms_trial/space/SPM/1918503025/Change+history/)
- [Bulk change](/cms_trial/space/SPM/1918506627/Bulk+change/)
- [Reports](/cms_trial/space/SPM/2481848664/Contextual+reports/)

### Resource panel

You can open the [Resource panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/) in **View** > **Resource panel**.

The panel shows all the resources assigned to the box and displays their total workload. In addition, the [Workload Details](/cms_trial/space/SPM/1918864229/Workload+details/) dialog lists all the tasks the resource is currently assigned to and shows the remaining capacity of that resource.

![Screenshot of the Resource panel in the Gantt module.](/cms_trial/assets/2cc268c5-5d3a-4cc3-830a-c920446c8ff1.png)

## View adjustment and actions

You can customize the view on the task structure and Gantt timeline sides using the options in the upper menu. Some of these options also let you carry out specific actions associated with the Gantt module.

### [Tasks](/cms_trial/space/SPM/1918800322/Create+tasks/)

Under the **Tasks** menu, you’ll find the following features:

- Create Jira work item
- Create BigPicture task
- Create BigPicture task from template

  - Manage templates (opens a [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page with [task templates](/cms_trial/space/SPM/1918702714/Task+template/))
- [Add work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918699591) (opens a modal where you can configure the scope for the current box)
- [Import tasks from file](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Import%20from%20a%20file&linkCreation=true&fromPageId=1918699591) (import your task templates from tools like MS Project, MS Excel, CSV, or OpenDocument files)

The import and export features are available with the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview)

- [Clone from another box](/cms_trial/space/SPM/1918636677/Clone+tasks+%2F+Clone+from+another+box/) (clones the existing scope from one box to another)
- [Set scheduling mode for all tasks](/cms_trial/space/SPM/1918831395/Scheduling+mode/) (overwrites the scheduling mode for all tasks in a box)
- [Resynchronize](/cms_trial/space/SPM/1918404058/Data+synchronization+with+connected+tools/) (triggers box data resynchronization with Jira/another connected tool)

![Screenshot of the Gantt module with the Tasks menu expanded.](/cms_trial/assets/b3c39484-7431-46e6-9b88-a3f41316f158.png)

### View

Under the View menu, you’ll find the following features:

- Expand by levels:

  - Expand n-th level (you can expand the task structure to any level. The number of available levels depends on the number of nestings present in the structure)
  - Expand all (expands the entire task structure)
  - Collapse all (collapses the entire task structure)

Alternatively, click **More actions** (**…**) on the **Summary** column (or the column set as the tree root in the [column view configuration](/cms_trial/space/SPM/1918668503/Column+view+creator/)) and mouse over the **Expand / collapse levels** option.

- Task structure - redirects to the [Task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) page in the box configuration
- [Group tasks](/cms_trial/space/SPM/1918830289/Group+tasks/) (groups tasks by one or multiple columns present in the current [column view](/cms_trial/space/SPM/1918668270/Column+view+(Gantt+and+Scope+modules)/))
- Sort

  - This option sorts data locally (only your view is affected), and the action can be reversed. The sorting criteria depend on the active columns in the current column view.

    Alternatively, you can click the column header to sort data on it A-Z/ Z-A.
- [Default task order](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Organize%20tasks&linkCreation=true&fromPageId=1918699591) A-Z/ Z-A (applies a global and irreversible work item sort in your view and in the view of other users)

  - Restore Jira tasks order
- Layout (customize the column view layout)

  - Row height

    - Compact
    - Regular
    - Wide
  - Grid line (turn on/ turn off the grid lines on the Gantt timeline)

    - Horizontal
    - Vertical
  - WBS lines (turn on/ turn off the grid lines in the column view)

    - Horizontal
    - Vertical
- Task labels:

  - Label position (determines where the task summary will be positioned on the taskbar)

    - Hidden
    - On taskbar
    - Next to taskbar
    - Smart labeling (displays summary on or next to the taskbar depending on whether the summary exceeds the taskbar length)
  - Show (adds more info on/next to the taskbar)

    - Key
    - Summary
    - Other scope info
    - Dates
    - Assignee
    - Priority
    - Scheduling mode
    - Notes
  - [Task color](/cms_trial/space/SPM/1918636160/Task+color/)

    - Status (colors taskbars by their status)
    - Manual (colors taskbars by manually selected colors)
- Dependencies

  - Category

    - Strong
    - Soft
  - Display

    - Expanded
    - Collapsed
  - Browse dependencies (open the **Dependencies** tab in the [**Infobar**](/cms_trial/space/SPM/1918800450/Dependencies+(Infobar)/))
- [Editor slider](/cms_trial/space/SPM/1918635307/Editor+slider/)
- [Resource panel](/cms_trial/space/SPM/1918798033/Resources+panel+in+Gantt+module/)

![Screenshot of the View menu in the Gantt module.](/cms_trial/assets/154bafd8-db95-4574-87f3-73d45f6df138.png)

### Indicators

Under the Indicators menu, you’ll find the following features:

- [Baselines](/cms_trial/space/SPM/1918404564/Baselines/) (baselines management)

  - New baseline
  - Save to version history
  - Delete
  - Manage baselines
- [Markers](/cms_trial/space/SPM/1918699490/Markers/)
- Timeboxes (Sprints, PIs)
- Week numbers
- [Parent task conflicts](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Period%20warnings&linkCreation=true&fromPageId=1918699591)
- Progress
- [Critical path](/cms_trial/space/SPM/1918405060/Critical+path/)
- [Overdue tasks](/cms_trial/space/SPM/1918537803/Overdue+tasks/)

![Screenshot of the Indicators menu in the Gantt module.](/cms_trial/assets/2515e520-7415-4112-ab2a-83262d164228.png)

### Export

The import and export features are available with the BigTemplate App from the [Atlassian Marketplace.](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel?hosting=cloud&tab=overview)

Click the **Export** button to export the current view to one of the available formats:

- PDF image
- CSV
- XLSX (MS Excel)
- MPP, MPX, PDF, XML (MS Project)

### Current view

The **current view** button shows the currently applied column setup (view). Click to open the dropdown and switch to another view.

### Save

If you introduce any changes to the current view, click the **Save** button to save it. To configure the view column, the Jira/App/Box Admin [permission](/cms_trial/space/SPM/1918829579/Permissions/) is required.

### Undo

The **Undo** button becomes active when you move or stretch (resize) the taskbar. You can reverse only the most recent action.

### Filters and search

Search the box using text and JQL-based queries. In addition, you can use the quick and date range filters to narrow down the scope of visible work items.

### Scenario mode

The scenario mode provides a safe space for you to test different “what-if” cases related to the project schedule and resources. You can create an unlimited number of scenarios, compare them, and, when you are happy with the outcome, merge them with the live version of the project.

### Editor slider

The **editor slider** provides additional options for the task structure and Gantt timeline. To use it, you must first enable it in the **View** options.