# Action parameters

Some action types support dynamic parameters. Dynamic parameters let you include SLA or Jira work item details in messages, comments, and notification content.

You can use dynamic parameters in:

- Email subjects and bodies
- Slack messages
- Comments

To add a dynamic parameter, type **$** or select one of the available parameter chips.

Here is the full list of parameters you can use:

| **Parameter** | **Type** | **Description** |
| --- | --- | --- |
| `$baseUrl` | String | Jira base URL. |
| `$slaDescription` | String | Name of the SLA. |
| `$slaValue` | String | SLA value as a time string. |
| `$slaStartDate` | String | Start time of the SLA. |
| `$slaEndDate` | String | End time of the SLA. |
| `$originStatus` | String | Origin status name (null if not set by status). |
| `$slaState` | String | The SLA’s state. |
| `$targetStatus` | String | Target status name (null if not set by status). |
| `slaTargetDate` | String | Target date of the SLA. |
| `$issue.key` | String | Work item key (for example, ABC-123). |
| `$issue.summary` | String | Summary of the work item. |
| `${issue.fields.reporter.displayName}` | String | Display name of the work item’s reporter. |
| `${issue.fields.priority.name}` | String | Priority of the work item. |
| `${issue.fields['customfield_10004'][*].name}` | String | Custom field for organizations. |
| `${issue.fields.duedate}` | String | Due date of the work item. |
| `${issue.fields.assignee.displayName}` | String | Display name of the work item’s assignee. |
| `${baseUrl}/browse/${issue.key}` | String | Link to the work item. |
| `$issue.fields.content[0].content.text` | String | Slack notification parameter for the work item description. |
| `${issue.fields['customfield_1000'].value}` | String | The single-choice custom field. |
| `${issue.fields['customfield_1000'][*].value}` | String | The select list multiple-choice custom field. |
| `$issue.fields.labels` | String | The label field. |