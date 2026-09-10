# Kanban board mode

## Kanban board mode (old navigation)

Click to expand the guide

## About the Kanban board view mode

Kanban mode is primarily used to conveniently change the status of the boxes. In this mode, the boxes are represented as cards (much like the tasks on the board in the Board module), while the board columns represent box statuses:

- **Not started**
- **In progress**
- **Closed**

Unlike in other view modes, in the Kanban mode, only sub-boxes directly under the current parent are visualized. These cards could be sub-boxes under a project box, such as Iterations or Stages, or other projects and portfolios under a portfolio box.

The name of the parent box is always shown in the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/), regardless of the view mode or module.

![Overview module, kanban board mode.](/cms_trial/assets/d53fd381-afd5-4a96-9725-80893062afd9.png)

## Actions in the Kanban board mode

You can carry out the following actions while in the Kanban board mode in the Overview module:

### Manage box lifecycle (context menu)

Jira/App/Box Admins can manage the [lifecycle of the boxes](/cms_trial/space/SPM/1918829911/Box+lifecycle/) by changing the status of the box and [archiving](/cms_trial/space/SPM/1918634657/Archive+box/) it. This can be done by:

- prompting the context menu under the **More actions** (**…**) button on the box card
- **right-clicking** the box card (anywhere but the box name link)

In addition, you can change the [box status](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/297763919) by moving the card (box) from one board (status) to another.

![Overview module, kanban mode with the context menu prompted.](/cms_trial/assets/efa216f7-27bf-46ce-9451-d49db963f8e5.png)

### Manage boxes (context menu)

Jira/App/Box Admins can [manage their boxes](/cms_trial/space/SPM/1918699321/Box+management/) by using the same context menu to:

- configure a box
- edit a box
- archive a box
- delete a box

In addition, they can click the **Add new** (**+**) in the upper menu to [create a new box](/cms_trial/space/SPM/1918406376/Create+box/).

### Open a box in a specific module

Click the **Open in module** button and select the module from the list to launch your box in that module. [Module availability](/cms_trial/space/SPM/1918535028/BigPicture+modules/) depends on the box type or box configuration.

### Mark a box as favorite

Open the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/) and click the **star icon** next to the box name to mark it as a favorite. It will help you find the marked box easily later. The list of favorite boxes is local and not shared among other users.

### Filter the boxes

Use the search and [filter functionalities](/cms_trial/space/SPM/1918505078/Favorite+%2F+Filter+by+(Overview+module)/) to narrow down the scope of visible boxes.

In the Kanban board view mode, only the parent boxes that are sub-boxes to the selected parent are visible.

In the example below, a portfolio box holds multiple projects that have their own respective children, such as Iterations or Program Increments, which are shown in the Hierarchy and Timeline modes. They are not listed in the Kanban board mode.

For that reason, in this example, if you search boxes by *Iteration,* the filters will not return any results.

![Portfolio box in the Overview module, Kanban board mode.](/cms_trial/assets/84cd3b9b-a437-4d39-8199-ba809c7fd049.png)

### Copy child box ID

Mouse over the box and copy its ID. You can later use it with your JQL queries or configure the box synchronization.

![Copy box id in the kanban board mode in the overview module.](/cms_trial/assets/101fd0b1-01bd-4699-9bdb-a7087d5d15ef.png)

### Track time-based box progress

You can see a progress bar at the bottom of a box card. Mouse over it to see the progress % that is based on the box duration and is displayed regardless of the box status.

![Box progress bar in the Kanban board mode in the overview module.](/cms_trial/assets/0faada07-7c48-42db-bb9d-26edc6586f29.png)

The progress is calculated according to the following formula:

*(Time passed from the start date till today / by a total box duration) x 100%*.

For example:

- Box start date: 2025/Aug/ 1
- Box end date: 2025/Aug/ 31
- Current date: 2025/Aug/25
- Progress = (25/31) x 100% ≈ 0.806 x 100% ≈ 0.81 x 100% = 81%

## Kanban board mode (new navigation)

Click to expand the guide

## About the Kanban board view mode

Kanban mode is primarily used to conveniently change the status of the boxes. In this mode, the boxes are represented as cards (much like the tasks on the board in the Board module), while the board columns represent box statuses:

- **Not started**
- **In progress**
- **Closed**

Unlike in other view modes, in the Kanban mode, only sub-boxes directly under the current parent are visualized. These cards could be sub-boxes under a project box, such as Iterations or Stages, or other projects and portfolios under a portfolio box.

The name of the parent box is always shown in the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/), regardless of the view mode or module.

![Screenshot of the Kanban mode in the Overview module.](/cms_trial/assets/f0b036c3-dd6e-4b27-8377-898f580cda5b.png)

## Actions in the Kanban board mode

You can carry out the following actions while in the Kanban board mode in the Overview module:

### Manage box lifecycle (context menu)

Jira/App/Box Admins can manage the [lifecycle of the boxes](/cms_trial/space/SPM/1918829911/Box+lifecycle/) by changing the status of the box and [archiving](/cms_trial/space/SPM/1918634657/Archive+box/) it. This can be done by:

- prompting the context menu under the **More actions** (**…**) button on the box card
- **right-clicking** the box card (anywhere but the box name link)

In addition, you can change the [box status](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/297763919) by moving the card (box) from one board (status) to another.

![Screenshot of right-clicking the box in the Kanban mode in the Overview module.](/cms_trial/assets/1cec6ac6-b9b3-4916-8022-5cab1abc31e5.png)

### Manage boxes (context menu)

Jira/App/Box Admins can [manage their boxes](/cms_trial/space/SPM/1918699321/Box+management/) by using the same context menu to:

- configure a box
- edit a box
- archive a box
- delete a box

In addition, they can click the **Create new** in the upper menu to [create a new box](/cms_trial/space/SPM/1918406376/Create+box/).

### Open a box in a specific module

Click the **Open in module** button and select the module from the list to launch your box in that module. [Module availability](/cms_trial/space/SPM/1918535028/BigPicture+modules/) depends on the box type or box configuration.

### Mark a box as favorite

Open the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/) and click the **star icon** next to the box name to mark it as a favorite. It will help you find the marked box easily later. The list of favorite boxes is local and not shared among other users.

### Filter the boxes

Use the search and [filter functionalities](/cms_trial/space/SPM/1918505078/Favorite+%2F+Filter+by+(Overview+module)/) to narrow down the scope of visible boxes.

In the Kanban board view mode, only the parent boxes that are sub-boxes to the selected parent are visible.

### Copy child box ID

Mouse over the box and copy its ID. You can later use it with your JQL queries or configure the box synchronization.

![Copy box id in the kanban board mode in the overview module.](/cms_trial/assets/101fd0b1-01bd-4699-9bdb-a7087d5d15ef.png)

### Track time-based box progress

You can see a progress bar at the bottom of a box card. Mouse over it to see the progress % that is based on the box duration and is displayed regardless of the box status.

![Box progress bar in the Kanban board mode in the overview module.](/cms_trial/assets/0faada07-7c48-42db-bb9d-26edc6586f29.png)

The progress is calculated according to the following formula:

*(Time passed from the start date till today / by a total box duration) x 100%*.

For example:

- Box start date: 2025/Aug/ 1
- Box end date: 2025/Aug/ 31
- Current date: 2025/Aug/25
- Progress = (25/31) x 100% ≈ 0.806 x 100% ≈ 0.81 x 100% = 81%