# 7.4.0 Release notes

**Release date:** November 23, 2026

Power Scripts for Jira Cloud 7.4.0 includes bug fixes that improve scripted field calculations, JQL synchronization, and script performance monitoring.

## Bug fixes

This release includes the following fixes:

- **Scripted fields calculate correctly when other fields are unavailable.** Fixed an issue where a scripted field referencing a deleted or unavailable custom field prevented other scripted fields on the same work item from calculating. Other scripted fields now continue to calculate and update correctly, even when one field can't be resolved.
- **Corrected JQL queries for scripted field synchronization.** Fixed an issue where project keys and category values weren't enclosed in quotation marks in generated JQL queries. This caused errors when synchronizing scripted fields for certain projects. JQL queries now use the correct syntax for scripted field synchronization, automatic synchronization, and project reindexing.
- **Improved script execution and performance monitoring.** Fixed issues with the **Kill** button in *Performance Monitoring > SIL Threads* and the **Traces** toggle, which now correctly reflects its enabled or disabled state. The app also enforces the **Async Max Script Runtime** limit and adds warning logs for long-running HTTP requests and large asynchronous queues to help identify potential performance issues.

**Questions and feedback**

- Explore features, pricing, and reviews on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!