# WBS widget on Jira work item page

Similarly to the task lists in the Gantt and Scope modules, the **WBS widget** displays the selected issue's hierarchical task structure, offering a concise view of the task’s relationships directly on the Jira issue detail page. The widget also visualizes different fields as columns you can customize and aggregate.

You need the Box Viewer security role at minimum to use the WBS widget.

![Jira issue detail page featuring BigPicture's WBS widget.](/cms_trial/assets/c4533bb2-bfd8-4aa2-9a36-4f51e28c65c7.png)

## Task hierarchy

The WBS widget displays the current task and its direct parents and children. It does not show other tasks (children) that share the same parent as the current task.

If the task list is long or heavily nested, narrow down the widget's visible scope by collapsing the children.

![A collapsed task (epic) on the WS widget.](/cms_trial/assets/70e013dd-4738-4c31-85c1-30d3501a2cc7.png)

## Customize column data

The WBS widget offers similar customization options as the columns on the WBS side in the Gantt and Scope modules. Only users with relevant security roles can modify columns and save changes.

### Add and remove columns

A Box Admin sets the default column view. Box Editors and Viewers can customize the columns and restore the default column view.

Click the **Manage columns** (gear icon ) button to modify the current column view.

![Click the cog icon to prompt the menu to customize columns and restore a view.](/cms_trial/assets/97ad9cbb-4bee-4f50-b8a5-bc172d726109.png)

Then, adjust column aggregation settings as you see fit (data aggregation is available only for columns containing data that can be aggregated).

![Box Editors and Box Viewers can add and remove columns on the wbs widget.](/cms_trial/assets/14a7c64e-a6af-4eb1-9a1f-27ff46efb556.png)

### Save changes to all users

**Box Admin** **role**

A Box Admin can save changes in the column view by clicking **Save changes for all users**. The changes they save are visible to Box Editors and Box Viewers.

![box admins can save changes in a current column view to be visible to all users.](/cms_trial/assets/53dea49f-6435-40ee-8cbb-808df450d6d7.png)

### Restore column view

**Box Admin role**

After adding or removing columns, a Box Admin can click **Restore columns** to return to the initial set. Once changes are saved, the **Restore columns** option becomes inactive.

**Box Editor/Viewer role**

Box Editors and Box Viewers can restore their column views to the default one set by the Box Admin.

![Use the Restore columns option to reset your column view to the default one.](/cms_trial/assets/3da46381-c90a-4795-8b1f-bd11f56398a2.png)

### Load aggregation data

You can load aggregation data on the WBS widget columns with the **Load data** button.

![The Load data button loads aggregation data on your WBS widget.](/cms_trial/assets/dccc8220-164d-4ea7-b34d-58cadf16f8d7.png)

When you click, the app willfully load the remaining information.

![Now, the widget shows aggregation data for the task and its children and parents.ta](/cms_trial/assets/e1ee0b6c-c76f-4e2c-8039-b7d3f76785cb.png)

## Box switcher

The task you are viewing could be part of the scope of different boxes and sub-boxes. To see which other boxes the task belongs to, click the **Box switcher** button.

If another box appears on the list, you can click it to switch to that box. The WBS widget will then display the same currently viewed task but in relationship to other tasks within that box's hierarchy.

![Use the box switcher button to see if the task belongs to the scope of another box.](/cms_trial/assets/4d97298d-0372-44f9-ae9d-920c78551d53.png)

## Show on Gantt

With the **Show on Gantt** button, you can switch back directly to the Gantt module. The currently viewed task will be highlighted on the WBS and Gantt chart.

![With the Show on Gantt button you can jump straight to the Gantt module.](/cms_trial/assets/e50cdaca-78e0-45d2-9776-19be1a07d1eb.png)![How to show a task on Gantt using the WBS widget..](/cms_trial/assets/4d1ec2b2-3ff7-46cc-8d3e-a811acaec746.mov)

### Limitations

If a currently viewed task is hidden because of the active filters in the Gantt module, the app will not highlight the task.

![How to show a task on Gantt using the WBS widget when the filters are active..](/cms_trial/assets/9599b512-f564-4e08-a635-40fa4a3d4ea6.mov)