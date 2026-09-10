# Use case: Organize tasks by assignees or teams using grouping

|  |  |
| --- | --- |
| **Goal** | **Group tasks by the Assignee or Team field to visualize and manage work more effectively.**  This helps you gain better insights into workload distribution. When using grouping, the same task can be displayed in multiple groups. |
| **Scenario** | A project manager wants to understand how tasks are distributed across the different teams and assignees involved. The default task structure is set to Agile (Epics and Sub-tasks). To quickly see which team or individual is responsible for which tasks without changing the task structure, they use the grouping feature. This allows the same tasks to appear in multiple groups. |
| **Key benefits** | - **Clear ownership visibility** - quickly check who is working on what without changing the task structure settings. - **Duplicated tasks** - grouping is the only exception when BigPicture will display one task multiple times. - **Better workload management** - identify overloaded team members and make quick adjustments. |

## Preconditions

Role You need at least a Box Editor role to use the Group tasks feature.

box The box needs to be populated with a Jira space.

## Organize tasks by assignees or teams using grouping step-by-step

In this example, we want to group tasks by the **Team** and **Assignee** columns.

1. Go to the **Gantt** or **Scope module**.
2. Check if the **Team** and **Assignee** fields are added as columns.
3. Click **Data** > **Group tasks**.

**Tip:** When tasks are grouped, you can customize the aggregation method for selected columns. For example, set the aggregation for the **Original Estimate** column to ‘*Sum, without parent’* to view the workload separately for teams and individuals.

The video presents how to group tasks by the Team and Assignee fields.

![Video of grouping tasks by the Team and Assignee fields in the Gantt module.](/cms_trial/assets/6d0268bf-48ef-418e-aae5-74cc4d0a7b76.mp4)

## Expected outcomes

- A project manager can quickly identify workload imbalances across teams and individuals.
- A flexible task view without changing the core configuration of the task structure.

## Additional resources

- [Group tasks](/cms_trial/space/SPM/1918830289/Group+tasks/)