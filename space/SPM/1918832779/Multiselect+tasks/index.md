# Multiselect tasks

You can multi-select Boxes or tasks using CTRL+left click (or CMD on Mac). Once selected, the group of tasks is highlighted in blue. You can, for example, drag and drop them between other tasks to move the group.

Alternatively, you can move the tasks using the arrows in the module's header.

A notification is displayed if the operation is partially successful or unsuccessful.

The following modules support multi-select:

- Overview
- Gantt
- Scope
- Board

## Available actions

The list of all available actions is presented in the table below:

| **Action** | **Description** |
| --- | --- |
| To select multiple tasks (selected tasks are highlighted in blue): |
| cmd or ctrl + left mouse button | select tasks one by one |
| shift + left mouse button | select a range of tasks |
| To unselect: |
| ESC | unselect all selected tasks |
| click out of the zone | unselect all selected tasks |
| cmd or ctrl + left mouse button | unselecting tasks one by one |

## Possible actions

Depending on the type of tasks selected, you can perform different operations listed below:

- parent task with all its children:

  - move up/down
  - indent, outdent
  - delete
  - color change
- parent task with selected children or without children:

  - delete
  - color change
- all children from a single parent, not including the parent task:

  - outdent
  - delete
  - color change
- selected children from one parent, not including the parent task:

  - move up/down
  - indent, outdent
  - delete
  - color change
- multiple children from different parent tasks, not including the parent tasks:

  - delete
  - color change
- multiple parent tasks without children:

  - delete
  - color change

### Examples

Overview module:

![Multiple rows are selected in the Overview module](/cms_trial/assets/483cddfe-e41b-4cea-bf57-4e0d49e46d5c.png)

Gantt module:

![Multiple rows are selected in the Gantt module](/cms_trial/assets/9aa5b41b-fbdd-42c4-aec5-1b9d6c932626.png)

Scope module:

![Multiple rows highlighted in the Scope module](/cms_trial/assets/77b510a0-ad27-49f6-95f0-30e3f179f88b.png)

Board module:

![Multiple tasks are highlighted in the Board module](/cms_trial/assets/1e9b350c-86f9-4bbe-a4f1-0e09cbaf0456.png)