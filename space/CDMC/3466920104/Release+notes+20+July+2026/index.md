# Release notes 20 July 2026

**Release date**: July 20, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**Version:** 5.0.10

---

## Bug fixes

The following bugs are fixed in this release:

- **Workflow email recipients**: Fixed an issue where the `@watchers` recipient in send-email triggers resolved to both page and space watchers, causing workflow emails to be sent to the entire space's watchers.

  - The `@watchers` token in send-email triggers now targets page watchers only.
- **Ghost workflow transitions**: Fixed an issue where simply viewing a page in an approval workflow state with an expiry date triggered a ghost "state changed" transition, incorrectly logged in Document Activity, along with a reset expiry date and duplicate approval notifications.

  - Viewing a page no longer re-triggers a state change, and workflow state, expiry, and Document Activity logs stay accurate.
- **Metadata macros**: Fixed an issue where the **Get Metadata** and **Set Metadata** macros intermittently rendered blank or wrong values on page load until refresh.

  - Both macros now show the correct value on first load, with no page refresh required.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!