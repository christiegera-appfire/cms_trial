# Scheduling mode

## Scheduling mode (old navigation)

Click to expand the guide

## Manual and automatic scheduling

The scheduling mode determines whether a task is scheduled manually or automatically, which gives you the option of deciding how much control you want over task scheduling in a Box.

The default scheduling mode depends on [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) settings. To learn more about the scheduling rules, see the [Automations](/cms_trial/space/SPM/1918535176/Automations/) page.

There are five different modes explained further below:

- Auto basic
- Auto bottom-up
- Auto top-down
- Manual
- Locked

The 'Auto bottom-up' scheduling mode is applied to tasks with empty date fields to avoid data corruption when the tasks are structured automatically using presets.

## Configuration

- The App admins can set the default mode of a box type in BigPicture Administration.
- The Box admins can change the default scheduling mode of a box in the box configuration.

To enable the task scheduling:

1. Go to **App configuration (wrench icon at top right)** > **BigPicture configuration** > **General** > **Fields**. Only Jira administrators can access this page. During the installation, the app creates a select list (single-choice) custom field 'Task modes'.

   ![scheduling-mode.png](/cms_trial/assets/ae11cb20-6982-41a5-8846-b2b15c9fbf08.png)

## Set the task scheduling mode

### Inline editing

You can use inline editing to change the scheduling mode of a task:

- Gantt
- Scope
- Board
- Risks

Keep in mind that a change in a task scheduling mode can have a significant scheduling impact. If needed, switch to a different module to assess the situation before making a change.

### Gantt module

In the Gantt module, there are multiple ways of changing a scheduling mode.

You can change the scheduling mode of a single task (or a group of tasks, using the [multi-select](/cms_trial/space/SPM/1918832779/Multiselect+tasks/) option) by using the **right-click** dialog:

![one-task-scheduling.png](/cms_trial/assets/6e515c14-8cfc-4103-acb5-dc890118ef42.png)

You can also select multiple tasks and click the three-dot menu in the middle:

![scheduling-mode-context-menu.png](/cms_trial/assets/0fb4f16f-f8fa-49b1-b510-185a63a41a54.png)

In addition, you can overwrite the scheduling mode for all tasks in a box by selecting **Data** > **Scheduling mode**.

![Data menu in the Gantt module. The Scheduling mode option is highlighted.](/cms_trial/assets/ff6b52f6-228a-4035-b835-49e381b5f69b.png)

## Available scheduling modes

### Auto basic mode

▢ Auto basic mode is the default scheduling mode in BigPicture.

Tasks in Auto basic mode react to automation based on non-working days, dependencies, and parents in Auto top-down and Locked mode.

Tasks set to Auto basic mode do **NOT** affect children’s dates (as tasks in Auto bottom-up mode) and do **NOT** shift children’s tasks when tasks are moved.

### Manual

[Unmapped macro: inline-media-image — no content to fall back on]

 The start/end dates of a task have to be manually changed.

Start/end dates are unaffected by:

- Dependencies
- Scheduling mode of other tasks (an "auto top-down" parent task won't reposition a "locked" child)
- A move of a parent task on a timeline

When in 'Manual' mode, you can enable the [period warnings](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Period%20warnings&linkCreation=true&fromPageId=1918831395) to show how your tasks impact other tasks in the task structure.

### Locked mode

[Unmapped macro: inline-media-image — no content to fall back on]

 The duration and position of Locked tasks can't be changed.

Start/end dates are unaffected by:

- Manual changes of start/end
- Dependencies
- Scheduling mode of other tasks (an "auto top-down" parent task won't reposition a "locked" child)
- A move of a parent task on a timeline

To change the start/end dates of a "locked" task, you have to change the scheduling mode first.

### Auto top-down mode

[Unmapped macro: inline-media-image — no content to fall back on]

 A parent task in an "auto top-down" mode repositions its children to fit within its period (when possible):

- "auto top-down" and "auto bottom-up" children are affected
- "locked" and "manual" children remain unaffected

**Child position - affected**

A parent task in an "auto top-down" mode repositions its children ("auto top-down" and "auto bottom-up") to fit within its period:

![image-20240820-081453.png](/cms_trial/assets/abc0684b-f140-414a-a88c-936fbd18e954.png)

When a child is longer than the parent, start dates are matched (child duration is NOT changed):

![image-20240820-081547.png](/cms_trial/assets/947f4bbe-ab7a-4721-9c01-a566bcf5c4af.png)

**Child duration (period warning)**

An "auto top-down" parent doesn't change the duration of a child.

When period warnings are active, the discrepancy of task periods is indicated:

![image-20240820-081625.png](/cms_trial/assets/27247ed4-359e-4485-976c-20dfced8a67b.png)![contentId-1918831395](/cms_trial/assets/bb0e4fe4-0c95-40d8-a279-87bd7d2c88a9.png)

### Auto bottom-up mode

[Unmapped macro: inline-media-image — no content to fall back on]

 An "auto bottom-up" task period changes based on its children's period, i.e.:

- Start date of the "auto bottom-up" task = earliest start dates of the child tasks
- End date of the "auto bottom-up" = latest end date of child tasks

![contentId-1918831395](/cms_trial/assets/fba0a63a-50ac-4783-8fb5-e26ecd24fc29.png)

## General rules and outcomes

The general rules and outcomes are presented in the table below:

| **Scheduling mode** | **Task impacted by other tasks or dependencies?** | **Task impacted by non-working days?** | **Does moving the task affect children?** | **Task start/end date editable /movable?** |
| --- | --- | --- | --- | --- |
| Auto basic | Yes | Yes | No | Yes |
| Locked [Unmapped macro: inline-media-image — no content to fall back on] | No | No | Yes | No |
| Manual [Unmapped macro: inline-media-image — no content to fall back on] | No | No | Yes | Yes |
| Auto top-down [Unmapped macro: inline-media-image — no content to fall back on] | Yes, by either   - parents - dependencies | Yes | Yes | Yes |
| Auto bottom-up [Unmapped macro: inline-media-image — no content to fall back on] | Yes, by either   - parents - children - dependencies | Yes | Yes | Yes |

## Scheduling mode of new tasks

When you add a new task in a Box, the default scheduling mode of that Box applies.

When you add a new task directly to the task source (for example, to a Jira project), the default scheduling mode is selected automatically.

For this, the App considers the default scheduling modes of all Boxes that the task falls into and then selects the dominant one, following the prioritization below:

Locked,

1. Auto bottom-up
2. Auto top-down
3. Manual
4. Locked

## Default scheduling mode for extra tasks

You can configure the default scheduling mode for each task type, including extra tasks such as Jira epics, components, projects, sprints, versions, etc. This way, new task types you add to a box in the future will get the default scheduling mode. The configuration works per box or box type.

Setting the default scheduling mode **does NOT** affect the existing task types. This feature ensures that **future task types** added to a box automatically get the default scheduling mode.

![contentId-1918831395](/cms_trial/assets/a72229aa-0a58-4e45-8bfd-7ad557085359.png)

### Edit the default scheduling mode

To edit the default scheduling mode for Jira components, projects, sprints, and versions:

1. Go to **Box configuration** > **Tasks** > **Scheduling**.
2. Expand the *Advanced configuration* tab.
3. Click **Edit** next to the task type.
4. Select the scheduling mode.
5. Click **Edit** to save.

The video presents how to edit the default scheduling mode for Jira components.

![Recording of editing the scheduling mode for Jira components.](/cms_trial/assets/d05a6360-210b-4e6f-8045-6175ee9c97a8.mp4)

### Add the default scheduling mode for new task types

To add the default scheduling mode for a new task type:

1. Click **Add task type**.
2. Select a task type.
3. Select the scheduling mode.
4. Click **Add** to save.

The video presents how to add a new task type and set the default scheduling mode.

![Recording of adding a new task type and setting its scheduling mode.](/cms_trial/assets/9b7fc9e7-a8f0-469e-9ad3-9ed64abd5b23.mp4)

### Delete the default scheduling mode for task types

To remove a task type and its default scheduling mode:

Jira components, projects, sprints, and versions are added automatically and **cannot** be deleted.

1. Find a task type.
2. Click **Delete** next to the task type.
3. Click **Delete** to confirm.

## Limitations

### Tasks based on Jira sprints

A sprint task cannot have a scheduling mode set to auto bottom-up.

[Unmapped block: nestedExpand]

### Scheduling mode vs strong dependencies

Go to [the Strong dependencies page](/cms_trial/space/SPM/1918701700/Strong+dependencies/) to find out more.

## Scheduling mode (new navigation)

Click to expand the guide

## Manual and automatic scheduling

The scheduling mode determines whether a task is scheduled manually or automatically, which gives you the option of deciding how much control you want over task scheduling in a box.

The default scheduling mode depends on [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) settings. To learn more about the scheduling rules, see the [Automations](/cms_trial/space/SPM/1918535176/Automations/) page.

There are five different modes explained further below:

- Auto basic
- Auto bottom-up
- Auto top-down
- Manual
- Locked

The 'Auto bottom-up' scheduling mode is applied to tasks with empty date fields to avoid data corruption when the tasks are structured automatically using presets.

## Configuration

- The App admins can set the default mode of a box type in BigPicture Administration.
- The Box admins can change the default scheduling mode of a box in the box configuration.

To enable the task scheduling:

Go to **App configuration (wrench icon at top right)** > **General** > **Fields**. Only Jira administrators can access this page. During the installation, the app creates a select list (single-choice) custom field 'Task modes'.

![image-20260309-105656.png](/cms_trial/assets/150a7cd6-f762-41eb-8c08-1c7c4898bf66.png)

## Set the task scheduling mode

### Inline editing

You can use inline editing to change the scheduling mode of a task:

- Gantt
- Scope
- Board
- Risks

Keep in mind that a change in task scheduling mode can have a significant impact on scheduling. If needed, switch to a different module to assess the situation before making a change.

### Gantt module

In the Gantt module, there are multiple ways to change the scheduling mode.

You can change the scheduling mode of a single task (or a group of tasks, using the [multi-select](/cms_trial/space/SPM/1918832779/Multiselect+tasks/) option) by using the **right-click** dialog:

![Screenshot of changing the scheduling mode for a task in the Gantt module.](/cms_trial/assets/316a070a-a146-41a1-91d7-e811a7e3a4b4.png)

You can also select multiple tasks and click the three-dot menu in the middle:

![Screenshot of multiselecting tasks in the Gantt module and changing their scheduling mode.](/cms_trial/assets/f50890e9-e033-44d6-b852-286bb9af4716.png)

In addition, you can overwrite the scheduling mode for all tasks in a box by selecting **Tasks** > **Set scheduling mode for all tasks**.

![Screenshot of setting the scheduling mode for all tasks in the Gantt module.](/cms_trial/assets/a608d5f7-b5ac-4ee9-8d7f-ef010fb5ed3f.png)

## Available scheduling modes

### Auto basic mode

▢ Auto basic mode is the default scheduling mode in BigPicture.

Tasks in auto basic mode react to automation based on non-working days, dependencies, and parents in auto top-down and locked mode.

Tasks set to auto basic mode do **NOT** affect children’s dates (as tasks in auto bottom-up mode) and do **NOT** shift children’s tasks when tasks are moved.

### Manual

[Unmapped macro: inline-media-image — no content to fall back on]

 The start/end dates of a task have to be manually changed.

Start/end dates are unaffected by:

- Dependencies
- Scheduling mode of other tasks (an "auto top-down" parent task won't reposition a "locked" child)
- A move of a parent task on a timeline

When in 'Manual' mode, you can enable the [period warnings](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Period%20warnings&linkCreation=true&fromPageId=1918831395) to show how your tasks impact other tasks in the task structure.

### Locked mode

[Unmapped macro: inline-media-image — no content to fall back on]

 The duration and position of Locked tasks can't be changed.

Start/end dates are unaffected by:

- Manual changes of start/end
- Dependencies
- Scheduling mode of other tasks (an "auto top-down" parent task won't reposition a "locked" child)
- A move of a parent task on a timeline

To change the start/end dates of a "locked" task, you have to change the scheduling mode first.

### Auto top-down mode

[Unmapped macro: inline-media-image — no content to fall back on]

 A parent task in an "auto top-down" mode repositions its children to fit within its period (when possible):

- "auto top-down" and "auto bottom-up" children are affected
- "locked" and "manual" children remain unaffected

**Child position - affected**

A parent task in an "auto top-down" mode repositions its children ("auto top-down" and "auto bottom-up") to fit within its period:

![image-20240820-081453.png](/cms_trial/assets/abc0684b-f140-414a-a88c-936fbd18e954.png)

When a child is longer than the parent, start dates are matched (child duration is NOT changed):

![image-20240820-081547.png](/cms_trial/assets/947f4bbe-ab7a-4721-9c01-a566bcf5c4af.png)

**Child duration (parent task conflicts)**

An "auto top-down" parent doesn't change the duration of a child.

When [parent task conflicts](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Period%20warnings&linkCreation=true&fromPageId=1918831395) are active, the discrepancy of task periods is indicated:

![image-20240820-081625.png](/cms_trial/assets/27247ed4-359e-4485-976c-20dfced8a67b.png)![Screenshot of the Parent task conflicts option checked in the Gantt module.](/cms_trial/assets/de4314a1-a7c5-4640-8fe1-45e9bf4175c3.png)

### Auto bottom-up mode

[Unmapped macro: inline-media-image — no content to fall back on]

 An "auto bottom-up" task period changes based on its children's period, i.e.:

- Start date of the "auto bottom-up" task = earliest start dates of the child tasks
- End date of the "auto bottom-up" = latest end date of child tasks

![contentId-1918831395](/cms_trial/assets/fba0a63a-50ac-4783-8fb5-e26ecd24fc29.png)

## General rules and outcomes

The general rules and outcomes are presented in the table below:

| **Scheduling mode** | **Task impacted by other tasks or dependencies?** | **Task impacted by non-working days?** | **Does moving the task affect children?** | **Task start/end date editable /movable?** |
| --- | --- | --- | --- | --- |
| Auto basic | Yes | Yes | No | Yes |
| Locked [Unmapped macro: inline-media-image — no content to fall back on] | No | No | Yes | No |
| Manual [Unmapped macro: inline-media-image — no content to fall back on] | No | No | Yes | Yes |
| Auto top-down [Unmapped macro: inline-media-image — no content to fall back on] | Yes, by either   - parents - dependencies | Yes | Yes | Yes |
| Auto bottom-up [Unmapped macro: inline-media-image — no content to fall back on] | Yes, by either   - parents - children - dependencies | Yes | Yes | Yes |

## Scheduling mode of new tasks

When you add a new task to a box, the box's default scheduling mode applies.

When you add a new work item directly to a Jira space, the default scheduling mode is selected automatically.

For this, the App considers the default scheduling modes of all boxes that the task falls into and then selects the dominant one, following the prioritization below:

Locked,

1. Auto bottom-up
2. Auto top-down
3. Manual
4. Locked

## Default scheduling mode for extra tasks

You can configure the default scheduling mode for each task type, including extra work items such as Jira epics, components, projects, sprints, versions, etc. This way, new work item types you add to a box in the future will get the default scheduling mode. The configuration works per box or box type.

Setting the default scheduling mode **does NOT** affect the existing work item types. This feature ensures that **future work item types** added to a box automatically get the default scheduling mode.

![contentId-1918831395](/cms_trial/assets/a72229aa-0a58-4e45-8bfd-7ad557085359.png)

### Edit the default scheduling mode

To edit the default scheduling mode for Jira components, spaces, sprints, and versions:

1. Go to **Box configuration** > **Tasks** > **Scheduling**.
2. Expand the *Advanced configuration* tab.
3. Click **Edit** next to the task type.
4. Select the scheduling mode.
5. Click **Edit** to save.

The video presents how to edit the default scheduling mode for Jira components.

![Recording of editing the scheduling mode for Jira components.](/cms_trial/assets/d05a6360-210b-4e6f-8045-6175ee9c97a8.mp4)

### Add the default scheduling mode for new task types

To add the default scheduling mode for a new work item type:

1. Click **Add task type**.
2. Select a work item type.
3. Select the scheduling mode.
4. Click **Add** to save.

The video presents how to add a new work item type and set the default scheduling mode.

![Recording of adding a new task type and setting its scheduling mode.](/cms_trial/assets/9b7fc9e7-a8f0-469e-9ad3-9ed64abd5b23.mp4)

### Delete the default scheduling mode for work item types

To remove a task type and its default scheduling mode:

Jira components, spaces, sprints, and versions are added automatically and **cannot** be deleted.

1. Find a work item type.
2. Click **Delete** next to the task type.
3. Click **Delete** to confirm.

## Limitations

### Work items based on Jira sprints

A sprint task cannot have a scheduling mode set to auto bottom-up.

[Unmapped block: nestedExpand]

### Scheduling mode vs strong dependencies

Go to [the Strong dependencies page](/cms_trial/space/SPM/1918701700/Strong+dependencies/) to find out more.