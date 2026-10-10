# Swimlanes (Board)

## Swimlanes - Board module (old navigation)

Click to expand the guide

## About the swimlane picker

The swimlane picker will help you manage your tasks based on the swimlane type you are interested in. With live synchronization, all changes are reflected immediately.

![image-20240625-081951.png](/cms_trial/assets/3b99d211-b286-44a9-8bfa-34073fa9bbe3.png)

## Swimlane types

You can switch between five swimlane types:

- Team
- Team members
- Status (read-only mode)
- Priority
- Color

Swimlanes are displayed in alphabetical order and cannot be rearranged.

![image-20240624-102822.png](/cms_trial/assets/ddfa5d3c-3edb-46f3-992e-178765084c76.png)

### Team

Select the **Team** swimlane to have a clear representation of each team's workload. The teams displayed on swimlanes are configured in the Teams module.

You can decide what teams are visible by selecting or deselecting them from the **Swimlane value** drop-down menu.

![image-20240624-092259.png](/cms_trial/assets/7513491b-83d8-4b38-831b-a417ceccf9d1.png)

### Team members

Select the **Team members** swimlane to show the distribution of tasks assigned to each individual, making it easy to track personal workloads and responsibilities.

Team members displayed on swimlanes come from teams configured in a box in the Teams module. If a person is not in any team, they aren’t visible as a swimlane.

![image-20240624-113937.png](/cms_trial/assets/f2fd45ab-31fb-4d62-9ca2-98e7684e7e9b.png)

### Status

Select the **Status** swimlane to see tasks sorted by their current state. The displayed statuses depend on task statuses in a box's scope.

The **Status** swimlane is available in the **read-only** mode with limited view settings. You can’t move tasks from/to the backlog, rearrange, or add new tasks.

![image-20240625-082616.png](/cms_trial/assets/9617087b-5439-4d7e-8e3a-3836ba356efc.png)

### Priority

Select the **Priority** swimlane to organize tasks according to their urgency or importance. This helps teams focus on high-priority items first. The priority levels displayed on swimlanes depend on task priorities in a box’s scope.

![image-20240625-080956.png](/cms_trial/assets/6547f920-1b65-40a8-a3eb-bf3d7ed51236.png)

### Color

Select the **Color** swimlane to group tasks by BigPicture colors, allowing for quick identification and differentiation based on custom criteria.

![image-20240625-083047.png](/cms_trial/assets/9441c742-aab2-48d8-8603-0445e2f1e8a9.png)

## Available view settings

Available view settings depend on the selected swimlane type.

| **View option** | **Available for swimlanes:** |
| --- | --- |
| **View > Layout**   - Compact - Regular - Wide  image-20240624-092954.png | - Team - Team members - Priority - Color |
| **View > Totals**  Type:   - None - Work progress - Capacity allocation   Aggregate by:   - Story points - Tasks - Time spent (standard format, days, or hours)  image-20240624-093335.png When the view is set to **Capacity allocation** and aggregation by **Story points,** you can edit the capacity:   1. Click on the **Edit** icon next to capacity. 2. Enter capacity in story points. 3. When ready, click **Save**.   When a team member is assigned to more than one team, you cannot edit their capacity on the swimlane. To edit the capacity, click the [**Capacity planning**](/cms_trial/space/SPM/1918798757/Capacity+planning+(Board+module)/) button at the top menu. image-20240625-073231.png | - Team - Team members |
| **View > Task warnings**  Tasks are marked in orange, and an **exclamation mark** icon appears next to each task that requires attention. image-20240624-113259.png | - Team - Team members - Status - Priority - Color |
| **View > Show objectives**  If objectives are defined, they are displayed above tasks. image-20240624-113547.png | - Team |

## Swimlane value

You can completely hide swimlanes of a given type depending on their value, giving you full control over what information is displayed.

Swimlane values will be displayed only if a checkmark is next to them.

- Use the search box to find swimlane values faster.
- Select or deselect all swimlane values with one click.

![image-20240624-103710.png](/cms_trial/assets/62324188-2af8-442f-8ee1-49070f423f70.png)

## Available actions

For **Team, Team members, Priority, and Color** swimlane types, you can:

- Add new tasks (Jira issues) directly to a selected timebox.
- Rearrange tasks between timeboxes and swimlanes.
- Drag and drop tasks from the backlog.
- Move tasks back to the backlog.

The **Status** swimlane is available in the **read-only** mode with limited view settings. You can’t move tasks from/to the backlog, rearrange, or add new tasks.

### Add new tasks

You can add new tasks (Jira issues) directly to a selected swimlane:

1. Click on the **plus** icon.
2. Complete the details.
3. Click **Create**.

![image-20240624-095235.png](/cms_trial/assets/628e64f2-53d8-4532-bb7d-978fc81e757a.png)

### Rearrange tasks

To rearrange tasks:

1. Find a task you want to move.
2. Left-click on the task.
3. Drag and drop the task to a new place.

