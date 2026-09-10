# Use case: Build a task structure with custom links ('is child of' / 'is parent of')

|  |  |
| --- | --- |
| **Goal** | **Structure and visualize work within BigPicture according to the parent-child relations of Jira work items.**  Enable a clear and hierarchical view of tasks in BigPicture. |
| **Scenario** | A project manager manages a software product and wants to see a parent-child hierarchy based on `is child of` and `is parent of` relations between Jira work items. This way, they can see related work items under parent tasks in BigPicture. |
| **Key benefits** | - **Hierarchical visualization** - display task structure based on parent-child relations of Jira work items. - **Direct reflection of Jira structure** - BigPicture mirrors the linked work items to ensure consistency. - **Better context for individual tasks** - tasks within their parent context provide a clear understanding of their purpose and contribution to project goals. |

## Preconditions

Role You need at least a Bbox Admin role to manage the box configuration.

box The box needs to be populated with a Jira space.

child of / parent of You need to have linked work items with the `is child of` and `is parent of` relations in Jira.

## Build a task structure with custom links step-by-step

1. Go to **box configuration** > **Tasks** > **Task structure**.
2. Expand **Advanced Configuration**.
3. Disable currently active structure builders.
4. Enable **Parent-Child**.

The changes are immediately reflected on the Gantt chart.

**Tip:** You can change the relation between tasks in BigPicture, for example, move a task under another parent task. All changes are instantly reflected in Jira.

If a work item is linked to multiple parent tasks in Jira, BigPicture will display it under only one of them in the hierarchy.

The video presents how to create a task structure based on the **Parent-Child** relations.

![Video presenting how to build task structure based on the Parent-Child relations.](/cms_trial/assets/15742cfd-828c-4ab4-9560-87e89095d23e.mp4)

## Expected outcomes

- Tasks are successfully organized based on the parent-child relations from Jira.
- A project manager can modify task structures directly within BigPicture, with all changes instantly synchronized back to Jira.
- Team members have a better context for their individual tasks and understand how their work contributes to parent tasks.

## Additional resources

- Expand to watch an overview video about the task structure in BigPicture.

Task structure overview (video)

- Expand to watch a video about the task structure based on components, versions, and sprints.

Task structures: Components, Versions, and Sprints (video)

- [Task structure](/cms_trial/space/SPM/1918832018/Task+structure/)