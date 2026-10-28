# Start/end date of newly created tasks

## Start/end date of new tasks (old navigation)

Click to expand the guide

The article below refers to a task being added to a single "Own scope" Box.

For example:

- The main Program-type Box has its "own" scope (tasks are added to the scope definition of the Box)
- The project Box can be further divided (for example, into Program Increments and Iterations)
- If Program Increments and Iterations are set up to function as "sub-scope" Boxes = their scope is based on the main Box.

In the example below, a task can be in the OMEGA Box (own scope) + Program Increment 1 (sub-scope Box) + Iteration 2 (sub-scope Box).

![Box tree with a Box highlighted and having sub-Boxes](/cms_trial/assets/7eb37c18-da99-417c-88c5-f676a10b1ac1.png)

## Start/end date not specified

Check [the Task Dates page](https://appfire.atlassian.net/wiki/spaces/DLP/pages/315262798) to learn more about tasks without start/end dates.

## Start/end date overwritten

Based on scheduling rules, the App can make changes to:

- task duration
- task placement on the timeline

### Priority of scheduling rules

The scheduling mode of a task is the strictest scheduling rule, but it relies on parent-child relationships within the task tree.

**Understanding the automatic rules that impact WBS is necessary to comprehend scheduling outcomes**.

General priority of scheduling rules:

1. Scheduling mode
2. Dependencies
3. Task period alignment

In reality, when you create a new task:

1. **WBS** is determined by:

   1. **Structure builders**

      1. structure builders can be based on **dependencies**
   2. **Manual task placement** (adding a task in a particular spot in the task structure)
2. **Task period alignment** applies

   1. rules of the "own scope" Box
   2. rules of the "sub-scope" Box**→ auto-assignment** (sync with a selected field)
3. **Scheduling mode** rules apply (based on WBS)

   1. auto top-down > auto bottom-up
4. **Dependencies** apply

   1. Strong dependencies dictate the placement of start/end dates
   2. Scheduling mode rules are prioritized. Dependency will still exist, but the outcome will be limited by scheduling mode

A newly created task changes based on other tasks but can also force existing tasks to change. The impact is presented in the following table:

| **New task** | **Impacted by** | **Impacts** |
| --- | --- | --- |
| dependencies | a task can be a target of a dependency (it is affected by the source task) | a task can be a source of a dependency (it affects other tasks) |
| scheduling mode | "auto top-down" parent impacts:   - "auto top-down" children - "auto bottom-up" children | all tasks impact an "auto bottom-up" parent |

### Task creation (field values) - scheduling mechanisms involved in task period calculation

When adding a task, the fields you fill in determine what scheduling mechanisms apply and how they will position a task.

Depending on:

- the setup of a Box
- task fields filled in

| **Mechanisms dependent on task field values** | **Result** | **Applicability** |
| --- | --- | --- |
| Structure Builders | **Automatic WBS structure** is based on Box Configuration > Tasks > **Task structure**.  Structure builder rules can be manually broken. This means that when you create a new task, it is placed according to Structure Builders, but afterward, you can move it.  **If structure builders don't apply, tasks will be created exactly where you have manually specified.** | **Applies only if structure builders are active AND task is affected by them.**  Box: Structure builders can be deactivated for a given Box  Task:  A task may remain unaffected if existing rules can't be applied to it (for example, "epic link" is used as one of the structure builders, but an epic link hasn't been defined for a task.) |
| sub-Box auto-assignment  (relevant to scheduling only if combined with Task period alignment) | Sub-Boxes (such as Iterations and Program Increments) can be synced with a selected field. This means tasks can be automatically assigned to sub-boxes based on a field value.  This can change the task period if **task period alignment rules** are active for a given Box (main Program-type Box, Iteration, Program increment, etc.) | **Relevant only if combined with Task period alignment rules. Otherwise, it has no impact on task scheduling.**  Box:  Auto-assignment rules can be created only when "sub-scope" sub-boxes exist  Task:  A task may remain unaffected if existing rules can't be applied to it (for example, the "sprint" field is used to sync tasks with Iteration sub-boxes, but it hasn't been filled in for a given task). |
| Task period alignment | While task period alignment isn't directly related to any field, depending on the scope definition rules:   - adding a field value can automatically assign a task to a sub-box - which will make task period alignment rules of that Box apply to a task | **Applies if task period alignment is active.**  Task period alignment rules are set up per Box (Box Configuration > Tasks > Scheduling). Check the settings of your main Program-type Box and its sub-Boxes.  You can "set assignment on lower levels" directly from the main Program-type Box. |
| Dependencies | During task creation, you can add dependencies. Scheduling rules resulting from those dependencies apply to a newly created task.  Keep in mind that links between tasks can function as:   - **strong dependencies** - soft dependencies (no scheduling impact) - **structure builders**   Adding a link can move the task within the WBS structure and the task on the timeline. | **This applies only if task links have been added.** |
| **Independent from task fields** |  |  |
| Scheduling mode | Scheduling mode of newly created tasks is based on **Box Configuration > Tasks > Scheduling** settings. | **Always applies.**  Box:  Scheduling mode of newly created task is always based on Box settings.  Task:  A task must always be in one of four available scheduling modes. |

## Position in WBS

**Task position in the tree structure affects what scheduling rules apply.**

**Position in the tree is vital, as it determines what task is in the role of a 'parent' and 'child.' Tree relationships determine how the scheduling mode rules are executed.**

Task place in WBS is affected by:

- structure builders
- where the task was manually created

A task can be moved after it was created, but:

- the rules resulting from the initial placement have already been applied (various task periods have been adjusted accordingly)
- Moving a task will trigger period recalculation to validate rules resulting from the new position (the task period will be changed if needed). Still, changes to other tasks won't necessarily be automatically reverted.

Therefore, creating a task in the correct place in the WBS is crucial.

[Unmapped block: nestedExpand]

### Structure Builders

Example:

"Epic link" is listed as a structure builder:

![Box settings, Tasks, Task structure - list of task types](/cms_trial/assets/8b13528b-2bda-442e-85c9-1d5f1831c70b.png)

The task is created directly in Jira. "Epic link" field has been filled in:

![epic-link-jira.png](/cms_trial/assets/c82cc847-b03d-481d-8e72-3bc7f58f9997.png)

The task is nested according to the structure builder settings of a Box:

![A list of tasks with one task with indentation](/cms_trial/assets/72d778a4-5ccb-4e5e-8980-6bf401bd4c30.png)

**Even when you try to create a task in a particular spot in the structure, it will be moved according to existing structure builders:**

![Task list, adding a task](/cms_trial/assets/735c23f6-8dde-404b-8924-965e58201520.png)![Epic link filled in in a Jira ticket](/cms_trial/assets/99511bdf-753c-480c-8a37-b16e2d233295.png)![Task list, an indented task is highlighted](/cms_trial/assets/81a79bdd-f37e-46b1-adae-1e57d6cc9289.png)

**Changing an existing task can result in a task being moved based on structure builders:**

![Task list, task being moved from the structure](/cms_trial/assets/7f27204a-5694-4265-8669-924ffd95e2bd.png)![jira-task-edit-epic.png](/cms_trial/assets/6f753c33-d571-49cc-9503-55c123ea36c2.png)![Task list, one of the tasks is highlighted](/cms_trial/assets/5fa6bc87-3aaf-47eb-bc76-9f69eeabace9.png)

Structure builder rules can be manually broken. This means that when you create a new task, it is placed according to Structure Builders, but afterward, you can move it manually within the structure.

### Inline task creation

Two key things to keep in mind:

- Between what tasks are you adding a task
- Is the structure expanded

Between same-level tasks

When you create a task between the same level tasks (collapsed structure = two tasks on the same level), you will create a same-level task:

![Task being created between tasks of the same level](/cms_trial/assets/1e5ffbf4-fea3-4a0f-9535-579408f6a3e4.png)

Task added:

![Task list, task is added between tasks of the same level](/cms_trial/assets/1bd1e7e4-2ca0-46f9-aed4-d3f3d98472df.png)

Between different level tasks

The "add task" inline button can be positioned between different level tasks when the task structure is expanded. The resulting task is always created at the more indented level (nested lower in the structure):

![Task list, adding task between tasks of different levels](/cms_trial/assets/620b7ac2-10c6-4dca-b42a-6cd967c1fbe2.png)

Task added:

![task-added-between-tasks-of-different-level.png](/cms_trial/assets/1cc380c9-aea7-4aae-8ded-c1445039bacf.png)

Additional example:

![Task list, adding a task](/cms_trial/assets/6121792e-694e-4c7b-9db1-5f1c3df433a1.png)![adding-task-example-result.png](/cms_trial/assets/d55a966d-e7c8-4cc0-bba9-f47ad630cf9e.png)

### **Add task button**

Click on a task to select it (it is highlighted in blue). A same-level task will be created when you use the "Add task" button, regardless of whether the tree is expanded.

When no task is selected, the App creates a new task under the last task that has been selected even if nothing is selected at the moment! Always remember to select a parent task when using this task creation method.

![Task list, adding task by a button](/cms_trial/assets/192f893f-57e8-4508-bee3-6b8f6526b2ed.png)

Resulting task:

![Task list, a task added to the list](/cms_trial/assets/1879fedb-d42d-41d1-8f5a-ad6aab079953.png)

### Directly in Jira

When you create a task directly in Jira, it is positioned at the least indented level possible and placed at the bottom of the list.

Task position in WBS depends on the structure builder settings of a Box.

![Create Issue window in Jira](/cms_trial/assets/ee521fca-ce82-4bc0-be5a-2152800366c4.png)![Task list, a task added to the list](/cms_trial/assets/d67e6215-b74a-447f-b573-6258f4924410.png)

## Scheduling mechanisms

In the sections below, you can find description of function of each scheduling rule.

### **Scheduling mode**

Tasks can be in one of four modes:

- **Locked** = task duration can't be changed (task unaffected by other scheduling rules; task limits period of children)
- **Manual** = task duration has to be changed manually (task unaffected by other scheduling rules)
- **Auto top-down** = task has to fit within the period of its parent
- **Auto bottom-up** = task period changes the period of its parent.

**What is the scheduling mode of newly created tasks?**

Box settings determine the scheduling mode of newly created tasks.

![General Settings, Scheduling, Auto bottom-up mode chosen](/cms_trial/assets/f487e345-74a1-4486-b80e-77d60f7ed120.png)

The "auto top-down" tasks have priority over "auto bottom-up" tasks.

| - **parent affects child** - **parent is affected by child** | **child** |
| --- | --- |
| **locked** | **manual** | **auto top-down** | **auto bottom-up** |
| **parent** | locked | N/A | N/A | **AFFECTS** | **AFFECTS** |
| manual | N/A | N/A | N/A | N/A |
| auto top-down | N/A | N/A | **AFFECTS** | **AFFECTS** |
| auto bottom-up | **AFFECTED BY** | **AFFECTED BY** | **AFFECTED BY** | **AFFECTED BY** |
| Summary:   - **"auto bottom-up" parent** = affected by period of any child task - **"locked" parent** = restricts period of "auto top-down" and "auto bottom-up" tasks - **"auto top-down" parent** = restricts period of "auto top-down" tasks and "auto bottom-up" tasks |

#### "Auto top-down" parent task

An "auto top-down" parent task forces a child to fit within its period.

Affected tasks:

- other "auto top-down" tasks
- "auto bottom-up" tasks.

During task creation:

| **Situation** | **Outcome** |
| --- | --- |
| New task **fits** within the parent task period | no changes made to the period of the new task |
| New task **partially fits** within the parent task period | task duration shortened - days outside of the parent task period are 'cut off' |
| New task has **no overlap** with the parent task period | task duration = 1d  task placed on a timeline closer to the start/end dates specified during task creation |

#### "Locked" parent task

A "locked" parent task forces a child to fit within its period.

Affected tasks:

- "auto top-down" tasks
- "auto bottom-up" tasks.

During task creation:

| **Situation** | **Outcome** |
| --- | --- |
| New task **fits** within the parent task period | no changes made to the period of the new task |
| New task **partially fits** within the parent task period | task duration shortened - days outside of the parent task period are 'cut off' |
| New task has **no overlap** with the parent task period | task duration = 1d  task placed on a timeline closer to the start/end dates specified during task creation |

#### "Auto bottom-up" parent task

An "auto bottom-up" parent task is affected by the period of any child (regardless of their scheduling mode).

### Dependencies

Strong dependencies move a task on a timeline.

Without the involvement of another mechanism, dependencies don't alter the task period.

Dependencies have a lower scheduling priority than scheduling mode.

The source of a dependency remains in its original position - the target of a dependency is moved.

| **Dependency** | **Result** |
| --- | --- |
| End to start | Two tasks connected with end-to-start dependency |
| End to end | two tasks connected with end-to-end dependency |
| Start to end | Two task connected with start-to-end dependency |
| Start to start | Two tasks connected with start-to-start dependency |

### Task period alignment

Task period alignment settings of a Box regulate the relationship between a task and the Box it's in.

| **Task period alignment** | **Results** |
| --- | --- |
| no alignment | task period = unaffected |
| precise alignment | Task period = Box period |
| smart adjustment | Task's time frame aligns with the start and/or end date of a Box. Task's length remains unchanged (whenever possible) |

Task period alignment won't be realized if it conflicts with parent task period mode requirements.

### Conflicts

Starting state to which scheduling mechanisms are applied:

| **start/end date unspecified during task creation** | **start/end date specified during task creation** |
| --- | --- |
| New task:   - duration = 1d - start/end date = creation date | New task:   - duration = based on start/end date - start/end date = as specified during creation |

#### Scheduling mode vs. dependency

Order of execution:

1. Scheduling mode is executed:

   1. auto top-down parent = child adjusted to fit
   2. auto bottom-up parent = parent changed based on the child.
2. Dependencies are executed:

   1. task moved according to a dependency
   2. if the "auto bottom-up" parent period has been changed during the scheduling mode execution, it won't be further changed (for example, if the parent has been lengthened to encompass the new child, it won't 'shrink' back down, even if it would be possible after dependency moved the task).

