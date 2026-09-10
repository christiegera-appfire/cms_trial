# Script types and triggers

Power Scripts for Jira Cloud uses SIL scripts that integrate with specific trigger points in Jira. These trigger points determine when scripts execute in Jira processes, giving you more control over your Jira instance while reducing manual work.

To effectively implement these scripts, you must have a solid understanding of core Jira concepts, such as custom fields, screens, workflows, issue types, and projects.

---

## Hook types and tasks

Scripts run automatically when their hooks are triggered, working seamlessly in the background. Each hook type enables different kinds of tasks. The following table shows the various hook types in Power Scripts for Jira Cloud, their trigger points within the system, descriptions, and example automation tasks that can be performed with each hook type.

| **Hook Type** | **Trigger Point** | **Description** | **Example Tasks** |
| --- | --- | --- | --- |
| Workflow hooks | Workflow transitions - before or after | Scripts triggered during workflow state changes | - Validate transitions - Update fields |
| Issue hooks | When viewing or editing issues | Scripts triggered by issue-related events | - Modify screens - Calculate field values |
| Scheduled hooks | At specified times | Scripts that run according to defined schedules | - Generate reports - Clean up data |
| External hooks | In response to external events | Scripts that connect with external systems | - Integrate with other systems |

---

## Script types reference

The following table outlines the main script types available in Power Scripts, describing what each component does, when it's triggered, and its primary purposes.

| **Script type** | **Description** | **Trigger point** | **Used to** |
| --- | --- | --- | --- |
| **Workflow Conditions/Validators** | Scripts that act as gatekeepers in the workflow process | Before any workflow transition | - Control transition visibility - Enforce user permissions - Implement security rules - Validate data - Prevent unauthorized actions - Prevent unauthorized actions |
| **Workflow Actions (Post Functions)** | Scripts that execute automated actions after a transition completes | After any workflow transition | - Create sub-tasks - Copy parent data - Calculate field values - Push data to databases - Send custom notifications - Perform automated follow-up tasks |
| **Listeners** | Scripts that monitor and respond to various system events across multiple workflows | After workflow transitions and other system events | - Monitor multiple workflows simultaneously - React to non-workflow actions (issue edits) - Respond to system events: new user creation, project creation, version creation, and issue updates. - Provide cross-workflow automation - Enable system-wide monitoring - Execute global automated responses |
| **Scheduled Jobs** | Scripts that run automatically at a specified time interval without user interaction | At defined time intervals (daily, weekly, monthly, or custom schedules) | - Work with issues in bulk - Execute time-based tasks such as:    - Escalate priority of overdue issues   - Auto-assign issues created that day |
| **JQL Keywords** | Prebuilt and custom functions that extend Jira's search capabilities | During JQL query execution | - Enhance Jira's native search functionality - Implement custom search keywords - Enable advanced issue-finding |
| **Prebuilt Service** | Integration scripts that enable two-way communication with external systems | When external systems make or receive calls | - Enable real-time two-way integrations - Process incoming external system calls - Send outgoing REST calls |
| **Webhooks** | Custom URL endpoints for external system communication | When external systems send messages | - Receive messages from external systems - Enable system-to-system integrations | |
| **SIL Runner Gadget** | Dashboard-based tool for custom button actions | On user interaction. For example, clicking a button. | - Create custom UI buttons - Implement simple forms - Enable non-admin access to scripts |
| **SIL Panel** | Scripts that run in a custom section within Jira issues | Within issue view | - Display custom content - Show custom charts/graphs - Present issue-specific information |