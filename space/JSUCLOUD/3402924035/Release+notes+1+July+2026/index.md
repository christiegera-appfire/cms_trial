# Release notes 1 July 2026

**Release date**: July 1, 2026

This release includes updates to JSU Automation Suite for Jira Workflows.

This release note covers JSU Cloud version `8.3.0` and includes the cumulative updates from versions `8.1.0`, `8.2.0`, and `8.3.0`.

---

## Improvements

The following improvements are available in this release:

### Improved JCMA migration handling

JSU includes migration handling improvements for Jira Cloud Migration Assistant. These updates help make migrations from Data Center to Cloud more reliable when workflow rule configurations include migration preconditions.

### Atlassian platform compatibility updates

JSU includes compatibility updates for upcoming Atlassian workflow and Jira Software API changes. These updates help maintain reliable rule behavior as Atlassian updates workflow and issue-search APIs.

### Improved error logging

JSU includes improved error logging to help diagnose configuration and execution issues more effectively.

---

## Bug fixes

The following fixes are included in this release:

- **Create a Linked Issue:** Fixed an issue where the Assignee field could not be set in the Copy/Set fields section of the [Create a Linked Issue post function](https://support.appfire.com/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function).
- **Create a Linked Issue:** Fixed an issue where the issue type did not appear in the configuration summary and some settings could return to their default values when the post function configuration was reopened.
- **Create a Linked Issue:** Fixed an issue with the subfunction dropdown in the post function configuration.
- **Calculated fields:** Fixed an issue where some UI elements could overflow outside the configuration container.
- **Assignee handling:** Fixed an issue where issue assignee settings could interfere with assignee configuration in a subfunction.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JSU!