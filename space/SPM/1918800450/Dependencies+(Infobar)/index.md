# Dependencies (Infobar)

## Dependencies (Inforbar) (old navigation)

## Overview

The [**Dependencies**](/cms_trial/space/SPM/1918536086/Dependencies/) section displays a list of task dependencies present in a given box and groups them:

- Correct dependencies (dependencies exist and affect scheduling properly).
- Broken dependencies (dependencies exist but they do not affect scheduling as they should, if at all).
- Non-scheduling dependencies (soft dependencies—dependencies that show task relationships but do not affect scheduling).

The Infobar sums up the dependencies in each category and displays the total on each group. That applies to dependencies that:

- Connect two tasks that both are in the scope of the current box.
- Connect one task that is in the scope of the current box and the other one that is in the scope of another box (for example, a cross-project dependency). Such a dependency is indicated with an out-of-view icon.

![The Ganttm module's Infobar, dependency section.](/cms_trial/assets/2945a2e1-dbde-47b5-95d9-cfef632d91e7.png)

## Dependency details

Expand a dependency to see the following information:

- Source task
- Target task
- Task key
- Task dates
- Status
- Dependency type
- Dependency details
- [Lag time](/cms_trial/space/SPM/1918406747/Lag+time/) (if applicable)
- [ASAP](/cms_trial/space/SPM/1918764948/ASAP+mode/) (if applicable)

## Actions in the dependencies tab

### Search for tasks

The **search bar** lets you find a specific task (or tasks) whose dependencies you want to inspect.

You can narrow down the search results to show only those dependencies of the selected tasks that have the ASAP mode enabled or disabled.

![Search bar options in the Dependencies tab.](/cms_trial/assets/f83a92c3-abee-4dd5-8f95-b275675c64a6.png)

### Focus on source/target task

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Focus on source** or **Focus on target**.

The **Focus on** feature focuses the Gantt timeline on the source or target task of a selected dependency. The app adjusts the timeline and highlights the source or target task.

Only the tasks that belong to the scope of the current box can be focused.

### Edit dependency

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Edit**.

### Delete dependency

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Delete**.
3. Click **Delete** to confirm the action.

## Out-of-view dependencies

Out-of-view dependencies cannot be displayed on the Gant chart but are included on the dependency list. The out-of-view icon indicates the out-of-view tasks when one of the dependent tasks (source or target) is:

- in the scope of the current box
- not visible due to the active filters or search query

If the task is out of scope or filtered out, you cannot snipe to it, either.

## Dependencies (Inforbar) (new navigation)

## Overview

The [**Dependencies**](/cms_trial/space/SPM/1918536086/Dependencies/) section displays a list of task dependencies present in a given box and groups them:

- Correct dependencies (dependencies exist and affect scheduling properly).
- Broken dependencies (dependencies exist but they do not affect scheduling as they should, if at all).
- Non-scheduling dependencies (soft dependencies—dependencies that show task relationships but do not affect scheduling).

The Infobar sums up the dependencies in each category and displays the total on each group. That applies to dependencies that:

- Connect two tasks that both are in the scope of the current box.
- Connect one task that is in the scope of the current box and the other one that is in the scope of another box (for example, a cross-project dependency). Such a dependency is indicated with an out-of-view icon.

![gantt-dependencies-list.png](/cms_trial/assets/8945e854-0afa-48c3-a7ef-6b6397488054.png)

## Dependency details

Expand a dependency to see the following information:

- Source task
- Target task
- Task key
- Task dates
- Status
- Dependency type
- Dependency details
- [Lag time](/cms_trial/space/SPM/1918406747/Lag+time/) (if applicable)
- [ASAP](/cms_trial/space/SPM/1918764948/ASAP+mode/) (if applicable)

## Actions in the dependencies tab

### Search for tasks

The **search bar** lets you find a specific task (or tasks) whose dependencies you want to inspect.

You can narrow down the search results to show only those dependencies of the selected tasks that have the ASAP mode enabled or disabled.

![gantt-dependencies-actions.png](/cms_trial/assets/e3008d09-58ad-4b07-a0c1-b6e0a4c644e6.png)

### Focus on source/target task

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Focus on source** or **Focus on target**.

The **Focus on** feature focuses the Gantt timeline on the source or target task of a selected dependency. The app adjusts the timeline and highlights the source or target task.

Only the tasks that belong to the scope of the current box can be focused.

The video presents the **Focus on task** feature.

![gantt-focus-on-source.png](/cms_trial/assets/a3e34095-c560-42e3-829e-0db82b8621f4.png)

### Edit dependency

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Edit**.

![dependency-edit-details.png](/cms_trial/assets/0b16786f-7a41-4ed6-8bbe-4a4241effbaa.png)

### Delete dependency

1. Click **More actions** (**…**) to open the context menu.
2. From the dropdown, select **Delete**.
3. Click **Delete** to confirm the action.

## Out-of-view dependencies

Out-of-view dependencies cannot be displayed on the Gant chart but are included on the dependency list. The out-of-view icon indicates the out-of-view tasks when one of the dependent tasks (source or target) is:

- in the scope of the current box
- not visible due to the active filters or search query

If the task is out of scope or filtered out, you cannot snipe to it, either.