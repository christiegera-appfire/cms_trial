# Task warnings (Board module)

Task warnings indicate that you might want to take action. If inconsistencies are detected, task warnings will help you assess the situation and decide if and how you want to address them.

![board-module-main-view.png](/cms_trial/assets/37549cd5-9abf-428d-bb67-ad8fcf03ca7e.png)

## Warnings display

To see warnings, ensure the **Task warnings** option is active, as indicated by a checkmark.

![tasks-warning.png](/cms_trial/assets/3dfd756c-871a-4656-9453-762aac0da7d9.png)

Warning indications will be visible directly on task cards:

![task-warnings-lead.png](/cms_trial/assets/b008cc36-2607-4e1c-b89c-b437b1aa72cd.png)

and in the panel on the right under **Warnings** (in a form of a list):

![board-warnings.png](/cms_trial/assets/0a871367-965c-4541-a26f-0cb73c1d0e37.png)

## Warning causes

A warning indicates one of the following:

### The task period doesn't match the Box period

![board-warnings.png](/cms_trial/assets/0a871367-965c-4541-a26f-0cb73c1d0e37.png)

### Assignee doesn't match the team

A given task has been assigned to a team, but the assignee is not a member of that team.

![image-20250401-140756.png](/cms_trial/assets/3e240f16-4e5d-487c-8f3e-8715b09be980.png)

## Warning information

To see the warning information pop-up, click on the exclamation point, either directly on the task card or in the sidebar on the right.

![warning-icons.png](/cms_trial/assets/9fffd8f2-86e0-4d18-b657-6373911572c9.png)

When you click the icon, a pop-up appears:

![task-warnings-align.png](/cms_trial/assets/5495c9a9-6ac2-4d72-86ed-011b936a0f12.png)![list-of-task-warnings.png](/cms_trial/assets/d458e7a6-41b5-4a8f-ab34-1cde3b9e4d6f.png)

## Locating a task on the Board

Go to the warnings list in the right-hand sidebar and click the warning icon:

- BigPicture will take you to the task
- the task is selected (highlighted in blue)

![warning-highlighted.png](/cms_trial/assets/a5400f39-e55e-45fc-890b-5ff80e0f1c2e.png)

## Solutions

Warnings do not have to be resolved. They inform you of certain discrepancies that you might want to fix, but if you do nothing about them, the Board module will still function without problems.

After assessing the situation, you may decide what actions are appropriate.

**The task period doesn't match the Box period**

If existing scheduling rules don't allow the task to be moved, using the "Align task period"/ "Re-plan for a matching Box" buttons won't work. Strong dependencies between tasks or period mode can make simplified rescheduling impossible.

The Gantt module can help you assess the situation and make necessary adjustments.

The automatic adjustment functions as follows:

- If possible, the task period won't be changed.
- If needed, the task period will be modified to fit the Box - if the task period exceeds the Box duration, the task period will be shortened to fit the Box.
- a task is moved as little as possible - it is moved only as much as needed to fit the Box.

#### The "Align task period" button

When you click the "Align task period" button, the task duration is modified to match the Box the task is planned for.

**Case 1**

Click the exclamation mark icon. You will see the following pop-up:

![warning-highlighted-team.png](/cms_trial/assets/775b1123-cb6c-486f-a268-de6aee2785be.png)

On Gantt chart:

![warning-on-gantt.png](/cms_trial/assets/752d0816-e54b-45e0-a1ed-598f6e9855df.png)

Click the **Align task period** button:

![align-task-period.png](/cms_trial/assets/0392de24-1fa1-49f5-918e-8eed28cda6ef.png)

The task period will be changed, and the warning will disappear:

![warning-disappear.png](/cms_trial/assets/a6261bb4-f1a3-4210-bbbc-c90787f5886b.png)

The task duration didn't change. The task has been moved as little as possible, so now it's at the very end of PI1.

![warning-p1.png](/cms_trial/assets/8073c9f0-4c15-4301-b98a-d460aadf9c32.png)

#### **Case 2**

