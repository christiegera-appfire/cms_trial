# Release notes 7 September 2026

**Release date**: September 7, 2026

This page outlines the updates included in the latest release of Connector for Salesforce & Jira Cloud.

**Marketplace** **version:** 28.7.0

**Salesforce version**: 4.79

---

## **New features**

## Automation

### Salseforce Automatically create Jira work items from Salesforce Flows

With the new **Create Jira work item** action in Salesforce Flows, you can turn any Salesforce event into a Jira work item, instantly and without manual effort.

Set it up once in Flow Builder: select your trigger, connection, Jira space, and work item type, and every matching record (like an escalated Case) automatically creates an associated Jira item. No copy-pasting, no context-switching, no missed context.

![image-20260903-132838.png](/cms_trial/assets/0a1b8c8e-6b6d-4111-b5d4-1292c9c75063.png)

**Benefits:**

- **Save time.** Eliminate manual ticket creation.
- **Stay in sync.** Salesforce records and Jira work items are automatically linked and kept up to date.
- **Full flexibility.** Allows you to create triggers depending on your needs, as available in Flow Builder under Actions.

For details, see [Automatically create Jira work items from Salesforce Flows](/cms_trial/space/CSFJIRA/3627581468/Automatically+create+Jira+work+items+with+Salesforce+Flows/).

## Comments filtering

## SalseforceJira Cloud **Improved tag filtering for Jira and Salesforce comments**

You can now filter both Jira and Salesforce comments by tag on each side of the integration. Filters are configured independently in Jira and in Salesforce:

- In Jira, tag filters control which Jira and Salesforce comments appear in the Salesforce Comments tab on a Jira work item.

  ![comment configuration in Jira](/cms_trial/assets/18ea36ab-3078-4544-b080-432f52364e7e.png)
- In Salesforce, tag filters control which Jira and Salesforce comments appear in the Jira Comments component.

  ![Comment configuration](/cms_trial/assets/efd3a6ab-30b3-4da0-a5d8-a8b7278c4084.png)

Existing tag filters have been automatically migrated to the new settings. In Jira, existing tags have been moved to the Salesforce comments tag filter. In Salesforce, existing tags have been moved to the Jira comments tag filter.

For details, see [Filter Salesforce comments in Jira work items](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/) and [Filter Jira comments in Salesforce Cases](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/).

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Connector for Salesforce & Jira Cloud!