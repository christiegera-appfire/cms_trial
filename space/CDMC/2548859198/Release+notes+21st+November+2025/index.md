# Release notes 21st November 2025

**Release date**: November 21, 2025

Our team is thrilled to announce the latest releases of Comala Document Management Cloud.

---

## Bug fixes

### Support for new Atlassian user ID format

Resolved an issue where the **Document Metadata** macro did not recognize Atlassian’s new user ID format. With this update, user parameters are now processed correctly, and the macro works as expected.

### Missing`resourceId`in resource map after data transfer

The metadata migration process is updated to consistently use the latest resource map created during content migration. This ensures the `resourceId` is included and prevents errors in subsequent workflow operations.

### Fixed Data-Transfer migration for workflows missing the `cwc-`prefix

Added validation to ensure all workflow IDs are valid UUIDs and include the required `cwc-` prefix. If a workflow ID is missing the prefix, it is now automatically corrected before the migration continues, ensuring a smooth and reliable transfer process.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Appfire’s Comala Document Management Cloud!

---