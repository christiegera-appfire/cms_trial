# Configure task scheduling

## Configure task scheduling (old navigation)

Click to expand the guide

On this page, you will find the information about the **Task scheduling mode**.

To read about **Task period alignment,** go to [Define task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/) page.

The scheduling option on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) configuration page determines how new tasks added to the box will interact with the scheduling mechanism, including factors like task dependencies and parent/child relationships.

This option sets a default configuration for all newly created boxes of that specific box type.

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Scheduling**. Scheduling mode on the box type configuration page. | For a box type (all boxes of a given type), you can configure:   - Default box scheduling mode |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Scheduling**. Scheduling mode on the box type configuration page. | For a particular box, you can configure:   - Box scheduling mode |

## Default scheduling mode

When the scope definition of a box type is set to **Sub-scope**, the scheduling mode of the new box is inherited from the parent (upper-level) box and cannot be modified.

Switching the box type settings from the **Sub-scope** to **Own** does not affect the existing boxes. If a box was created when the scope definition of the box type was set to the **Sub-scope**:

- you cannot change that scope,
- you cannot modify its default scheduling mode.

The default scheduling mode is **auto basic** and applies only to newly created tasks (tasks that were added to the box's scope for the first time.) If a task was added to the scope prior to the scheduling mode change, its existing mode will remain unchanged.

For Boxes with the **Own** scope, you can choose from four available [scheduling modes](/cms_trial/space/SPM/1918831395/Scheduling+mode/):

- Auto basic
- Auto bottom-up
- Auto top-down
- Lock
- Manual

## Add a new task to the scope of a box

You can add a new task to the scope of a box in the following ways:

- use the **+Task** button in the Scope, Gantt, Board, Risks, and Resources modules.
- change the [scope definition](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) of a box.

Jira sprint, version, component, and project always have the default scheduling mode set to manual, regardless of the scheduling mode you set as default.

We recommend using the **Manual** scheduling mode to ensure that your task will not be automatically rescheduled based on the configuration of structure builders and dependencies. You can enable automation anytime, but you might not be able to easily revert changes.

## Configure task scheduling (new navigation)

Click to expand the guide

On this page, you will find the information about the **Task scheduling mode**.

To read about **Task period alignment,** go to [Define task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/) page.

The scheduling option on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) configuration page determines how new tasks added to the box will interact with the scheduling mechanism, including factors like task dependencies and parent/child relationships.

This option sets a default configuration for all newly created boxes of that specific box type.

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Scheduling**. Screenshot of the Scheduling page in the box type configuration. | For a box type (all boxes of a given type), you can configure:   - Default task scheduling mode |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Scheduling**. Screenshot of the Scheduling page in the box configuration. | For a particular box, you can configure:   - Task scheduling mode |

## Default scheduling mode

When the scope definition of a box type is set to **sub-scope**, the scheduling mode of the new box is inherited from the parent (upper-level) box and cannot be modified.

Switching the box type settings from the **sub-scope** to **own** does not affect the existing boxes. If a box was created when the scope definition of the box type was set to the **sub-scope**:

- You cannot change that scope.
- You cannot modify its default scheduling mode.

The default scheduling mode is **auto basic** and applies only to newly created tasks (tasks that were added to the box's scope for the first time.) If a task was added to the scope prior to the scheduling mode change, its existing mode will remain unchanged.

For Boxes with the **own** scope, you can choose from four available [scheduling modes](/cms_trial/space/SPM/1918831395/Scheduling+mode/):

- Auto basic
- Auto bottom-up
- Auto top-down
- Lock
- Manual

## Add a new task to the scope of a box

You can add a new task to the scope of a box in the following ways:

- Click **Task** > **Create** > **Jira work item/BigPicture task** in the Gantt, Scope, Board, and Resources modules.
- Click **Risks** > **Create new risk** in the Risks module.
- Populate the box with [work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/).

Jira sprint, version, component, and space always have the default scheduling mode set to manual, regardless of the default scheduling mode you set.

We recommend using the **Manual** scheduling mode to ensure your task is not automatically rescheduled based on the configuration of structure builders and dependencies. You can enable automation at any time, but you might not be able to easily revert changes.