![2024-06-24_12-23-37.mp4](/cms_trial/assets/f3b4f4d8-c7ca-40b9-bae4-3e90cec98c7b.mp4)

### Move tasks from/to the backlog

To move tasks from/to the backlog:

1. Expand the **Infobar** panel.
2. Find a task.
3. Drag and drop the task to a new place.

![2024-06-24_12-20-51.mp4](/cms_trial/assets/177df39b-4403-418a-868a-77d48fe9490a.mp4)

## Constraints

1. **Team - "Unknown" swimlane**

Most tasks are either unassigned (no team assigned) or are assigned to a particular team.

When the assignment is unclear, a task is placed in the **Unknown**row (below the "unassigned" row):

- "Other Box team" → a task has been assigned to a team, but that team doesn't exist in the context Box (the team hasn't been added to the Box you're in). The task is in the scope of another Box - in that Box, the task is already assigned to a team.
- "Unknown" → team information can't be matched to any existing Boxes that contain a task (the task has been assigned team information, such as a team code; however, no matching team has been found in any Boxes the task is in).
- "Undetermined" - in the app, multiple teams have the same information (team code). The app can't determine which team the task should belong to.

1. **Team members - "Unassigned" swimlane**

If there is no assignee, a task is visible under the **Unassigned** swimlane.

1. **Dependencies**

When a swimlane value is hidden, dependencies between cards of the hidden swimlanes will not be displayed.

1. **Capacity totals**

For the **Team members** swimlane, capacity totals are calculated as a sum of team members' capacity in a given timebox. In periods when a team member is not active, their capacity equals 0 and cannot be edited on the board. If the task is assigned to the member in this period, the capacity calculation is displayed with overallocation (e.g., 10/0 story points when the task is estimated at 10 story points).

The team member’s activity depends on the configuration in the Teams module.

1. **Tasks assigned to an individual are auto-assigned to their team**

When the [Tasks assigned to an individual are auto-assigned to their team](/cms_trial/space/SPM/1918408224/Automatic+assignment/) option is enabled and you change the assignee of a task by dragging and dropping a task on the swimlane, BigPicture validates if a team matches the assignee (team member).

- With one-to-one assignments where the team of the team member is known (the user belongs to only one team in the box) - the team is updated.
- With one-to-many assignments, where the team member belongs to more than one team in the box, the user is informed with the message “*Team member assigned belongs to more than one team, team field was not updated*”.

## Swimlanes - Board module (new navigation)

Click to expand the guide

## About the swimlane picker

The swimlane picker will help you manage your tasks based on the swimlane type you are interested in. With live synchronization, all changes are reflected immediately.

![Screenshot of the swimlane picker in the Board module.](/cms_trial/assets/5ffb4b1c-d6e7-4f1a-85fc-232f645399f2.png)

## Swimlane types

You can switch between five swimlane types:

- Team
- Team members
- Status (read-only mode)
- Priority
- Color

Swimlanes are displayed in alphabetical order and cannot be rearranged.

### Team

Select the **Team** swimlane to have a clear representation of each team's workload. The teams displayed on swimlanes are configured in the Teams module.

You can decide what teams are visible by selecting or deselecting them from the **Swimlane value** drop-down menu.

![Screenshot of the Team swimlane in the Board module.](/cms_trial/assets/c1cad31d-95f1-4831-8b74-02c15ca3385c.png)

### Team members

Select the **Team members** swimlane to show the distribution of tasks assigned to each individual, making it easy to track personal workloads and responsibilities.

Team members displayed on swimlanes come from teams configured in a box in the Teams module. If a person is not in any team, they aren’t visible as a swimlane.

![Screenshot of the Team members swimlane in the Board module.](/cms_trial/assets/190d8707-7383-4d11-a339-b05aa438d676.png)

### Status

Select the **Status** swimlane to see tasks sorted by their current state. The displayed statuses depend on task statuses in a box's scope.

The **Status** swimlane is available in the **read-only** mode with limited view settings. You can’t move tasks from/to the backlog, rearrange, or add new tasks.

![Screenshot of the Status swimlane in the Board module.](/cms_trial/assets/9f3ed0bc-26cb-4714-a389-f5a5be3a5625.png)

### Priority

Select the **Priority** swimlane to organize tasks according to their urgency or importance. This helps teams focus on high-priority items first. The priority levels displayed on swimlanes depend on task priorities in a box’s scope.

![Screenshot of the Priority swimlane enabled in the Board module.](/cms_trial/assets/04167b8f-b065-4080-8153-043701202b35.png)

### Color

Select the **Color** swimlane to group tasks by BigPicture colors, allowing for quick identification and differentiation based on custom criteria.

![Screenshot of the Color swimlane enabled in the Board module.](/cms_trial/assets/8b466897-c152-48ec-a7d0-07fcb848064e.png)

## Available view settings

Available view settings depend on the selected swimlane type.

