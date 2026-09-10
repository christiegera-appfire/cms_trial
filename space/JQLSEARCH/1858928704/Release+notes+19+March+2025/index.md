# Release notes 19 March 2025

**Release date**: March 19, 2025

Our team is pleased to announce the latest release of JQL Search Extensions for Jira Cloud.

---

## Bug fixes

The following bugs were fixed in this release:

### Saving queries

- Users can no longer save a query that was never run. Previously, a tooltip displayed this restriction, but users could modify and save the query without first running the search.

### Editing filters

- Users can no longer save a modified filter if the query shown in the query field and the executed query do not match. Previously, users could modify a filter while the query was still running and then save it, which caused a mismatch between the query results and the new filter query. When saved, unexpected results or errors could occur.

### Filter updates

- Filters automatically refresh when a user reopens the *Extended Search* page. Previously, they were refreshed only with a full page reload. If a user navigated away from the page, for example, to edit a filter and then returned, the *Extended Search* page showed outdated filters because no new request was triggered.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JQL Search Extensions!