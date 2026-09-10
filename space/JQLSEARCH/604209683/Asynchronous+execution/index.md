# Asynchronous execution

In Jira Server, the search queries are executed in the same Java Virtual Machine (JVM) as Jira. On a cloud hosting, the JQL Search Extensions service is a separate deployment communicating with Jira over the REST API. As a result, all operations in Jira Cloud are indexed asynchronously, and any changes in Jira are reflected in the JQL with a slight delay.

Filters are indexed periodically through the automatic sync process. If a filter hasn’t been used for 7 days or more, it won’t be included in the automatic sync. The sync status is displayed on the Extended Search filters page.

You can run a [manual sync](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) for any of your saved Extended Search filters to prioritize syncing and ensure your most critical filters are current. See [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) to learn more about filter limitations.