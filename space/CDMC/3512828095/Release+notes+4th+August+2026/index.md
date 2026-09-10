# Release notes 4th August 2026

**Release date**: August 4, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**Version:** 5.0.19

---

## Bug fixes

- CQL queries by approver no longer fail with an HTTP 400 error. The search alias is now registered, and approver data is indexed correctly.
- The Document State macro now resolves the page’s actual space from Confluence before looking up the workflow. This corrects issues where an incorrect `spaceId` from Forge could apply the wrong workflow and cause unexpected state resets.

## Migration improvements

This release includes stability and security improvements to space settings and workflow management.

- Workflow toggles now include accessible names, improving support for screen readers.
- Background job data now excludes user display names, improving data privacy.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!