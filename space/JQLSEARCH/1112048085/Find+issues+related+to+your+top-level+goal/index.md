# Find issues related to your top-level goal

## Summary

You want to identify issues related to your key OKR or Initiative and monitor their status.

You can use JQL Search Extensions Jira hierarchy functions to build filters for the dashboard you use to monitor issues.

## Step 1: Create the filters with JQL queries

1. To open the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page, go to **Apps** > **JQL Search Extensions**.
2. To see all issues supporting your OKR, enter a query using the childrenofIssuesInQueryRecursive function, then click **Search**.

   ```sql
   issue in childrenOfIssuesInQueryRecursive("project='My project' and type=Epic and labels='OKR-H2-2024'")
   ```
3. Click **Save the query as a filter**.
4. Enter a filter name, for example, `Issues supporting H2 OKRs`, then click **Save**.
5. To identify the blockers of issues supporting your OKRs, create a new filter to look for all issues blocking your project with the query:

   ```none
    issue in linkedIssuesOfQuery("project='My project'", "is blocked by")
   ```
6. Click **Save the query as a filter**.
7. Enter a filter name, for example, `Blockers of project MyProject`, then click **Save**.
8. Use this filter in a new query: `filter='Blockers of project MyProject' and labels='OKR-H2-2024'` to see which blockers relate to your OKRs.
9. Click **Save the query as a filter**.
10. Enter a filter name, for example, `Issues blocking My Project OKRs`, then click **Save**.

## Step 2: Add the filter data to your dashboard

1. Go to **Dashboards** > **My Dashboard** (or your chosen dashboard to monitor issues).
2. Add the **Issue Statistics** gadget and select `Issues supporting H2 OKRs` from the list of available filters.
3. Click Save. The status of all the issues supporting your H2 OKRs displays.
4. Add the other filter data as required.

## Interactive walkthrough

Follow the interactive demo to see how to recreate the use case in the app.

*Interactive demo of the use case described on this page.*