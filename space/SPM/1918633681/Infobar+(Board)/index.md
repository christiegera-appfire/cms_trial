# Infobar (Board)

## About the Infobar panel

The **Infobar** in the Board module provides information on crucial box content aspects, including:

- Backlog
- Dependencies
- Warnings

## Switch between the tabs

You can easily choose what information the Infobar shows. All you need to do is click on the tab in the upper section of the Infobar. The example below shows the **Backlog** view.

![Screenshot of the Infobar sidebar in the Board module.](/cms_trial/assets/cb3459cd-1576-47b6-af39-1fa55455ed81.png)

## Backlog

The **Backlog** is a list of tasks such as new features, changes to existing features, bug fixes, infrastructure changes, or other activities a team may deliver to achieve a specific outcome. Backlog items in this section can be displayed as:

- List of tasks (flat mode)
- Hierarchy of tasks (work breakdown structure mode)

![Screenshot of the Backlog tab in the Board module.](/cms_trial/assets/11c2f214-c2b9-4d4b-80ca-9ca74ae9bd5f.png)

### Backlog - available actions

The table presents a lit of available actions you can perform in the Backlog tab.

| **Action** | **Description** |
| --- | --- |
| Sort task order | Tasks are displayed based on how they are organized within the Gantt/Scope modules. In the Board module, the backlog on the right allows you to rearrange tasks belonging to the same parent only - manually rearranging tasks in the backlog (by drag-and-drop) will cause changes to the structure within Gantt/Scope modules. contentId-1918633681contentId-1918633681 |
| [Quick filters](/cms_trial/space/SPM/1918635901/Quick+filters/) | You can narrow down what is being displayed using Quick Filters. |
| [Search box](/cms_trial/space/SPM/1918407393/Search+box/) | Search will check the contents of **all text fields** of Jira issues and the **issue key**, such as:   - Summary - Description - Environment - Comments - Custom fields    - Free text field (unlimited text)   - Text field (<225 characters)   - Read-only text field |
| Snipe to result | When you use the **Snipe to result** option, you are taken to each item that matches the search query. |
| Switch between upper-level and sub-boxes | When you switch to a lower-level box, you can narrow down the backlog items. You can choose the scope of the issues you would like to see in your backlog sidebar:   - Context box - show the full scope of the box. - Sub-box - narrows the scope to the task assigned to the visible first-level sub-boxes (tasks need to be assigned to these boxes in order to appear in the backlog).   For example, while viewing the Iteration level (Program increment is a parent Box type to an Iteration Box type), you can show the whole backlog. contentId-1918633681 or show items that were assigned to Program Increment 2 only: contentId-1918633681 |
| Show planned tasks | Hide tasks that are already planned and displayed on the Board. Planned tasks are indicated with the color green, and unplanned tasks are not highlighted. contentId-1918633681 The following rules apply:   - Any task that is unplanned and within the applied filter → white background, black font - Any parent task that is unplanned and outside of the applied filter (parents must be displayed to present task hierarchy properly)  → white background, grey font - Any task that is already planned and within the applied filter  → green background, black font - Any parent task that is already planned and outside of the applied filter (parents must be displayed to present task hierarchy properly)  → green background, grey font |
| [Column view](/cms_trial/space/SPM/1918537147/Column+view+in+backlog+(Board+module)/) | Configure the columns of the backlog sidebar by adding different fields and setting the display and aggregation options. |
| [Move tasks](/cms_trial/space/SPM/1918864819/Move+tasks/) (manual hierarchy) | You can manually move tasks across the [task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/). |
| [Inline edit](/cms_trial/space/SPM/1918637324/Inline+edit/) | Double-click to inline edit the text and number fields within the backlog. |

## [Dependencies](/cms_trial/space/SPM/1918668845/Dependencies+in+the+Board+module/)

One of Infobar's sections focuses on task dependencies. The dependencies fall into four categories and resemble links configured in dependency configuration.

The **Dependencies** tab contains all information on task dependencies:

- Dependencies between the tasks in the scope of the current box.
- Dependencies between the tasks in the current box and other boxes (indicated by an icon).

![image-20240925-074702.png](/cms_trial/assets/4dd3fb94-754a-4149-bb43-57361d0f76c8.png)

## [Warnings](/cms_trial/space/SPM/1918636230/Task+warnings+(Board+module)/)

Go to the **Warnings** tab to see a list of all task warnings. Click on a selected warning to check its details and resolve a problem.

![image-20240520-113738.png](/cms_trial/assets/99058e76-f443-4166-955e-b5c8403edc3d.png)

A dialog describes a problem and suggests the next steps.

![image-20240520-114126.png](/cms_trial/assets/9e06d5dc-c82c-49b4-bbe8-795cf1fd5633.png)

### Locate tasks on Board through backlog

If you need to quickly locate a task with a validation error in your **Board** module:

1. Enter the Board module through the **Switch module** dropdown menu.
2. In the right pane, click the **Warnings** tab.
3. Select the row of the task required.
4. Click the orange icon in the first column of the tab.
5. The system will automatically move to the location of your task within the **Board** module.

![contentId-1918633681](/cms_trial/assets/b5847f83-9c92-40d9-b33f-56da3887fe65.png)