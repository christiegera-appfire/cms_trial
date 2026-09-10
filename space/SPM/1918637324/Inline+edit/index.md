# Inline edit

## Inline edit (old navigation)

Click to expand the guide

## About inline editing

**Inline editing** lets you quickly update your tasks on the same page instead of jumping between several edit pages. Once you modify a particular field, a change will be instantly reflected on the board, the host platform (your Jira instance currently used), and external platforms (if they are connected).

Inline editing is activated with a single click:

Image — asset pipeline pending  
Video of inline editing in the Gantt module.

Depending on the module structure, inline changes can be made in the areas indicated by a visible frame, as shown in the table below.

| **Area / Module** | **Inline editing is available for** | **Example** |
| --- | --- | --- |
| [Overview](/cms_trial/space/SPM/1918502655/Overview+module/) | Column views (Hierarchy mode & Timeline mode) | A new box in the Overview module |
| [Gantt](/cms_trial/space/SPM/1918797129/Gantt+module/) | Column views | Adding an assignee in the Gantt module |
| Gantt chart (task details dialog) | Choosing Auto-bottom up scheduling mode in the Gantt chart |
| Data → Group tasks | Setting To Do status in the Gantt module |
| [Scope](/cms_trial/space/SPM/1918666763/Scope+module/) | Column views | Setting an end date in the Scope module |
| Data → Group tasks | Choosing assignee in the Scope module |
| [Board](/cms_trial/space/SPM/1918796888/Board+module/) | Task cards  To learn more about customizing Task Cards, go to [Card view creator](/cms_trial/space/SPM/1918832263/Card+view+creator/). | Choosing color in the Board module |
| Backlog |
| [Resources](/cms_trial/space/SPM/1918535629/Resources+module/) | Task details dialog (Task details) | Task details in the Resource module |
| Workload details → Workload contouring  Workload contouring can be edited only in the manual workload mode. Otherwise, it is calculated automatically. | Choosing contouring in the Resources module |
| Unscheduled tasks panel | Assigning assignee to the unassigned tasks |
| [Teams](/cms_trial/space/SPM/1918829775/Teams+module/) | Membership period (Start Date) | Teams availablity |
| Team member availability |
| [Risks](/cms_trial/space/SPM/1918666681/Risks+module/) | Risk cards | Choosing an assignee in the Risks module |
| Risk table | Unassigned tasks in the Risks module |
| [Calendar](/cms_trial/space/SPM/1918699000/Calendar+module/) | Calendar view / Dashboard | Choosing assignee in the Calendar module |
| Upcoming tasks | Upcoming tasks displayed in the Calendar module |
| Task list | Task list in the Calendar module |
| [Financials](/cms_trial/space/SPM/1918404223/Financials+module+(NEW)/) | Initiative → Work costs breakdown: Summary, Start date, End date, Team | inlin-edit-initiative.png |
| Portfolio → Initiative costs and budgets: Budget | inline-edit-portfolio.png |
| [BigPicture Administration](/cms_trial/space/SPM/1918829342/App+administration/) | Administration → Resources → Skills | Color is chosen in the Skills settings |

Note that you can also inline edit Strategic theme/Objective and Key Result data in selected OKR columns. Visit [Edit OKRs](/cms_trial/space/SPM/1918669695/Edit+OKRs/) to learn more.

## Editable fields

You can edit inline:

