# October 5, 2026

**Release date**: October 5, 2026

This release of **JMWE for Jira Cloud** cover the migration to Atlassian Forge.

---

## Enhancements

## Transition to Forge

**JMWE for Jira Cloud** has moved to Atlassian Forge! The overall functionality and experience within JMWE remains the same, with a few small differences. See [JMWE is moving to Atlassian Forge](/cms_trial/space/JMWEC/3708780578/JMWE+is+moving+to+Atlassian+Forge/) for details on what’s changed.

**Connect End of Support**:

- Atlassian has [announced](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps) the end of support for the Connect framework by the end of 2026.
- Appfire recommends upgrading JMWE app to the Forge version to stay current with future enhancements and security updates.

**Rollout schedule**

The new version will automatically roll out to customers over the next few days or weeks. Atlassian manages the deployment schedule across all instances.

### Upgrade to Forge manually

**Please review** the page [JMWE is moving to Atlassian Forge](/cms_trial/space/JMWEC/3708780578/JMWE+is+moving+to+Atlassian+Forge/) before starting a manual upgrade. There are changes to JMWE on Forge and steps you may need to complete before and after the upgrade!

You can also upgrade manually if you want. To upgrade the app to the Forge version, you need Jira administrative privileges.

1. Navigate to **Apps** > **Manage apps**.
2. Under *Connected apps,* JMWE will display an **Update** label if the update has been made available to your organization. Click **View app details**.
3. To upgrade the app, click **Accept & update**.
4. The *Confirm app update* dialog opens. Click **Update**.

The app uses different domains to serve content on Forge. If you have restrictive firewall or proxy settings, your network administrator needs to allowlist certain domains to ensure JMWE continues to work as expected.

Make sure to allowlist:

- `*.atlassian-dev.net` (including all subdomain levels)

See also [Atlassian's IP addresses and domains](https://support.atlassian.com/organization-administration/docs/ip-addresses-and-domains-for-atlassian-cloud-products/) documentation for complete details and follow all Atlassian recommendations.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!