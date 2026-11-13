# Dashboard Hub

Dashboard Hub is a powerful tool for monitoring and visualizing key metrics and KPIs across your organization. It provides a central location for viewing and analyzing data from various sources, including customer support systems, marketing platforms, and financial reporting tools.

Integrating Dashboard Hub with Time to SLA can provide valuable insights into how your organization is performing in meeting its SLAs.

## Met vs Breached SLA

At the moment, there is the “Met vs Breached SLA” gadget, which displays the SLA status of support tickets in a clear and easy-to-read chart, allowing teams to quickly identify which tickets are breached, met, or in progress. This gadget is **multi-project**, so you can report across your whole portfolio of projects.

![Time to SLA Dashboard Hub tile for SLA metrics](/cms_trial/assets/19f6909d-dffa-47b0-ab77-19295a79712a.png)

The gadget displays the total number of SLA instances. If a work item has multiple SLAs in it, then each SLA will be counted separately. Let’s explore how you can set it up in your instance.

## Prerequisites

- You must have Dashboard Hub installed in your instance to carry out the instructions on this page.
- You must create a Time to SLA datasource. Refer to the [Dashboard Hub documentation](https://appfire.atlassian.net/wiki/spaces/RDD/pages/146309293) for detailed information. The API token you need from Time to SLA to create a datasource requires the "SLA" and "Issue SLA" generated to use in Dashboard Hub to have the "SLA" and "Issue SLA" access.

  ![Time to SLA Dashboard Hub dashboard with SLA gadget configuration](/cms_trial/assets/c2dd5bb8-4db1-46f5-99fb-2a41d396c574.png)

## Configuration

1. Go to the dashboardyou want to add the gadget to. Click **Edit**.
2. Click **Add gadget** or **Add a new gadget.**
3. Search `Met vs Breached SLA`.
4. Click **Add.** The *Met vs Breached SLAs* configuration screen will appear.

   ![Time to SLA Dashboard Hub dashboard with SLA performance gadgets](/cms_trial/assets/41416f57-dd83-4276-8ede-f1236de38add.png)
5. Select a Time to SLA datasource. Remember that you have to [create the datasource](https://help.roninpixels.com/RDD/add-and-manage-datasources) first.
6. The **JQL (Jira Query Language) query or filter** to filter the list of work items (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). If you don’t add any and click “Load”, the gadget will request all the content in the source instance, which might cause performance issues.

We recommend adding at least one clause. For example, to list all the work items of the space *Teams in Space*, use the clause `project = "TIS”`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.

1. Select the **SLA** to display the data from.
2. For the **View Type**, select between four different charts: Grouped bar chart, Stacked bar chart, Stacked area chart, or the Multi-line chart.
3. The **Group by period of time**, to display the data grouped by weeks, months, quarters or years.
4. The **Filter by date**, i.e.,the period of time you want to display in the time series of the graph. In other words, when the start date of the selected SLAs begins on the x-axis of the chart.
5. Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring each gadget individually with the same default configuration.
6. Click **Save**.

The gadget will now appear on your dashboard.