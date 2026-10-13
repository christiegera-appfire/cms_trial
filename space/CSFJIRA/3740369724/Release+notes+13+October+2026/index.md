# Release notes 13 October 2026

**Release date**: October 13, 2026

This page outlines the updates included in the latest release of Connector for Salesforce & Jira Cloud.

**Jira Marketplace** **version**: 29.7.0

---

## Jira Cloud Bug fixes

- **Migration fixes**: Fixed a DC to Cloud migration where issue type mappings with no Cloud counterpart kept their DC ID, which could match an unrelated Cloud issue type.  
  Issue type IDs without a Cloud counterpart are now prefixed with `server_id_` during migration. After migrating, you can easily spot these mappings as not migrated and invalid.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Connector for Salesforce & Jira Cloud!