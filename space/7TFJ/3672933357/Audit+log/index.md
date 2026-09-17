# Audit log

The **Worklogs Audit Log** is a centralized tracking feature that gives you complete transparency and accountability over time-tracking and worklog changes across your organization. It records a detailed history of all created, edited, and deleted worklogs, helping administrators and managers audit changes, track compliance, and review historical modifications.

![audit-log.png](/cms_trial/assets/ada9e906-c7de-42ee-8829-22466d1afed9.png)

## Key Features and Capabilities

- **Comprehensive Change History:** Automatically logs all major lifecycle events for worklogs, including creation, edits, and deletions.
- **Detailed Context and Metadata:** Captures granular details for each event, such as:

  - Jira issue keys and summaries
  - Start times and durations (including previous versus updated values for edits)
  - Assignees and affected users
  - Billable status and custom field modifications
  - Source integration details (for example, Jira import updates)
- **Advanced Filtering Options:** Quickly narrow down audit entries using robust filters:

  - **Date Range:** Filter by specific timeframes (for example, Current month).
  - **Performed By:** Track who executed the action.
  - **Affected Users:** Filter logs associated with specific team members.
  - **Action Type:** Filter by specific operations (Created, Edited, Deleted).
  - **Source:** Isolate logs by their originating source.

## **Audit Log Table Structure**

The Audit Log interface presents data in a clear, tabular view comprising the following columns:

1. **Date:** The exact timestamp when the worklog action occurred.
2. **Performed By:** The name and profile of the user (or system process) who made the change.
3. **Email**: A related email address.
4. **Action:** The type of operation performed (for example, *Created worklog*, *Edited worklog*).
5. **Details:** Comprehensive breakdown of the entry, displaying issue links, timing, duration changes, custom field values, billable flags, and affected users.