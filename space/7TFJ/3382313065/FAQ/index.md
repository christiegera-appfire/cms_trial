# FAQ

This guide addresses common questions regarding time tracking, approvals, reporting, and permissions within the app.

## Overview and Core Concepts

### What is 7pace for Jira?

7pace is a professional time tracking and timesheet management application integrated directly into Jira Cloud. It is designed to capture time against Jira issues, support period-based timesheet submissions and manager approvals, and provide clear reporting for operational visibility.

> **Note:** 7pace focuses strictly on execution-level time tracking and reporting. It is not a project planning, baselining, or resource capacity forecasting system.

### Do I need Jira to use 7pace?

**Yes**. 7pace runs entirely inside Jira Cloud. It relies on your native Jira projects, work items, and permissions to log time and generate reports. Users must have access to the relevant Jira projects to track time against them.

### Can 7pace support work item–level time entry for billing or chargeability?

**Yes**. Users log time directly against specific Jira work items (e.g., tasks, stories, bugs). Multiple team members can log time to the same item, making it ideal for client billing, project costing, or chargeability tracking. All recorded data can be reviewed and exported directly through 7pace.

### Can 7pace be used with Jira Service Management (JSM)?

**Yes**. Jira Service Management issues (Incidents, Requests, Problems) function like standard Jira issues. If a user has access to the JSM project, they can seamlessly log time on those tickets using 7pace.

### Does 7pace support project baselining or planning?

**No**. 7pace does not feature project planning, roadmapping, or baselining capabilities. It is dedicated to capturing, approving, and analyzing actual time spent. For planning and resource management, external project management apps or native Jira tools should be utilized.

## Logging Time

### Can multiple people log time to the same Jira issue?

**Yes**. While Jira typically allows only one assignee per issue at a time, 7pace permits any user with access to that issue to log their individual hours against it.

### Can time be logged on any accessible Jira issue?

**Yes**. Users can log time to any Jira work item they have permission to view, regardless of whether that item is part of a specific sprint, release, or planning view.

### Can time be charged to multiple Jira projects in the same timesheet?

**Yes**. 7pace operates at the Jira site level. This allows users to log time across entirely different Jira projects (including Jira Service Management) within a single timesheet period, provided they have the required Jira project permissions.

### How do users log time in 7pace?

7pace offers flexible options for tracking time directly from your Jira environment:

- **From Jira Issues:** Log time directly inside the Jira issue view or from your project boards.
- **Duration vs. Time Range:** Users can type a flat duration (e.g., `2h 30m`) or use the **Timeframe** mode to specify exact start and end times. When using a timeframe, 7pace automatically calculates the total duration.
- **Editing & Deleting:** Users can easily update or remove their own logged time entries directly from their timesheet or the issue itself, provided the tracking period is still open.

### Why doesn’t a specific task automatically appear on my Timesheet?

The 7pace Timesheet view displays tasks based on recency and recent logging activity, rather than assignment alone. If an assigned task has not had time logged against it recently, it may drop off the main view to keep your interface clean.

- **Solution:** If a task is not visible, simply use the search bar within the timesheet interface to find it by name or issue key and add it manually.

### Can issues be locked to prevent further time logging?

**Yes**. 7pace administrators can configure automation rules that restrict time logging. For example, a rule can be set to automatically block new time entries on any work item that has reached a final workflow status (e.g., *Done*, *Closed*, or *Cancelled*), either immediately or after a set number of days.

### Can the time display format be changed?

**No**. The internal time format within the 7pace UI is globally standardized and not individually configurable. However, formatting can be adjusted as needed once the data is exported into external tools like Excel or CSV.

### Does time logged on child work items roll up to parent work items?

**Partially**. 7pace leverages Jira’s native parent-child hierarchy. Time logged on a sub-task will automatically roll up to its parent task, and up to an Epic. However, time does not roll up across generic, non-hierarchical issue links (e.g., "relates to" or "blocks").

### Can worklogs be hidden from certain users who can view a Jira issue?

