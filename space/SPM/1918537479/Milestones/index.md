# Milestones

## Milestones (old navigation)

Click to expand the guide

## Introduction

You can track project milestones using the **Infobar** section in the Gantt module. Navigate to the selected milestone by clicking on the "Target" icon next to the milestone on the list.

![contentId-1918537479](/cms_trial/assets/4dbf9e69-1a93-4026-9055-997a8f701c0b.png)

## Convert tasks to milestones

Milestones can be interpreted as:

- Markers of reaching an identifiable stage in any task or project.
- Software release life cycle states.

On the timeline, milestones are represented as diamonds.

Milestones represent a point in time - milestone duration is 0 days.

**Parent tasks cannot be converter to milestones.**

If a task has children in the task tree (WBS) it can't be converted into a milestone - scheduling mode interactions between parent/child would not be possible.

### Convert a single task to a milestone

To convert a single task to a milestone or vice versa, right-click on the selected task (on the task list) or use the ". . ." button in the vertical dialog.

You can also use [inline editing](/cms_trial/space/SPM/1918637324/Inline+edit/) to turn a task into a milestone.

![contentId-1918537479](/cms_trial/assets/2a5c0b42-f657-4295-a36c-5066cc02cef1.png)

#### Start/end date recalculation

During conversion, the task end date is set as the milestone date.

Before conversion:

![image-20250314-124708.png](/cms_trial/assets/1743f6a0-c809-4a5d-a5f9-6f2d0ff78168.png)

After conversion:

![image-20250314-124735.png](/cms_trial/assets/e2ae13ad-827f-416c-ab1b-b9cb784bb0fd.png)

### Convert multiple to milestones / tasks

Use the [multi-select](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297572082) option to select a few tasks and milestones and right-click to **"Convert all to..."**:

- Milestone
- Task

When you select a milestone and a task and right-click **"Convert all to.. > Task"**:

- A milestone is converted to a task.
- A task remains unchanged because it is already a task.

![contentId-1918537479](/cms_trial/assets/9e701d3a-b4da-4a3b-ac3c-38f07b9fe257.png)

### Convert [a task with one date](/cms_trial/space/SPM/1918538029/Task+dates/) to a milestone

When a task **with one date** (“Start Date” or “End Date”) is converted to a milestone, the “Start Date” becomes the same as the “End Date”.

![contentId-1918537479](/cms_trial/assets/9436a94b-d4ca-419a-9146-77ce445754c2.png)

## Create a basic task as a milestone

1. Click the **+**(plus icon) > **Create task**> **Basic task.**

   ![image-20250314-125001.png](/cms_trial/assets/27ace13d-1432-4615-ac5a-71b4b3bbfb8e.png)
2. Fill in the task information.

   ![image-20250314-125024.png](/cms_trial/assets/74f33ea9-ef47-4ff8-aa20-c1b498ba3ce1.png)
3. Activate the toggle switch.

   ![contentId-1918537479](/cms_trial/assets/482fd4bc-16ed-4134-80e2-6325e95ecaa1.png)

## Milestone synchronization

You can synchronize milestone information using the "Label" field. When you convert a task to a milestone, the app will create a #milestone label:

![contentId-1918537479](/cms_trial/assets/840571a4-e4a2-4e73-a5e8-1f24842af359.png)

Labels will be added or removed in the following scenarios:

- A task is converted into a milestone -> the #milestone label in Jira is added.
- A milestone is converted into a regular task -> the #milestone label in Jira is removed.
- A milestone is converted into a parent task -> the #milestone label in Jira is removed.

Note: Depends on field mapping.

## Milestone overview - Infobar

You can show the list of milestones using the Gantt's Infobar:

- Only milestones expanded on the Gantt chart are visible on the list.

![contentId-1918537479](/cms_trial/assets/47a2180e-104b-45ef-b0c9-066e33d36e85.mov)

- If a user wants to see only milestones from selected parent tasks, they need to expand those parent tasks and collapse parent tasks they are not interested in.
- If a user wants to see all the milestones in the program, they need to expand all of the tasks by clicking "Expand all" on a tree root column header.

  ![contentId-1918537479](/cms_trial/assets/d56a4d4c-f202-495d-9736-7cd71dada943.png)

## Dependencies vs milestones

