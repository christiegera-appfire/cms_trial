# Release notes 22nd September 2026

**Release date**: September 22, 2026

This page outlines the updates included in the latest release of Comala Document Management Cloud.

**App version:** 51.1.0

**Release version:** 5.0.30

---

## Enhancements

- Workflow conditions can now use event-payload references such as `@Event.Label@` and `@Event.FileName@`. You can also use dynamic value references as the value a condition compares against, allowing conditions to evaluate values from the triggering event or other workflow context.
- The triggering event is now available in the workflow context during trigger evaluation, giving triggers access to the event that started them.
- Clearer permission-denied message for guest users in the Comala Document Management state dialog.

## Bug fixes

The folowing bugs are fixed in this release:

- The Copy Page action can now be saved when the target page is left empty. Previously, you couldn't add or save the action without specifying a target page.
- Approve and Reject trigger actions on Forge now apply to the intended reviewer, not the logged-in user.
- Workflow definitions that contain an empty transition element no longer prevent pages from transitioning.
- The Space Document Report now displays the correct workflow scope when a space workflow overrides a page workflow.
- The Document Activity macro now exports to PDF successfully. Previously, a missing account identifier caused the export to fail.

### Security updates

- Retrieving workflows from Space Settings now requires space administrator permissions for the applicable space.

### Maintenance and platform updates

- Comala Document Management now includes an Isolated Cloud (IC) compatible manifest and supports manual deployment to Isolated Cloud environments.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire's Comala Document Management Cloud!