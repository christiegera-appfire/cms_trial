# Release Notes 30 June 2025

**Release date**: June 30, 2025

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira, Confluence, Bitbucket and monday.com.

[unmapped inline: placeholder]

## Enhancements

## New Dashboards Creation Experience

We’ve simplified how you create dashboards! The new creation flow helps users get started faster with a cleaner interface, fewer steps, and smarter defaults. Now, it easier than ever to build meaningful dashboards in just a few clicks.

![Dashboard Hub Release Notes 30 June 2025 dashboard preview](/cms_trial/assets/3fe9f074-8e1e-4f54-b6cc-0baeb0048266.jpg)

## BigPicture Global Template

Configure all the metrics in your [BigPicture PPM Insights template](/cms_trial/space/RDD/1942979108/BigPicture+PPM+Insights+template/) in a single step!

![Dashboard Hub Release Notes 30 June 2025 template preview](/cms_trial/assets/b5fac85b-f9d3-485b-b0b5-74ea778377c3.jpg)

## JCMA: Dataplane to Dashboard Hub

The Dataplane reports <https://appfire.atlassian.net/wiki/spaces/dataplane/pages/455968098> and <https://appfire.atlassian.net/wiki/spaces/dataplane/pages/455967412> are now automatically migrated to their equivalent gadgets [Work Items Entering Status by Date](/cms_trial/space/RDD/1914273796/Work+Items+Entering+Status+by+Date/) and [Time in Status](/cms_trial/space/RDD/866058316/Time+in+Status/) respectively in Dashboard Hub. Reports with multiple segments (e.g., multi pie charts) are now also supported in automatic migrations.

We’ve also improved error handling and diagnostics to reduce unhandled migration cases and make troubleshooting easier.

## Performance Improvements

- New rendering engine for charts for a better performance.

## Misc

- Line charts have drill-through capabilities now.

---

## Bug fixes

The following bugs are fixed in this release:

- Gadgets now correctly display weeks with zero counts even when the filter range starts with a zero-count week.
- In some cases, if the app hadn’t been accessed for a while, the previously selected dashboard failed to load on first access.
- Export to PNG in gadgets used on native Jira dashboards now works correctly.
- Some JQL searches returning more than 100 issues were not sorted.
- JQL failed in Custom Reports within Confluence macros.
- Dashboards accessed via the Jira Service Management Customer Portal failed to load in cases where a high number of customers (large groups) were granted access.
- The **Met vs Breached SLA** gadget (Time to SLA integration) was not displaying data and showed broken or incorrect legend labels.
- Chart configuration options (hiding results or changing colors) were not always displayed.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-chart-report-diagram-external-share?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in the Dashboard Hub family of apps!

---