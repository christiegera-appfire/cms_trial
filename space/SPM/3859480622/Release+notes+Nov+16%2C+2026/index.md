# Release notes Nov 16, 2026

**Release date**: November 16, 2026

This page outlines the updates included in the latest release of BigPicture.

**Version:** 8.76

---

## New

## Resources

### Add partial absence in hours

When adding a partial absence, users can input an exact number of hours. This allows for more precise tracking of resource capacity. Use the toggle switch to select a partial absence option.

![image-20261027-070601.png](/cms_trial/assets/c5e5e49f-5530-405a-b904-7530c0d3a55d.png)

## Priorities module BigPicture Advanced

### Prioritization templates can be created at the app and box level

Only App Admin or App Priorities Admin can create and edit global (app-level) templates.

Any box admin can create and edit local (box-level) templates, which are not available in any other box.

During template creation, App Admin and Priorities Admin can choose whether to create an app-level or box-level template.

![Screenshot of the App-level and Box-level templates in the Priorities module.](/cms_trial/assets/11a9a524-0456-48a4-8d40-9e75fc0b1de7.png)

[Read more](https://appfire.atlassian.net/wiki/x/hQDDYw)

## Financials module BigPicture Advanced

### You can set up individual cost rates

Use **Individual hourly rates** to define person-specific rates. Choose Individual rates in Calculation Settings for a specific portfolio or initiative (box). The app uses that value to calculate the person’s work costs instead of the team rate, helping you reflect differences in roles, seniority, or contract terms while keeping the team rate as the baseline for everyone else.

![administration-individual-hourly-rates.png](/cms_trial/assets/0a0d6239-12b3-44e8-91c9-740b97ae9c41.png)

[Read more](/cms_trial/space/SPM/1918830158/Financials+(Administration)/)

## OKR module BigPicture Advanced

### Dependencies

Visual dependency and contribution mapping provides a transparent view of how OKRs connect across teams and strategic initiatives.

Designed to support both Portfolio Leaders and PMO Managers, this capability makes it easy to track cross-functional relationships centrally, identify blockers early, and ensure work is properly sequenced.

By clarifying how individual efforts contribute to broader company goals, leaders can proactively manage risks, coordinate cross-team planning, and keep strategic execution aligned.

![Dependencies page in the OKR module.](/cms_trial/assets/28ea9b5e-4e1e-4dcf-80cf-5decfd96c30a.png)

[Read more](/cms_trial/space/SPM/3850666100/OKR+Dependencies/)

---

## Enhancements

## Bulk change

### Select a range of tasks for a bulk change

You can select a range of tasks by checking the first task's checkbox, and then holding the **Shift** key and clicking the last task's checkbox. You can continue to select more tasks or more task ranges before initiating the bulk change.

![Multi-select for bulk edit.mp4](/cms_trial/assets/6fb05c4e-4907-4479-8611-078076f2c4ac.mp4)

## Milestones

### Milestones section in the Gantt Infobar shows all the milestones in the box

**Before the change**

The Milestones section in the Gantt Infobar lists only milestones, which are expanded in the WBS.

**After the change**

The Milestones section in the Gantt Infobar shows all milestones in the box, regardless of the structure's collapsed/expanded state.

**Note**: Visibility of milestones is dependent on active filters.

![image-20261027-102752.png](/cms_trial/assets/1df9a5ca-2ad5-49cb-ad4f-ffc8b3f623ea.png)

### Week number is visible for milestones

When you activate week numbering on the Gantt timeline, a week number appears inside a milestone. The change applies only to the Gantt module.

![image-20261027-103528.png](/cms_trial/assets/58df69c5-4c1c-434a-bf08-33b79803a60d.png)

## Groupping

When you group tasks by status, the order follows the status categories

Groups display one after another, reflecting their Status Category.

- If OKRs are part of the task tree, they are displayed first. OKRs have just two status categories: Open or Closed. BigPicture Advanced
- Work Items have three status categories: To do, In progress, Done.

The order:

1. Open OKRs
2. Closed OKRs
3. TO DO work items
4. IN PROGRESS work items
5. DONE work items

## Warnings

### In the Gantt module, the app warns you when task dates don’t match the timebox dates

The warnings were already available in the Board module. They are now also available in the Gantt module.

![image-20261116-131532.png](/cms_trial/assets/3b659835-de53-4f04-a755-2a68db7d89c1.png)

Adjust the module view settings to ensure you see the warnings.

![image-20261116-131647.png](/cms_trial/assets/dd13a79f-5680-4589-bf64-3f17325aef3a.png)

## Permissions BigPicture Advanced

### Jira Global permissions for the Priorities module have been replaced with app permissions

User access to the Priorities module is based on global roles defined in the BigPicture Security tab (App Admin, Priorities Admin) and Box permissions.

![image-20261116-132243.png](/cms_trial/assets/d2f41317-3192-4a4c-9181-6060b437f98f.png)

## Financials module BigPicture Advanced

### **View Financials data at the root box level**

You can aggregate financial data from:

- multiple **Portfolios**
- their **Initiatives**
- lower levels boxes

You are able to:

- View **aggregated financial data** across multiple portfolios.
- Understand **total budgets and actual costs** across initiatives & portfolios.
- Identify **financial risks or overruns** across the organization.
- Use financial data for **strategic planning and reporting**.

The root box is the highest-level box in your hierarchy (in the image below, it is the “Main” box).

![image-20261116-140801.png](/cms_trial/assets/47c820fe-6e84-403e-a35c-39c09094ee75.png)

The data for the boxes placed under the root box is agregated in the Financials module.

![image-20261116-141152.png](/cms_trial/assets/65503152-8694-4583-aaf0-3d185fc9ba24.png)

**Note**: You can see only data for the boxes you have access to.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appfire.atlassian.net/servicedesk/customer/portal/11).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise?tab=overview&hosting=cloud).

**Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to continually improve our apps and products. You are the driving force behind why we create software. We appreciate your trust in BigPicture Enterprise Cloud!

|  |  |
| --- | --- |
| **Release date** | August 31, 2026 |
| **Highlights** | - enhancements    - **Show on Gantt:** The button is greyed out when Gantt is disabled for the box.   - **End Date:** The date picker opens on the Start Date when one is provided.   - **Old navigation:** A banner reminds users that the old navigation will be deprecated on October 1, 2026. |