# Release notes 26 October 2026

**Release date**: October 26, 2026

This page outlines the updates included in the latest release of Connector for Salesforce & Jira Cloud.

**Salesforce version**: 4.85

**Marketplace version:** 29.11.0

---

## **Features**

### SALESFORCE JIRA CLOUD Time to SLA integration for Connector for Salesforce & Jira

### See Jira work item SLAs directly in Salesforce

SLAs set in Time to SLA now appear on your Salesforce record pages, next to the Jira work items linked to each record. Support teams can check whether a work item is on track without switching to Jira.

#### What's new

- **Time to SLA for Jira:** Add it to a record page in Lightning App Builder to see the SLAs and how many are breached for the linked work items.
- **Integrations:** Jira admins can assign a Time to SLA scope to one or more connected Salesforce instances, so each instance uses the right SLAs.
- **One token per tenant:** Connect Time to SLA once, and every integration uses it.

#### Get started

1. In Jira, go to **Apps > Connector for Salesforce and Jira > App settings > Integrations**, add your Time to SLA token, and create an integration.
2. In Salesforce, add the **Time to SLA for Jira** component to a record page.

![Time to SLA for Jira component ](/cms_trial/assets/0a3cfaca-5a30-42cb-89f6-a6c7d4fa229d.png)

**Learn more**:

- [Set up Time to SLA to Connector for Salesforce & Jira](https://appfire.atlassian.net/wiki/x/mYDi2g)
- [Troubleshooting the Time to SLA integration](/cms_trial/space/CSFJIRA/3759046770/Troubleshooting+the+Time+to+SLA+integration/)
- [Integrate Salesforce and Jira for SLA management](/cms_trial/space/CSFJIRA/3688857603/Integrate+Salesforce+and+Jira+for+SLA+management/)

---

## JIRA CLOUD Bug fixes

- **Salesforce connection**: Fixed errors when multiple Jira spaces are linked to the same Salesforce connection by improving how Jira API requests are handled.
- **Bulk push issue**: Fixedbulk push operations from Jira to Salesforce so they update the expected Salesforce fields, and preserved rich-text formatting during synchronization.
- **Creating Jira Service Management (JSM) work items**: Fixed an intermittent "None.get" error. JSM work items can now be created reliably from Salesforce with the Use Request Type fields option enabled.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=reviews).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in Connector for Salesforce & Jira Cloud!