See [the Dependencies vs milestones page](/cms_trial/space/SPM/1918537271/Dependencies+vs+milestones/) for more information.

## Milestones (new navigation)

Click to expand the guide

## Introduction

You can track project milestones using the **Infobar** section in the Gantt module. Navigate to the selected milestone by clicking on the "Target" icon next to the milestone on the list.

![Screenshot of the Milestones tab in the Infobar in the Gantt module. ](/cms_trial/assets/3bf6dbb6-56bc-4474-8c54-0f4c2f1f090d.png)

## Convert tasks to milestones

Milestones can be interpreted as:

- Markers of reaching an identifiable stage in any task or project.
- Software release life cycle states.

On the timeline, milestones are represented as diamonds.

Milestones represent a point in time - milestone duration is 0 days.

**Parent tasks cannot be converted to milestones.**

If a task has children in the task tree (WBS) it can't be converted into a milestone - scheduling mode interactions between parent/child would not be possible.

### Convert a single task to a milestone

To convert a single task to a milestone or vice versa, right-click on the selected task (on the task list) or use the ". . ." button in the vertical dialog.

You can also use [inline editing](/cms_trial/space/SPM/1918637324/Inline+edit/) to turn a task into a milestone.

![Screenshot of the Convert to milestone option for a task in the Gantt module.](/cms_trial/assets/e684a34a-ee7c-4de6-88df-ae366234cb5b.png)

#### Start/end date recalculation

During conversion, the task end date is set as the milestone date.

Before conversion:

![image-20250314-124708.png](/cms_trial/assets/1743f6a0-c809-4a5d-a5f9-6f2d0ff78168.png)

After conversion:

![image-20250314-124735.png](/cms_trial/assets/e2ae13ad-827f-416c-ab1b-b9cb784bb0fd.png)

### Convert multiple to milestones / tasks

Use the [multi-select](/cms_trial/space/SPM/1918637506/Multiselect+(Gantt+module)/) option to select a few tasks and milestones and right-click to **"Convert all to..."**:

- Milestone
- Task

When you select a milestone and a task and right-click **"Convert all to.. > Task"**:

- A milestone is converted to a task.
- A task remains unchanged because it is already a task.

![Screenshot of the Convert all to option in the Gantt module.](/cms_trial/assets/e5a29731-a29e-4e33-b92f-f6feea1dcde7.png)

### Convert [a task with one date](/cms_trial/space/SPM/1918538029/Task+dates/) to a milestone

When a task **with one date** (“Start Date” or “End Date”) is converted to a milestone, the “Start Date” becomes the same as the “End Date”.

## Create a BigPicture task as a milestone

1. Click **Tasks** > **Create task**> **BigPicture task.**
2. Fill in the task information.
3. Activate the **Create as a milestone** toggle switch.

![Screenshot of creating a BigPicture task as a milestone in the Gantt module.](/cms_trial/assets/b2e56a57-4a33-4a72-9222-c120e9bfa284.png)

## Milestone synchronization

You can synchronize milestone information using the "Label" field. When you convert a task to a milestone, the app will create a #milestone label:

![contentId-1918537479](/cms_trial/assets/840571a4-e4a2-4e73-a5e8-1f24842af359.png)

Labels will be added or removed in the following scenarios:

- A work item is converted into a milestone -> the #milestone label in Jira is added.
- A milestone is converted into a regular task -> the #milestone label in Jira is removed.
- A milestone is converted into a parent task -> the #milestone label in Jira is removed.

Note: Depends on field mapping.

## Milestone overview - Infobar

You can show the list of milestones using the Gantt's Infobar:

- Only milestones expanded on the Gantt chart are visible on the list.

- If a user wants to see only milestones from selected parent tasks, they need to expand those parent tasks and collapse the parent tasks they are not interested in.
- If a user wants to see all the milestones in the program, they need to expand all tasks by clicking "Expand all" on the tree root column header.

  ![Screenshot of the Expand all icon on the Summary column in the Gantt module.](/cms_trial/assets/c976d291-189b-4d7a-b0bd-4351fe0de697.png)

## Dependencies vs milestones

See [the Dependencies vs milestones page](/cms_trial/space/SPM/1918537271/Dependencies+vs+milestones/) for more information.