- fields that are synchronized with external platforms
- BigPicture built-in fields (that can't be synchronized with external platforms), such as "Color"

The following table presents a list of field types that can be edited inline.

| **Field type** | **Example** |
| --- | --- |
| Text Jira_text_fields.png | "Name" |
| "Description" |
| "Summary" |
| "Text single line" type custom fields  “Text multi-line” type custom fields  **Note**: Only simple text can be edited (elements such as tables, lists, or links can’t be managed using inline editing of a text field). Content appears as a single line - additional formatting of the field content is not possible in BigPicture. Only up to 255 characters are handled by the inline editing of a text field. |
| Number | "Story Points" |
| "Progress" |
| "Cost [Eur]" |
| "Number" type custom fields |
| Date | "Date Picker" Jira fields |
| Built-in fields, e.g., "End Date", "Start Date" |
| Fields where data type = date |
| Select list (single choice) | "Select list (single choice)" type custom fields |
| Labels | "Labels" type custom fields |
| User data | "Assignee" |
| Estimation data | "Original Estimate" |
| "Remaining Estimate" |
| Status | "Status" (changes can be made to column values in the Backlog panel on the right only. **Unavailable on Jira Cloud**)  **Note:** If Resolution is required by a workflow, inline editing is blocked.  This applies when a Jira workflow displays an extra screen (typically Resolution, but it could also be any other field, e.g., time spent, or version). Even if the screen contains only non-required fields, a user has to go to Jira to close the task.  "Basic Task status"  Basic Tasks can have three statuses: To-do, In progress, and Done. When creating a new Basic Task, every new task automatically has the To-do status. The tasks are not built-in fields in BigPicture and are not integrated with Jira.  More information is available in the [Concept of a field](/cms_trial/space/SPM/1918633429/Concept+of+a+field/). |
| Milestone | Milestone |
| Skills | “Skills” |
| BigPicture built-in fields  (can’t be mapped to display values from external tools) | "Color" |
| "Duration Working Days" |
| "Workload Contouring Mode" |

"Duration Working Days" can be edited when the "Scheduling Mode" field is set to "Manual" or "Auto top-down." Modifying the value will adjust the "Start Date" and "End Date" fields to a new duration in working days. The value cannot be set to "0". BigPicture reverts such a change to the previous value.

## Non-editable fields

A group of fields, such as the "Team," "Sprint," "Icon," and "URL link," cannot be edited inline.

## Limitations

1. The inline editing will be disabled when aggregations are selected for a particular column.
2. Inline editing is possible for fields that can be edited and are not blocked by other settings or factors. As an example, if the "Scheduling Mode" is set to "Locked", you will not be able to edit the "Start Date" and "End Date" fields.
3. Inline editing is disabled for fields that are not added to the screen scheme in the Jira project. If the option is enabled, the App verifies if the field is on the project scheme before trying to update the field. If the field is not present on the scheme, then the App does not overwrite it. As a result, the warning message appears about '[Respect Jira screen scheme](/cms_trial/space/SPM/1918703088/Respect+Jira+screen+scheme/)' and a user should contact a Jira admin to review the project settings.

   ![Screenshot of the Respect Jira screen scheme toggle switch.](/cms_trial/assets/30dc16e8-1a96-4241-a13f-f0d95b9082e3.png)![Screenshot of inline editing the End Date in the Scope module.](/cms_trial/assets/c6e4747c-d7ff-4810-b855-5a85f5ec19fa.png)

## Inline edit (new navigation)

Click to expand the guide

## About inline editing

**Inline editing** lets you quickly update your tasks on the same page instead of jumping between several edit pages. Once you modify a particular field, a change will be instantly reflected on the board, the host platform (your Jira instance currently used), and external platforms (if they are connected).

Inline editing is activated with a single click:

![Video presenting inline editing in the Gantt module.](/cms_trial/assets/8853dff5-d21c-4316-ab29-8cd2c52f6db9.mp4)

Depending on the module structure, inline changes can be made in the areas indicated by a visible frame, as shown in the table below.

| **Area / Module** | **Inline editing is available for** |
| --- | --- |
| [Overview](/cms_trial/space/SPM/1918502655/Overview+module/) | - Column views (Hierarchy mode & Timeline mode)  Screenshot of inline editing in the Overview module. |
| [Gantt](/cms_trial/space/SPM/1918797129/Gantt+module/) | - Column views - Gantt chart (task details dialog) - View → Group  Screenshot of inline editing in the Gantt module. |
| [Scope](/cms_trial/space/SPM/1918666763/Scope+module/) | - Column views - View → Group  Screenshot of inline editing in the Scope module. |
| [Board](/cms_trial/space/SPM/1918796888/Board+module/) | - Task cards (to learn more about customizing task cards, go to [Card view creator](/cms_trial/space/SPM/1918832263/Card+view+creator/)) - Backlog  Screenshot of inline editing in the Board module. |
| [Resources](/cms_trial/space/SPM/1918535629/Resources+module/) | - Task details dialog (task details) - Workload details → Workload contouring  Workload contouring can be edited only in the manual workload mode. Otherwise, it is calculated automatically. - Backlog  Screenshot of inline editing in the Resources module. |
| [Teams](/cms_trial/space/SPM/1918829775/Teams+module/) | - Membership period (Start Date) - Team member availability  Screenshot of inline editing in the Teams module. |
| [Risks](/cms_trial/space/SPM/1918666681/Risks+module/) | - Risk cards - Risk table  Screenshot of inline editing in the Risks module. |
| [Calendar](/cms_trial/space/SPM/1918699000/Calendar+module/) | - Calendar view / Dashboard - Upcoming tasks - Task list  Screenshot of inline editing in the Calendar module. |
| [Financials](/cms_trial/space/SPM/1918404223/Financials+module+(NEW)/) | - Initiative → Work costs breakdown: Summary, Start date, End date, Team - Portfolio → Initiative costs and budgets: Budget  Screenshot of inline editing in the Financials module. |
| [BigPicture Administration](/cms_trial/space/SPM/1918829342/App+administration/) | - Administration → Resources → Skills  Screenshot of inline editing in BigPicture Administration. |

Note that you can also inline edit Strategic theme/Objective and Key Result data in selected OKR columns. Visit [Edit OKRs](/cms_trial/space/SPM/1918669695/Edit+OKRs/) to learn more.

## Editable fields

You can edit inline:

- fields that are synchronized with external platforms
- BigPicture built-in fields (that can't be synchronized with external platforms), such as "Color"

The following table presents a list of field types that can be edited inline.

| **Field type** | **Example** |
| --- | --- |
| Text Jira_text_fields.png | "Name" |
| "Description" |
| "Summary" |
| "Text single line" type custom fields  “Text multi-line” type custom fields  **Note**: Only simple text can be edited (elements such as tables, lists, or links can’t be managed using inline editing of a text field). Content appears as a single line - additional formatting of the field content is not possible in BigPicture. Only up to 255 characters are handled by the inline editing of a text field. |
| Number | "Story Points" |
| "Progress" |
| "Cost [Eur]" |
| "Number" type custom fields |
| Date | "Date Picker" Jira fields |
| Built-in fields, e.g., "End Date", "Start Date" |
| Fields where data type = date |
| Select list (single choice) | "Select list (single choice)" type custom fields |
| Labels | "Labels" type custom fields |
| User data | "Assignee" |
| Estimation data | "Original Estimate" |
| "Remaining Estimate" |
| Status | "Status" (changes can be made to column values in the Backlog panel on the right only. **Unavailable on Jira Cloud**)  **Note:** If Resolution is required by a workflow, inline editing is blocked.  This applies when a Jira workflow displays an extra screen (typically Resolution, but it could also be any other field, e.g., time spent, or version). Even if the screen contains only non-required fields, a user has to go to Jira to close the task.  "BigPicture Task status"  BigPicture tasks can have three statuses: To-do, In progress, and Done. When creating a new BigPicture task, every new task automatically has the To-do status. The tasks are not built-in fields in BigPicture and are not integrated with Jira.  More information is available in the [Concept of a field](/cms_trial/space/SPM/1918633429/Concept+of+a+field/). |
| Milestone | Milestone |
| Skills | “Skills” |
| BigPicture built-in fields  (can’t be mapped to display values from external tools) | "Color" |
| "Duration Working Days" |
| "Workload Contouring Mode" |

"Duration Working Days" can be edited when the "Scheduling Mode" field is set to "Manual" or "Auto top-down." Modifying the value will adjust the "Start Date" and "End Date" fields to a new duration in working days. The value cannot be set to "0". BigPicture reverts such a change to the previous value.

## Non-editable fields

A group of fields, such as the "Team," "Sprint," "Icon," and "URL link," cannot be edited inline.

## Limitations

1. The inline editing will be disabled when aggregations are selected for a particular column.
2. Inline editing is possible for fields that can be edited and are not blocked by other settings or factors. As an example, if the "Scheduling Mode" is set to "Locked", you will not be able to edit the "Start Date" and "End Date" fields.
3. Inline editing is disabled for fields that are not added to the screen scheme in the Jira project. If the option is enabled, the App verifies if the field is on the project scheme before trying to update the field. If the field is not present on the scheme, then the App does not overwrite it. As a result, the warning message appears about '[Respect Jira screen scheme](/cms_trial/space/SPM/1918703088/Respect+Jira+screen+scheme/)' and a user should contact a Jira admin to review the project settings.

   ![Screenshot of the Respect Jira screen scheme toggle switch.](/cms_trial/assets/30dc16e8-1a96-4241-a13f-f0d95b9082e3.png)