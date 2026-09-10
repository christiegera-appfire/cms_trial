# Met vs Breached SLAs

## Overview

This gadget is designed to **help support teams track and monitor the status of their service level agreements (SLAs)**. With this information, teams can take the necessary actions to ensure that all SLAs are being met and customer satisfaction is maintained. Whether you're a support manager, team lead, or individual contributor, this gadget is an essential tool for keeping your SLA performance on track.

This gadget requires <https://appfire.atlassian.net/wiki/spaces/TTSC>

Data Center version <https://appfire.atlassian.net/wiki/spaces/TTS> not available by default, check [Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)

This gadget displays the SLA status of support tickets in a clear and easy-to-read chart, allowing teams to quickly identify which tickets are breached, met, or in progress.

![Dashboard Hub met vs breach slas](/cms_trial/assets/bc3a0ed5-10e0-41c7-8377-f1eddbd394b7.png)

This gadget is **multi-project**, so you can report across your whole portfolio of projects.

### View Type

You can select among four different visual metaphors to represent your chart: Grouped bar chart, Stacked bar chart, Stacked area chart, or the Multi-line chart.

Important:

- The gadget displays the total number of SLA instances. If an issue has multiple SLAs in it, then each SLA will be counted separately.
- The API token you need from Time to SLA to create a datasource requires the SLA and Issue SLA generate to use in Dashboard Hub has to have the "SLA" and "Issue SLA" access.

![Dashboard Hub API token configuration](/cms_trial/assets/d66aec12-0d02-4522-9389-0ca43c671f5d.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a **Time to SLA** datasource, remember that you have to create this datasource first.
- The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). If you don’t add any and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend adding at least one clause, for example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- The **SLA** to display the data from, remember that these SLAs are the ones provided by the <https://appfire.atlassian.net/wiki/spaces/TTSC> app.
- The **View Type**, select between four different charts: Grouped bar chart, Stacked bar chart, Stacked area chart, or the Multi-line chart.
- The **Group by period of time**, to display the data grouped by weeks, months, quarters or years.
- The **Filter by date**, i.e.,the period of time you want to display in the time series of the graph. In other words, when the start date of the selected SLAs begins in the x-axis of the chart.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration