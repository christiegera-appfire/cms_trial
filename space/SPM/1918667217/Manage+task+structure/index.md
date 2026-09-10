# Manage task structure

## Manage task structure (old navigation)

## Introduction to task structure

Task structure can be generated automatically by BigPicture.

On this page, you'll learn how to set up and manage task structure within your box. Structure builders let you create, tweak, and maintain task hierarchies for a clear and organized workflow.

This guide will walk you through the different types of structure builders, how to activate and prioritize them, how to manually modify the task structure, and how to reset the task structure when needed.

### What is a task structure?

Task structure is created by organizing tasks within a box into a tree hierarchy. It helps you visualize relationships between tasks and provides a clear view of task sequences, priorities, and workflow.

### What can be included in the task structure?

| **Task structure can contain:** |
| --- |
| Jira issues | Including epics and sub-tasks. |
| Additional tasks based on Jira items | - Sprints - Components - Versions - Projects |
| Basic tasks | **Note**: The position of basic tasks cannot be automated - structure builders don’t apply to basic tasks.  You can use basic tasks when structure builders are active, but basic tasks have to be manually positioned in the tree. |
| Milestones | Milestones have to be at the bottom of a task hierarchy. A milestone has only one date and cannot be a parent of other tasks.  A task that is a parent cannot be converted into a milestone. |
| Trello tasks | Trello tasks have separate structure builders. |

**Note**: to see sprints, components, versions, and projects as tasks either:

- activate the structure builders - the tasks will show up automatically according to active structure builders
- adjust scope definition settings

### Where can I see the task structure?

| **Task structure can be viewed in:** |
| --- |
| Gantt module | Screenshot shows the Gantt module. Task structure is highlighted with a blue frame. |
| Scope module | Screenshot shows the Scope module. Task structure is highlighted with a blue frame. |
| Board module | Screenshot shows the Board module. Task structure is highlighted with a blue frame. |

### Is the task structure the same for all users?

The task structure is set up per box and is the same for all users.

## How to create a task structure

To create a task tree hierarchy in BigPicture:

1. **Access Structure Settings**: Go to `Box configuration > Tasks > Task structure`.
2. **Activate Structure Builders**: Choose between built-in or link-based builders and activate them.
3. **Order Builders**: Arrange the structure builders to reflect task priorities.
4. **Manual Adjustments**: Reposition tasks as needed to fine-tune the hierarchy.
5. **Reset if Necessary**: Reset the task structure to correct any issues or start fresh.

### Automatic task structure

Use **structure builders** to automatically create a task structure based on task information in Jira. See the [Automatic task structure (structure builders)](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) page.

The **bi-directional sync** means that, based on the active structure builders, changes made in Jira are reflected in the task tree, and vice versa. This synchronization helps maintain up-to-date and accurate task management, making it easier to track dependencies, prioritize tasks, and manage workflows effectively.

1. Go to **Box Configuration** > **Tasks** > **Task structure**
2. Open **Advanced**
3. Toggle the switches
4. Click **Save**. New task structure is created.

### Manual task structure

You can position tasks directly in BigPicture modules. See the [Manual task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/) page.

## What are structure builders

The order of structure builders reflects the levels of the hierarchy - the first structure builder determines the highest level within the structure.

| **Structure builder** | **Description** |
| --- | --- |
| Built-in structure builders | When you activate one of the built-in structure builders, a task representing a Sprint, Component, Version, or Project will be automatically added in the task types box in the automated rules of the Scope definition page. |
| Link-based structure builders | The link-based structure builders use a Jira link to define the parent/child relation. Soft links can also be used as structure builders. |
| Tree preview | The Structure Preview in the *Advanced Configuration* shows how the structure of the tasks will look based on your advanced configuration. |
| Conflicting structure builders | A warning about a conflict appears when the structure cannot be generated according to the user’s preference. |

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task structure**. image-20250327-084049.png | For a box type (all boxes of a given type), you can configure:   - Default task structure - Advanced configuration |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Task structure**. image-20250327-084155.png | For a particular box, you can configure:   - Box task structure - Advanced configuration |

**Who can manage structure builders:**

- Box Admin
- App Admin

**Who can move the tasks in the tree:**

- Box Editor
- Box Admin
- App Admin

## Default task structure settings

The task structure (task hierarchy) can be generated automatically for each box based on its type configuration. You can set a default task structure for each box type, eliminating the need to configure it every time you create a new box. The default settings can be overwritten for each box.

The task structure settings are available only if the scope type of a box is set to **Own scope** on the scope definition configuration page.