#### Scheduling mode vs. task period alignment

Order of execution:

1. Task period alignment is executed.
2. Scheduling mode is executed - it overwrites the previous changes if necessary.

#### Dependency vs. task period alignment

Order of execution:

1. The task period alignment is executed.
2. The task is moved according to the dependency.

This means that based on task period alignment, a task can be shortened/extended and then moved on a timeline. Since dependencies themself don't modify the task period, task duration will be determined by task period alignment, but the position will be based on strong dependencies.

#### Dependency vs. task period alignment vs. scheduling mode

Order of execution:

1. Task period alignment is executed.
2. Scheduling mode is executed.
3. Dependency is executed.

## Start/end date of new tasks (new navigation)

Click to expand the guide

The article explains the logic of start/end dates of a new task added to a single Own scope box.

Key points about Own scope boxes:

- The Own-scope box, for example, a Program box, has its "own" scope. It means you define which Jira work items you want to add to that box directly in the **box configuration** > **Tasks** > [**Work items from Jira**](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/).
- Tasks inside an Agile/Classic/Hybrid project box can be divided into sub-boxes (for example, into Program Increments and Iterations).
- If Program Increments and Iterations are configured to function as Sub-scope boxes, their scope is determined by the main parent box.

Visit the page about [Scope types](/cms_trial/space/SPM/1918766536/Scope+types/) to learn more about Own scope and other box scope types in BigPicture.

