# 3.2.20 Release notes

**Release date:** May 15, 2026

This page outlines the updates included in the latest release of Power Scripts for Jira Cloud.

---

## Enhancements

The following enhancements are included in this release:

### Improved custom field options functions

The following functions now accept a context name or context ID as an alternative to the project and issue type mappings when identifying which context to target:

- [admGetCustomFieldOptions](/cms_trial/space/PSJC/791511311/admGetCustomFieldOptions/)
- [admAddCustomFieldOptions](/cms_trial/space/PSJC/791282009/admAddCustomFieldOptions/)
- [admUpdateCustomFieldOptions](/cms_trial/space/PSJC/790528847/admUpdateCustomFieldOptions/)
- [admDeleteCustomFieldOptions](/cms_trial/space/PSJC/790627240/admDeleteCustomFieldOptions/)

Previously, these functions required a `JProjectIssueTypes []` value to identify the context, which combines projects with arrays of issue types. This approach did not work for contexts scoped to a project but configured to apply to all issue types, since there was no way to represent "all issue types" in the required format. You can now achieve this by using an empty array of issue types.

Example: a custom field context applies to a project with no issue type restriction. Previously, passing an empty array for issue types returned an error. Now this is fixed but you can also identify the context by name instead:

```javascript
admUpdateCustomFieldOptions("My Select Field", updatedOptions, "ACME Project Context");
```

Passing the context name is also more readable and resilient: if project keys or issue type configurations change, scripts that reference the context by name continue to work without modification.

---

**Questions and feedback**

- Explore features, pricing, and reviews on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!