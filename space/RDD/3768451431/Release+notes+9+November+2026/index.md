# Release notes 9 November 2026

**Release date**: November 9, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## New features

## AI Insights for Dashboard Hub

Insights is your guide to Dashboard Hub. It explains your data, suggests improvements, and answers your questions, right on your dashboard.

![Example of dashboard insights in Dashboard Hub](/cms_trial/assets/c18f928e-64e4-4065-ad2d-b0ba3d723c97.png)

- Spot trends, changes, and anything unusual, so you can act on problems early.
- Get tips to improve your data visualizations.
- Get answers to how-to questions based on Dashboard Hub's user documentation.
- Use it in Dashboard Hub Pro and Dashboard Hub for Confluence.

This feature requires Dashboard Hub data to be hosted in the US region. See [Data residency](/cms_trial/space/RDD/146309741/Data+Residency+(Cloud)/) to learn more.

See [Dashboard AI insights](/cms_trial/space/RDD/3683385641/Dashboard+AI+insights/) to learn more.

---

## Enhancements

## Jira Formula Custom Field support

Dashboard Hub now supports Jira Cloud’s Formula Custom Fields. When Jira calculates a numeric formula value on a work item (for example, a Risk Score), that value is now available for use across your dashboards.

- Custom formula fields appear alongside your other custom fields in tables and charts.
- You can select them as columns, group by them, and aggregate them with SUM, AVG, MIN, MAX, and COUNT.
- Formula custom fields that are configured with a searcher template are available in dashboard filters.

## Cycle Time and Lead Time gadgets

You can now choose an In Progress status as the end status. When you set up either gadget, the end status dropdown lists In progress statuses after the Done statuses. This lets you measure time up to a point before work is finished. Gadgets you've already configured keep working as before.

## JCMA migrations from Dataplane to Dashboard

Improvements made to enhance the overall experience when using JCMA to migrate Dataplane reports to Dashboard Hub.

## Minor UX improvements

We made improvements to the user interface to deliver better consistency and messaging.

---

## Bug fixes

The following bugs are fixed in this release:

- **Jira work-week settings**: Pie charts now show time totals matching your Jira work-week settings. Pie charts previously calculated logged time using a 24h day/7-day week instead of your Jira settings (for example, 8h day/5-day week), so totals didn’t match the table view.
- **Historical Insights**: Fixed an issue where the gadget returned inconsistent counts when filtering by status category. Past statuses are now matched to their correct category, so equivalent filters return the same results.

---

## Retirement of External Page gadget

The External Page gadget is retired and won't display data on your dashboards. To keep your views clean, remove the gadget from any affected dashboards.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!