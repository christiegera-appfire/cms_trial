# Save and reuse an extended search

Save a JQL Search Extensions query as a reusable Jira filter, then use it in dashboard gadgets and reports. For example, save a search for work items linked to epics and return to it during dependency reviews instead of rebuilding the query.

## Save a search

Use the following steps to save a query.

1. Go to **Apps** > **JQL Search Extensions**.
2. Open **Extended Search**.
3. On the *Classic JQL* tab, enter this query or an extended query of your own:

   ```text
   issue in linkedIssuesOfQuery("type = Epic")
   ```
4. Run the search and verify that it returns the work items you expect. If it returns no results, use an extended query that matches work in your Jira instance.
5. Select **Save as filter**.
6. Enter a unique filter name, such as `Work linked to epics`, then select **Save**.

Your saved filter is available on the *Extended Search filters* page and in Jira's filters list.

## View your Extended Search filters

To reopen the filter you saved from Extended Search:

1. Go to **Apps** > **JQL Search Extensions**.
2. In the sidebar, select **Extended Search filters**.
3. Find `Work linked to epics`, or the name you used for your filter.
4. Use the filter's **Actions** menu to open it in Jira search.

The Extended Search filters list provides access to your saved filters and their management actions.

![2026-09-18_22-40-04.png](/cms_trial/assets/3d9bcc8c-a4c3-4065-bb10-01d78a3d5755.png)

You can also open **Filters** > **View all filters** in Jira and select your saved filter.

![Issue_Filters_in_Jira.jpeg](/cms_trial/assets/7002bcdc-4262-4495-a30b-91e952b454bf.jpeg)

### Reference the filter in JQL

In Jira's advanced search, run the following query to reuse the saved Extended Search filter. Replace the filter name if you used a different one.

```text
filter = "Work linked to epics"
```

You can now return to the search without re-entering the extended query.

## Try JQL Search Extensions

To evaluate the app, open the [JQL Search Extensions for Jira Cloud Marketplace listing](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview) and select **Try it free**. Follow [Install and prepare JQL Search Extensions](https://support.appfire.com/space/JQLSEARCH/3677651309/Install+and+prepare+JQL+Search+Extensions) before testing your search.