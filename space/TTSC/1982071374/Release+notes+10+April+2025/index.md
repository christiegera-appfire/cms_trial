# Release notes 10 April 2025

**Release date**: April 10, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Switched to new Jira JQL API

Updated our internal JQL handling to use Atlassian’s new endpoints for retrieving issues and their counts via JQL. There are no visible changes for end users, but these updates ensure future compatibility and improved backend performance.

### Public REST API pagination update

The `/api/issue-sla` endpoint now supports pagination using `nextStart` and accepts the `start` parameter as a **string** instead of a number. This change aligns with Atlassian's updated pagination model, which replaces `startAt` with page tokens.

---

## Bug fixes

The following bugs are fixed in this release:

- Resolved a responsive design bug on the *Where is my SLA?* screen. The layout now displays correctly on all screen sizes.
- Enhanced the efficiency and reliability of the bulk event processor for smoother SLA updates and better performance under high load.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---