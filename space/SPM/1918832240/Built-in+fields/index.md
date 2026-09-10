# Built-in fields

## Built-in fields (old navigation)

Click to expand the guide

## About built-in fields

Built-in fields, one of the two field types in BigPicture, can take information from various external platforms and map it to a built-in field. This effectively lets you see a single column showing values for multiple types of tasks coming from many external platforms and native BigPicture elements.

Visit the [Concept of a field](/cms_trial/space/SPM/1918633429/Concept+of+a+field/) page to learn more about the field types.

## Built-in fields matrix

The table below provides you with an overview of how built-in fields function in the App.

| **Task Attribute** | **Mapped to External Platform**  **(non-configurable)** | **Mapped to External Platform** **(configurable)** | **Available for basic tasks** **(tasks that exist only in the app)** | **Comment** |
| --- | --- | --- | --- | --- |
| Icon | YES | NO | YES | If an icon is not available on the external platform, the default icon will be used (same as for basic tasks) |
| Key | YES | NO | YES | The built-in “Key” column aggregates issue/task/card keys from different platforms and displays them in a single column. A “Key” field cannot be modified to display a different value.  [Unmapped block: nestedExpand] |
| Summary | YES | NO | NO | A built-in summary field cannot be removed. The mapping of the field can’t be changed.  [Unmapped block: nestedExpand] |
| Start date | YES | YES | YES | The mapping of the start date (built-in) field for Jira can be changed in the App Configuration.  Trello cards don’t have a start date. A built-in field uses the due date value (effectively, the built-in field start and end dates of Trello cards are both mapped to the Trello due date).  Basic Task dates are displayed in a built-in Start date column.  [Unmapped block: nestedExpand] |
| End date | YES | YES | YES |  |
| Baseline start date | YES | YES | YES |  |
| Baseline end date | YES | YES | YES |  |
| Progress | YES | YES | YES |  |
| Milestone | YES | YES | YES | Native app field. It exists only as a built-in field, but its value can be mapped to display a Jira value.  [Unmapped block: nestedExpand] |
| Period mode | YES | YES | YES |  |
| Color | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. |
| Task ID | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. contentId-1918832240 |
| Assignee | YES | NO | YES | Single-choice field.  The Jira task's assignee field corresponds to the default Jira assignee field (the mapping cannot be changed).  For basic tasks, information is stored in BigPicture and isn’t synchronized with Jira. Assignee (built-in).mp4 |
| Skills | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. |
| Status | YES | NO | NO |  |
| Duration Calendar Days | NO | NO | YES | Based on the number of calendar days (start to end date). contentId-1918832240  - counts all days between the start/end date (including weekends, holidays, etc.) - inline editing (NO) |
| Duration working days | NO | NO | YES | Based on the number of working days (non-working days excluded). duration calendar days.png  - counts days between the start/end date → excludes weekends, holidays, absences of an assignee etc. - inline editing (YES) |
| Outline level | NO | NO | YES | Dynamically built data type - the values aren't permanently associated with tasks; the field value adjusts to reflect WBS changes.  **Display Options:**   - indent level - sequential index  contentId-1918832240 **Outline level** → shows how deep the task is in the tree structure (WBS). outline level.png **Sequential Index** → shows where the task is located in the WBS structure (similar to the notation of the table of contents in the book) contentId-1918832240 **Note:** filtering does not affect the Sequential Index. |
| Overdue Start/End Date | NO | NO | NO | The **Overdue Start Date** field calculates the difference between the current task Start Date (when the status category is To Do).   - Datatype: number - Only calculates full calendar days - If the difference is larger than 0, the difference as a number of days is displayed as an integer - If the difference is 0 or smaller, the field is blank - If the status category is In Progress or Done, the field is blank - No inline editing - Aggregations: default numeric datatype aggregations   The **Overdue End Date** calculates the difference between the current task End Date (when status category is not Done).   - Data type: number - Only calculates full calendar days - If the difference is larger than 0, the difference as a number of days is displayed as an integer - If the difference is 0 or smaller, the field is blank - If the status category is Done, the field is blank - No inline editing - Aggregations: default numberic datatype aggregations  contentId-1918832240contentId-1918832240 |
| Team | NO | NO | YES | The **Team** field is based on the Team datatype. A team created in BigPicture is visible in a column view on the Gantt and Scope modules and can be inline edited.  The field can also be used even if not synchronized. Check **App Configuration** > **General** > **Fields** > **General mapping**. contentId-1918832240 |
| Workload Contouring Mode | NO | NO | YES | Workload contouring allows the task’s effort to be spread over its duration. There are three automatic options and one manual mode to choose from.   - Flat - Front-loaded - Back-loaded - Manual (available only for **BigPicture Enterprise**)  contentId-1918832240 |
| Sub-box | YES | NO | YES | The field displays the names of the child boxes in which the task is located (only the name of the box one level down is displayed). The field can hold more than one box name, as a task can be present in more than one box.  The field is in the readonly mode. sub-box.png The field is especially useful in higher-level boxes to group tasks: sub-box-grouping.png |
| Priority | YES | NO | YES | Jira provides default priorities such as Highest, High, Medium, Low, and Lowest.  **Jira work items**:  Jira Admins can modify the default priorities, create new ones, and add them to existing projects by associating these priorities with [project priority schemes](https://support.atlassian.com/jira-cloud-administration/docs/configure-priorities-for-projects/).  **Basic tasks**:   - Priority schemes do not apply to basic tasks. Only the default priorities can be assigned to a basic task.  Priority built-in field. |

### Basic tasks

A built-in field lets you easily visualize all data related to [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/) native to the BigPicture itself. Some values, such as Assignee, are not available (because this attribute doesn’t exist for them), but all existing attributes of basic tasks can be displayed using built-in fields.

## Mapping options for built-in fields

See the [Mapping options for built-in fields](/cms_trial/space/SPM/1926234390/Mapping+options+for+built-in+fields/) page to learn more.

## Built-in fields (new navigation)

Click to expand the guide

## About built-in fields

Built-in fields, one of the two field types in BigPicture, can take information from various external platforms and map it to a built-in field. This effectively lets you see a single column showing values for multiple types of tasks coming from many external platforms and native BigPicture elements.

Visit the [Concept of a field](/cms_trial/space/SPM/1918633429/Concept+of+a+field/) page to learn more about the field types.

## Built-in fields matrix

The table below provides you with an overview of how built-in fields function in the App.

| **Task Attribute** | **Mapped to External Platform**  **(non-configurable)** | **Mapped to External Platform** **(configurable)** | **Available for BigPicture tasks** **(tasks that exist only in the app)** | **Comment** |
| --- | --- | --- | --- | --- |
| Icon | YES | NO | YES | If an icon is not available on the external platform, the default icon will be used (same as for basic tasks) |
| Key | YES | NO | YES | The built-in “Key” column aggregates issue/task/card keys from different platforms and displays them in a single column. A “Key” field cannot be modified to display a different value. Screenshot of the Jira work item Key in the Gantt module. |
| Summary | YES | NO | NO | A built-in summary field cannot be removed. The mapping of the field can’t be changed. |
| Start date | YES | YES | YES | The mapping of the start date (built-in) field for Jira can be changed in the App Configuration.  Trello cards don’t have a start date. A built-in field uses the due date value (effectively, the built-in field start and end dates of Trello cards are both mapped to the Trello due date).  BigPicture task dates are displayed in a built-in Start date column. |
| End date | YES | YES | YES |  |
| Baseline start date | YES | YES | YES |  |
| Baseline end date | YES | YES | YES |  |
| Progress | YES | YES | YES |  |
| Milestone | YES | YES | YES | Native app field. It exists only as a built-in field, but its value can be mapped to display a Jira value. |
| Period mode | YES | YES | YES |  |
| Color | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. |
| Task ID | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. Screenshot of the Task ID column in the Gantt module. |
| Assignee | YES | NO | YES | Single-choice field.  The Jira work item’s assignee field corresponds to the default Jira assignee field (the mapping cannot be changed).  For BigPicture tasks, information is stored in BigPicture and isn’t synchronized with Jira. |
| Skills | NO | NO | YES | Native App field. It can’t be mapped to display values from external tools. |
| Status | YES | NO | NO |  |
| Duration Calendar Days | NO | NO | YES | Based on the number of calendar days (start to end date). contentId-1918832240  - counts all days between the start/end date (including weekends, holidays, etc.) - inline editing (NO) |
| Duration working days | NO | NO | YES | Based on the number of working days (non-working days excluded). duration calendar days.png  - counts days between the start/end date → excludes weekends, holidays, absences of an assignee etc. - inline editing (YES) |
| Outline level | NO | NO | YES | Dynamically built data type - the values aren't permanently associated with tasks; the field value adjusts to reflect WBS changes.  **Display Options:**   - indent level - sequential index  contentId-1918832240 **Outline level** → shows how deep the task is in the tree structure (WBS). outline level.png **Sequential Index** → shows where the task is located in the WBS structure (similar to the notation of the table of contents in the book) contentId-1918832240 **Note:** filtering does not affect the Sequential Index. |
| Overdue Start/End Date | NO | NO | NO | The **Overdue Start Date** field calculates the difference between the current task Start Date (when the status category is To Do).   - Datatype: number - Only calculates full calendar days - If the difference is larger than 0, the difference as a number of days is displayed as an integer - If the difference is 0 or smaller, the field is blank - If the status category is In Progress or Done, the field is blank - No inline editing - Aggregations: default numeric datatype aggregations   The **Overdue End Date** calculates the difference between the current task End Date (when status category is not Done).   - Data type: number - Only calculates full calendar days - If the difference is larger than 0, the difference as a number of days is displayed as an integer - If the difference is 0 or smaller, the field is blank - If the status category is Done, the field is blank - No inline editing - Aggregations: default numeric datatype aggregations  contentId-1918832240contentId-1918832240 |
| Team | NO | NO | YES | The **Team** field is based on the Team datatype. A team created in BigPicture is visible in a column view on the Gantt and Scope modules and can be inline edited.  The field can also be used even if not synchronized. Check **App Configuration** > **General** > **Fields** > **General mapping**. contentId-1918832240 |
| Workload Contouring Mode | NO | NO | YES | Workload contouring allows the task’s effort to be spread over its duration. There are three automatic options and one manual mode to choose from.   - Flat - Front-loaded - Back-loaded - Manual (available only for **BigPicture Enterprise**)  contentId-1918832240 |
| Sub-box | YES | NO | YES | The field displays the names of the child boxes in which the task is located (only the name of the box one level down is displayed). The field can hold more than one box name, as a task can be present in more than one box.  The field is in the readonly mode. Screenshot of the Sub-box column in the Gantt module. The field is especially useful in higher-level boxes to group tasks: |
| Priority | YES | NO | YES | Jira provides default priorities such as Highest, High, Medium, Low, and Lowest.  **Jira work items**:  Jira Admins can modify the default priorities, create new ones, and add them to existing projects by associating these priorities with [project priority schemes](https://support.atlassian.com/jira-cloud-administration/docs/configure-priorities-for-projects/).  **BigPicture tasks**:   - Priority schemes do not apply to BigPicture tasks. Only the default priorities can be assigned to a BigPicture task.  Priority built-in field. |

### BigPicture tasks

A built-in field lets you easily visualize all data related to [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/) native to the BigPicture itself. Some values, such as Assignee, are not available (because this attribute doesn’t exist for them), but all existing attributes of BigPicture tasks can be displayed using built-in fields.

## Mapping options for built-in fields

See the [Mapping options for built-in fields](/cms_trial/space/SPM/1926234390/Mapping+options+for+built-in+fields/) page to learn more.