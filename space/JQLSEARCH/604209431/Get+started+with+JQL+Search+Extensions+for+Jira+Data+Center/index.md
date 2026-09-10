# Get started with JQL Search Extensions for Jira Data Center

To get started with JQL Search Extensions for Jira Data Center (JSE):

1. Install the latest version of JQL Search Extensions for Jira Data Center.
2. In Jira, go to [Advanced Search](/cms_trial/space/JQLSEARCH/604209431/Get+started+with+JQL+Search+Extensions+for+Jira+Data+Center/).
3. Start typing the JQL query: `issue in`.
4. Jira autocompletes your query, and you can choose the required function. For example, you can run the query `issue in linksCountGreaterThan(2)`.

See the full list of JQL functions in the JQL functions [reference documentation](https://appfire.atlassian.net/l/cp/CDfkTFku).

You must start your queries with `issue in` to use the functions.

## Install JSE for Jira Data Center

1. Log in to your instance of **Jira** as an administrator.
2. Select **Settings** > **Manage Apps**.
3. Select **Find new apps** from the left sidebar menu.
4. On the *Find new apps* page, use the search bar to find the version JQL Search Extensions for Jira that you need.
5. Click **Free trial** to start the trial or **Buy now** to purchase a license.
6. Click **Accept and install** on the confirmation page.
7. You’ll be prompted to log in to your MyAtlassian account.
8. Enter your credentials and click **Generate license**.
9. Once the license key is generated, select **Apply license** to get started with the app. If you're using an older version of UPM, you can copy and paste the license into your Jira instance.

If required, can also find the older versions of **JQL Search Extensions for Jira** compatible with your instance on the [version history page](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira/version-history?versionHistoryHosting=dataCenter) on our Marketplace listing.

## Enter a query in Advanced search in Jira

1. In the top navigation bar in Jira, select **Issues** > **Search for issues**. The JQL Advanced search page displays.
2. Enter `issue in` followed by the JSE function that you want to use, for example, `commentsCountGreaterThan("4")` to find issues that have more than four comments.

**See an example in the interactive walkthrough:**