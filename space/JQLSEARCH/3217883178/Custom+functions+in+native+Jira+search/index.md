# Custom functions in native Jira search

JQL Search Extensions (JSE) integrates directly with Jira's native advanced search interface. You can use JSE custom functions directly in the native Jira search bar.

The app automatically translates these custom functions into a format Jira understands, allowing you to use JSE's extended search power without leaving the standard Jira search context.

![custom-functions-adv-search.png](/cms_trial/assets/072a749e-03d6-429e-97b6-25bbc092a11d.png)

### Syncing and filters

Saved filters are automatically synchronized every 10 minutes. This ensures that your search results remain accurate as your Jira data changes.

### Complex queries and timeouts

Jira has a native wait limit of 25 seconds for search responses. If a complex custom function exceeds this limit, you’ll see the following error message:

`Processing the query exceeded Jira wait limits. We're still processing your query in the background. Click 'Search' again in a few seconds to view the results.`

If this happens, Jira continues to process your query in the background. Wait a few moments and then click **Search** again to view your results.