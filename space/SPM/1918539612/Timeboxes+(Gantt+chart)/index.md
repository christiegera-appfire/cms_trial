# Timeboxes (Gantt chart)

## Overview

[Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) define consecutive timeframes used for work planning. They represent such sub-boxes as Sprints, Iterations, Program Increments, and Stages.

- You can only display sequential box types using the Gantt module.
- The boxes with [sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) set as **Overlapping** will not be displayed. You can change the sequentiality on the [box type configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page: **Administration** > **Box types** > select box type > **Advanced** (requires the [App Admin](/cms_trial/space/SPM/1918829579/Permissions/) security role).

You can create and edit timeboxes using the [Hierarchy](/cms_trial/space/SPM/1918799130/Hierarchy+mode/) and [Timeline](/cms_trial/space/SPM/1918538282/Timeline+mode/) view modes of the Overview module.

Timeboxes are suitable for both agile and non-agile teams. Non-agile teams can simply rename Program Increments and Iterations to years, quarters, or months, and start planning their short- or long-term goals using the [Board module](/cms_trial/space/SPM/1918796888/Board+module/).

In the SAFe ART box, timeboxes can represent:

- Program Increment
- Iteration

In a waterfall/classic box, timeboxes can represent:

- Stages

In the Hybrid Project box, timeboxes can represent:

- Hybrid Stages

## Overlapping boxes

You can only show sequential timeboxes which means they can not overlap.

## Box status colors

The colors of the boxes reflect the current status:

- **Not started** (gray)
- **In progress** (blue)
- **Closed** (green)

You can change the box status using the Overview module's [Kanban board mode](/cms_trial/space/SPM/1918700991/Kanban+board+mode/), or by using the **right-click** context menu.

## Auto-scheduling

You can enable auto-scheduling of your tasks. When you do, the app will update your tasks' dates to fit within the boxes' period when you plan a task in different timeboxes.

There are two strategies:

- Precise alignment
- Smart alignment

## Enable timeboxes on the Gantt chart

![additional-information-gantt-timeline.png](/cms_trial/assets/1375a794-5e01-4fb6-95bc-ac4a0d6bd8e6.png)

1. [Configure timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) for your project.
2. Click **More actions** (**…**) in the upper-right corner of the Gantt timeline to open the context menu.
3. Check the **Timeboxes**.

In the example below, you can see the Program Increment, which is the higher-level (parent) timebox to Iteration timeboxes.

![Timeboxes o nthe Gantt timeline.](/cms_trial/assets/203f9a76-0076-464a-afce-10058decf4da.png)