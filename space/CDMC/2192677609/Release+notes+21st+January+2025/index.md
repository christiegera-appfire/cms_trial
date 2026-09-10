# Release notes 21st January 2025

**Release date**: January 21, 2025

Our team is thrilled to announce the latest releases of Comala Document Management Cloud.

---

## Bug fixes

The following issues are fixed in this release:

- resolved a problem where the [send-email trigger action](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/614012300) did not send emails when a Confluence user was added as a recipient using the **user** parameter

This issue occurred when specifying recipients for the **send-email** action using the `“user":` parameter in the [code editor](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/1466237019) or the **Use**r option in the **Add Actio**n dialog box in the [visual editor](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/614010813). It caused inconsistencies in identifying or delivering emails to the intended recipients.

- fixed an issue where multiple approvals in a state were not displayed in the order specified in the [document approvals macro](https://appfire.atlassian.net/wiki/spaces/CDMCD/pages/614012920)

Multiple approvals added to a workflow state are displayed in the macro by default in alphabetical order. However, the document approvals macro can be configured to display the approvals in the state in a different sequence.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Are you stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually.

You are the driving force behind why we create software. We appreciate your trust in Appfire Comala Document Management Cloud.