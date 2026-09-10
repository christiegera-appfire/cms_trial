# Release notes 22 April 2026

**Release date**: April 22, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Permissions page updates

We updated the Permissions page by replacing Settings with Administration to match the current section naming and added a new permission option for non-editable SLA Field access.

### Improved SLA notifier performance

We improved the SLA notifier sending architecture to support better performance.

### Added more data to Jira Automation payloads

We added `workingHoursOfWorkingDay` to the payload sent to Jira Automation rules.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where bulk issue property set requests failed for all work items in the array if even one work item was rejected. Now, valid work items can be processed as expected.
- Fixed an issue where the Reset SLA post function was not resetting the SLA correctly.
- Fixed an issue where the SLA panel appeared in the customer portal even when no SLA was configured for the related request type.
- Fixed an issue where scheduled reports could time out due to an out-of-memory problem.
- Fixed an issue in DC to Cloud SLA migration where SLAs with a JQL scope could create a default goal without scope details. Default goals are no longer created for migrated SLAs that use JQL scope in Data Center.
- Fixed an issue where the TTS Duration custom field could inconsistently show elapsed time or remaining time after page refresh.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!