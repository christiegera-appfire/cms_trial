# Release notes 11 August 2026

**Release date**: August 11, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Updated job processor API permissions

We’ve updated authorization checks for the job processor API so permissions are now enforced based on the task type.

- **Export:** Non-admin users with the appropriate Import/Export permission can now use export functionality. Previously, the API incorrectly rejected these users.
- **Import:** Users with access to the Import/Export page can continue to use import functionality.

Because Import/Export permissons were previously not enforced as intended, we recommend that administrators **review existing Import/Export grants** and make sure they are assigned to the right users.

We’ve also tightened access to the SLA recalculation REST API. API tokens that have only the **SLA Configurations** permission can no longer access: `GET /api/sla-recalculation/{jobId}` and `POST /api/sla-recalculation/{jobId}`.

---

## Bug fixes

The following bugs are fixed in this release:

- When an unsupported action ("Fire an Event") is created in Cloud through JCMA, the action page goes blank when editing any notification. Going forward, unsupported actions will no longer be created in Cloud.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!