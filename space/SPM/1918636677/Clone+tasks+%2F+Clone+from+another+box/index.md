# Clone tasks / Clone from another box

The **Clone existing scope** and **Clone from another box** options offer the same functionality. This option comes under two different names due to the new navigation that is currently being rolled out in BigPicture.

## Clone tasks (old navigation)

Click to expand the guide

## Create tasks by cloning

Cloning adds tasks to the Box in which you initiate it.

If you want to clone the scope of a Box "Alfa" into "Beta", you have to go to the "Beta" Box and carry out the cloning there - during the cloning, you select a Box that serves as a source of tasks; those tasks are then added to a Box in which you have clicked "Clone existing scope".

Only the following field values can be cloned:

| **Data** | **Cloning result (Yes / No)** |
| --- | --- |
| Jira issue | yes |
| Task structure | yes |
| Issue types | conditional yes   - If the spacedoes have the required issue types in the issue type scheme, they will be matched. - If a new space with different issue types (issue scheme) is used, the default issue type will be used for all tasks that cannot be matched (usually, it will be either "story" or "task"). - **Sub-tasks will be cloned as default issue types. It is not possible to maintain the distinction.** |
| Jira epics | yes |
| Dependencies | Yes. All dependencies (both soft and strong) get copied, and all the settings (ASAP, lag time, etc.) are preserved. |
| Summary field | yes |
| Start / End date synchronized fields | yes |
| Skills | yes |
| Manual Colors | yes |
| Milestones | yes |
| Original Estimate | yes |
| Basic tasks | yes  Additionally, task templates can be created or inherited, allowing you to create a whole group of Basic tasks with a single click. Basic tasks in a time template can't be nested (it is possible to change their placement in the hierarchy later). |
| Trello tasks | yes  Conned as Basic tasks. |
| Status | no  Task status depends on the Jira project configuration. The initial status of its workflow (for example, "OPEN") is applied to all copied tasks. |
| Other fields besides Summary and synchronized date fields | no |
| Required fields | no  The required fields can not be populated by the app; before cloning tasks, **make sure all possible fields are set as optional.** |
| Version or Component | no  The app is capable of creating Jira Issues and recreating the structure. It is not capable of creating anything that is not a Jira Issue while cloning, therefore it will automatically replace the original Version or Component with a Basic Task. |

No other information will be copied during the cloning process, even if fields are filled in and set to "required".

## Steps

To open the clone scope dialog click "+add" button and select 'Clone existing scope':  

[Unmapped macro: inline-media-image — no content to fall back on]

Next:

- select the Box you want to clone (tasks from that box are copied)
- select the target project to store the cloned tasks (tasks are copied to a selected Jira space - you can set up a new, empty project for the clone)

Image — asset pipeline pending  
contentId-1918636677

Cloned tasks will be added gradually.

The process progress is indicated by the icon:

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

**Refresh the page so that you can observe the results.**

Image — asset pipeline pending  
contentId-1918636677

## Automatic linking of the original and cloned tasks

When you clone tasks, the original task and the new task can be linked, depending on the settings.

[Unmapped macro: button-handy — no content to fall back on]

## Possible problems and solutions

### Setting up an empty Jira project

Cloning JIRA tasks effectively means they get copied. To successfully perform such action, you not only need a source (a Jira space that you make a copy of) but also somewhere to put them (a Jira space where the copied issues live). The copies are visualized in the App, but they must exist somewhere in Jira itself.

You can easily create a new, empty Jira space. If you wish, you can use an existing Jira space to perform this action ("Create with shared configuration" option) - this will result in copying the Jira space setup (permission, notification, issue security, workflow, issue type, issue type screen, field configuration).

You don't have to set up an empty Jira space and can use an existing one. In such cases, copied issues will be added to the existing ones.

[Unmapped block: nestedExpand]

### Copy issues

In the App, in the Gantt module, click the "+" Add task button and select "clone existing scope" from the list ("clone existing scope" functionality is also available in the [Scope module](/cms_trial/space/SPM/1918666763/Scope+module/)).

In the first drop-down select a Box - the scope of that Box (Jira projects, issues, etc) will be copied. Keep in mind, that you are not selecting a Jira space, you are selecting a Box; tasks from that Box get copied. This means, that if a Box includes multiple projects or just a limited number of issues from one project, that's what will get copied.

The second drop-down gives you the destination Jira space.

If the destination Jira space already contains issues, they will automatically be included in the scope.

scope = copied items + existing destination items

