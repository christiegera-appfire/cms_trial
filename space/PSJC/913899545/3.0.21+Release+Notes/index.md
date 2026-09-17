# 3.0.21 Release Notes

**Release date**: April 17, 2024

Our team is excited to announce the 3.0.21 release of Power Scripts for Jira Cloud.

---

## New features

- Implemented new performance improvements
- Introduced **Scripted Custom Fields**: New custom fields that return values using JavaScript to calculate their output. Your JavaScript can access the values in other fields and Jira APIs. Scripted fields can also be created with dependencies, triggering automatic recalculations if those fields are updated
- Updated support for the execution of large updates and refreshing issues to help with asynchronous updates from other add-ons

---

## Enhancements

- Added the following new routines:

  - New field configuration management routines
  - addSilPostfunction: Supports the installation of some example workflows
  - issueExists
  - getCustomersObjects: Returns **JUser[ ]**
  - refreshIssue(key)
  - saveModifiedIssues()
  - getIssueEntityPropertyKeys(key): New issue entity properties routine
- Enhanced the security headers

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed a bug with getWorklogsForIssuesperforming differently on Power Scripts for Jira Cloud versus Jira Server
- Fixed a bug with a bad escape sequence when working with inline URLs.
- Fixed a Non-Person Entity (NPE) in userRoles

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview&hosting=cloud).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Power Scripts for Jira Cloud!