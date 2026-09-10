# Release notes 5.94

**Release date**: April 21, 2026

This page describes the latest release of 7pace Timetracker for Azure DevOps.

---

## Highlight

### Access to the application lost

This week, we identified a critical issue affecting user access to the 7pace application. Following the deployment of two targeted fixes, service has been restored for the vast majority of users.

#### Root Cause

The interruption was caused by an unannounced change in Microsoft’s authentication token structure. Microsoft has moved away from treating authentication tokens as a "data contract," resulting in unexpected payload changes that disrupted our previous integration.

For more information, check [this Azure DevOps Blog post](https://devblogs.microsoft.com/devops/authentication-tokens-are-not-a-data-contract/).

#### Current Status

- **Resolved:** Primary access and authentication workflows are back online.
- **Known Issue:** We are currently investigating reports of intermittent stability issues specifically related to the **SignalR component**. If you experience connection drops or real-time update delays, please refresh your browser or contact our support team.

## Fixes

- Fixed authorization error
- The scroll behavior for the dropdown on the Reminder page has been fixed
- An error on the Reminders page upon reopening the data fixed.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.visualstudio.com/items?itemName=7pace.Timetracker).
- Stuck with something? Raise a ticket through our [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/35).
- Do you love using our app? Let us know what you think [here](https://marketplace.visualstudio.com/items?itemName=7pace.Timetracker&ssr=false#review-details).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in 7pace Timetracker for Azure DevOps!

---