# Release notes 1 October 2026

**Release date**: October 1, 2026

This page outlines the updates included in the latest release of Connector for Salesforce & Jira Cloud.

**Jira Marketplace** **version**: 29.3.0

**Salesforce** **version**: 4.82

---

## SALESFORCE New feature

## Automate Salesforce record updates to Jira with Flow Builder

With the new **Push updates to Jira** action in Salesforce Flows, you can keep Jira work items in sync with Salesforce, automatically and without manual effort.

Set it up once in Flow Builder: select your trigger and Jira connection, and every matching record change is automatically pushed to the associated Jira work items, following the synchronization rules configured for that connection. You can use the action in record-triggered flows and schedule-triggered flows. Setup is easier than before, as you no longer need to manually enable Apex Class Access in Profiles.

For example, you can create a record-triggered flow that pushes Case updates to associated Jira work items whenever an escalated Case changes. Or you can create a schedule-triggered flow that pushes updates for a specific record at regular times.

For details, see [Automatically create Jira work items with Salesforce Flows](/cms_trial/space/CSFJIRA/3627581468/Automate+Jira+actions+with+Salesforce+Flow+Builder/).

![Push updates to Jira](/cms_trial/assets/a8002e52-de9c-4a08-9dd7-1119fe07f463.png)

---

## JIRA CLOUD Bug fixes

**Jira Comments (NextGen) not loading**

**Issue:** Some customers saw incomplete Jira comments on Salesforce Cases.

**Improved:** Loading of Jira comments and attachment sync on Salesforce Cases is now more reliable.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in Connector for Salesforce & Jira Cloud!