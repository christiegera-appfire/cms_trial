# Release notes 17 February 2026

**Release date**: February 17, 2026

Our team is pleased to announce the latest release of JQL Search Extensions for Jira Cloud.

---

## New features

## childrenCount keyword

The `childrenCount` keyword helps you find work items that have a specified number of children or none. childrenCount=0, for example, can help you identify epics for which no stories have been created. The keyword uses Jira’s child-parent hierarchy and custom hierarchies to return the count of children at the next level.  
See [Issue hierarchy](/cms_trial/space/JQLSEARCH/604209353/Issue+hierarchy/) for more information and examples.

## userMentionedInComment keyword

The `userMentionedInComment` keyword helps you find work items that mention a specified user in a comment. See [Comments](/cms_trial/space/JQLSEARCH/604209943/Comments/) for more information and examples.

## userMentionedInLastComment keyword

The `userMentionedInLastComment` keyword helps you find work items that mention a specified user in the latest comment. See [Comments](/cms_trial/space/JQLSEARCH/604209943/Comments/) for more information and examples.

---

## Bug fix

The following fix is included in this release summary:

### commentLastCreatedby and commentLastUpdatedby fields

- Resolved an issue where the `commentLastCreatedBy` and `commentLastUpdatedBy` fields returned issues with no comments and issues where the current user made the last comment. Now, if the query excludes the current user or issues without comments, these fields return the correct results.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers. You are the driving force behind our software, and we appreciate your trust in JQL Search Extensions!