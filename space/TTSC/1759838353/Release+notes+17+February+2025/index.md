# Release notes 17 February 2025

**Release date**: February 17, 2025

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## Enhancements

### Incoming webhook changes implemented

We've updated the Incoming Webhook functionality in Time to SLA to align with Atlassian’s upcoming security changes.

Atlassian is updating how incoming webhook triggers are routed. Any automation rules created before January 28, 2025, will continue to work until May 30, 2025, but must be migrated to the new endpoint to remain functional beyond this date.

If you use incoming webhooks in your automation rules, we strongly recommend reviewing and updating them as needed.

We’ve updated our SLA Notification configuration to support this transition to include a **Automation Webhook Secret** section. From now on, when creating a notification that will trigger a Jira automation rule, you must provide this information.

![Time to SLA release notes February 2025 showing updated SLA interface](/cms_trial/assets/cd259663-aa8b-4325-99f1-497f4f698320.png)

For more information, refer to the [documentation](/cms_trial/space/TTSC/1464075666/Use+SLA+actions+with+Jira+automation/).

## Bug fixes

The following bugs are fixed in this release:

- Previously, when modifying an SLA field condition from 'is set' to 'changed to', the condition was automatically set to 'is equal to', which was unintended behavior. Additionally, when scrolling down, the user selection area was not visible. This issue has now been fixed.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---