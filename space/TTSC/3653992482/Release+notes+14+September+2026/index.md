# Release notes 14 September 2026

**Release date**: September 14, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Introducing Workflow Intelligence reports

You can now use **Workflow Intelligence** to see how work moves through your workflow and understand where time is being spent.

Instead of looking only at aggregated results, Workflow Intelligence lets you analyze duration data at the individual work item level and break it down by fields such as assignee, status, priority, or time period.

Watch the video below to get a quick overview:

Image — asset pipeline pending  
Time to SLA - Workflow Intelligence.mp4

#### What’s new

With Workflow Intelligence, you can:

- Start quickly with report templates or create a report from scratch.
- Choose how to analyze your data using main and sub-columns. For example, view time by assignee and break it down further by status.
- Merge related values into a single column. For example, combine several completed statuses into Done.
- Summarize your results to surface work time distribution, average elapsed time, and other insights based on your report configuration.
- Include SLA data to review compliance, breaches, SLAs in progress, and detailed SLA running time.
- Expand individual work items to see either an SLA breakdown or workflow breakdown and understand exactly where their time was spent.
- Customize the report display with duration formats and cell-coloring thresholds.
- Save and organize reports into personal folders so they’re easier to find later.

You can also open the most impacted work items from an **Executive report** directly in Workflow Intelligence when you want to investigate a result in more detail.

To try it, go to **Reports** > **Workflow Intelligence** and create your first report.

Learn more about [**Workflow Intelligence reports**](/cms_trial/space/TTSC/3637936320/Workflow+Intelligence+report/).

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where resetting an SLA could fail with a **“Remote could not verify the Forge Invocation Token”** error because of incorrect Administration permission handling.
- Fixed an issue in JCMA migrations where SLA contexts retained their Data Center SLA IDs instead of using the newly generated Cloud IDs. This could prevent users from editing the SLA panel after migration.
- Fixed an issue where changing the configuration of a disabled SLA could unintentionally enable it.
- Fixed an issue where an already executed, non-recurring SLA started action could run again if SLA recalculation occurred shortly after the SLA started. This could overwrite the result of a later SLA met action and leave related custom fields out of sync with the SLA’s current state.
- Fixed an issue where SLA report date filters were incorrectly passed as the end date in REST calls. This affected all report types except the Executive report.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!