The task period falls between PI1 and PI2.

![case-2.png](/cms_trial/assets/2dab3249-aca0-4a51-b3a9-7396557d6777.png)

The following pop-up appears in the Board module:

![align-task-period-2.png](/cms_trial/assets/6da1f691-f889-4251-8650-cb955aa74218.png)

After clicking the **Align task period** button:

- the task has been moved
- task period didn't change

![resources-config.png](/cms_trial/assets/a63915c1-983a-4f5d-a9e7-6f4f467a4d2f.png)

#### **Case 3**

Task duration exceeds the Box period (Iteration 3):

![case-3.png](/cms_trial/assets/7cc44904-1eef-4e57-946f-1d21c7cc6b0d.png)

The following pop-up appears in the Board module:

![align-task-period-case-3.png](/cms_trial/assets/4bbc42bb-7e87-4663-ab86-e3a62caf08eb.png)

After clicking the **Align task period** button:

- task period was adjusted to fit within the Iteration Box

![iteration-3.png](/cms_trial/assets/3d1e9fd6-bba2-4fbf-b441-966e828e9fe2.png)

#### The "Re-plan for a matching Box" button

When you click the "Re-plan for a matching Box" button, the task is planned for a matching Box.

Click on the exclamation point. You will see the following pop-up:

![align-tasks-warning-icons.png](/cms_trial/assets/0b265f72-d663-42bd-a19b-06966466a27c.png)

On the Gantt chart:

![period-match.png](/cms_trial/assets/a36588cf-425f-4d4f-9828-aa96d864eb61.png)

Click the **Re-plan for a matching Box** button:

![replan.png](/cms_trial/assets/1089451c-aeb0-423a-917a-0cd353be8897.png)

The task will be moved to a matching Box and the warning will disappear:

![training-log.png](/cms_trial/assets/4a8a2935-a4ea-4321-b597-45039cd91545.png)

On the Gantt chart you can see that the task was moved. The task duration hasn't changed:

![resource-config-migration.png](/cms_trial/assets/8169765e-6ff3-4a74-892c-78219b0928a6.png)

### Assignee doesn't match the team - Solutions

#### The **Plan for another team** button

If the assignee is already a member of a different team, you can easily assign the task to that team.

![assignee-match.png](/cms_trial/assets/3210552d-5fe5-4c23-a349-9f6450589985.png)

Click on the exclamation mark icon:

![team-ios.png](/cms_trial/assets/fd642922-b8f1-4fb3-a6c8-7a258e4d2d1e.png)

Click the "Select team" drop-down. You will see the list of all the teams the assignee belongs to:

![team-ios-highlight.png](/cms_trial/assets/14817d2d-c4f7-400a-bae8-5e676b297056.png)

Select a team from the list and click the "**Plan for another team**" button to move the task to a different swimlane and change the team.

![plan-for-another-team-highlight.png](/cms_trial/assets/c8d938ed-777c-4a8f-ad96-9a301fb1e53c.png)

You can also always use the drag-and-drop mechanism to change team assignments.

![move-task-2.png](/cms_trial/assets/ebbf441e-26fd-4b6a-8e2d-4b76738c5a07.png)

#### The "Go to Teams" button

If the assignee is not a member of any team, you will be able to easily go to the Teams module to manage team members.

![contentId-1918636230](/cms_trial/assets/7d8a284c-8ff9-4759-9ec3-170922b0c16a.png)

Click on the exclamation point. Next, use the "Go to Teams" button to open the Teams module:

![go-to-team-button.png](/cms_trial/assets/ca370e87-b2d4-41e3-af1c-2fd1127daf9d.png)

Add the assignee to the team.

![new-member.png](/cms_trial/assets/4cd25d1a-ecbe-4fe5-996e-31e3ae338437.png)

## Warnings search functionality

The warnings list has its own search box. You can use the task summary and key to locate a task on the list and narrow down results.

![warning-search.png](/cms_trial/assets/7707d748-22c9-4fc5-8cc0-bae338818c2b.png)