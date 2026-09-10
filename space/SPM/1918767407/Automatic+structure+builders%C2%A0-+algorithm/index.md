# Automatic structure builders - algorithm

## Structure builders - basic rules

Below are some main points worth remembering when using structure builders:

- The order in which the elements are listed corresponds to the order in which they will be nested (it defines the sequence of the parent finding loops).
- The order of active builders can be changed - once you activate the elements you wish to use, you can drag them to a different spot on the list.
- Once the structure builders are defined and the tasks loaded in the Box, the structure is preserved by the App until a change is forced to rebuild it (for example, manually moving the tasks or resetting the structure and implementing a new order of structure builders)—un-toggling elements will not undo changes previously saved and implemented.
- Rearranging the structure builders does not mean that the remembered task structure is reorganized (the system always applies the rules to the existing state of things, so if you already have a structure in place, it won't be overridden - rules will apply only wherever possible).
- Tasks already in the scope of a Box may have different parents than those newly added (even though they have the same potential parents, like links or projects) as it depends on the structure builders' settings at the moment of adding a task.
- Tasks newly added to the scope of a Box follow the rules currently defined in the structure builders' settings.
- It is important to pay attention to the inverse option while using the 'Link based' structure builders to get the parent-child relations represented correctly in the task structure.
- The "Relates to" Link structure builder may be misleading, as it is difficult to distinguish between inward and outward links.

When a full-sync is executed, the following steps regarding structure building are performed:

1. The App adds all additional tasks (all tasks which are not Jira issues, Projects, Components, Versions, Agile Backlogs, Agile Sprints, in case of Trello, Boards, Lists, Checklists Checklist Items) to have all tasks in the scope (and as a consequence: all potential parent tasks in the scope).
2. A App executes two following loops to build a proper task structure:

   1. a loop for all active structure builders,
   2. a loop for all tasks in the scope.
3. It means that:

   1. At first, the App tries to find a parent task for every task consecutively based on the first active structure builder,
   2. Then, it tries to find a parent task again for every task consecutively based on the second active structure builders, etc., until all active structure builders are verified.
4. The following rules are applied by finding a parent task for a given task within a consecutive structure builder:

   1. The app always respects an already built structure by indenting a task (if an indent of the task would be contradictory to its current parent tasks, then an indent is not executed so that a structure builder never overwrites the current task structure)
   2. an indented task is always moved with all its child tasks.

Please note that the final result of the automatically built task structure based on the active structure builders can be different depending on the structure at the moment of the full sync.

If you want to reorganize your task structure entirely after it was already built, follow the steps:

1. Switch of all structure builders,
2. Select "reset Work Breakdown Structure" option,
3. Click "Save and sync".

After taking those steps, your scope will be flattened. Activate the new structure builders to build a respective task hierarchy again.

## Example

The input data is presented in the table below:

#1 Tasks in the scope:

| **Task** | **Jira project** | **Fix Versions** | **Epic link** |
| --- | --- | --- | --- |
| Project A | na. | na. | na. |
| Version 1.0 | A | na. | na. |
| Version 2.0 | A | na. | na. |
| Epic-1 | A | - | na. |
| Epic-2 | A | 1.0 | na. |
| Story-1 | A | 1.0 | Epic-1 |
| Story-2 | A | - | Epic-1 |
| Story-3 | A | - | Epic-2 |
| Story-4 | A | 1.0 | Epic-2 |
| Story-5 | A | 2.0 | Epic-2 |

#2 Active structure builders:

1. Project
2. Version
3. Epic

#3 The list of the tasks at the beginning of the WBS building is flat (no parent tasks).

### **Output data**(automatically built structure)

| **1st level** | **2nd level** | **3rd level** | **4th level** | **Explanation of the task position in a structure** |
| --- | --- | --- | --- | --- |
| Project A |  |  |  | **the task does not have a parent resulting from active structure builders** |
|  | Version 1.0 |  |  | **the parent is Project A, as:**   - **"Project structure builder" condition is met** |
|  |  | Epic-2 |  | **the parent is Version 1.0, as:**   - **"Project structure builder" condition is met** - **"Version structure builder" condition is met** |
|  |  |  | Story-3 | **The parent is Epic-2, as:**   - **"Project structure builder" condition is met** - **"Epic structure builder" condition is met** - **"Version structure builder" condition is not applicable (Epic1 does not have a version specified)** |
|  |  |  | Story-4 | **The parent is Epic-2, as:**   - **"Project structure builder" condition is met** - **"Epic structure builder" condition is met** - **"Version structure builder" condition is met** |
|  |  | Story-1 |  | **The parent is Version 1.0, as:**   - **"Project structure builder" condition is met** - **"Version structure builder" condition is met** - **"Epic structure builder" condition is ignored ie. version structure builder has a higher priority and Epic builder would cause a conflict (Epic-1 is not included in Version 1.0)** |
|  | Version 2.0 |  |  | **The parent is Project A, as:**   - **"Project structure builder" condition is met** |
|  |  | Story-5 |  | **The parent is Version 2.0, as:**   - **"Project structure builder" condition is met** - **"Version structure builder" condition is met** - **"Epic structure builder" condition is ignored ie. version structure builder has a higher priority and Epic builder would cause a conflict (Epic-1 is not included in Version 2.0)** |
|  | Epic-1 |  |  | **The parent is Project A, as:**   - **"Project structure builder" condition is met** - **"Version structure builder" condition is not applicable (Epic-1 does not have any version specified)** |
|  |  | Story-2 |  | **The parent is Project A, as:**   - **"Project structure builder" condition is met** - **"Version structure builder" condition is not applicable (Epic-1 does not have any version specified)** - **"Epic structure builder" condition is met** |