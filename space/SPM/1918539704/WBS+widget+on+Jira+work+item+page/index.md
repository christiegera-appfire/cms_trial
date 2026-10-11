# WBS widget on Jira work item page

Similarly to the task lists in the Gantt and Scope modules, the **WBS widget** displays the selected issue's hierarchical task structure, offering a concise view of the task’s relationships directly on the Jira issue detail page. The widget also visualizes different fields as columns you can customize and aggregate.

You need the Box Viewer security role at minimum to use the WBS widget.

Image — asset pipeline pending  
Jira issue detail page featuring BigPicture's WBS widget.

## Task hierarchy

The WBS widget displays the current task and its direct parents and children. It does not show other tasks (children) that share the same parent as the current task.

If the task list is long or heavily nested, narrow down the widget's visible scope by collapsing the children.

Image — asset pipeline pending  
A collapsed task (epic) on the WS widget.

## Customize column data

The WBS widget offers similar customization options as the columns on the WBS side in the Gantt and Scope modules. Only users with relevant security roles can modify columns and save changes.

### Add and remove columns

A Box Admin sets the default column view. Box Editors and Viewers can customize the columns and restore the default column view.

Click the **Manage columns** (gear icon ) button to modify the current column view.

Image — asset pipeline pending  
Click the cog icon to prompt the menu to customize columns and restore a view.

Then, adjust column aggregation settings as you see fit (data aggregation is available only for columns containing data that can be aggregated).

Image — asset pipeline pending  
Box Editors and Box Viewers can add and remove columns on the wbs widget.

### Save changes to all users

**Box Admin** **role**

A Box Admin can save changes in the column view by clicking **Save changes for all users**. The changes they save are visible to Box Editors and Box Viewers.

Image — asset pipeline pending  
box admins can save changes in a current column view to be visible to all users.

### Restore column view

**Box Admin role**

After adding or removing columns, a Box Admin can click **Restore columns** to return to the initial set. Once changes are saved, the **Restore columns** option becomes inactive.

**Box Editor/Viewer role**

Box Editors and Box Viewers can restore their column views to the default one set by the Box Admin.

Image — asset pipeline pending  
Use the Restore columns option to reset your column view to the default one.

### Load aggregation data

You can load aggregation data on the WBS widget columns with the **Load data** button.

Image — asset pipeline pending  
The Load data button loads aggregation data on your WBS widget.

When you click, the app willfully load the remaining information.

Image — asset pipeline pending  
Now, the widget shows aggregation data for the task and its children and parents.ta

## Box switcher

The task you are viewing could be part of the scope of different boxes and sub-boxes. To see which other boxes the task belongs to, click the **Box switcher** button.

If another box appears on the list, you can click it to switch to that box. The WBS widget will then display the same currently viewed task but in relationship to other tasks within that box's hierarchy.

Image — asset pipeline pending  
Use the box switcher button to see if the task belongs to the scope of another box.

## Show on Gantt

With the **Show on Gantt** button, you can switch back directly to the Gantt module. The currently viewed task will be highlighted on the WBS and Gantt chart.

Image — asset pipeline pending  
With the Show on Gantt button you can jump straight to the Gantt module.

Image — asset pipeline pending  
How to show a task on Gantt using the WBS widget..

### Limitations

- If the **Show on Gantt** button is greyed out, the Gantt module is not enabled for the selected box. Enable the Gantt module in the box configuration first.

  Image — asset pipeline pending  
  Screenshot of the Show on Gantt button disabled.
- If a currently viewed task is hidden because of the active filters in the Gantt module, the app will not highlight the task.

Image — asset pipeline pending  
How to show a task on Gantt using the WBS widget when the filters are active..