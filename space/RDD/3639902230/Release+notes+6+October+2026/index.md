# Release notes 6 October 2026

**Release date**: October 6, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## New features

## Dashboard Hub audit log

Dashboard Hub Pro and Dashboard Hub for Confluence now have an audit log that records changes to your datasources, dashboards, and gadgets, including sharing and permissions. See [Dashboard Hub audit log](/cms_trial/space/RDD/3659464768/Dashboard+Hub+audit+log/) to learn more.

Only Jira or Confluence administrators can view the audit log. It records actions taken inside Dashboard Hub and doesn’t replace your site administrator audit log.

![The Audit Log in Dashboard Hub](/cms_trial/assets/55c9ac13-f489-44ca-86af-bcf8cfbf76a7.png)

---

## Enhancements

## Assets Custom Charts

- Group Assets charts and tables by object type. When your query returns objects from more than one object type, you can now group a chart by object type and add an Object type column to tables. This makes it easy to compare and label objects such as Software Services, Applications, and Capabilities.
- Faster loading and a clearer object count. The gadget now loads objects created in the last 30 days as soon as you add it, so you see data straight away. When you run an AQL query, the number of objects it returns now appears just above the **Load** button so you can check the result before you build a chart or table.

## Worklog Insights

Added the option to segment work logged by Jira groups. This offers greater flexibility for larger organizations removing the limitation of selecting users individually.

## JCMA migrations from Dataplane to Dashboard

Improvements made to the enhance the overall experience when using JCMA to migrate Dataplane reports to Dashboard Hub.

---

## Bug fixes

The following bugs are fixed in this release:

- **Assets Custom Charts**:

  - Objects from different object types that share an attribute name (for example, Current status) no longer merge into a single column with blank values. Each object now shows its own attribute values.
  - The Linked work items column now displays its contents.
- **Jira Custom Charts**: Custom Charts no longer fail to load when grouped by certain custom fields. Grouping a Custom Chart by some multi-value custom fields (like Sentiment) could stop the chart from loading. These charts now display correctly.
- **Jira work-week settings**: Pie charts now show time totals using your Jira work-week settings. Pie charts calculated logged time using a 24h day / 7-day week instead of your Jira settings, for example, 8h day / 5-day week, so totals didn’t match the table view. They now match.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!