Only users with the App Admin security role can edit the Box types and access the Administration.

To set the default scheduling mode for the box type:

1. Click the **App settings** (wrench icon) in the top right corner.
2. Select**Box types** from the dropdown list.
3. On the Administration page, click a box type name to open its settings.
4. On the box type configuration page, go to **Tasks** > **Task structure**.

![Box type configuration page.](/cms_trial/assets/9e4403df-7db3-4b70-896f-aff1237baceb.png)

The default task structure in Program and Classic types of boxes is set to **Project** > **Epic** > **Sub-task**; in other boxes, the default task structure is set to **Epic** > **Sub-task**.

## Jira structure builders

See the [Jira structure builders](/cms_trial/space/SPM/1918863244/Jira+structure+builders/) page.

## Reset task structure (WBS)

### Change structure builders

Adjust the structure builders and click "Save". The task structure is rebuilt accordingly.

### Clear manual indents

Clear the changes that were manually made to the task structure.

The structure that was based on the structure builders is not affected.

![image-20240313-150615.png](/cms_trial/assets/1e601ce1-e042-4a68-9d1a-0ce0ebafe570.png)

**Trello structure builders**

When you connect external tools, you will see an additional section with Structure builders specific to that tool. In the case of Trello, these include Boards, Lists, Checklists, and Checklist Items.

[Unmapped block: nestedExpand]

## Automated structure building - algorithm explained

See the <https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1895628981/Automatic+structure+builders+-+algorithm?force_transition=4c24370d-b1d7-4059-86d9-a3894f869083> page.

## Constraints

| **Limitation** | **Description** |
| --- | --- |
| Milestones | Milestones can’t be a parent task.   - If a task is a parent, it can’t become a milestone - If a task is a milestone, the structure builders won’t make it into a parent. |
| Task structure vs scheduling mode | Scheduling mode of tasks affects their period based on the child-parent relationship. Take that into account when setting up a task structure. |
| Task edition blocked in Jira | When task editing is blocked in Jira, a task can be moved in the BigPicture WBS structure. Task position in WBS can be changed if it doesn't result in any changes in Jira.  Tasks can be moved:   - Vertically (up or down in the tree structure) - Horizontal (indent level can be changed)   Exception:  If the automatic WBS rules are in place and a change of a task position would require a change of task fields, the indentation is blocked. |

## Manage task structure (new navigation)

## Introduction to task structure

Task structure can be generated automatically by BigPicture.

On this page, you'll learn how to set up and manage task structure within your box. Structure builders let you create, tweak, and maintain task hierarchies for a clear and organized workflow.

This guide will walk you through the different types of structure builders, how to activate and prioritize them, how to manually modify the task structure, and how to reset the task structure when needed.

### What is a task structure?

Task structure is created by organizing tasks within a box into a tree hierarchy. It helps you visualize relationships between tasks and provides a clear view of task sequences, priorities, and workflow.

### What can be included in the task structure?

| **Task structure can contain:** |
| --- |
| Jira issues | Including epics and sub-tasks. |
| Additional tasks based on Jira items | - Sprints - Components - Versions - Projects |
| Basic tasks | **Note**: The position of basic tasks cannot be automated - structure builders don’t apply to basic tasks.  You can use basic tasks when structure builders are active, but basic tasks have to be manually positioned in the tree. |
| Milestones | Milestones have to be at the bottom of a task hierarchy. A milestone has only one date and cannot be a parent of other tasks.  A task that is a parent cannot be converted into a milestone. |
| Trello tasks | Trello tasks have separate structure builders. |

**Note**: to see sprints, components, versions, and projects as tasks either:

- activate the structure builders - the tasks will show up automatically according to active structure builders
- adjust scope definition settings

### Where can I see the task structure?

| **Task structure can be viewed in:** |
| --- |
| Gantt module | Screenshot shows the Gantt module. Task structure is highlighted with a blue frame. |
| Scope module | Screenshot shows the Scope module. Task structure is highlighted with a blue frame. |
| Board module | Screenshot shows the Board module. Task structure is highlighted with a blue frame. |

### Is the task structure the same for all users?

The task structure is set up per box and is the same for all users.

## How to create a task structure

To create a task tree hierarchy in BigPicture:

1. **Access Structure Settings**: Go to `Box configuration > Tasks > Task structure`.
2. **Activate Structure Builders**: Choose between built-in or link-based builders and activate them.
3. **Order Builders**: Arrange the structure builders to reflect task priorities.
4. **Manual Adjustments**: Reposition tasks as needed to fine-tune the hierarchy.
5. **Reset if Necessary**: Reset the task structure to correct any issues or start fresh.

