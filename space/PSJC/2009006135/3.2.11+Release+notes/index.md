# 3.2.11 Release notes

**Release date**: May 7, 2025

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud.

This release introduces fixes that improve reliability for email processing workflows and ensure proper synchronization with Atlassian products.

---

## Bug fixes

### Fixed IMAP email body retrieval

- Resolved an issue where the email body was not being properly retrieved when using IMAP for Incoming Mail.
- Users can now successfully access email body content via the `mail.body` property.
- This fix ensures complete email data is available for processing in your scripts.

### Fixed global JQL synchronization

- Resolved a synchronization issue that occurred during global sync operations.
- Updated JQL search handling to comply with Atlassian's new requirement prohibiting empty JQL searches.
- Global synchronization (without specific project or project category filters) now works correctly.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!

---