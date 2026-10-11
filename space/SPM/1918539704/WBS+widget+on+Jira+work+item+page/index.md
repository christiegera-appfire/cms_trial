# WBS widget on Jira work item page

Similarly to the task lists in the Gantt and Scope modules, the **WBS widget** displays the selected issue's hierarchical task structure, offering a concise view of the task’s relationships directly on the Jira issue detail page. The widget also visualizes different fields as columns you can customize and aggregate.

You need the Box Viewer security role at minimum to use the WBS widget.

![Jira issue detail page featuring BigPicture's WBS widget.](/cms_trial/assets/648168f6-333e-4d33-9c11-3dbb2153cd64.png)

## Task hierarchy

The WBS widget displays the current task and its direct parents and children. It does not show other tasks (children) that share the same parent as the current task.

If the task list is long or heavily nested, narrow down the widget's visible scope by collapsing the children.

![A collapsed task (epic) on the WS widget.](/cms_trial/assets/8bd397e9-d53f-4c55-a977-d2d39d34f11a.png)

## Customize column data

The WBS widget offers similar customization options as the columns on the WBS side in the Gantt and Scope modules. Only users with relevant security roles can modify columns and save changes.

### Add and remove columns

A Box Admin sets the default column view. Box Editors and Viewers can customize the columns and restore the default column view.

Click the **Manage columns** (gear icon ) button to modify the current column view.

![Click the cog icon to prompt the menu to customize columns and restore a view.](/cms_trial/assets/5a02a881-a807-4684-8e25-a3e53e50574a.png)

Then, adjust column aggregation settings as you see fit (data aggregation is available only for columns containing data that can be aggregated).

![Box Editors and Box Viewers can add and remove columns on the wbs widget.](/cms_trial/assets/98ac7b43-393b-49d0-afb7-86d020030f48.png)

### Save changes to all users

**Box Admin** **role**

A Box Admin can save changes in the column view by clicking **Save changes for all users**. The changes they save are visible to Box Editors and Box Viewers.

![box admins can save changes in a current column view to be visible to all users.](/cms_trial/assets/417bb013-ea32-4dcb-8f3e-adb55ca624d8.png)

### Restore column view

**Box Admin role**

After adding or removing columns, a Box Admin can click **Restore columns** to return to the initial set. Once changes are saved, the **Restore columns** option becomes inactive.

**Box Editor/Viewer role**

Box Editors and Box Viewers can restore their column views to the default one set by the Box Admin.

![Use the Restore columns option to reset your column view to the default one.](/cms_trial/assets/4559ef44-3d1b-4083-a6cf-bcf1c4169ca2.png)

### Load aggregation data

You can load aggregation data on the WBS widget columns with the **Load data** button.

![The Load data button loads aggregation data on your WBS widget.](/cms_trial/assets/2a84232c-6563-4ec3-98a2-8c4c818f5015.png)

When you click, the app willfully load the remaining information.

![Now, the widget shows aggregation data for the task and its children and parents.ta](/cms_trial/assets/a3ac85d8-6599-4d36-bc4a-df6606cf9c1f.png)

## Box switcher

The task you are viewing could be part of the scope of different boxes and sub-boxes. To see which other boxes the task belongs to, click the **Box switcher** button.

If another box appears on the list, you can click it to switch to that box. The WBS widget will then display the same currently viewed task but in relationship to other tasks within that box's hierarchy.

![Use the box switcher button to see if the task belongs to the scope of another box.](/cms_trial/assets/f597638c-601c-47d8-a39c-b7607ef3849d.png)

## Show on Gantt

With the **Show on Gantt** button, you can switch back directly to the Gantt module. The currently viewed task will be highlighted on the WBS and Gantt chart.

![With the Show on Gantt button you can jump straight to the Gantt module.](/cms_trial/assets/1d76a0be-9414-4a5a-a9d1-882e370065fd.png)![How to show a task on Gantt using the WBS widget..](/cms_trial/assets/ec05f673-7bc1-4512-849d-16d7bf3b071d.mov)

### Limitations

- If the **Show on Gantt** button is greyed out, the Gantt module is not enabled for the selected box. Enable the Gantt module in the box configuration first.

  ![Screenshot of the Show on Gantt button disabled.](/cms_trial/assets/cf836275-6bda-4123-a7dc-990f3bd2dabd.png)
- If a currently viewed task is hidden because of the active filters in the Gantt module, the app will not highlight the task.

![How to show a task on Gantt using the WBS widget when the filters are active..](/cms_trial/assets/b55227e7-0749-4b6e-910b-8ac74a8cebe8.mov)