# Own-scope

When the scope definition is set to **own-scope**,the box scope has a separate task structure and serves as the base scope for sub-scopes. Automatic rules can sync it. Use it when you want to define and extend the scope of a box by selecting tasks from Jira and connected tools.

Box admins can define the automatic rules to pull in tasks (from Jira or connected tools) or view and erase them from the scope manually. The quickest way to set up the scope is to use the automatic rules.

Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings. See the <https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1858864073/Scope+definition+box+types?force_transition=71b47b01-cff8-41bd-bee2-c5d1099fd965> page for more information.

In boxes with own-scope, you can select items from the list of available Jira boards, previously saved JQL filters, or Jira projects. You may also add elements representing versions, components, sprints, projects, and backlogs by selecting appropriate task types. Those items will be represented in the task hierarchy and can be used to organize the task structure.

Boxes of this scope type display aggregated status and time-tracking reports in the Overview module's Hierarchy mode.

Users with a box editor security role can impact the box scope by creating new tasks using the **+Add task** button (however, they can't access the scope definition settings).

See the screenshot![Screenshot of the Gantt module with an own scope box.](/cms_trial/assets/b6bba29e-2164-47ed-982e-beb0277d0c21.png)

## Scope definition elements

### Scope of the context box

### [Excerpt "scope-context-box-own" from page "Work items for Jira elements and actions" not found] Scope of the sub-boxes

### [Excerpt "scope-sub-box-intro" from page "Work items for Jira elements and actions" not found] [Excerpt "scope-sub-box-own" from page "Work items for Jira elements and actions" not found] Switch between levels of child boxes

### [Excerpt "switch-between-levels" from page "Work items for Jira elements and actions" not found] Basic info and status of child boxes

[Excerpt "basic-info-child-boxes" from page "Work items for Jira elements and actions" not found]

## Automatic rules

### Scope owner

A Box can contain only the items that the **scope owner** can access (viewing access is sufficient).

If you try to add items that the scope owner can’t access, you won't save the scope successfully.

![scop-owner.png](/cms_trial/assets/355b6576-9dac-491a-9a42-95e8a3b276d5.png)

A scope owner doesn't have to be an actual user added to the Box in any capacity(doesn't have to be a Box Admin, Editor, or Viewer). The permissions of the scope-owner user account in the external tool are the basis for task syncing. Tasks will be pulled into the scope of a Box only if the scope owner can access them (at least as a viewer).

See the example

For example, Angela is the scope owner in the BigPicture demo (Jira server instance name) and selected the PI Planning project as the scope of the **PI Planning (Smart house project)** box. If there are tasks Angela isn't allowed to view in that project, those tasks can't be added to the box's scope.

When connecting with tools such as Trello, specify the scope owner for each connection. You cannot change the scope owner once a connection is established.

![BigPicture-BigPicture-demo - 2020-08-25T163429.870.png](/cms_trial/assets/07610b90-4ac1-467d-93ef-1e354f88efd1.png)

Suppose you set up a Jira user account called "BigPicture," and this user has at least viewing access to all projects. In that case, you can easily always list them as the scope owner (there is no danger of box users getting access to things they shouldn't see - if a user can't view an issue in Jira, the item will be greyed out in the App). Users will never get access to Jira items they shouldn't view or modify. Suppose a user can't view and modify an item in the connected tool (because of insufficient permissions). In that case, they won't be able to do it using the App - BigPicture allows users to perform only the actions they can perform in the connected tool.

In general, user permissions should match (a user should have the same permissions in the BigPicture Boxes/Programs as they do in Jira).

### Scope filters

If your tasks are already created in Jira, you can define the scope using the following filters:

- Boards - select from the list created Jira Board (Kanban and Scrum board)
- JQL filters - select from the list of previously saved JQL filters
- Projects - select from the list of available projects.

If you connect with Trello, you can only select Trello Boards.

![tasks-scope-definition.png](/cms_trial/assets/dbf3f376-391f-448d-874b-cd97cefa3eb4.png)

**You can select multiple items, increasing the number of issues within the scope, as the "OR" operator is used for Board, Filters, and Projects.**

![scope-definition-project.png](/cms_trial/assets/db0c0fea-c40d-453f-8ca8-ab844d0c0cfd.png)

### OKR linked work

In addition to Jira projects, boards, or JQL filters, you can populate your box with Jira work items linked to the selected OKRs.

When you select OKRs, the linked Jira work items, with or without their child items, are automatically added or removed from the box scope as you link or unlink them.

This is especially useful when you practice goal setting across multiple teams, where Jira items are distributed across different projects.

![OKR linked work on the scope definition page.](/cms_trial/assets/58b4415a-dc25-419b-8948-4232b5a92478.png)

You can add only those work items to the box scope to which you were granted permission to see the OKRs.

