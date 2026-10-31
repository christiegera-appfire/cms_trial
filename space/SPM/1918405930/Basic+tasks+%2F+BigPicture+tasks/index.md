# Basic tasks / BigPicture tasks

Basic tasks have been renamed to **BigPicture tasks** as part of the new navigation rollout.

Both names refer to the same functionality. You may see either term depending on whether you’re using the previous navigation or the new navigation that is currently being rolled out in BigPicture.

## Basic tasks (old navigation)

Click to expand the guide

Basic tasks are stored by the App and are NOT synchronized with Jira or other connected tools like Trello. They can be viewed only using the App's Gantt, Scope, Board modules, or the WBS Widget.

They can coexist with other tasks and work great as placeholders or temporary tasks, and simulate higher levels in the hierarchy or serve as additional information boxes. The Appuses them to replace non-issue Jira entities (like Components, Versions, Projects,) which it is unable to recreate in Jira while cloning the scope.

See the video about basic tasks below.

## Scheduling

Basic tasks follow the same set of rules (including linking, sorting, etc.). However, dependencies (links) between basic tasks will not be synchronized. As basic tasks are not Jira issues, they do not use Jira fields, hence no dates are set as Start or End dates.

However, it is possible to aggregate the MIN (earliest) or MAX (latest) date from all the children's tasks by editing the Column Views, converting tasks to Milestone, and setting Baselines just like with other tasks. You can also manually color-code your basic tasks and multiple tasks using Task templates

## Common use cases

As basic tasks are not stored in the Host Platform (in Jira) you can use them in a variety of ways. You can, for example:

- convert them to milestones
- convert them to Jira issues
- use basic tasks as placeholders
- use basic tasks as additional notes
- use basic tasks to create a custom hierarchy and aggregate data

### Convert a basic task into a Jira issue and select the issue type

1. Right-click on the issue in the WBS and select **Convert to Jira issue.**

   ![contentId-1918405930](/cms_trial/assets/8acb87d5-1b32-4fb7-b4a2-cd70c7669f4d.png)
2. Select a project in which a Jira issue will be created.

   ![contentId-1918405930](/cms_trial/assets/dc5678f9-569f-42b0-8055-710983c5c5fd.png)
3. Select Issue type (Task, Story, Bug, or Epic, etc.) to a Jira issue that will be created.

![convert.png](/cms_trial/assets/3a45bc0f-bb8d-4152-9135-a212bf163144.png)

1. The Jira issue creation dialog will appear. Fill out and modify the issue fields. Once you're done, click **Create**.

![image-20250324-130317.png](/cms_trial/assets/18c6ae6c-3449-4fe4-b4e7-cd4485531fe5.png)

If the Jira issue's screen scheme does not contain some of the basic task fields, their field values will be lost after the conversion.

For example, if you have set an "original estimate" for a basic task, but the project in which you want to place a Jira issue doesn't allow for the use of the "original estimate" field, the app doesn't have a place to save the values.

If you convert a basic task into a Jira issue, values that can't be saved are lost.

![contentId-1918405930](/cms_trial/assets/b1ed7e7a-c30f-4575-98ca-cb40b4ec970f.png)

1. In place of a basic task you will see a Jira issue

![contentId-1918405930](/cms_trial/assets/e82fd3ab-8fe3-408a-8d2f-0215c8d8de77.png)

## Create a basic task

1. Click the **+**(plus icon) > **Create task**> **basic task**

   ![contentId-1918405930](/cms_trial/assets/1e9a5a2e-0ecc-4854-b6c0-bb3be27664da.png)
2. Fill in the task information. It is not mandatory to add Start date and End date.

   ![contentId-1918405930](/cms_trial/assets/de74d5e3-924f-4ed2-add0-cc1c1449ada9.png)
3. Click **Create**

### Create another

When the box is selected → after you click **Create**a new task creation box automatically appears.

![contentId-1918405930](/cms_trial/assets/524ac437-9c95-482f-b14f-ba2e1c217678.png)

### Basic task statuses

basic tasks can have three statuses to choose from:

- To-do
- In progress
- Done

