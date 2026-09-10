# Multiselect (Gantt module)

## About task multi-select

You can select several tasks on the task tree to carry out bulk actions like deleting or converting. Task multi-select can save you a lot of time compared to handling tasks individually.

All the tasks you select are highlighted so that you know which tasks you have selected so far.

Tasks can be multi-selected in the scenario mode and in the live mode.

![Eight tasks selected on the tree structure in the Gantt module.](/cms_trial/assets/953966c4-1878-4c5e-ae69-6496d9f735ad.png)

## How to select multiple tasks

You can select tasks using the keyboard and mouse. The table below presents the multi-select actions you can perform on the task tree.

Depending on your Windows hardware, you may need to use the **Fn** button in place for **Ctrl**.

| **Action** | **Description** |
| --- | --- |
| **Ctrl** or **Cmd** + mouse **left-click** | Multi-select individual tasks.   1. Hold down the **Ctrl** (Windows)/ **Cmd** (Mac) key. 2. **Left-click** the tasks you want to select. 3. Release **Ctrl**/**Cmd** to scroll your task tree and press again to continue selecting more tasks. |
| [Unmapped block: nestedExpand] |
| **Shift** + mouse **left-click** | Select a range of tasks.   1. Hold **Shift** 2. **Left-click** the first and final task to highlight the entire group. |
| [Unmapped block: nestedExpand] |

## Unselect tasks

| **Action** | **Description** |
| --- | --- |
| **Esc** | Unselect all selected tasks. |
| Click anywhere within the upper area (excluding buttons, bars, and clickable icons). | Unselect all selected tasks. |
| [Unmapped block: nestedExpand] |
| Click any task on your task tree. | Unselect all selected tasks. |
| **Ctrl** or **Cmd** + mouse **left-click** | Unselect individual tasks.   1. Hold down the **Ctrl** (Windows)/ **Cmd** (Mac) key. 2. **Left-click** the tasks you want to unselect. |
| [Unmapped block: nestedExpand] |

## Actions on multi-selected tasks

Once you select the tasks you want, you can carry out bulk actions on them. **Right-click** any selected task (anywhere but the task key) or use the **editor slider** to access the edit options.

Depending on the type of tasks you have selected (parent or a child), some actions will be possible, while some will be grayed out. The table below presents possible actions on the multi-selected tasks.

In the [Gantt module](/cms_trial/space/SPM/1918797129/Gantt+module/), you can change the [scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) of any combination of selected tasks, regardless of their relationships.

| **Selected tasks** | **Actions** |
| --- | --- |
| A parent without children | - edit - select all children (option available only through the right-click context menu) - position - organize children - create/delete baseline - change scheduling mode - create dependency - convert to milestone - convert to… - delete - change task color |
| [Unmapped block: nestedExpand] |
| Parent with own children | - delete - organize children - create/delete baseline - change scheduling mode - convert to milestone - convert all to… (if at least one of the children is a milestone) - change task color |
| [Unmapped block: nestedExpand] |
| Children of the same parent (without the parent) | - delete - outdent - create/delete baseline - change scheduling mode - [convert to milestone](/cms_trial/space/SPM/1918537479/Milestones/) - convert all to… (if at least one of the children is a milestone) - change task color |
| [Unmapped block: nestedExpand] |
| A mix of children of different parents (without parents) | - delete - create/delete baseline - change scheduling mode - convert to milestone - convert all to… (if at least one of the children is a milestone) - change task color |
| [Unmapped block: nestedExpand] |
| Multiple parents (without children) | - delete - move up (unless the top parent is selected) - move down - indent - organize children - create/delete baseline - change scheduling mode - change task color |
| [Unmapped block: nestedExpand] |
| A mix of different parents and children | - delete - organize children - create/delete baseline - change scheduling mode - convert all to… (if at least one of the children is a milestone) - change task color |
| [Unmapped block: nestedExpand] |