#### Work item inclusion

Select one of the following options:

- **Direct links only** if you want to add only work items that are directly linked to a Key Result (for example, you want to see only Epics that you linked to KRs, but without stories or other sub-items under that Epic).
- **All child items** if you want to include all children that belong to the linked Jira work item (for example, an Epic with all its sub-items).

#### Strategic themes & Objectives

![Strategic themes and Objectives dropdown expanded.](/cms_trial/assets/c99e8aea-74af-4a3b-844b-e481a403e136.png)

Select a Strategic theme or an Objective whose linked Jira work items you want to include in the scope of the box.

You can link Jira work items only to KRs and not directly to Objectives or Strategic Themes. When you select an Objective or Strategic Theme from the dropdown, it means that the Jira work items associated with the child KRs should also be included in the scope.

#### Key Results

Select a Key Result whose linked Jira work items you want to include in the scope of the box, and select one of the Work item inclusion options.

![Key Results dropdown expanded.](/cms_trial/assets/3b44edbf-e878-4161-8619-ae9c0916ec77.png)

### Narrow down

The "narrow down" field lets you further specify what exactly you want to see in a box.

To narrow the scope you can:

- Use labels
- Use JQL

The narrow down fields "AND" operator in relation to the items added to the scobe above (spaces, boards, filters).

**Note**: This option applies only to Jira, as there is no JQL in Trello.

See the example

The configuration below will result in a box containing all tasks that aren’t in status ‘done’ from the two included spaces (previously projects).

![scope-definition-general.png](/cms_trial/assets/aba3d4a7-bbb7-4c5e-b87d-9bad9cf4faf3.png)

## Manually added tasks

Tasks that do not match the automatic rules of scope definition (project/ board/ filter) are listed in the "manually added tasks" section.

This section remains hidden until needed - it is visible only when it contains at least one task.

![scope-definition-manually-added-tasks.png](/cms_trial/assets/591844ca-5fb2-401c-8334-967feb6d8ce7.png)

Manually added tasks do not fit the scope filter.

See the example

1. A user adds a new task using the "+" button in Gantt but creates a task in Project A, while the Box scope is defined as Project B:
2. A box has two sub-boxes with the scope type set to "Own." Sub-Box1 has the scope defined as Board 1 and sub-Box2 as Board 2. When a user moves a task from sub-Box 1 to sub-Box 2 using the Board module, the task will be added to the list of manually added tasks in sub-Box2.

The Box Admin can erase all the tasks in this section by clicking the "Eraser" icon.

Earlier versions of the App had a "Remove tasks, not in filter" feature, and all the tasks that **do NOT** fit the scope filters will be added to the "manually added task" list on this page.

See the example

For example, let's add risk to the 'PI Planning (Smart house project)' Box using the create task dialog, but instead of the PI Planning project, select a different one - Risk register:

![project-risk-register.png](/cms_trial/assets/eaf843ef-db82-4bf4-a4d2-3e793fef002b.png)

As a result, the risk is added to the board and appears in the Manually added tasks section:

![pi-planning-to-do.png](/cms_trial/assets/8d655c1f-2bb3-4ca0-9b8d-3ef47a620db7.png)![pi-planning-risk.png](/cms_trial/assets/6b1cee26-81b9-470f-9f5d-cecc8658bf9e.png)

## Manually removed tasks

Manually removed task → task moved from one Box with scope type set to Own to another with the scope type also set to Own.

**Retired in BigPicture 8.5 and higher.**

## Task types

You can select which elements will be displayed as tasks and, when possible, synchronized with a connected tool (such as Jira).

Task types are added automatically when respective structure builders are activated. For example, enabling the Sprint structure builder will add the Sprint task.

Additional elements will be added as basic tasks (since they don't exist as Jira issues/Trello Cards - they must be added in some form to be part of the task structure).

You can add the following **Jira** task types to the scope:

- Project
- Version (Start date and Release date can be synchronized)

See the screenshot![tree-row.png](/cms_trial/assets/a5f5581a-84b9-46f8-9160-074473f5c2ce.png)

- Agile Backlog
- Sprint (start date and end date of the Sprint can be synchronized)
- Component

**Note**:  
The 'Issues' Task Type is always automatically selected for Jira.

![advanced-configuration-issues.png](/cms_trial/assets/b25325d0-edb5-473b-9f93-8428d45f6c98.png)

In the case of **Trello**, you can add the following:

- Cards
- Lists
- Check Items
- Boards
- Check Lists

See the example

You can display the Trello Lists just like any other task:

![contentId-1918765868](/cms_trial/assets/ea5ca4f7-7221-4786-b7dd-b21c40a6f313.png)

Columns (such as Icon, Key, Summary, etc.) display information based on selected field types. Make sure your column views have been configured to meet your business needs.