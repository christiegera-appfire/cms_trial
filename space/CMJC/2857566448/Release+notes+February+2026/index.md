# Release notes February 2026

**Release date**: February 5, 2026

Our team is thrilled to announce the latest release of Configuration Manager for Jira (CMJ) Cloud.

---

## Enhancements

## JMWE Workflow Support

Configuration Manager for Jira Cloud now supports the deployment of workflow elements fromJira Misc Workflow Extensions (JMWE).

During deployment, CMJ Cloud can read JMWE’s internal workflow logic and safely synchronize those configurations with the Destination site. It updates system-generated logic where needed for consistency, while intentionally preserving any custom scripts or JQL already defined on Destination, so existing customizations are never accidentally overwritten. Post-functions are created and configured as expected, but script-like inputs on the target remain untouched to avoid disrupting local behavior.

**Behavior limitations**

Some post-functions, such as Slack-related or shared action functions, are migrated as configured, but external references are not resolved during deployment.

## JSU Workflow Support

Configuration Manager for Jira Cloud now supports the deployment of all workflow configurations (9 post-functions, 2 conditions, 1 validator) from Jira Suite Utilities (JSU).

## Migration to Forge

Configuration Manager for Jira Cloud has moved to the [Forge](https://developer.atlassian.com/platform/forge/) framework.

**Connect End of Support**

- Atlassian has [announced](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps) the end of support for the Connect framework in late 2026.
- Appfire recommends upgrading the Configuration Manager for Jira Cloud to the Forge version to stay current with future enhancements and security updates.

---

## Bug fixes

The following bugs are fixed in this release:

## Snapshot creation

Fixed a bug where a snapshot could remain in the *In Progress* status if CMJ failed to create it.

## Deleted projects

Fixed a bug where data for a deleted project in a snapshot could become unavailable after creating a new snapshot version.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Configuration Manager for Jira (CMJ) Cloud!

---