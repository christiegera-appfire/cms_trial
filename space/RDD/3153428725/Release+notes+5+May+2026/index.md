# Release notes 5 May 2026

**Release date**: May 5, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## New features

## Adaptive Filters

### Welcome to a new viewer experience in Dashboard Hub!

When we first released our Dynamic Filters feature, you could select up to five preset field filters to highlight specific Jira metrics and focus on data most relevant to you. These filters were always available on the dashboard, whether they were shared publicly or restricted to individuals or teams. Now, dashboard editors can select which filters are available in their dashboards or restrict filters altogether, providing more flexible ways to view important data and enhance security. To better represent the new functionality, we have renamed the feature, **Adaptive Filters**.

See [Adaptive Filters](/cms_trial/space/RDD/146309549/Adaptive+Filters/) to learn more about the new customization options.

## Historical Insights gadget

The Historical Insights gadget lets you visualize how specific Jira field values or numeric totals have changed over time. Unlike standard gadgets that display the current state of your data, this gadget samples historical data at defined intervals to show you exactly what your space looked like on a specific date. See [Historical Insights](/cms_trial/space/RDD/3058532407/Historical+Insights/) to learn more.

### **When to use the gadget**

Use this gadget to answer critical historical questions, such as:

- **Volume Trends:** See how many High Priority work items were in your backlog at the start of every month.
- **Workload Snapshots:** View the total sum of Story Points sitting in an In PRogress status at the beginning of each week.
- **Historical Distribution:** Compare how field values such as Assignee or Project were distributed across a specific date range.

### Migrations from Dataplane Reports

If you use Dataplane Reports for Jira Data Center and are planning a migration to Jira Cloud, Dashboard Hub’s Historical Insights gadget supports the migration of the following Historical Values reports:

- Issues Values By Date
- Issues Values Snapshots By Date
- Issues Values Snapshots Sum By Date

Other Dataplane Historical Values reports are mapped to other Dashboard Hub gadgets, such as Jira Custom Charts reports. To learn more about feature parity between Dataplane and Dashboard Hub, refer to the [Feature Comparison table](/cms_trial/space/RDD/438796304/Feature+comparison+for+Dataplane+Data+Center+vs+Dashboard+Hub+Pro+Cloud/).

## Display data from native Jira Agile reports

We added an option to use data from Jira’s native Velocity and Burndown reports for our [Scrum Velocity](/cms_trial/space/RDD/146309468/Scrum+Velocity/) and [Sprint Burndown](/cms_trial/space/RDD/146309738/Sprint+Burndown/) gadgets. This lets you use Jira’s agile calculations to display your data. This option is available only when the gadget uses a Jira datasource connected by API token.

---

## Enhancements

## Created vs Resolved Work Items

- Added a **Group By** option to the [Created vs Resolved Work Items](/cms_trial/space/RDD/2710011923/Created+vs+Resolved+Work+Items/) gadget that includes Day, Week, Month, Quarter, and Year. This lets you switch between identifying immediate bottlenecks and analyzing long-term trends. When you select a specific interval, the chart aggregates all work items created or resolved within that window into a single data point, for example, grouping all January activity into one monthly total.
- New tooltips added to the gadget metrics to help dashboard viewers interpret the data.

---

## Platform updates

**Reminder:** Atlassian replaced App Passwords with API Tokens for Bitbucket authentication in September 2025. App Passwords will be fully deprecated June 9, 2026.

See Atlassian’s support [documentation](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/) to learn more about this change.

When you create or update a Bitbucket Cloud datasource, use your Atlassian account email as the username and a scoped API Token as the password. Existing datasources using App Passwords will continue to work until June 9, 2026; we recommend migrating before that date. See [Bitbucket integration](/cms_trial/space/RDD/2381316116/Integration+with+Bitbucket/) to learn how to create or migrate your Bitbucket datasource with an API token.

---

## Bug fixes

The following bugs are fixed in this release:

- **AQL Search gadget**: Resolved an issue where the **Configure** action was not available on new and existing gadgets.
- **Datasource permissions**: Resolved an issue where Dashboard owners were unable to add users to datasources. As a result, even when users had the necessary dashboard permissions, attempts to edit gadgets could lead to empty fields and loss of gadget configuration.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!