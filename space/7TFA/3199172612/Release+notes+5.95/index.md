# Release notes 5.95

**Release date**: May 5, 2026

This page describes the latest release of 7pace Timetracker for Azure DevOps.

---

## Fixes

### Issues with WebContext panel

We have resolved the connectivity issues affecting the **WebContext panel**. Following the recent changes to Microsoft’s authentication protocols, some real-time features were failing to maintain a stable connection.

**What was fixed:**

- **Resolved Connection Drops:** Fixed an issue where the WebContext panel would lose connection or display a 404 error due to the transition from VSS to Entra token policies.
- **Improved Stability:** The SignalR component now correctly recognizes Entra tokens, ensuring that your data updates in real-time without manual refreshes or errors.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.visualstudio.com/items?itemName=7pace.Timetracker).
- Stuck with something? Raise a ticket through our [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/35).
- Do you love using our app? Let us know what you think [here](https://marketplace.visualstudio.com/items?itemName=7pace.Timetracker&ssr=false#review-details).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in 7pace Timetracker for Azure DevOps!

---