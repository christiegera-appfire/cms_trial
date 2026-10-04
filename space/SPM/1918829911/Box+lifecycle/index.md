# Box lifecycle

## Box lifecycle (old navigation)

Click to expand the guide

## Box status

The box status determines whether you can edit items assigned to that box and whether the Actual Business Values column appears in the [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918829911).

You can set the status of each box as one of the following:

- **Not started** (gray) - the box will be executed in the future, so it is still in the planning phase
- **In progress** (blue) - the box is currently in execution
- **Closed** (green) - the box is finished

You can see the status of the box you're in at the top left:

![Gantt module, closed status of box](/cms_trial/assets/d49a5aa6-2113-4c7b-9894-9ee0e4d5b6a4.png)

## Change box status

You can change the status in the following ways:

| **Location** |  | **Instruction** | **Screenshot** |
| --- | --- | --- | --- |
| [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) | [Hierarchy mode](/cms_trial/space/SPM/1918799130/Hierarchy+mode/) | - **Right-click** a box swimlane.   or   - Open the dropdown under **More actions** (…) next to the box. | Changing box status in the Overview module, hierarchy mode. |
| [Timeline mode](/cms_trial/space/SPM/1918538282/Timeline+mode/) | - **Right-click** a box swimlane (left pane).   or   - **Right-click** a box bar on the timeline (right pane). | Changing box status in the Overview module, timeline mode. |
| [Kanban board mode](/cms_trial/space/SPM/1918700991/Kanban+board+mode/) | - **Right-click** the box card (anywhere on the whitespace).   or   - Open the dropdown under **More actions** (…) at the bottom of the box card. | Changing box status in the Overview module, kanban board mode. |
| [Board module](/cms_trial/space/SPM/1918796888/Board+module/) | - **Right-click** the box.   or   - Open the dropdown under **More actions** (…) on the box. | Changing box status in the Board module. |
| [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918829911) | - **Right-click** the box.   or   - Open the dropdown under **More actions** (…) on the box. | Changing box status in the Objectives module. |
| [Box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page | On the box configuration > Tasks > [Scope definition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918829911):   - **Right-click** the box.   or   - Open the dropdown under **More actions** (…) on the box. | Changing box status on the box configuration page. |

## Transitions

The following transitions between statuses are allowed:

- Not started → In progress and vice versa
- In progress / Not started → Closed and vice versa

When you complete the work and want to close the box, you are prompted to decide what to do with the remaining open objectives once it is already closed:

- mark open objectives as failed and continue
- mark open objectives as abandoned
- do not modify the status of open objectives

After reopening the box, all objectives marked as Failed remain in a given status. These objectives will also be automatically cloned and added to the next box with the Open status.

Closing an upper-level box means that all the sub-boxes of that box will also be closed.

![Close box system message](/cms_trial/assets/b3abd81d-08bb-4d03-bdaa-941c8e78e6d3.png)

## Limitations of closed boxes

- Box configuration is unavailable for closed boxes.
- Closed boxes are in a read-only mode.
- Data in closed boxes is not updated.

![Module switcher with Configuration field greyed-out](/cms_trial/assets/db8c72ee-f92e-49ed-9ca1-66c6f43a627f.png)

## Box lifecycle (new navigation)

Click to expand the guide

## Box status

The box status determines whether you can edit items assigned to that box and whether the Actual Business Values column appears in the [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918829911).

You can set the status of each box as one of the following:

- **Not started** (gray) - the box will be executed in the future, so it is still in the planning phase
- **In progress** (blue) - the box is currently in execution
- **Closed** (green) - the box is finished

The status of the current box is displayed in the top bar:

![A Not started status in the top bar.](/cms_trial/assets/34ef5f40-1b65-46bb-96c3-c07b16ab77d3.png)

## Change box status

You can change the status in the following ways:

| **Location** |  | **Instruction** | **Screenshot** |
| --- | --- | --- | --- |
| [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) | [Hierarchy mode](/cms_trial/space/SPM/1918799130/Hierarchy+mode/) | - **Right-click** a box swimlane.   or   - Open the dropdown under **More actions** (…) next to the box. | Changing box status in the Overview module, hierarchy mode. |
| [Timeline mode](/cms_trial/space/SPM/1918538282/Timeline+mode/) | - **Right-click** a box swimlane (left pane).   or   - **Right-click** a box bar on the timeline (right pane). | Changing box status in the Overview module, timeline mode. |
| [Kanban board mode](/cms_trial/space/SPM/1918700991/Kanban+board+mode/) | - **Right-click** the box card (anywhere on the whitespace).   or   - Open the dropdown under **More actions** (…) at the bottom of the box card. | Changing box status in the Overview module, kanban board mode. |
| [Board module](/cms_trial/space/SPM/1918796888/Board+module/) | - **Right-click** the box.   or   - Open the dropdown under **More actions** (…) on the box. | Changing box status in the Board module. |
| [Objectives module](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Objectives%20module&linkCreation=true&fromPageId=1918829911) | - **Right-click** the sub-box.   or   - Open the dropdown under **More actions** (…) on the sub-box. | Changing sub-box status in the Objectives module. |
| [Box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page | On the box configuration > Tasks > [Work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Populate%20a%20box%20with%20taks%20%28work%20items%20from%20Jira%29&linkCreation=true&fromPageId=1918829911):   - **Right-click** the box.   or   - Open the dropdown under **More actions** (…) on the box. | Changing box status on the box configuration page. |

## Transitions

The following transitions between statuses are allowed:

- **Not started** → **In progress** and vice versa
- **In progress** / **Not started** → **Closed** and vice versa

When you complete the work and want to close the box, you are prompted to decide what to do with the remaining open objectives once they are already closed:

- Mark open objectives as failed and continue
- Mark open objectives as abandoned
- Do not modify the status of open objectives

After reopening the box, all objectives marked as **Failed** remain in a given status. These objectives will also be automatically cloned and added to the next box with the **Open** status.

Closing an upper-level box means that all the sub-boxes of that box will also be closed.

![Close box system message.](/cms_trial/assets/b3abd81d-08bb-4d03-bdaa-941c8e78e6d3.png)

## Limitations of closed boxes

- Box configuration is unavailable for closed boxes.

![Box configuration is grayed out for the closed sub-box.](/cms_trial/assets/9f6e346f-6cfa-47d7-86ef-bf7fb29d4c04.png)

- Data in closed boxes is not updated.
- Closed boxes are in a read-only mode.