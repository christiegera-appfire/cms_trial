# How do I fix "This Visualforce page is deprecated in favor of a new and much improved JiraIssuesCasePage"?

## Answer:

Upon upgrading the Salesforce package from version 1.3 or older, the **JIRA Issues Page** (OverviewPanel) may display the info message. This is due to a deliberate change in the package which requires Salesforce administrators to update to a new Visualforce page available in version 1.4 and newer.

To use the new Visualforce page:

1. Edit the page layout.
2. Remove the **JIRA Issues Page** (OverviewPanel) from the layout.
3. Under the **Case Layout** panel, scroll through until you find **Visualforce Pages**.

   ![contentId-3103916040](/cms_trial/assets/8c2fea7f-7395-4bc4-bc51-66266d858386.png?version=1&modificationDate=1678795520149&cacheVersion=1&api=v2)
4. Now click *and* drag **JIRA Issues** to desired location.
5. Then, click **Save**.