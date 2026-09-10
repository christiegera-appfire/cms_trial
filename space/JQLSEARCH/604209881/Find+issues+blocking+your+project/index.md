# Find issues blocking your project

## Summary

Imagine your project is already overdue, and the issues scheduled for the next release depend on issues in multiple projects. Finding and managing these issues can be time-consuming and complicated. With JQL Search Extensions for Jira, you can **easily identify all issues blocking your project**.

## Step 1: Create a new dashboard

1. Go to **Dashboards** > **Create dashboard**.
2. Name the dashboard `Project blockers`, then click **Save**.

## Step 2**:** Create a filter with a JQL query

1. Go to Jira advanced issue search (issue navigator).
2. Enter the JQL query using JQL Search Extensions keywords to find issues blocking your release:

   ```sql
   linkType = blocks AND linkedByIssueProject = SEARCH and linkedIssueStatusCategory != "Done"
   ```
3. Click **Save filter**.
4. Name the filter `Issues blocking search project` then click **Save**.
5. (Optional) You can further narrow this search, with these options:

   1. Try`linkedIssueType = Story` to search for issues that are blockers for stories in your project.
   2. Try `linkedIssuePriority = Blocker` to search for issues that are dependent on blockers in your backlog.
   3. Try adding more keywords: `assignee = unassigned` to identify issues that are being worked on

See all available *Links* keywords in the [JQL functions and keywords reference](/cms_trial/space/JQLSEARCH/604209395/JQL+functions+and+keywords+reference/) page.

## Step 3**:** Present data on the dashboard

Add the following gadgets to the dashboard that you created in Step 1:

- **Filter Results** gadget: use the saved filter: `Issues blocking search project`.
- **Pie Chart** gadget: use the saved filter: `Issues blocking search project` and set statistic type to **Status**.
- **Issue Statistics** gadget: use the saved filter: `Issues blocking search project` and set statistic type to **Project.**
- **Created vs Resolved** gadget, use saved filter: `Issues blocking search project`.

![contentId-604209881](/cms_trial/assets/e5e74cf0-487a-4e61-8830-05edfcdfdc9d.png)

Configured gadgets give you a live insight into how your project depends on other projects, the exact issues that your project depends on, the status of these issues, and whether the dependencies are closed before new ones are created.

## Interactive walkthrough

Follow the interactive demo to see how to recreate the use case in the app.

*Interactive demo of the use case described on this page.*