# Release notes 20 October 2026

**Release date**: October 20, 2026

This page outlines the updates included in the latest release of Connector for Salesforce & Jira Cloud.

**Marketplace version:** 29.9.0

**Salesforce version:** 4.83

---

## Enhancement

### JIRA CLOUD **Field mappings are optional again**

You can once again create and save an entity mapping (for example, Jira Task → Salesforce Case) without adding any field mappings.

Recent versions required at least one field mapping per entity mapping. This requirement has been removed, so a binding that contains an entity mapping with no fields no longer blocks saving other changes to that binding.

Note that an entity mapping without field mappings only associates records and doesn't sync any values, so add field mappings wherever you want data to flow between Jira and Salesforce.

---

## SALESFORCE Bug fixes

- **Jira Issues (Next-gen) component**: When a Case had no associated Jira issues, the empty screen always showed an **Associate / Create** button, even if your admin had turned those actions off. The empty state now follows your configuration, as the component header button already did.

  - Both actions disabled: no button is shown.
  - Associate disabled: Only a **Create** button is shown.
  - Create disabled: Only an **Associate** button is shown, with no option to create a Jira issue.

- SALESFORCE **Create Jira Issue dialog**: We fixed an issue in the Create Jira Issue dialog. If you changed the issue type and clicked **Create** quickly, the Jira issue could be created with field values from the previous issue type’s mapping, which caused the error “Select a valid option for Issue and try again.”

  - **Create** now stays disabled until the fields for the selected type have finished loading, and the issue is always created with the mapping for the selected issue type.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in Connector for Salesforce & Jira Cloud!