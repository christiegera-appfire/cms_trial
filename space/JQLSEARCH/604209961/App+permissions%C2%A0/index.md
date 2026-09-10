# App permissions 

If the search results are different from your expectations (e.g., no subtasks found, although there are some), this is usually due to problems with permission configuration.

To perform correctly, the app must have **Browse Project** and **Edit Issues** permissions for all projects searched.

## Identify access problems

If you see that the indexing progress bar has stalled, you can identify the problematic issues.

Run this query in Jira Advanced Search to find all issues that are not indexed:

`issue.property["jql-search-extensions"].addonVersion.version is empty`

The results should identify projects with incorrect permissions schemes. Proceed with the fixes to the schemes documented in the next section. After completing all the project fixes, contact [our support team](https://appf.re/support) to arrange reindexing.

The above query may be slow on large Jira instances. If you’re getting errors:

- make sure you run the query in Jira’s advanced search and not inside the app
- retry the search a few times, and each time, make sure you wait for a few minutes until you retry

### Project permission scheme

Find the permission scheme associated with the projects where the app isn't working correctly (there can be multiple permission schemes to fix for multiple projects).

- **Project → Project settings → Permissions**

Ensure that the project role `atlassian-addons-project-access`is there. If not, grant **Browse Projects**and **Edit Issue** to this project role.

![contentId-604209961](/cms_trial/assets/697f74ac-583c-4753-9615-642644836600.png)![contentId-604209961](/cms_trial/assets/777fa44b-26e1-4e1d-9da2-ece215f14211.png)