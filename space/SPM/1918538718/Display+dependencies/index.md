# Display dependencies

## Introduction

Adjust dependency settings at the top to modify the view. Click the **Browse dependencies** to expand the Infobar panel with dependencies.

![gantt-dependencies-menu.png](/cms_trial/assets/c3fbf45e-5844-4446-a1f9-f924d7f0faec.png)

## Display dependencies

### Expanded

Dependencies are displayed as arrows:

| **Link** | **Arrow** |
| --- | --- |
| Non ASAP | Blue arrow: Screenshot of the line for non-asap dependencies. |
| ASAP | Grey arrow: Screenshot of the line for asap dependencies. |
| Soft dependency | Grey dotted arrow: Screenshot of the line for soft dependencies. |
| Out-of-view  dependencies | Screenshot of the line for out-of-view dependencies. |
| Highlighted dependency | A dependency arrow is **in bold** when you highlight a dependency or task on the task tree to which the dependency applies. image-20240730-095137.png |
| Not highlighted dependency | A dependency arrow's color is subdued when a task associated with the dependency is not highlighted. image-20240730-095429.png |

To see the outgoing dependencies list, click on a dot.

![Screenshot of the outgoing dependencies list in the Gantt module of BigPicture.](/cms_trial/assets/35207080-375d-4203-98a3-3ad3ca2317f5.png)

To see the incoming dependencies list, click on a dot.

![Screenshot of the incoming dependencies list in the Gantt module of BigPicture.](/cms_trial/assets/47a17aa1-0468-40c0-a772-c3429dc740e6.png)

#### Broken dependencies

If a strong dependency cannot be fulfilled because of other scheduling rules, it is displayed as an orange arrow (soft dependencies don't have a scheduling impact; therefore, they cannot be broken).

For example, a task can be done manually or in locked scheduling mode.

![broken-dependency-example.png](/cms_trial/assets/f02d781c-e40b-4bcf-8cf3-4f9871dd8aa6.png)

#### The number of dependencies exceeds the module capability

If the number of dependencies is too high to handle visually, they won't be shown as arrows.

### Collapsed

If a task has any dependencies, they are indicated as a number in a dot.

![Screenshot of collapsed dependencies in the Gantt module.](/cms_trial/assets/9541d086-9526-4966-bb21-a5fa7ba9c9bd.png)

To view dependency information, click on a dot.

- **Incoming dependencies** - the task is a target (endpoint) of dependencies. The source tasks (starting points of the dependencies) are listed.
- **Outgoing dependencies**- the task is a source (starting point) of outgoing dependencies. The target tasks (the endpoints of the dependencies) are listed.

### Task details - list of dependencies

In the task details dialogue, you can see the full list of outgoing and incoming dependencies.

Click on a task on the Gantt chart to open the task details dialogue. The dialogue box can be expanded:

![Screenshot of the task details dialog in the Gantt module of BigPicture.](/cms_trial/assets/c323b43d-2df5-4f5a-b3bb-a9e2d848430b.png)

### Infobar

You can view the full dependency list in the [Infobar](/cms_trial/space/SPM/1918799264/Infobar+(Gantt)/).

![Screenshot of all dependencies in the Infobar panel of the Gantt module.](/cms_trial/assets/a1af612a-3c05-4e9c-9dbe-3408b2415684.png)

## Dependencies and task dates

When many tasks are linked by dependencies, and one of the tasks loses both dates (start and end dates), **dependencies are saved**. The arrow between tasks will temporarily disappear, but you can still check the dependency by switching to the **Collapsed** display and clicking on a number in a dot next to the task.

![Screenshot of an example for a collapsed dependency on the Gantt chart.](/cms_trial/assets/361e0d4e-534f-471e-a6e6-cc7e94130332.png)

The arrow between tasks will appear once you assign at least one date to the task.

![Screenshot of an example for a collapsed dependency with no end date on the Gantt chart.](/cms_trial/assets/d32fe200-7109-4d43-a77a-a9a54db43e0c.png)

## Out-of-view dependencies

Out-of-view dependencies can't be displayed on the Gantt chart.

|  |  |
| --- | --- |
| A source or target task is in the scope of another box | Only one task is visible on the Gantt chart, while the other one is in a different box. As a result, dependency cannot be visualized.  The out-of-view status is indicated by:   - Crossed-eye icon in the Infobar. image-20240924-093858.png  - Crossed-eye icon in the task details dialog box under the **Inward** or **Outward dependencies**.  Out-of-view dependency indicated in the task details dialog box.  - Grayed out **Focus on the source/ target**option. A source or target task is in the scope of another box. As a result, it cannot be visualized on the Gantt timeline in the current box.  A grayed out Focus on the source option in the Gantt iInfobar. |
| A source or target task is not visible because of active filters | Only one task is visible, while the other task is hidden because of active filters.  As a result, dependency cannot be visualized.  The out-of-view status is indicated by:   - Crossed-eye icon in the Infobar. image-20240924-093858.png  - Grayed out **Focus on the source/ target**option. A source or target task is in the scope of another box. As a result, it cannot be visualized on the Gantt timeline in the current box. |