# Conflicting structure builders

The general rule of structuring tasks is that the order of the structure builders is important and determines the resulting structure.

As the App can not duplicate tasks, when you enable conflicting structure builders, your tasks will be nested under the structure builder with higher priority (higher on the list).

The most common conflicts are listed in the table below:

| **Structure builder** | **Description** |
| --- | --- |
| Projects and sprints | Sprints can be only created on Jira software boards which use a JQL filter to define the scope of tasks. Sprints are not related to any particular Jira project or in other words, you can add tasks from any Jira project to a Sprint. Automated task structure in this case will generate two separate branches. |
| Component and Versions | Components are subsections of a project; used to group data while versions control the scope of the release. When used together will create separate branches in the task structure. Depending on the order of the structure builders, an issue once nested under one of them will not move. |
| Version and Sprints | As it is not possible to set a version of a Sprints in Jira it is also not possible to create such a structure. |
| Components and Sprints | Components are subsections of a project; creating a structure with Sprints just like in the case of versions would create two separate branches. |