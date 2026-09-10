# Release notes 27th August 2026

**Release date**: August 27, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 50.19.0

**Release version:** 5.0.26

---

## Enhancements

### Clearer Document Activity for state resets

Document Activity now identifies state reset events. Reset entries read *Changed state from [X] to [Y] (state reset)*, so it’s easy to see when a state was reset.

---

## Bug fixes

- Guest users attempting to approve a document in the Forge app now see a clear message explaining they don’t currently have permission, instead of an unexpected error. Approving documents as a guest user isn’t supported in the Forge app yet, and we’re working with Atlassian to enable it in a future release.
- The workflow state panel no longer shows the wrong workflow or a stale approval state after changes to the space workflow, label, or enablement. Revisiting a page now reflects the correct state.
- Fixed an issue where content did not move to its configured target state when the expiration date was reached. State expiration now transitions content as expected.
- E-signature Token Administration and state dialog setup no longer fail with *Authentication Required* or email lookup errors.
- Reviewers with view-only page access can now approve or reject a document from the state dialog without encountering an error.

---

## Performance improvements

Improved page load performance by streamlining how the app retrieves real-time updates for content state, permissions, and restrictions.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!