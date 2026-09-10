# Undo operation on task

## Overview

The **Undo** button ▢ reverses a single, most recent action. It is possible to undo an action in the:

Gantt module

- Board module
- Resources module

The button becomes available when you take the following actions:

- Resize a taskbar on the Gantt chart in the Gantt module (live and scenario mode)
- Move a taskbar on the Gantt chart in the Gantt module (live and scenario mode)
- Move or resize a taskbar in the Resources module (scenario mode)
- Move a task on the board in the Board module

## Access

To undo an action, you can use the keyboard shortcut: ctrl/cmd + z or click the **Undo** button.

| **Gantt module (live mode)** | **Gantt module (scenario mode)** | **Board module** | **Resources module (scenario mode)** |
| --- | --- | --- | --- |
| Undo button in the live mode in the gantt module. | Undo button in the scenario mode in the gantt module. | Undo button in the board module. | Undo button in the scenario mode in the resources module. |

The Undo button is grayed out by default. It becomes available when the user performs an operation that can be undone. Performing an undo operation or reloading the page makes the Undo button grayed out again.

## Confirm undoing the last action

After pressing the Undo button, the app displays a screen asking the user if he wants to undo the change (Undo or Cancel). The screen shows the issue Key, a summary of the operation, the name of the user who introduced the change, and the date and time of the operation.

If the last operation cannot be undone after pressing the Undo button (because some other changes took place elsewhere in the system in the meantime), the app displays a screen saying the undo operation cannot be performed.

In other cases, the confirmation screen shows the issue Key, a summary of the operation, the action owner, and the date and time of the operation. This screen doesn’t appear for actions undone in the scenario mode.

![Undo action confirmation screen.](/cms_trial/assets/11ea7c7a-5483-4907-a956-63969d1d4341.png)

## Undo action in the scenario mode

The Undo operation appears when you switch to the scenario mode in the Gantt or Resources module.

For more information, visit the [Scenarios](/cms_trial/space/SPM/1918634045/Scenarios/) page.