![contentId-1918405930](/cms_trial/assets/8653950b-50e0-432c-bd84-b9d0d51223c0.png)

### Keyboard shortcut

1. Select a task on WBS (task tree on the left)
2. Use the shortcut to open the 'task creation box

   ![contentId-1918405930](/cms_trial/assets/1b0c5513-ba21-47d8-9c64-18514e2ec928.png)

### Create as a milestone

To create a [milestone](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297047019), activate a toggle switch.

![image-20250324-130422.png](/cms_trial/assets/c3e42557-725c-463a-8789-cd554a06bbbc.png)

## Task structure based on basic tasks

Building the task structure using the basic task can only be done manually using drag & drop or indent/outdent arrows.

## Basic tasks templates

basic tasks can be arranged into [Templates](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298321856). Use this to add multiple tasks that represent repeatable items, such as project phases.

## Assignee

Basic tasks can be assigned to users in the Resources module. To assign a task use the drag-and-drop mechanism. (You can also add the Assignee column in the Gantt module and then edit the fields in this column - it works for the Assignee field, not Jira Assignee).

[Unmapped macro: multimedia — no content to fall back on]

The [**built-in**](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298027369) assignee field will correctly display the assignment in **other modules** (in the Gantt module you can also use this field to assign a user to a basic task).

![contentId-1918405930](/cms_trial/assets/1c0634d3-fc70-48a0-b5c6-995a4eb9eaa8.png)![contentId-1918405930](/cms_trial/assets/b21ddd75-2b88-42df-bf22-c983abf34994.png)

## Assign team to basic tasks

It is possible to quickly assign a given Team to basic tasks by inline editing in a column view.

![contentId-1918405930](/cms_trial/assets/899b2b16-e4f5-4e9c-ac13-bf87ba9a5c55.png)

## Workload of basic tasks

In the "Manual" [workload contouring](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297046379) mode, you can assign workload to basic tasks. It will be accounted for in the general capacity calculation in the same manner as all other tasks.

![contentId-1918405930](/cms_trial/assets/c03af0bc-e427-44a1-b4d3-9ea0eae70ee5.png)![contentId-1918405930](/cms_trial/assets/93e739bc-1d39-4f9d-8320-a531087347b3.png)

## Limitations

### Task reports

[Task reports](/cms_trial/space/SPM/1918863921/Task+report/) cannot be created for basic tasks.

## BigPicture tasks (new navigation)

Click to expand the guide

BigPicture tasks are stored by the App and are NOT synchronized with Jira or other connected tools, such as Trello. They can be viewed only using the Gantt, Scope, Board modules, or the WBS Widget.

They can coexist with other tasks and work great as placeholders or temporary tasks, and simulate higher levels in the hierarchy or serve as additional information boxes.

See the video about BigPicture tasks below.

## Scheduling

BigPicture tasks follow the same set of rules (including linking, sorting, etc.). However, dependencies (links) between BigPicture tasks will not be synchronized. As BigPicture tasks are not Jira work items, they do not use Jira fields, and no start or end dates are set.

However, it is possible to aggregate the MIN (earliest) or MAX (latest) date across all the children's tasks by editing the column views, converting tasks to milestones, and setting baselines just like with other tasks. You can also manually color-code your BigPicture tasks and multiple tasks using [task templates](/cms_trial/space/SPM/1918503892/Manage+task+templates/).

## Common use cases

Since BigPicture tasks are not stored in the host platform (Jira), you can use them in a variety of ways. You can, for example:

- Convert them to milestones
- Convert them to Jira work items
- Use BigPicture tasks as placeholders
- Use BigPicture tasks as additional notes
- Use BigPicture tasks to create a custom hierarchy and aggregate data

### Convert a BigPicture task into a Jira iwork item and select the work item type

1. Right-click on the BigPicture task in the WBS and select **Convert to Jira issue.**

   ![Screenshot of the Convert to Jira issue button.](/cms_trial/assets/629d754c-7e87-49c6-a701-ae7418022cd7.png)
2. Select a Jira space and work item type.

   ![Screenshot of the Convert BigPicture task to Jira issue window.](/cms_trial/assets/804e5393-6349-408c-aad2-39aa85b2f08f.png)