In the example below, the same task can appear in the **OMEGA** Box (Own scope box), **Program Increment 1** (Sub-scope box), and **Iteration 2** (Sub-scope box).

![Box tree with a Box highlighted and having sub-Boxes](/cms_trial/assets/7eb37c18-da99-417c-88c5-f676a10b1ac1.png)

## Start/end date not specified

It is possible to add a new task to a box without specifying its start/end dates. Check the [Task dates page](https://appfire.atlassian.net/wiki/spaces/DLP/pages/315262798) to learn more.

## Start/end date overwritten

Depending on the scheduling rules, BigPicture can make changes to:

- Task duration
- Task placement on the timeline

### Priority of scheduling rules

The task scheduling mode relies on parent-child relationships within the task tree. It is the strictest scheduling rule that can affect task start/end dates.

Understanding the automatic rules that impact the task tree is necessary to understand task scheduling outcomes.

The general priority of scheduling rules is as follows:

1. [Scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/)
2. [Dependencies](/cms_trial/space/SPM/1918536086/Dependencies/)
3. [Task period alignment](/cms_trial/space/SPM/1918700014/Task+period+alignment+(Automation)/)

In reality, however, when you create a new task, the order is as follows:

1. First, a task hierarchy is determined by

   1. [Structure builders](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/)

      1. Those structure builders can be based on dependencies (links)
   2. Manual task placement (you can add a task in a particular place in the task hierarchy)
2. Then, the task period alignment applies

   1. Rules of the Own scope box
   2. Rules of the Sub-scope box→ auto-assignment (start/end date syncs with a selected work item field)
3. Then, the scheduling mode rules apply (based on the task hierarchy)

   1. Auto top-down > Auto bottom-up
4. And finally, dependencies apply

   1. Strong dependencies dictate the placement of the start/end dates
   2. Scheduling mode rules are prioritized. Dependency will still exist, but the outcome will be limited by the scheduling mode

The dates of a newly created task can change based on other tasks. Such a task can also force the dates of existing tasks to change. The impact is presented in the table:

| **New task** | **Impacted by** | **Impacts** |
| --- | --- | --- |
| Scheduling mode | **Auto top-down** parent impacts:   - **Auto top-down** children. - **Auto bottom-up** children. | All tasks impact an **Auto bottom-up** parent. |
| Dependencies | A task can be a target task of a dependency. In such a case, it is affected by the source task. | A task can be a dependency source task. In such a case, it affects other tasks. |

### Field-based scheduling mechanisms involved in task period calculation

When you add a task to a box, the task fields you fill in determine which scheduling mechanisms apply and, as a result, where the task is positioned on the timeline.

Depending on the box setup and the task fields you fill in, the behavior can be as follows:

| **Mechanisms dependent on task field values** | **Result** | **Applicability** |
| --- | --- | --- |
| Structure builders | Automatic task hierarchy is configured in the **box configuration** > **Tasks** > **Task structure**.  Structure builder rules can be manually broken. This means that when you create a new task, it is first placed according to the structure builders. But afterward, you can move it.  If structure builders are not active, tasks will be created exactly where you have manually specified their location. | Applies only if structure builders are active and the task is affected by them.  **Box**: Structure builders can be deactivated for an individual box.  **Task**:  A task can remain unaffected if the existing rules cannot be applied to it.  For example, an epic link is used as one of the structure builders, but such a link was not defined for a task. |
| Sub-box auto-assignment  (relevant to scheduling only if combined with Task period alignment) | Sub-boxes (such as Iterations and Program Increments) can be synced with a selected field. This means tasks can be automatically assigned to sub-boxes based on a field value.  This can change the task period if task period alignment rules are active for a selected box (e.g., parent Program box, Iteration, Program increment, etc). | Relevant only if combined with Task period alignment rules. Otherwise, it has no impact on task scheduling.  **Box**:  Auto-assignment rules can be created only when the sub-scope sub-boxes exist.  **Task**:  A task can remain unaffected if existing rules cannot be applied to it. For example, the **Sprint** field is used to sync tasks with the Iteration sub-boxes, but it was left blank for a given task. |
| Task period alignment | If task period alignment is not directly related to any field, then, depending on the scope definition rules:   - Adding a field value can automatically assign a task to a sub-box → this will make the task period alignment rules of that box apply to a task. | Applies if task period alignment is active.  Task period alignment rules are set up per box (**box configuration** > **Tasks** > **Scheduling**). Check the settings of your main Program box and its sub-boxes.  You can set an assignment on lower levels directly from the main Program box. |
| Dependencies | During task creation, you can add dependencies. Scheduling rules resulting from those dependencies apply to a newly created task.  Keep in mind that links between tasks can function as:   - Strong dependencies (have scheduling impact) - Soft dependencies (have no scheduling impact) - Structure builders   Adding a link can move a task within a task hierarchy and on the timeline. | This applies only if task links are added. |
| **Independent of task fields** |  |  |
| Scheduling mode | The scheduling mode for newly created tasks is set in the **box configuration > Tasks** > **Scheduling**. | **Always applies.**  **Box**:  The scheduling mode of the newly created task is always based on the box settings.  **Task**:  A task must always be in one of five available scheduling modes. |

## Position in the task hierarchy

A task's position in the task hierarchy determines which scheduling rules apply.

Position in the hierarchy is critical, as it determines which task is the parent and which is the child. Tree relationships determine how the scheduling mode rules are executed.

The task’s place in the task hierarchy is affected by:

- Structure builders.
- Place in the hierarchy where you manually created a task.

A task can be moved after it was created, but:

- The rules resulting from the initial placement are already applied (various task periods are adjusted accordingly)
- Moving a task will trigger period recalculation to validate rules resulting from the new position (the task period will be changed if needed). Still, changes to other tasks will not necessarily be automatically reverted.

For those reasons, creating a task in the correct place in the task hierarchy is crucial.

Visit the [Move task](/cms_trial/space/SPM/1918864819/Move+tasks/) page to learn how to manually move a task within the task hierarchy.

## Scheduling mechanisms

### **Scheduling mode**

Tasks can be in one of five modes:

- **Locked** - Task duration cannot be changed (a task is unaffected by other scheduling rules; task limits the period of its children).
- **Manual** - Task duration must be changed manually (a task unaffected by other scheduling rules).
- **Auto top-down** - a child task adjusts to fit within the period of its parent.
- **Auto bottom-up** - a parent task adjusts to fit within the period of its children.
- **Auto-basic** - a default mode for newly created tasks. Task adjusts as per its dependencies and non-working days.

You can configure the scheduling mode for the new tasks in the **box settings** > **Tasks** > **Scheduling**.

![Scheduling page in the box configuration. A dropdown with scheduling modes is expanded.](/cms_trial/assets/48d9748f-4f32-4a33-9284-b6eb69d7da01.png)

The **Auto top-down** tasks have priority over the **Auto bottom-up** tasks.

| - **Parent affects the child** - **Parent is affected by the child** | **Child** |
| --- | --- |
| **locked** | **manual** | **auto top-down** | **auto bottom-up** |
| **Parent** | locked | n/a | n/a | affects | affects |
| manual | n/a | n/a | n/a | n/a |
| auto top-down | n/a | n/a | affects | affects |
| auto bottom-up | affected by | affected by | affected by | affected by |
| Summary:   - An **Auto bottom-up** parent is affected by the period of any child task - A **Locked** parent restricts the period of Auto top-down and Auto bottom-up tasks. - An **Auto top-down** parent restricts the period of Auto top-down and Auto bottom-up tasks. |

#### Auto top-down parent task

An **Auto top-down** parent task forces a child to fit within its period.

Affected tasks:

- Other Auto top-down tasks
- Auto bottom-up tasks

During task creation:

| **Situation** | **Outcome** |
| --- | --- |
| New task fits within the parent task period | No changes made to the period of the new task |
| New task partially fits within the parent task period | Task duration shortened - days outside of the parent task period are 'cut off' |
| New task has no overlap with the parent task period | Task duration = 1d  Task placed on a timeline closer to the start/end dates specified during task creation |

#### Locked parent task

A **Locked** parent task forces a child to fit within its period.

Affected tasks:

- Auto top-down tasks
- Auto bottom-up tasks

During task creation:

| **Situation** | **Outcome** |
| --- | --- |
| New task fits within the parent task period | No changes made to the period of the new task |
| New task partially fits within the parent task period | Task duration shortened - days outside of the parent task period are 'cut off' |
| New task has no overlap with the parent task period | Task duration = 1d  Task placed on a timeline closer to the start/end dates specified during task creation |

#### Auto bottom-up parent task

An **Auto bottom-up** parent task is affected by the period of any child (regardless of their scheduling mode).

### Dependencies

Strong dependencies move a task on a timeline. If no other mechanism is involved, dependencies do not alter the task period. Dependencies have a lower scheduling priority than scheduling mode. The source task remains in its original position while the target task is moved.

| **Dependency** | **Result** |
| --- | --- |
| End to start | Two tasks connected with end-to-start dependency |
| End to end | two tasks connected with end-to-end dependency |
| Start to end | Two task connected with start-to-end dependency |
| Start to start | Two tasks connected with start-to-start dependency |

### Task period alignment

The task period alignment settings of a box determine the relationship between a task and the box that task belongs to.

| **Task period alignment** | **Results** |
| --- | --- |
| No alignment | Task period = Unaffected |
| Precise alignment | Task period = Box period |
| Smart adjustment | Task's timeframe aligns with the start and/or end date of a box. Task's length remains unchanged (whenever possible) |

Task period alignment won't be realized if it conflicts with the parent task period mode requirements.

### Conflicts

Start state to which scheduling mechanisms are applied:

| **Start/end date unspecified during task creation** | **Start/end date specified during task creation** |
| --- | --- |
| New task:   - duration = 1d - start/end date = creation date | New task:   - duration = based on start/end date - start/end date = as specified during creation |

#### Scheduling mode vs. dependency

Order of execution:

1. Scheduling mode is executed:

   1. Auto top-down parent = child adjusted to fit
   2. Auto bottom-up parent = parent changed based on the child.
2. Dependencies are executed:

   1. Task moved according to a dependency
   2. If the "auto bottom-up" parent period has been changed during the scheduling mode execution, it won't be further changed (for example, if the parent has been lengthened to encompass the new child, it won't 'shrink' back down, even if it would be possible after the dependency moved the task).

#### Scheduling mode vs. task period alignment

Order of execution:

1. Task period alignment is executed.
2. Scheduling mode is executed; it overwrites previous changes if necessary.

#### Dependency vs. task period alignment

Order of execution:

1. The task period alignment is executed.
2. The task is moved according to the dependency.

This means that based on task period alignment, a task can be shortened/extended and then moved on a timeline. Since dependencies themself don't modify the task period, task duration will be determined by task period alignment, but the position will be based on strong dependencies.

#### Dependency vs. task period alignment vs. scheduling mode

Order of execution:

1. Task period alignment is executed.
2. Scheduling mode is executed.
3. Dependency is executed.