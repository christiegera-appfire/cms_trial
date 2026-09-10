# Release notes 3 June 2026

**Release date**: June 3, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## Breaking change

This release introduces a [breaking change](/cms_trial/space/RDD/3262939446/Breaking+changes/). A change to the permission scope is needed to support the Subscriptions feature.

Your Jira or Confluence administrator must approve and manually update the app to access new features and maintain future access to the app.

---

## New features

## Dashboard Subscriptions

You can now subscribe to a dashboard in Dashboard Hub Pro and Dashboard Hub for Confluence. Subscriptions are automated, secure, and shareable point-in-time reports that reduce manual effort, improve reporting reliability, and ensure that all stakeholders reference the same data.

### How it works

At the scheduled time, Dashboard Hub:

1. Captures a static, read-only version of the dashboard as it currently appears.
2. Stores the snapshot as a static asset so the data cannot change after capture. The snapshot is stored for one year, after which it is deleted.
3. Generates a unique public link for that snapshot.
4. Sends an email to all configured recipients containing the link and any optional message you have added.

See [Dashboard subscriptions](/cms_trial/space/RDD/2934407285/Dashboard+subscriptions/) to learn more.

## Bulk update JQL for dashboards

You can now apply the same JQL query to update all compatible gadgets at once. This is useful if you:

- **Reuse dashboards** across sprints, projects, or teams by re-pointing them at new data.
- **Share a dashboard template** and need to adapt it quickly for different contexts.
- **Maintain large dashboards** and want confidence that every gadget is looking at the same dataset.

See [How to bulk update the JQL of dashboard gadgets](/cms_trial/space/RDD/3242852356/How+to+bulk+update+the+JQL+of+dashboard+gadgets/) to learn more.

## Assets Custom Charts

The Assets Custom Charts gadget lets you turn AQL query results into charts, pivot tables, and aggregated views, so you can answer questions like “*How many laptops does each department have?*” or “*Which software licenses expire this quarter?*” without leaving your dashboard.

Dashboard Hub already lets you search and display Assets data in a table with the AQL Search gadget, but many teams using Assets for IT inventory, license management, or configuration tracking need more than a flat table to report on their data. Use an AQL query to pull in asset objects, then choose from the same view types available in Jira Custom Charts: tables, 1D and 2D pivot tables, bar, line, area, pie, and tile charts. Group, aggregate, and customize colors and segments to build the exact report your stakeholders need.

See [Assets Custom Charts](/cms_trial/space/RDD/3294855178/Assets+Custom+Charts/) to get started.

---

## Enhancements

### Formula Cards variables

You can now customize the variable label in the Formula Cards gadget. Instead of default labels, such as `a` or `b`, custom variables let you define your own labels to reference when writing a formula expression, for example, `donework-updatedrecently =`.

![DH-Formula-Cards-variables.png](/cms_trial/assets/63ee9f66-065f-4d71-bbba-cfaf6a3bad5a.png)

### Transition Time From Status to Status

We added an option to the Transition Time From Status to Status to better support migrations of the Time to Next Status report from Dataplane Reports. The gadget now includes a Direct transition only option that counts only transitions that move directly between the selected statuses, ignoring any intermediate statuses.

![DH-direct-transitions-only.png](/cms_trial/assets/7450162b-445a-4535-9da1-92b6022444bb.png)

---

## Bug fixes

The following bugs are fixed in this release:

- **Custom Reports**: Resolved an issue that caused errors when loading extra details for each item in a list (for example, one request per row). Now, report loading waits until each item is ready before loading the extra data, making the experience more stable and predictable.
- **Jira Custom Charts**: Resolved an issue with story point calculations. Story point calculations now correctly show the average points over time, not per work item.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!