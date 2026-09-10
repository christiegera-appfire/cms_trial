# Team code field

The Team field mapping can be configured per Jira project.

![contentId-1918767884](/cms_trial/assets/a4e69e79-862a-4b69-8440-bb6ca844cbb6.png)

To use a different team field mapping, you must create a separate mapping for a Jira project, even if the only discrepancy between the general and project configurations is just one field.

Switch to the **"Custom mapping"** tab to configure mapping per the Jira project. Settings are created per Jira project (not per box).

Either add a new project and create a configuration or modify the existing one.

![contentId-1918767884](/cms_trial/assets/8f6777bd-ab18-45f7-809f-c7891c5f7bea.png)

## [Team code](/cms_trial/space/SPM/1918798278/Teams+(Resource+management)/)

The functioning of team codes is dependent on resource configuration.

## Multi-team assignment

The App does not support assigning multiple Teams to a task. In the case of multiple labels, the App assigns the task to the first team in alphabetical order.

When a task with multiple team labels is reassigned using the App, all other team labels will be removed.

## Supported field types

You can sync team assignments with any custom field of the following types:

- "Labels"
- "Select list (single choice)"

Example of fields with values:

![contentId-1918767884](/cms_trial/assets/58d07e67-4566-403d-90e4-8d06ed300aa4.png)

### Labels field

When using labels, the App can automatically generate a Team label when a Team is assigned to a task. You can assign a Team manually by adding a label that must include the 'team#' prefix before the Team code.

Even though labels are convenient, they are prone to human error, such as typos. We recommend using the dedicated "Labels" type field, as the native Jira "Labels" field might be used for other purposes.

### Select list field

In the case of select list fields, you must predefine the select options using the Team codes. This can be done by Jira admin only in Jira administration (settings) > Issues > Custom fields > (Your Team field) > Configure:

![contentId-1918767884](/cms_trial/assets/e036f7b6-c896-48ca-aab0-778526282594.png)

## Field data migration

When a field that's different from the one currently used is selected, the option to migrate data will appear below the filed picker:

![contentId-1918767884](/cms_trial/assets/9a8bb1db-8678-4624-a86f-a7437850da88.png)

Data migration of a particular issue can fail in the following cases:

- When migrating from a single select field to a labels field: team code contains whitespaces.
- When migrating to a single select field: a field does not contain the team code in the list of select options (the app does not create the select options during the migration process).

Data migration happens in the background, so the user might not be aware of that process. Depending on the number of issues that call for an update, it might be time-consuming. We recommend performing such migration during a Jira maintenance session.