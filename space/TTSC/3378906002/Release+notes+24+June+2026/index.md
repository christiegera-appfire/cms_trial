# Release notes 24 June 2026

**Release date**: June 24, 2026

This page outlines the updates included in the latest release of Time to SLA for Jira Cloud.

---

## New features

### Actions: Manage SLA notifications and automations from one place

We’ve redesigned how SLA notifications and automations are managed in Time to SLA.

Previously, if you wanted to review or update notifications, you had to open each SLA configuration individually. With this release, all SLA actions are now centralized in a dedicated **Actions** page, making it easier to view, manage, and maintain your automations from a single location.

For detailed documentation, refer to the dedicated [*Actions*](/cms_trial/space/TTSC/35881090/Actions/) [page](/cms_trial/space/TTSC/35881090/Actions/).

#### New Actions page

A new *Actions* tab is now available in the Time to SLA navigation bar.

![Actions page showing all SLA actions across configurations, including filters, status, and action management options.](/cms_trial/assets/0a9d264e-ff93-49f0-bf0a-6549b0e90152.png)

Watch this video for a quick 3-minute overview:

The **Notifications** button inside each SLA configuration has also been replaced with **Actions**. This change reflects the expanded scope of the feature: actions can now do more than send notifications. They can also update Jira work items, add comments, trigger Jira automation rules, and more.

You can access SLA actions in two ways:

- Select **Actions** from the top navigation to view and manage actions across all SLA configurations.
- Open a specific SLA configuration and select **Actions** to view and manage the actions related to that SLA.

  ![SLA configuration page highlighting the Actions button for managing actions for a specific SLA.](/cms_trial/assets/860794b7-7a34-4096-a47c-e158ab23a90b.png)

From the *Actions* page, you can:

- View all actions across your SLA configurations in one place
- Search and filter actions by SLA or action type
- Check action execution history
- Edit, disable, or delete existing actions

#### Create lightweight SLA-driven automations

Actions allow you to automatically respond to SLA events such as approaching targets or breached SLAs.

![New action page showing the available SLA action types, including sending emails, Slack messages, and triggering Jira automation.](/cms_trial/assets/c6ff9751-18d4-42a2-be54-d44374580069.png)

Available action types include:

- Send an email
- Send a Slack message
- Trigger a Jira automation rule
- Add a comment
- Change assignee
- Change priority
- Set Jira fields

For example, when an SLA is breached, you can automatically:

- Increase the work item priority
- Reassign the work item to an escalation team member
- Add an internal comment
- Send a Slack notification to the team
- Trigger a Jira automation rule for additional workflows

#### Why this matters

The new *Actions* page gives administrators a single place to manage notifications and automated responses, reducing the need to navigate between multiple SLA configurations. It also makes it easier to build proactive workflows that keep teams informed and help prevent SLA breaches before they happen.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed an issue where users with a Jira license couldn’t see the SLA panel, even when the app was configured to allow standard Jira users without an agent license to view it. The SLA panel now respects the configured visibility settings correctly.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!