| **View option** | **Available for swimlanes:** |
| --- | --- |
| **View > Layout**   - Compact - Regular - Wide  Screenshot of the Layout options in the Board module. | - Team - Team members - Priority - Color |
| **View > Aggregation**  Type:   - None - Work progress - Capacity allocation   Aggregate by:   - Story points - Tasks - Time spent (standard format, days, or hours)   When the aggregation is set to **Capacity allocation** by **Story points,** you can edit the capacity:   1. Click on the **Edit** icon next to capacity. 2. Enter capacity in story points. 3. When ready, click **Save**.   When a team member is assigned to more than one team, you cannot edit their capacity on the swimlane. To edit the capacity, go to [**Board > Capacity planning**](/cms_trial/space/SPM/1918798757/Capacity+planning+(Board+module)/). Screenshot of the capacity planning section in the Board module. | - Team - Team members |
| **View >** [**Task warnings**](/cms_trial/space/SPM/1918636230/Task+warnings+(Board+module)/)  Tasks are marked in orange, and an **exclamation mark** icon appears next to each task that requires attention. Screenshot of task warnings enabled in the Board module. | - Team - Team members - Status - Priority - Color |
| **View > Objectives**  If objectives are defined, they are displayed above tasks. Screenshot of Objectives enabled in the Board module. | - Team |

## Swimlane value

You can completely hide swimlanes of a given type depending on their value, giving you full control over what information is displayed.

Swimlane values will be displayed only if a checkmark is next to them.

- Use the search box to find swimlane values faster.
- Select or deselect all swimlane values with one click.

![Screenshot of the swimlane value in the Board module. ](/cms_trial/assets/f13d933a-4a4a-43bb-a943-e375adb9aa0e.png)

## Available actions

For **Team, Team members, Priority, and Color** swimlane types, you can:

- Add new tasks (Jira work items) directly to a selected timebox.
- Rearrange tasks between timeboxes and swimlanes.
- Drag and drop tasks from the backlog.
- Move tasks back to the backlog.

The **Status** swimlane is available in the **read-only** mode with limited view settings. You can’t move tasks from/to the backlog, rearrange, or add new tasks.

### Add new tasks

You can add new tasks (Jira work items) directly to a selected swimlane:

1. Click on the **plus** icon.

   ![Screenshot of the plus icon in the Board module.](/cms_trial/assets/e8d158a2-7d95-4a02-b973-f2c3bfac4699.png)
2. Complete the details.
3. Click **Create**.

### Rearrange tasks

To rearrange tasks:

1. Find a task you want to move.
2. Left-click on the task.
3. Drag and drop the task to a new place.

![Video of rearranging tasks in the Board module.](/cms_trial/assets/e88716fd-c51e-4447-8be4-269c71dcbdef.mp4)

### Move tasks from/to the backlog

To move tasks from/to the backlog:

1. Expand the **Infobar** panel.
2. Find a task.
3. Drag and drop the task to a new place.

![Video of moving tasks from the backlog to the board in the Board module.](/cms_trial/assets/db775a95-d7aa-447e-ab1c-c1e1d0d13bb5.mp4)

## Constraints

1. **Team - "Unknown" swimlane**

Most tasks are either unassigned (no team assigned) or are assigned to a particular team.

When the assignment is unclear, a task is placed in the **Unknown**row (below the "unassigned" row):

- "Other box team" → a task has been assigned to a team, but that team doesn't exist in the context box (the team hasn't been added to the box you're in). The task is in the scope of another box - in that box, the task is already assigned to a team.
- "Unknown" → team information can't be matched to any existing boxes that contain a task (the task has been assigned team information, such as a team code; however, no matching team has been found in any boxes the task is in).
- "Undetermined" - in the app, multiple teams have the same information (team code). The app can't determine which team the task should belong to.

1. **Team members - "Unassigned" swimlane**

If there is no assignee, a task is visible under the **Unassigned** swimlane.

1. **Dependencies**

When a swimlane value is hidden, dependencies between cards of the hidden swimlanes will not be displayed.

1. **Capacity totals**

For the **Team members** swimlane, capacity totals are calculated as a sum of team members' capacity in a given timebox. In periods when a team member is not active, their capacity equals 0 and cannot be edited on the board. If the task is assigned to the member in this period, the capacity calculation is displayed with overallocation (e.g., 10/0 story points when the task is estimated at 10 story points).

The team member’s activity depends on the configuration in the Teams module.

1. **Tasks assigned to an individual are auto-assigned to their team**

When the [Tasks assigned to an individual are auto-assigned to their team](/cms_trial/space/SPM/1918408224/Automatic+assignment/) option is enabled and you change the assignee of a task by dragging and dropping a task on the swimlane, BigPicture validates if a team matches the assignee (team member).

- With one-to-one assignments where the team of the team member is known (the user belongs to only one team in the box) - the team is updated.
- With one-to-many assignments, where the team member belongs to more than one team in the box, the user is informed with the message “*Team member assigned belongs to more than one team, team field was not updated*”.