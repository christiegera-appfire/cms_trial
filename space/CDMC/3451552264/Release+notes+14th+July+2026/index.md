# Release notes 14th July 2026

**Release date:** July 14, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**Version:** 5.0.6 & 5.0.7

---

## Bug fixes

- Incomplete label information sent by Confluence no longer causes errors. These events are skipped safely, and valid label changes continue to work as expected.
- The rejection notification no longer appears repeatedly when you open or refresh a page while its workflow is still loading.
- Workflow labels are now validated in the Visual Builder and Code Editor. Uppercase or duplicate labels are blocked, with a clear error message explaining what needs to change. (Labels must be lowercase.)
- Floating messages set by a **Set message** action on an **On expire** trigger now appear correctly once content expires.
- In the Workflow Builder, the user picker for preassigned groups now appears before the editing panel rather than being hidden behind it.
- Users who don’t have access to a space no longer see a workflow error when opening a restricted page. Permission-denied cases are now handled quietly, without flagging errors.
- The Document Approvals macro now correctly displays approval history on migrated pages when set to a past workflow state. Empty states now reference the configured state name.

---

**Questions and Feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!