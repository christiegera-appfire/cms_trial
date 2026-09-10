# Extended Search filters

## What are Extended Search Filters

Extended Search filters let you save and reuse advanced JQL queries across Jira and other supported apps. In JQL Search Extensions for Jira, you can create Extended Search filters to simplify complex issue searches, share reusable queries, and use the same filter in dashboards, reports, automation rules, and integrations. This page explains how to create, manage, sync, share, and use Extended Search filters in Jira.

| **Extended Search filters page** | **Jira filters list including Extended Search filters** |
| --- | --- |
| Extended Search filters page showing saved filter names, owners, and sync status. | Jira filters list displaying Extended Search filters alongside standard Jira filters. |

There are important differences to remember when managing filter permissions and editing filter names and queries. The following sections explain where to perform specific actions.

## Create an Extended Search filter

1. On the *Extended Search* page, run a JQL query.
2. Once the search results are displayed, click **Save the query as a filter**.

   ![Extended Search results page with the Save query as a filter button highlighted.](/cms_trial/assets/ed112bdc-32fc-4187-bb8b-f86b83bce9c5.png)
3. In the *Save query as a filter* window, enter a filter name, then click **Save**. Filter names should be unique.

   ![Save query as a filter window showing the filter name field and Save button.](/cms_trial/assets/21734514-8984-471d-bd8d-ee4a1e44da69.png)

   You can now search with your filter in Jira search and everywhere else, for example, `filter="All child levels - all projects"`.

Filters are shared with other authenticated users by default. You can make it private or share it with more people in Jira [filter permissions management](https://support.atlassian.com/jira-cloud-administration/docs/manage-shared-filters/).

## Use Extended Search filters in JQL queries

You can apply an Extended Search filter to a JQL query in Jira, Extended Search, and in other applications using the following expression:

`filter="YOUR FILTER NAME"`

### Extend other apps

Saved Extended Search filters can be used in other apps for more refined issue searches. For example, you can use an Extended Search filter to set the scope for post functions in JSU Automation Suite for Jira Workflows and in JMWE to set the scope for event-based and scheduled actions. See [App integrations](/cms_trial/space/JQLSEARCH/1120043993/App+integrations/) to learn more about how you can use filters in other Appfire apps, Jira, and third-party solutions.

### Use filters in reports and dashboards

You can use your Extended Search filters in your Jira dashboard gadgets for more precise reporting. See our [use cases](/cms_trial/space/JQLSEARCH/604209757/Use+cases/) to learn how.

## Manage Extended Search filters

The *Extended Search filters* page displays the details of your saved Extended Search filters. If you have several filters, you can search by filter name and owner.

**To view the Extended Search filters page:**

1. Go to **Apps** > **JQL Search Extensions**.
2. In the left sidebar, select **Extended Search filters**. The list of Extended Search filters displays.

From the *Actions* menu, you can:

- Open the filter in Jira search,
- Manually sync the filter,
- Edit the filter JQL,
- Edit the filter name, and
- Delete a filter.

Editing or deleting an Extended Search filter should always be done from the *Extended Search filters* page, not directly in Jira.

![Extended Search results page with the Actions button for the My Links Count Filter Name highlighted and opened.](/cms_trial/assets/2cee0f3e-1aa6-411c-bf91-f03eca69b899.png)

### Sync a filter manually

Filters that you regularly use are automatically indexed (**synced**) every few minutes. If you do not use a filter for 7 days or more, it won’t be synced automatically.

If several filters are used across your instance, you can prioritize a sync to ensure critical filters are up to date when needed. The *Last Reindexed* column shows the time of the last sync and the no sync status of filters that are not included in the automatic sync process.

![Screenshot of the Extended Search filters page with the no sync status highlighted.](/cms_trial/assets/95abaeb5-a299-4f08-8da2-55b510e8edf7.png)

**To perform a manual sync:**

1. Go to the *Extended Search filters* page and locate the required filter.
2. In the *Actions* column, click the **More options …** icon, then select **Sync filter** from the list of actions. A status message displays.
3. Once the sync is complete, click **Confirm**. Do not close the web page during a manual sync.

### Edit a filter query

**To edit a filter query:**

1. Go to the *Extended Search filters* page and locate the required filter.
2. In the *Actions* column, click the **More options …** icon, then select **Edit query**.
3. Enter a new query and click the **Search** icon.
4. Click **Save**.The edited filter appears on the *Extended Search filters* page.

### Rename a filter

If you change the filter name, you need to update all references to the filter name in your Jira JQL queries and any third-party apps. Filter names should be unique.

**To change a filter name:**

1. Go to the *Extended Search filters* page and locate the required filter.
2. In the *Actions* column, click the **More options** icon, then select **Edit name**.
3. Enter a new filter name, then click **Save**.

### Delete a filter

Do not delete filters directly in Jira. Always do it in the *Extended search filters* page.

**To delete a filter:**

1. Go to the *Extended Search filters* page and locate the required filter.
2. In the *Actions* column, click the **More options** icon, then select **Delete**.
3. Click **Delete** to proceed.

Filters are normally deleted in Jira during this process. If the filter was deleted in Jira before being deleted in JQL Search Extensions, you can still delete it from a list.

## Filter owners

Admins can change the owner of shared filters in Jira. Once the owner is changed in Jira, you should wait a few minutes for JQL Search Extensions to detect the change. If the filter's owner changes, it is removed from the current user's filter list but not from the system. The new owner can use the filter.

**To change a filter owner:**

1. From the top navigation bar in Jira, select **Filters** > **View all filters** and locate the required filter.
2. Select the **More options** icon, then select **Change owner** from the list of options.
3. Select a new owner, then click **Change owner**.

   ![Filters page with the Filters tab highlighted and the Change Owner dialog opened.](/cms_trial/assets/a6ddccee-e6d0-4dd3-ade3-77395d6b1af8.png)

You can’t reverse a change to the filter owner. Only the new owner can make changes to the permissions.

## Share filters

Extended Search filters are shared with other authenticated Jira users by default.

**To change the filter permissions:**

1. From the top navigation bar in Jira, select **Filters** > **View all filters** and locate the required filter.
2. Select the **More options** icon, then select **Edit** from the list of options.
3. Under *Viewers* or *Editors*, select the desired permissions, then click **Add**. You can give edit permissions to groups or individual users. Learn more about [sharing Jira filters](https://support.atlassian.com/jira-software-cloud/docs/save-your-search-as-a-filter/#Savingyoursearchasafilter-sharing_filtersShareafilter) in Atlassian’s documentation.
4. Once you have made all the required changes, click **Save**.

   ![Edit filter dialog opened with the Viewers field highlighted and the My organization option selected.](/cms_trial/assets/dc956faa-2d4e-468f-8117-a9753ba46140.png)

## Limitations

Note the following limitations to Extended Search filters:

- currentUser(), votedIssues(), watchedIssues() always use the filter owner user session and evaluate the filter owner user.
- If you haven't used a filter for seven days or more, it won’t be synced automatically. You can perform a manual sync to refresh your filter data anytime. Refer to the *Extended Search filters* page to confirm the last time your filters were synced correctly.

Do not edit the JQL of a filter directly in Jira. The JQL is overwritten periodically by our sync service.