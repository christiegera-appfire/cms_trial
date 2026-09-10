# Troubleshooting: Conflicting structure builders

## Problem

When multiple structure builders, such as Projects, Sprints, Components, or Versions, are enabled at the same time, you’ll see the conflict warning.

BigPicture **CAN’T** duplicate tasks. When you enable conflicting structure builders, your tasks will be nested under the structure builder with the higher priority (higher on the list).

**Exception**: The only case where a task can be displayed more than once is when tasks are grouped. For more information, see the [Use case: Organize tasks by assignees or teams using grouping](/cms_trial/space/SPM/2399241449/Use+case%3A+Organize+tasks+by+assignees+or+teams+using+grouping/) page.

![Screenshot of the Task structure page showing the Advanced Configuration section. The Structure Preview and the Version and Component structures are shown.](/cms_trial/assets/ff0e0cf9-5b30-4bfb-ba18-b78cd8c7951d.png)

## Solution

The order of structure builders determines how tasks are organized. The structure builder that is higher on the list takes priority, and tasks will be nested under it if a conflict arises.

To avoid issues, structure builders should be organized thoughtfully. The table below outlines common structure builder conflicts and how they behave.

| **Structure builder** | **Description** |
| --- | --- |
| Projects and sprints | Sprints can only be created on Jira software boards that use a JQL filter to define the scope of tasks. Sprints are not related to any particular Jira project, or in other words, you can add tasks from any Jira project to a Sprint. Automated task structure in this case will generate two separate branches. |
| Components and Versions | Components are subsections of a project; used to group data while versions control the scope of the release. When used together will create separate branches in the task structure. Depending on the order of the structure builders, an issue once nested under one of them will not move. |
| Versions and Sprints | As it is not possible to set a version of a Sprints in Jira it is also not possible to create such a structure. |
| Components and Sprints | Components are subsections of a project; creating a structure with Sprints just like in the case of versions would create two separate branches. |

## More information

Task structure overview

Expand to see a video about task structure in BigPicture

automatic task structure

To learn more about automatic task structure, see the [Automatic task structure (structure builders)](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) page.

manual task structure

To learn more about manual task structure, see the [Manual task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/) page.