# 3.2.19 Release notes

**Release date**: May 1, 2026

This page outlines the updates included in the latest release of Power Scripts for Jira Cloud.

---

## Enhancements

## Improved functions for retrieving email addresses

The following functions now make it easier to retrieve email addresses:

- *getUser* - The function includes a new optional parameter,`forceIncludeEmail` (boolean). When set to true, the result includes the user email.
- *getUserByFullName* - The function includes a new optional parameter, `forceIncludeEmail` (boolean). When set to `true`, the result includes the user email.
- *getUserByEmail* - Now returns the user’s email in the result.
- *userEmailAddress* - Returns the user’s email address.

We've improved how Power Scripts retrieves user profile data, including email addresses. Previously, functions such as `userEmailAddress()`, `getUser()`, `getUserByEmail()`, and `getUserByFullName()` could return user records with missing email addresses. These functions now handle email retrieval and missing profile data more reliably, ensuring that user email addresses are quickly returned when available and that accounts with incomplete profile data no longer cause errors.

---

## Bug fixes

The following bugs are fixed in this release:

- Resolved an issue where users encountered a 403 error from the `autotransition` function when the add-on tries to impersonate itself using `asUser.`
- Resolved an issue where the `originalEstimate` function could not be set using SIL scripts if the field was not previously set from the issue.
- Resolved an issue where the `createIssue` function does not set the due date field.
- Resolved an issue where the user receives an error message in the SIL debugger: `Can't start the debug. Another session might be in progress`, even without a previous session active.
- Resolved an issue where copying an ADF field containing a hyperlink fails and shows a `ERROR parsing document` message.
- Resolved an issue where an ADF parsing error appears only when a cell is empty.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews). [unmapped inline: placeholder]

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!