[Unmapped block: nestedExpand]

### Cloning Option is Unavailable:

[Scope type](/cms_trial/space/SPM/1918766536/Scope+types/) dictates whether the option is available.

#### In Boxes with "Own" scope

If a Box type was created with "Own" scope, the option is available. You can clone a scope of an existing Box (with "Own" scope) or import a file.

[Unmapped block: nestedExpand]

#### In Boxes with "Own" scope from boxes with "Sub" scope

If you try to copy tasks from a Box with "Sub" scope type, you won't be able to select it as a source. "None" and "Sub" scope type Boxes won't be coming up on the list of possible options, as the action doesn't make sense. A Box with "Sub" scope doesn't have its own scope you could copy.

[Unmapped block: nestedExpand]

#### In Boxes with "Sub" scope

If a Box has been created with "Sub-scope" the options are inactive.

The scope of a box with a "sub-scope" type is based strictly on the upper-level Box; a sub-Box itself doesn't have its own scope. You can't clone or import tasks to a Box that doesn't have its own scope. The action has to be performed in the upper-level Box with "Own" scope.

[Unmapped block: nestedExpand]

#### "None" scope Boxes

A Box with "None" scope doesn't display any tasks at all, it only aggregates its sub-Boxes.

You can't clone a scope into a Box with "None" scope.

You can't clone a scope from a Box with "None" scope - you can't find such a Box on a list of available scope sources. This means you can't select such a Box, not on purpose, not accidentally, as a source to be cloned.

### Required Fields

The most common reason for the cloning process to fail is related to Jira Field Configuration.

Image — asset pipeline pending  
contentId-1918636677

The "Required" fields have to be changed to "Optional" for the time when the App is importing the program.

Keep in mind, that the change of the Field Configuration scheme has to be applied to the target Jira project (the project issues get copied to).

Image — asset pipeline pending  
contentId-1918636677

We recommend creating a temporary scheme instead of changing an existing one. This way, other spaces will not be affected. Then, when needed, you apply a "temporary" configuration to a space instead of changing an existing configuration (that may be in use by multiple different projects) to minimize the impact.

To make things easier you may copy an existing configuration:

Image — asset pipeline pending  
contentId-1918636677

Name it to make things clear for other users:

Image — asset pipeline pending  
contentId-1918636677

Click on the field configuration name and change all items to "optional" within it:

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

Add a new field configuration scheme:

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

Make sure that the correct field configuration is associated with the scheme:

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

Go to the Jira space that is added to the Box scope (the project Jira issues will be copied to):

Image — asset pipeline pending  
contentId-1918636677

Find the field configuration:

Image — asset pipeline pending  
contentId-1918636677

Change the scheme:

Image — asset pipeline pending  
contentId-1918636677

Image — asset pipeline pending  
contentId-1918636677

You can proceed with the cloning after changing the Field Configuration.

## Clone from another box (new navigation)

Click to expand the guide

## Create tasks by cloning from another box

Cloning adds tasks to the box where you initiated it.

If you want to clone the scope of a box "Alfa" into "Beta", you have to go to the "Beta" box and carry out the cloning there. During the cloning, you select a box that serves as a source of tasks; those tasks are then added to a box from which you clicked **Clone from another box**.

Only the following field values can be cloned:

| **Data** | **Cloning result (Yes / No)** |
| --- | --- |
| Jira work item | yes |
| Task structure | yes |
| Work item types | conditional yes   - If the spaces have the required work item types in the work item type scheme, they will be matched. - If a new space with different work item types (work item scheme) is used, the default work item type will be used for all work items that cannot be matched (usually, it will be either "story" or "task"). - **Sub-tasks will be cloned as default work item types. It is not possible to maintain the distinction.** |
| Jira epics | yes |
| Dependencies | Yes. All dependencies (both soft and strong) get copied, and all the settings (ASAP, lag time, etc.) are preserved. |
| Summary field | yes |
| Start / End date synchronized fields | yes |
| Skills | yes |
| Manual Colors | yes |
| Milestones | yes |
| Original Estimate | yes |
| BigPicture tasks | yes  Additionally, task templates can be created or inherited, allowing you to create a whole group of BigPicture tasks with a single click. BigPicture tasks in a time template can't be nested (it is possible to change their placement in the hierarchy later). |
| Trello tasks | yes  Connected as BigPicture tasks. |
| Status | no  Task status depends on the Jira space configuration. The initial status of its workflow (for example, "OPEN") is applied to all copied tasks. |
| Other fields besides Summary and synchronized date fields | no |
| Required fields | no  The required fields can not be populated by the app; before cloning tasks, **make sure all possible fields are set as optional.** |
| Version or Component | no  The app can create Jira work items and recreate the structure. It is not capable of creating anything that is not a Jira work item while cloning, therefore, it will automatically replace the original Version or Component with a BigPicture task. |

