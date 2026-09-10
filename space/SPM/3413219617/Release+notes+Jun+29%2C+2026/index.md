# Release notes Jun 29, 2026

**Release date**: June 29, 2026

This page outlines the updates included in the latest release of BigPicture.

**Version:** 8.73

---

## New

## OKR module

### OKR restrictions for individual OKRs

OKR restrictions add an extra layer of control for individual Strategic themes, Objectives, and Key Results (OKRs), allowing users to manage who can view and edit specific OKRs. There are two types of restrictions:

- **Visibility restriction** - Limits the visibility of an OKR to a specific group of users or teams.
- **Editing restriction** - Restricts editing capabilities, such as creating sub-items or linking Jira work items, to a selected group of users or teams.

Based on this setup, you can:

- Restrict only **Key Result1** and/or **Key Result2** (if the Strategic theme or Objective is not restricted).
- Restrict only the **Objective** (if the Strategic theme is not restricted). This action will also cause Key Result1 and Key Result2 to be restricted.

  ![A hierarchy of restricted OKRs.](/cms_trial/assets/c9c22367-8adb-4a23-9e72-cdb403818895.png)
- Restrict the **Strategic theme**. This action will also cause Objective, Key Result1, and Key Result2 to be restricted.

All OKRs inherit the restriction from their parent.

The OKR module’s **Settings** are **global**—any changes you make also apply to the organization's settings.

![General settings in the OKR module.](/cms_trial/assets/2df3c971-134c-4c95-ada4-01b50b0cf7ee.png)

[Unmapped macro: refined-button — no content to fall back on]

## UI changes - user roles management

Permissions to all modules can be managed in one of two places: App Administration or Box Configuration, depending on the permission context.

Permissions for the **Financials, OKR, and Priorities** modules are managed in App administration.

In the Security tab of the app Administration, you can manage the following roles:

- App Admin
- App Financial Admin
- App Financial Viewer
- App OKR Admin
- App OKR User
- App Priorities Admin
- App Resources Admin
- App User

![image-20260629-121156.png](/cms_trial/assets/9a43594f-d3b5-459e-9c97-2b8a181e79df.png)

## Multi-team planning postponed to next release

### Multi-team planning is available in the Resources module

![image-20260629-131630.png](/cms_trial/assets/bc1c4903-4568-4323-b7ac-c090809f3705.png)![image-20260629-131336.png](/cms_trial/assets/46088928-d979-47b9-b176-5da231105851.png)

## Workload distribution

### The resources grid reflects the actual logged time

Previously, workload was distributed based on BigPicture workload continuing settings and didn’t reflect the actual logged time.

Now, the time spent is displayed exactly on the day when it is logged in Jira.

- If a user logs time before the task start date, the time logs are displayed on the Start Date.

  - Example: task dates are May 1, 2026 - May 5, 2026, user logged 2 hours on April 29 and 3 hours on April 30 → it is displayed as 5 hours on May 1.
- If a user logs time after the task end date, the worklogs are displayed on the End Date.

  - Example: task dates are May 1, 2026 - May 5, 2026, user logged 1 hour on May 6 and 1 hour on May 7 → it is displayed as 2 hours on May 5th.

![image-20260629-125907.png](/cms_trial/assets/ba43cbab-6278-412e-b802-e30cd9b2e37e.png)

## Public API

### New endpoints have been added

The endpoints are documented on the [developer portal](https://developer.bigpicture.one/reference/whatisbigpicture).

- Public API to create, update, and delete global teams
- Public API to manage team members
- Public API for assigning skills to individuals is added
- Public API for managing Workload and Holiday plans
- endpoint with the details of user capacity and worklogs
- Public API for adding & managing skills is added

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in BigPicture Enterprise Cloud!

|  |  |
| --- | --- |
| **Release date** | June 29, 2026 |
| **Highlights** | - new - enhancements |