**No**. Jira security models dictate that if a user has permission to view an issue, they can view all worklogs associated with it. 7pace security roles manage feature access inside the 7pace application itself but cannot override native Jira issue-level visibility.

### What search capabilities are available in the “Add Time” dialog?

Users can search for work items by entering the issue name or the unique Jira issue key. If an administrator has configured a **Search Filter** rule, users can also refine their search using specific custom fields defined by the organization.

### How can I organize or view work by project in the Timesheet view?

The standard Timesheet view is optimized for quick data entry and displays the Jira issue key, which identifies the project. For deeper hierarchy mapping, the **Items Hierarchy** view shows parent-child structures. For advanced grouping, filtering, or sorting by project, users should use the **Times Explorer** tab.

## Time Submission, Approval, and Locking

### How does the time approval workflow work?

The 7pace approval workflow ensures data integrity through a structured submission cycle:

1. **Log & Track:** Users log their hours throughout the tracking period.
2. **Submit:** The user submits their completed timesheet period for review. This action locks their entries for that period. (Users can "Recall" a submission to make changes, provided it hasn't been approved yet).
3. **Review:** Managers review the submitted hours.
4. **Approve or Reject:**

   - **Approve:** Officially locks the period. The user can no longer edit or recall their time unless an authorized manager reopens it.
   - **Reject:** Sends the timesheet back to the user for modifications.

### What exactly does “Submit Period” do?

Clicking "Submit Period" signals to your manager that your hours are complete and ready for review. It locks the timesheet period to prevent accidental edits.

> **Note:** Submitting a period does *not* alter the status of your Jira issues; it only processes the 7pace time records.

### Who can approve timesheets in 7pace?

Approvals are role-based. When a user submits a period, they designate an approver. Only the selected approver, a designated 7pace Manager, or a Global Manager/Admin can approve the timesheet. Unsubmitted periods can only be approved or locked by a Global Manager or Admin.

### Is bulk approval or approval automation supported?

**No**. Timesheets must be evaluated individually. Managers must manually review and either approve or reject each user's period submission.

### Can approvers be designated per individual task or story?

**No**. In 7pace, approvals are processed uniformly by time period (e.g., weekly or bi-weekly blocks) for the user's entire timesheet, rather than on an issue-by-issue basis.

### Who can edit time once a period is locked?

Editing permissions depend entirely on how the period was locked:

- **Approval-Based Lock (Per User):** Locked for the individual user upon submission or approval. The designated approver or an admin must unlock/reopen the period before the user or manager can make edits.
- **Admin/Global Period Lock:** Locked globally for all users across the system (typically for accounting closures). Only a 7pace Admin or Global Manager can lift this lock to allow edits.

### Does 7pace log who approved a timesheet?

**Yes**. 7pace maintains historical data of approvals. The approver's name and the approval timestamp are visible in both the **Approval Periods** view and the **Times Explorer**, and this data can be included in report exports.

### Who receives time submission reminders?

When automated reminders are enabled by an administrator, notification emails are sent to all active users on the Jira site who have accessed 7pace at least once, reminding them to log or submit their time.

- **Troubleshooting:** If a user is not receiving reminders, verify that their Atlassian account email privacy settings are not set to "Private".

## Delegation, Audit, and Calendars

### Can managers log or modify time on behalf of other users?

**Yes**. Users granted administrative or manager roles (e.g., Manager, Global Manager, Administrator) can add, edit, delete, or reassign worklogs for other team members using the **Times Explorer** interface. However, they can still only interact with issues and projects they have native permission to access within Jira.

### Is there an audit trail for worklog changes?

**Yes**. Because 7pace writes directly to Jira, any creations, modifications, or deletions of worklogs are natively recorded within the individual Jira issue's **History** tab.

### Can working days or custom holidays be configured in 7pace?

7pace respects Jira’s global week-start configuration (e.g., starting the week on Sunday vs. Monday). However, it does not support custom local holiday calendars, country-specific non-working days, or individualized user shift calendars out of the box.

### Does 7pace support native overtime tracking?

7pace does not feature built-in overtime calculations or distinct overtime approval paths. A common practice to handle this is configuring a custom 7pace worklog field (e.g., an "Overtime" checkbox or dropdown) allowing users to separate regular hours from overtime hours within their daily entries.

## Reporting, Analytics, and Exports

### How can I view and export time data from 7pace?

The **Times Explorer** serves as the primary reporting engine in 7pace. Users can filter, search, group, and arrange columns to design custom reporting views. Once structured, this data can be exported directly to Excel or CSV formats for external use or billing processing.

### What data fields are included in 7pace exports?

Exports pull all columns currently visible in your customized Times Explorer view. This typically includes:

- Logged Hours & Worklog Dates
- User Names
- Jira Issue Keys & Summaries
- Project Names
- Approver Names & Approval Statuses
- Any active 7pace custom fields (such as billable designations)

### What is the difference between "Time Spent" and "Logged Time"?

- **Time Spent:** This is a cumulative, native Jira field displaying the *total accumulated time* logged by all users over the entire lifespan of a single Jira issue.
- **Logged Time:** This refers to the *individual, discrete worklog entries* created by specific users on specific dates that combine to equal the total Time Spent.

### Are there reports for pending, approved, or rejected timesheets?

**Yes**. Managers can view real-time compliance statuses within the **Approval Periods** dashboard. Additionally, users can use the *Approval Status* and *Approver* columns inside the **Times Explorer** to filter or group data by specific approval lifecycle stages.

### Can I track how many timesheets a specific manager has approved?

**Yes**. By navigating to the **Times Explorer**, you can filter the data by a specific *Approver* and set the *Approval Status* to "Approved". This generates a filterable list that can be tallied or exported.

### How can managers identify users who have not submitted their time?

Managers can monitor submission compliance in two ways:

1. **Approval Periods View:** Under this tab, timesheets are categorized by status, allowing managers to quickly isolate users sitting in the "Not Submitted" category for any given period.
2. **Atlassian Analytics:** If integrated, organizations can utilize Atlassian Analytics dashboards to filter by *Submission Status* and download comprehensive lists of non-submitters.

### Are 7pace custom fields accessible in Atlassian Analytics?

No. Custom fields created natively within 7pace are isolated to the 7pace application ecosystem and do not automatically sync as native data fields within external Atlassian Analytics infrastructure.

## Integrations and Permissions

### Can imported Jira work items be used for time tracking in 7pace?

**Yes**. Work items imported into Jira via CSV files, backup migrations, or external APIs function identically to native Jira issues. As long as they are active and accessible on your Jira site, users can track time against them in 7pace.

### Does Jira Automation interact with 7pace?

**Partially**. Jira Automation can read and update core Jira fields that 7pace interacts with or displays (such as modifying issue statuses or updating native time fields). However, Jira Automation cannot trigger 7pace-specific workflow actions, such as submitting or approving timesheet periods.

### How is access and security controlled in 7pace?

Access relies on a dual-layered permission model:

1. **Jira Security (Data Visibility):** Jira dictates what data a user can see. If a user does not have permission to view a project or issue in Jira, they cannot see it or log time against it in 7pace.
2. **7pace Roles (Feature Actions):** 7pace internal roles (assigned in *7pace Settings -> Role Management*) dictate what functional actions a user can perform, such as submitting timesheets, managing approvals, or running global administrative configurations.

### What Jira permissions are required to log time across different projects?

To successfully track time, a user must possess both **Browse Projects** and **Work on Issues** permissions within the native Jira Permission Scheme for every project they intend to log time against.

### Can administrators restrict who can transition tasks to closed statuses?

**Yes**, but this is managed strictly through native **Jira Workflows**. Project or site administrators can restrict status transitions (like moving an issue to *Done* or *Closed*) to specific project roles, groups, or assignees to prevent premature task closure.

### What permissions are required to become a 7pace Manager?

To review, reject, or approve team timesheets, a user must be assigned either the **Manager**, **Global Manager**, or **Administrator** role within the 7pace Role Management settings. Note that their visibility remains bound by Jira project security; they can only manage time data for Jira projects they have explicit permission to browse.