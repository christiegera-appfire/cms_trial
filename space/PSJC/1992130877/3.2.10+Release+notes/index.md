# 3.2.10 Release notes

**Release date**: March 30, 2025

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud.

This release includes enhanced compatibility with Atlassian's new JQL search REST endpoints and introduces the new getStatusCategory() function to aid Jira DC to Cloud migrations.

---

## Enhancements

### Moved to Atlassian's new JQL search REST endpoints

This change was necessary as Atlassian is deprecating the old REST endpoints ([CHANGE-2046](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-2046)). The move ensures continued compatibility with Atlassian's evolving API infrastructure and maintains the reliability of JQL-based searches within our application.

This update changes how recent issue updates appear in search results. You might notice that recent changes aren't immediately reflected in searches. For cases requiring immediate read-after-write consistency, the new API offers the `reconcileIssues` parameter, which accepts up to a maximum of 50 issue IDs and ensures these specific issues display their latest updates in the results. This helps maintain data consistency for operations where current information is critical.

If you experience issues with search result consistency after this update, see Atlassian's documentation on the [JQL Search API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-search/#api-rest-api-3-search-jql-post) for more information about the behavior of the new endpoints and how to use the `reconcileIssues` parameter to address consistency concerns.

### Implemented a new function: getStatusCategory()

We've added a new [getStatusCategory()](/cms_trial/space/PSJC/1986232329/getStatusCategory/) function to help customers migrating from Jira DC to Jira Cloud. This enhancement addresses a specific gap for customers transitioning their SIL Listeners between environments — certain trigger events available in Jira DC are not directly available in Jira Cloud.

The new `getStatusCategory()` function provides a workaround by allowing scripts to check an issue's status category, enabling customers to implement equivalent functionality in their Cloud environment. This helps maintain continuity in workflow automation during migration and ensures that critical business processes dependent on these status transitions can continue to function properly in Jira Cloud.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!

---