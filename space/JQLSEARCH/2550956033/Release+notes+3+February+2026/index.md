# Release notes 3 February 2026

**Release date**: February 3, 2026

Our team is pleased to announce the latest release of JQL Search Extensions for Jira Cloud.

---

## New features

## New JQL function

### **linkedIssuesOfQueryRecursive() function**

For a given JQL subquery (content in parentheses), this new function finds work items linked to the resulting work items, and those recursively linked to those, up to a defined depth, or until no additional linked items remain. See [Issue links](/cms_trial/space/JQLSEARCH/604209269/Issue+links/) for more information and examples.

To preserve system performance, the `linkedIssuesOfQueryRecursive()` function is available to use only after the initial indexing process completes.

## **Admin tool for AI Search**

Jira Administrators can now control access to the AI natural language search in JQL Search Extensions for Jira Cloud. This helps organizations review or maintain compliance with their AI policies.  
To turn the AI Search feature on or off, click **Admin tools** on the *Extended Search* page, then select the **AI Search** checkbox as required. AI Search is available to users by default.

![JSE-Admin-tools-checkbox.png](/cms_trial/assets/d0e8607b-bb5e-4142-96f0-ef50420f3e48.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers. You are the driving force behind our software, and we appreciate your trust in JQL Search Extensions!

|  |  |
| --- | --- |
| **Release date** | February 3, 2026 |
| **Highlights** | - New recursive function - AI Search admin tool |