No other information will be copied during the cloning process, even if fields are filled in and set to "required".

## Steps

To clone tasks from another box:

1. Click **Tasks** > **Clone from another box**.

   Image — asset pipeline pending  
   Screenshot of the Clone from another box option in the Tasks menu in the Gantt module.
2. Next:

   1. Select the box you want to clone (tasks from that box are copied).
   2. Select the target space to store the cloned work items (work items are copied to the selected Jira space; you can set up a new, empty space for the clone).

      Image — asset pipeline pending  
      Screenshot of the Clone existing scope window.
3. Cloned tasks will be added gradually. The process progress is indicated by the icon:

Image — asset pipeline pending  
Screenshot with the Importing tasks status.

Image — asset pipeline pending  
Screenshot with the Imported successfully status.

1. Refresh the page so that you can observe the results.

## Automatic linking of the original and cloned tasks

When you clone tasks, the original task and the new task can be linked, depending on the settings. See more on the [Scope cloning](/cms_trial/space/SPM/1918767832/Scope+cloning/) page.

## Possible problems and solutions

### Setting up an empty Jira space

Cloning Jira work items effectively means they get copied. To successfully perform such an action, you not only need a source (a Jira space you make a copy of) but also to destination (a Jira space where the copied work items live). The copies are visualized in the App, but they must exist somewhere in Jira itself.

You can easily create a new, empty Jira space. If you want, you can use an existing Jira space to perform this action (**Create with shared configuration** option) - this will result in copying the Jira space setup (permission, notification, work item security, workflow, work item type, work item type screen, field configuration).

You don't have to set up an empty Jira space and can use an existing one. In such cases, copied work items will be added to the existing ones.

[Unmapped block: nestedExpand]

### Copy issues

When cloning tasks from another box, keep in mind that you are not selecting a Jira space, you are selecting a box (tasks from that box get copied). This means that if a box includes multiple spaces or just a limited number of work items from a single space, that's what will be copied.

The second drop-down gives you the destination Jira space.

If the destination Jira space already contains work items, they will automatically be included in the scope.

scope = copied items + existing destination items

Image — asset pipeline pending  
Screenshot of the Clone existing scope window.

### Cloning option is unavailable:

[Scope type](/cms_trial/space/SPM/1918766536/Scope+types/) dictates whether the option is available.

#### In boxes with "Own" scope

- If a box type was created with "Own" scope, the option is available. You can clone a scope of an existing box (with "Own" scope) or import a file.

#### In boxes with "Own" scope from boxes with "Sub" scope

- If you try to copy tasks from a box with "Sub" scope type, you won't be able to select it as a source. "None" and "Sub" scope type boxes won't be coming up on the list of possible options, as the action doesn't make sense. A box with "Sub" scope doesn't have its own scope you could copy.

#### In boxes with "Sub" scope

- If a box has been created with "Sub-scope" the options are inactive.

The scope of a box with a "sub-scope" type is based strictly on the upper-level box; a sub-box itself doesn't have its own scope. You can't clone or import tasks to a box that doesn't have its own scope. The action has to be performed in the upper-level box with "Own" scope.

#### "None" scope boxes

- A box with "None" scope doesn't display any tasks at all; it only aggregates its sub-boxes. You can't clone a scope into a box with "None" scope.
- You can't clone a scope from a box with "None" scope - you can't find such a box on a list of available scope sources. This means you can't select such a box, not on purpose, not accidentally, as a source to be cloned.

### Required fields

The most common reason for the cloning process to fail is related to Jira Field Configuration.

Image — asset pipeline pending  
contentId-1918636677

The "Required" fields have to be changed to "Optional" for the time when the App is importing the program.

Keep in mind that the change of the Field Configuration scheme has to be applied to the target Jira space (the space where work items get copied to).

Image — asset pipeline pending  
contentId-1918636677

We recommend creating a temporary scheme instead of changing an existing one. This way, other spaces will not be affected. Then, when needed, you apply a "temporary" configuration to a space instead of changing an existing configuration (that may be in use by multiple different spaces) to minimize the impact.

[Unmapped block: nestedExpand]