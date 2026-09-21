# Use case: Organize tasks and sort by column

|  |  |
| --- | --- |
| **Goal** | **Organize and sort tasks based on selected fields (columns) to improve task visibility and project clarity.**  Globally [Organize tasks](/cms_trial/space/SPM/1918667546/Organize+tasks%2F+Default+task+order/) in ascending or descending order and choose a column by which they will be sorted. The change will apply to all users of a given box.  locally [Sort by](/cms_trial/space/SPM/1918699591/Navigation+and+interface+(Gantt+module)/) column data by one of the available criteria. This option sorts data locally (only your view is affected), and the action can be reversed.  manually Change the task’s position with the following options: **Move to top**, **Move up**, **Move down**, **Move to bottom**, **Outdent**, **Indent**. |
| **Scenario** | Globally A project manager wants to see all tasks organized by the **End date** column in ascending order to get a clear overview of the entire team's upcoming deadlines.  locally A team member wants to sort tasks by the **Status** column in descending order to see tasks with the TO DO status at the top of the structure.  manually A project manager wants to manually reorder tasks in the Gantt module to reflect changing priorities. They use the **Move to top** option to shift a high-priority task closer to the top of the list and the **Indent** option to nest related subtasks under it for better visual hierarchy. |
| **Key benefits** | - **Improved visibility** - organizing tasks globally for everyone provides a unified view of the task structure for all users, ensuring everyone is on the same page. - **Flexibility** - you can use any available fields added as a column. - **Personalized views** - if you don’t want to affect others, use the local Sort by feature. - **Flexible task reordering** - manually adjust the hierarchy of tasks. |

## Preconditions

Role You need at least a Box Editor role to use the Organize tasks and Sort by features.

box The box needs to be populated with a Jira space.

## Organize tasks and sort by column step-by-step

Globally **Organize tasks**

In this example, we want to organize tasks by the *End date* column in ascending order for all box users.

1. Go to the **Gantt** or **Scope module**.
2. Check if the **End date** field is added as a column.
3. Click **Data** > **Organize tasks A-Z** > **End Date**. The change will apply to all users of a given box.

The video presents how to organize tasks by the *End date* column.

![Video showing how to organize tasks by the End date column.](/cms_trial/assets/2173b87b-2842-4d27-b5de-5bd180ce57ff.mp4)

locally **Sort by column**

In this example, we want to sort tasks by the **Status** column in descending order.

1. Go to the **Gantt** or **Scope module**.
2. Check if the **Status** field is added as a column.
3. Method 1:

   1. Mouse over the **Status** column and click **Customize column (…)** > **Sort tasks** > **Z-A.**
4. Method 2:

   1. Expand the **Sort by** column at the top menu > select **Status** and set direction to **Z-A**.
5. That’s all. The change will apply only to you.

The video presents how to sort tasks by the *Status* column.

![Video showing how to sort tasks locally by the Status column.](/cms_trial/assets/bcad9b3e-4bac-47b1-8e09-f520d9ee7327.mp4)

manually In this example, we want to manually move one task to the top of the list and indent two other tasks under it.

1. Go to the **Gantt** or **Scope module**.
2. Right-click the task and select **Position** > **Move to top**.
3. Multi-select two tasks, right-click, and select **Position** > **Indent**.

![reposition-tasks.mp4](/cms_trial/assets/860a461c-9068-4725-89e3-7b77a4200308.mp4)

tip You can also drag and drop tasks or enable the **Editor slider** in the Gantt module and reposition them with the available arrows.

![editor-slider.mp4](/cms_trial/assets/f1837190-4275-4e97-8ba7-a34c8f6fb55d.mp4)

## Expected outcomes

- When a project manager organizes tasks globally, all box users get a shared view.
- Team members can individually sort tasks to suit their needs.
- Manually make changes to the task structure to reflect project changes.

## Additional resources

- [Organize tasks/ Default task order](/cms_trial/space/SPM/1918667546/Organize+tasks%2F+Default+task+order/)
- [Navigation and interface (Gantt module)](/cms_trial/space/SPM/1918699591/Navigation+and+interface+(Gantt+module)/)