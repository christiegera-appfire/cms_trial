# REST APIs

JQL Search Extensions doesn’t offer any REST endpoints, but all the additional JQL keywords and functions are available through the search REST API.

You can use them in your scripts as you would use native JQL. For example, this REST API call to Jira works correctly if JQL Search Extensions is installed:

`/rest/api/2/search/jql?jql=linksCount>2`