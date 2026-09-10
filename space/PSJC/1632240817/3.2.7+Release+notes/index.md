# 3.2.7 Release notes

![Release Notes.png](/cms_trial/assets/481fbc4a-0c5e-47bf-8f61-4571cdb61827.png)

**Release date**: January 15, 2025

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud.

This release introduces new custom field functions for improved Jira Cloud migrations and fixes a critical Power Scripts migration issue.

---

| **Contents** |
| --- |
| - [Enhancements](#enhancements) - [Introduced new custom field functions to simplify Jira Cloud migrations](#introduced-new-custom-field-functions-to-simplify-jira-cloud-migrations) - [Bug fixes](#bug-fixes) |

---

## Enhancements

### Introduced new custom field functions to simplify Jira Cloud migrations

To better support customers with large migrations to Jira Cloud, we've added several new custom field functions:

- [getCustomFieldIdByName](/cms_trial/space/PSJC/1624965365/getCustomFieldIdByName/): Retrieves the ID of a custom field based on its name.
- [getCustomField](/cms_trial/space/PSJC/1626374145/getCustomField/): Fetches details of a specific custom field using its ID.
- [getAllCustomFields](/cms_trial/space/PSJC/1626898458/getAllCustomFields/): Returns a list of all custom fields available in the Jira instance.

These functions utilize the Jira Cloud platform REST API, making it easier to manage and migrate custom fields programmatically.

---

## Bug fixes

The following bugs are fixed in this release:

- Resolved an issue impacting Power Scripts migrations to Jira Cloud  
  A bug was causing the Power Scripts app to stop unexpectedly midway through the migration process to Jira Cloud, significantly delaying migration projects. The underlying cause has been identified and fixed, allowing Power Scripts migrations to complete as expected.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think here. [unmapped inline: placeholder]

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [unmapped inline: placeholder]!

|  |  |
| --- | --- |
| **Release date** | January 17, 2025 |
| **Highlights** | - New custom field functions to simplify Jira Cloud migrations. - Fixed issue impacting Power Scripts migrations to Jira Cloud. |