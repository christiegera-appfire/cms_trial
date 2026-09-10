# 3.2.24 Release notes

**Release date:** July 31, 2026

This page outlines the updates included in the latest release of Power Scripts for Jira Cloud.

---

## Enhancements

The following enhancements are included in this release:

### Added support for the `addWebhookResponseHeader()` SIL function

Power Scripts for Jira Cloud now supports the [addWebhookResponseHeader()](/cms_trial/space/PSJC/434472844/addWebhookResponseHeader/) SIL function, bringing it into parity with the Data Center version.

This resolves an issue where scripts using the function failed with a `Routine not defined` error after moving to Cloud. If you migrate SIL scripts that rely on webhook response headers, they now work without requiring changes or workarounds.

### Improved Jira Cloud Migration Assistant (JCMA) migration handling

Power Scripts now detects and ignores duplicate migration data that may be sent by Atlassian's Jira Cloud Migration Assistant (JCMA) during a migration.

This prevents duplicate Power Scripts data from being created in the destination Cloud instance, reducing the need for manual cleanup when duplicate migration payloads are received.

**Questions and feedback**

- Explore features, pricing, and reviews on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!