3. The Jira work item creation dialog will appear. Fill out and modify the fields. Once you're done, click **Create**.

   ![Screenshot of the Jira work item creation dialog.](/cms_trial/assets/d6b42672-d7d6-4862-a494-2a16e05464ba.png)

If the Jira work item's screen scheme does not include some of the BigPicture task fields, their field values will be lost during conversion.

[Unmapped block: nestedExpand]

1. In place of a BigPicture task, you will see a Jira work item.

   ![Screenshot of the converted BigPicture task to a Jira work item.](/cms_trial/assets/9c8e7f1c-17b6-4526-9e99-3d0413a1c024.png)

## Create a BigPicture task

1. Click **Tasks** > **Create** > **BigPicture task**.

   ![Screenshot of the Create BigPicture task feature in the Gantt module.](/cms_trial/assets/4f080ab6-6722-4437-97be-8b5cf88eacfe.png)
2. Fill in the task information. It is not mandatory to add the start date and end dates.

   ![Screenshot of the Create BigPicture task dialog.](/cms_trial/assets/5dd469b3-3d94-45d8-8fdc-34c29f06b7af.png)
3. Click **Create BigPicture task**.

### Create another

When the **Create another** box is selected, and you click **Create BigPicture task**,a new task creation window automatically appears.

![Screenshot of the Create BigPicture task dialog with the Create another box checked.](/cms_trial/assets/ff258cbe-347a-42b3-a487-796f66e27748.png)

### BigPicture task statuses

BigPicture tasks can have three statuses to choose from:

- To Do
- In progress
- Done

![Screenshot of the available BigPicture task statuses.](/cms_trial/assets/efb149a7-d830-4550-bbb9-bddc4e678327.png)

### Keyboard shortcut

1. Select a task on the WBS (task tree on the left).
2. Use the shortcut to open the BigPicture task creation window.

   ![Screenshot of the keyboard shortcuts for BigPicture tasks.](/cms_trial/assets/22d8d208-6a99-4362-b7d1-1571643cffac.png)

### Create as a milestone

To create a [milestone](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297047019), toggle the switch.

![Screenshot of the Create BigPicture task dialog with the Create as a milestone toggle switched.](/cms_trial/assets/0ad80889-ebfe-4c0b-9371-c0c250fb7ff6.png)

## Task structure based on BigPicture tasks

Building the task structure using the BigPicture task can only be done manually using drag & drop or indent/outdent arrows.

## BigPicture tasks templates

BigPicture tasks can be arranged into [templates](/cms_trial/space/SPM/1918503892/Manage+task+templates/). Use this to add multiple tasks that represent repeatable items, such as project phases.

## Assignee

BigPicture tasks can be assigned to users in the Resources module. To assign a task, use the drag-and-drop mechanism. You can also add the Assignee column in the Gantt module and then edit the fields in this column - it works for the Assignee field, not Jira Assignee.

![Video presenting how to drag and drop a task to assign it to a user in the Resources module.](/cms_trial/assets/3cbe36e2-c5be-4d6f-b31a-a21500a6a568.mp4)

The [built-in](/cms_trial/space/SPM/1918633429/Concept+of+a+field/) assignee field will correctly display the assignment in **other modules** (in the Gantt module, you can also use this field to assign a user to a BigPicture task).

## Assign team to BigPicture tasks

It is possible to quickly assign a given team to BigPicture tasks by inline editing in a column view.

![Screenshot of the Team column added to the Gantt column view.](/cms_trial/assets/012eb266-fb00-494f-a378-33ac423a9f54.png)

## Workload of BigPicture tasks

In the "Manual" [workload contouring](/cms_trial/space/SPM/1918767273/Workload+contouring/) mode, you can assign workload to BigPicture tasks. It will be accounted for in the general capacity calculation in the same manner as all other tasks.

![Screenshot of a BigPicture task with the Manual contouring mode selected.](/cms_trial/assets/7bdb6c33-2e5b-4569-9a0d-c8d4d2b68727.png)

## Limitations

### Task reports

[Task reports](/cms_trial/space/SPM/1918863921/Task+report/) cannot be created for BigPicture tasks.