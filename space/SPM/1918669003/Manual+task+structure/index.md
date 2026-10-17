# Manual task structure

## About manual task structure

You can structure your tasks manually or use the structure builders. You can use both ways and generate a complex structure but let's start with the basics.

Before you start structuring your tasks, make sure that you understand the basic concepts related to task scheduling (see the [Automations](/cms_trial/space/SPM/1918535176/Automations/) page).

## Structure tasks manually

The Gantt and Scope modules allow you to structure your tasks manually. There are different ways to do that, including:

- [Drag-and-drop in the Board module](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1773568180/Move+tasks#Drag-and-drop)
- [Right-click in the Board module](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1773568180/Move+tasks#Right-click)
- [Keyboard shortcuts](/cms_trial/space/SPM/1918535300/Keyboard+shortcuts/)
- Arrows on the Scope module's header
- Arrows on the task vertical dialog

You can move selected tasks or groups of tasks (using the multi-select feature).

Once the parent-child relationship is created, it will appear in all modules that can display the task structure: [Board backlog](/cms_trial/space/SPM/1918633681/Infobar+(Board)/), Scope, Gantt, and [WBS widget](/cms_trial/space/SPM/1918767142/WBS+widget/).

## Move tasks manually

When manually repositioning **a task in the task structure**, **task fields are updated to match structure builders**. The sync mechanism mirrors the user's changes in the task structure in BigPicture in Jira issues. In other words, if the user indents, outdents, or drags and drops tasks within the task structure, relevant changes in tasks' fields responsible for their position are made automatically. The fundamental prerequisite for the changes to be made is active structure builders.

You **cannot** manually move tasks in portfolio boxes (non-scope boxes). To move or reorder tasks, go to the sub-box level where a task is located.

![Screen Recording 2022-03-30 at 06.54.13.mov](/cms_trial/assets/63f3c066-c0b9-4c52-898d-a97b921d67d6.mov)

### Built-in

Built-in structure builders' values are applied to all nested tasks (regardless of the indentation level). In the example below, the 'epic link' has been used as a structure builder.

![image-20240313-150254.png](/cms_trial/assets/7da717d9-bc8b-4d1c-b272-a75e43d1113a.png)

### Link-based

Link-based structure builders are applied only one level down (to a direct child of a task).

Multiple link-based structure builders can apply at the same time, but they cannot overlap with built-in structure builders.

## Indent and outdent tasks

Use the arrows in the dialog, which appears when you click a task, to structure your tasks manually:

- An arrow pointing right will indent the task or  SHIFT + ->
- An arrow pointing left will outdent the task or SHIFT + <-

See the example from the Gantt module.

![Screenshot of indenting and outdenting tasks in the Gantt module.](/cms_trial/assets/b81ff139-a1e7-4187-896b-e240754b737b.png)

See the example from the Scope module.

![Screenshot of manually moving tasks in the Scope module.](/cms_trial/assets/ac030786-bed8-481b-be89-aca88d4730f7.png)

## Active structure builder conflicts

When a [structure builder](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) is enabled, the app will block an operation if it leads to a conflict, and you will see a warning.

![Screenshot of active structure builder conflict. ](/cms_trial/assets/cbf36891-940b-4e93-93ae-484a3c21561b.png)