### Automatic task structure

Use **structure builders** to automatically create a task structure based on task information in Jira. See the [Automatic task structure (structure builders)](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) page.

The **bi-directional sync** means that, based on the active structure builders, changes made in Jira are reflected in the task tree, and vice versa. This synchronization helps maintain up-to-date and accurate task management, making it easier to track dependencies, prioritize tasks, and manage workflows effectively.

1. Go to **Box Configuration** > **Tasks** > **Task structure**
2. Open **Advanced**
3. Toggle the switches
4. Click **Save**. New task structure is created.

### Manual task structure

You can position tasks directly in BigPicture modules. See the [Manual task structure](/cms_trial/space/SPM/1918669003/Manual+task+structure/) page.

## What are structure builders

The order of structure builders reflects the levels of the hierarchy - the first structure builder determines the highest level within the structure.

| **Structure builder** | **Description** |
| --- | --- |
| Built-in structure builders | When you activate one of the built-in structure builders, a task representing a Sprint, Component, Version, or Project will be automatically added in the task types box in the automated rules of the Work items from Jira page. |
| Link-based structure builders | The link-based structure builders use a Jira link to define the parent/child relation. Soft links can also be used as structure builders. |
| Tree preview | The Structure Preview in the *Advanced Configuration* shows how the structure of the tasks will look based on your advanced configuration. |
| Conflicting structure builders | A warning about a conflict appears when the structure cannot be generated according to the user’s preference. |

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task structure**. image-20250327-084049.png | For a box type (all boxes of a given type), you can configure:   - Default task structure - Advanced configuration |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Task structure**. image-20250327-084155.png | For a particular box, you can configure:   - Box task structure - Advanced configuration |

**Who can manage structure builders:**

- Box Admin
- App Admin

**Who can move the tasks in the tree:**

- Box Editor
- Box Admin
- App Admin

## Default task structure settings

The task structure (task hierarchy) can be generated automatically for each box based on its type configuration. You can set a default task structure for each box type, eliminating the need to configure it every time you create a new box. The default settings can be overwritten for each box.

The task structure settings are available only if the scope type of a box is set to **Own scope** on the scope definition configuration page.

Only users with the App Admin security role can edit the Box types and access the Administration.

To set the default scheduling mode for the box type:

1. Click the **App settings** (wrench icon) in the top right corner.
2. Select**Box types** from the dropdown list.
3. On the Administration page, click a box type name to open its settings.
4. On the box type configuration page, go to **Tasks** > **Task structure**.

![Box type configuration page.](/cms_trial/assets/9e4403df-7db3-4b70-896f-aff1237baceb.png)

The default task structure in Program and Classic types of boxes is set to **Project** > **Epic** > **Sub-task**; in other boxes, the default task structure is set to **Epic** > **Sub-task**.

## Jira structure builders

See the [Jira structure builders](/cms_trial/space/SPM/1918863244/Jira+structure+builders/) page.

## Reset task structure (WBS)

### Change structure builders

Adjust the structure builders and click "Save". The task structure is rebuilt accordingly.

### Clear manual indents

Clear the changes that were manually made to the task structure.

The structure that was based on the structure builders is not affected.

![image-20240313-150615.png](/cms_trial/assets/1e601ce1-e042-4a68-9d1a-0ce0ebafe570.png)

**Trello structure builders**

When you connect external tools, you will see an additional section with Structure builders specific to that tool. In the case of Trello, these include Boards, Lists, Checklists, and Checklist Items.

[Unmapped block: nestedExpand]

## Automated structure building - algorithm explained

See the <https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1895628981/Automatic+structure+builders+-+algorithm?force_transition=4c24370d-b1d7-4059-86d9-a3894f869083> page.

## Constraints

| **Limitation** | **Description** |
| --- | --- |
| Milestones | Milestones can’t be a parent task.   - If a task is a parent, it can’t become a milestone - If a task is a milestone, the structure builders won’t make it into a parent. |
| Task structure vs scheduling mode | Scheduling mode of tasks affects their period based on the child-parent relationship. Take that into account when setting up a task structure. |
| Task edition blocked in Jira | When task editing is blocked in Jira, a task can be moved in the BigPicture WBS structure. Task position in WBS can be changed if it doesn't result in any changes in Jira.  Tasks can be moved:   - Vertically (up or down in the tree structure) - Horizontal (indent level can be changed)   Exception:  If the automatic WBS rules are in place and a change of a task position would require a change of task fields, the indentation is blocked. |