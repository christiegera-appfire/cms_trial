# Release notes 4.0.2 and 3.1.2

**Release date**: July 2, 2026

Planning Poker for Jira Data Center versions 4.0.2 for Jira 11 and 3.1.2 for Jira 10 include bug fixes for sessions that use alternative socket transport mode.

**Jira compatibility**: Jira 11 and Jira 10

These fixes apply only when **alternative socket transport mode** is enabled in the plugin settings. This setting is commonly used when server-sent events are blocked by corporate proxies, VPNs, or load balancers.

---

## Bug fixes

This release includes the following bug fixes:

- Fixed an issue where the estimation backlog could fall out of sync with the session state when polling was enabled. A completed issue could remain in the backlog, appear in both estimated and to estimate lists, or be available for re-estimation.
- Fixed an issue where selecting **Replay** after a timer ended could show a single dash card and skip the active voting phase when polling was enabled.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1212495/planning-poker?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Planning Poker.