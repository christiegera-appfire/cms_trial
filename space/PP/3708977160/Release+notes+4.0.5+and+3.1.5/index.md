# Release notes 4.0.5 and 3.1.5

**Release date**: September 29, 2026

Planning Poker for Jira Data Center versions 4.0.5 for Jira 11 and 3.1.5 for Jira 10 include bug fixes and security fixes.

**Jira compatibility**: Jira 11 and Jira 10

---

## Bug fixes

This release includes the following bug fixes:

- Fixed errors when editing and saving numeric custom fields in the **Edit Issue** modal; empty values now clear the field correctly, and non-empty values are sent as numbers.
- Fixed the active issue panel losing issue type, summary, and other Jira metadata after using **Quick Add** or adding a sub-task to the backlog.
- Prevented using **Quick Add** to add an issue that is currently being estimated in an active or discussion round, and added a clear error message for this case.
- Fixed game cloning failing after a Jira project was renamed.
- Updated the finish-game confirmation to show the backlog warning only when there are unfinished issues or an active or discussion round in progress; the warning text now states *All unfinished issues will remain in estimation backlog.*

---

## Security fixes

This release includes the following security fix:

- Upgraded a vulnerable dependency to address known security issues.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=datacenter&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=datacenter&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Planning Poker.