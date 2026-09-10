# Planning in the Board module

Working with the board will only allow you to move around editable tasks in Jira and when the tasks are assigned to a box with a status different than done. So, if a task's Jira status is set to done, you might not be able to move it, and BigPicture will tell you why. This applies to both cards assigned to boxes and those in the backlog sidebar.

Basic operations on tasks include:

- Planning
- Bulk re-planning
- Adding tasks to the scope
- [Creating dependencies](/cms_trial/space/SPM/1918668845/Dependencies+in+the+Board+module/)
- [Create task-based objectives](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918702275)

You can perform the above actions using drag and drop (except for adding tasks to the scope). Once you select the tasks and drag them, all the timebox areas where you can drop them will be highlighted. Read more about working with tasks on the Task multi-select page.

![Screenshot of the Board module with the Backlog sidebar opened.](/cms_trial/assets/941f8dd6-f900-4d1a-9963-82ebf9964244.png)

## Planning

Timeboxes define consecutive timeframes used for work planning. It helps to think of them as, e.g., sprints, iterations, increments, or stages.

You can add tasks to timeboxes (e.g., program increment, iteration, stage, etc.) by a simple drag-and-drop action. You only need to drag a task from the backlog and drop it in the timebox you choose. You can freely move your tasks between timeboxes and the backlog:

![Video of planning tasks in the Board module.](/cms_trial/assets/35a557d5-c825-4f41-9789-1713e22cdd25.mp4)

If you synchronize your Board module with one of the task fields, you can also add your tasks to the board by simply editing the synchronized field. Just make sure all the tasks you want to plan are in the box's scope (scope definition).

See the example

If you set up the board in such a way that at the lower level, each team uses its own Jira Agile board and each Iteration is in sync with the sprint number, the team only needs to choose the right sprint in the Sprint field of a task card to automatically add this task to a timebox assigned to this team at the upper level.

You can also create timeboxes manually or create Timboxes from Jira boards automatically.

### Tasks with children

When you assign a task to a box (for example, program increment), and it has children that are not assigned to any program increment, the parent task is still visible in the backlog, so the context of children is still visible:

![Screenshot of moving tasks from the Backlog to the board.](/cms_trial/assets/e1945c00-5b65-4ac9-bd2f-685fc21755ed.png)

Once all the children have been assigned, the parent task is no longer visible in the backlog (unless you have selected the **Show already planned tasks** option).

![Screenshot of the Show already planned tasks option in the Board module.](/cms_trial/assets/c5c86401-c790-4a9f-b936-63f3e74cc322.png)

## Bulk re-planning

You can streamline your work by selecting multiple tasks and moving them between timeboxes and the backlog. To select multiple tasks, press and hold the Command key on a Mac or Control key on Windows, then click the tasks. To select multiple tasks listed together, click the first task, press and hold the Shift key, and click the last task. All tasks in between are included in the selection.

Use CTRL+left click on Windows or CMD+click on a Mac to select multiple tasks.

## Add tasks to the scope

Another way of adding your tasks is by clicking the **+** button at the bottom of every timebox. This way, you change the box's scope.

When you add a task to the scope, the following task fields will be updated:

- Box field
- Team field
- Parent box field (if available and synchronized)