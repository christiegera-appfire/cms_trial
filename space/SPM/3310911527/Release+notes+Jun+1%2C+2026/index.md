# Release notes Jun 1, 2026

**Release date**: June 1, 2026

This page outlines the updates included in the latest release of BigPicture.

**Version:** 8.72

---

## New

## Financials module

### Add an expense from a numbers Jira custom field

Map a custom expense to an existing Jira number-type custom field, to pull cost values directly from work items. See custom expense types in the Other Expenses section of the Financials Module to easily understand the full cost breakdown of your plan.

For example, work items could have the custom fields "Hardware spendings”, and "Software spendings". Adjust the settings of the Financials to differentiate these cost types from the already existing personnel costs in the module's charts.

![image-20260601-123504.png](/cms_trial/assets/8922b75f-5db0-460a-a041-338989d7ceef.png)

## Public API

### Automatic OKR updates done using API

Update OKRs automatically using API. Adjust the visibility of the automated updates using the   
”Show automated updates” toggle switch.

![image-20260601-085710.png](/cms_trial/assets/f39c47db-e111-4fc3-950a-5f2f96f13886.png)

**Note**: Historical API records cannot be hidden. Only the updates added after this release are affected.

Visit the developer portal to view API documentation for [objectives](https://developer.bigpicture.one/reference/updateobjective) and [key results](https://developer.bigpicture.one/reference/updatekeyresult).

## Structure builders

You can now create a task structure based on teams assigned to tasks. It is always the last structure builder (lowest level), to avoid conflicts.

![image-20260601-115613.png](/cms_trial/assets/db564085-e2a8-404d-bb50-2e3c6f44685c.png)

---

## Enhencements

## Financials module

### Calculation settings are visible on portfolio and timebox levels

Now you have the ability to view Financials settings on both Portfolio and timebox levels. Information is read-only - settings have to be adjusted directly in an initiative.

![image-20260601-120458.png](/cms_trial/assets/d56a9d63-f5b0-4fcb-ab27-372eaf879990.png)

## Public API

### **Before the change**

Endpoint <https://developer.bigpicture.one/reference/getteamsallocatedtoboxes-1> gets extra objects in the response:

- profile URLs of the team members.
- skills of the team members, including skill name, skill start date, and skill end date.

Endpoint <https://developer.bigpicture.one/reference/getresourcetaskassignment-1> gets extra objects in the response:

- Skill name for task.
- Skill name, skill start date, and skill end date for individuals and teams.

## User Interface changes (new navigation)

- Hinde invalid API tokens

![image-20260601-130557.png](/cms_trial/assets/32d34ff6-7e1c-4477-afce-f924432340fe.png)

- New shortcut for Gantt and Scope modules (Shift + S) opens the scope definition modal.

![image-20260601-130914.png](/cms_trial/assets/06d9b9fb-5536-4b7c-92b7-64eba0212c5d.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in BigPicture Enterprise Cloud!

|  |  |
| --- | --- |
| **Release date** | June 1, 2026 |
| **Highlights** | - new - enhancements |