# Release notes 27 November 2025

**Release date**: November 27, 2025

Our team is pleased to announce the latest release of JSU Automation Suite for Jira Workflows.

This release note covers JSU Cloud versions 4.4.0 and 4.5.0.

---

## Bug fixes

The following fixes are included in this release summary:

- **Related issue status condition:** Resolved an issue where the condition acted on work items in both directions of the relation type. For example, a condition set to act on work items blocking the work item in transition would also act on work items blocked by that work item. Now the condition applies only to the work items that match the direction of the selected relation.
- **Related issue status validator:** Resolved an issue where the validator didn’t check all the child work items in an epic, allowing the epic to be closed even when only one child was in the Done status. Now the validator ensures that the epic can be closed only when all child work items are in the Done status.
- **Related Issue Status condition and validator:** Resolved an issue where the selected related issue status was not saved for epics.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JSU!