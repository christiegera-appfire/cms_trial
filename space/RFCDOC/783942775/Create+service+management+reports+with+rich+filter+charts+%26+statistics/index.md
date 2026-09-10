# Create service management reports with rich filter charts & statistics

If you are involved in a company service management function, you will know that reporting is critical for your team's success. Your leadership will want regular reports to show that you meet company objectives for SLAs and customer satisfaction levels. They will like this information in an easily digestible format, allowing them to break the data down by different teams or service desks and look at trends over time. They want to see where the successes are but quickly find problematic trends that allow preemptive responses to potential failures.

This article shows you how to create a powerful support request reporting dashboard with [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) that fulfills the needs described above. It allows you to report progress against targets and monitor your work for success and problem patterns. This is a key part of delivering an effective ITSM strategy.

**Contents:**

- [Prerequisites](#prerequisites)
- [Use case](#use-case)
- [Solution: Use a rich filter-powered dashboard for support request reporting](#solution-use-a-rich-filter-powered-dashboard-for-support-request-reporting)
- [At-a-glance reporting on overall SLA targets](#at-a-glance-reporting-on-overall-sla-targets)
- [Break down SLA targets by team and project](#break-down-sla-targets-by-team-and-project)
- [Generating quick charts](#generating-quick-charts)
- [Show historical progress against targets.](#show-historical-progress-against-targets)
- [Rich filter features resources.](#rich-filter-features-resources)
- [Start building the Support request reporting dashboard](#start-building-the-support-request-reporting-dashboard)
- [Set up your filters](#set-up-your-filters)
- [Set up your time series](#set-up-your-time-series)
- [Set up the Rich Filter Simple Gauges gadget](#set-up-the-rich-filter-simple-gauges-gadget)
- [Set up the first Rich Filter Statistics gadget](#set-up-the-first-rich-filter-statistics-gadget)
- [Set up the first Rich Filter Two Dimensional Statistics gadget](#set-up-the-first-rich-filter-two-dimensional-statistics-gadget)
- [Set up the second Rich Filter Two Dimensional Statistics gadget](#set-up-the-second-rich-filter-two-dimensional-statistics-gadget)
- [Set up the second Rich Filter Statistics gadget](#set-up-the-second-rich-filter-statistics-gadget)
- [Set up the Rich Filter Flexi Charts gadget](#set-up-the-rich-filter-flexi-charts-gadget)
- [Set up the Rich Filter Time Series Chart gadget](#set-up-the-rich-filter-time-series-chart-gadget)
- [Final result](#final-result)

## Prerequisites

This article assumes that you are using [Jira Service Management](https://www.atlassian.com/software/jira/service-management).

## Use case

Imagine the following scenario (your exact situation might have different numbers of projects or teams or other constraints, but the principles are the same):

- You have three different service management projects to support three different products.
- To answer support requests, you have support agents grouped into two teams that provide coverage for different geographical regions.
- The support agents in each team specialize in different products, with the aim of providing good overall coverage across all of them.
- You want to create an efficient way of reporting on Time to first response / Time to resolution SLAs and customer satisfaction that can show trends over time and progress across multiple projects by team, customer, customer request type, individual assignee, etc.

How can you provide this level of reporting in an easy-to-digest format, all in one place?

## Solution: Use a rich filter-powered dashboard for support request reporting

[Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) provides a perfect feature for reporting your support request progress, which you'll see in action through the article. Rich filters are based on a standard Jira filter, hence the issues listed in rich filter gadgets can be cross-project. This enables you to build a single dashboard to report on multiple service management projects, giving rich filters a definite advantage over Jira's built-in Service Management reporting, defined for single projects.

To provide a solution to satisfy the use case detailed above, we are going to show you how to create the following dashboard:

![Final result service management reports.png](/cms_trial/assets/47f3e12c-9f67-4e29-b6fa-51ef958769a4.png)

First of all, however, we'll explore how this dashboard works and how it can facilitate effective, powerful reporting across all your projects, customers, and teams. Later on, we'll walk you through how to build it.

### At-a-glance reporting on overall SLA targets

On the left-hand side of the dashboard, we've got a set of gauges that provides a top-level view of where we are in terms of meeting our SLAs. Here we are showing % of met for both time to first response (TTFR) and time to resolution (TTR) SLAs:

![time to first response (TTFR).png](/cms_trial/assets/f46696ed-1467-4657-bcb1-4a6f846945df.png)

This is a good place to talk about the quick filters inside the *Rich Filter Controller*. We can use these controls to filter the data shown in all the other rich filter gadgets, meaning that we can dynamically create more specific data breakdowns whenever needed. For example, we can filter by**Team** and **Project**: *Fox Service Desk*:

![filter by Team and Project-.png](/cms_trial/assets/b666e6cd-0019-47ab-bfb1-b897e0016eb8.png)

Our gauges will now show % of met for our SLAs, only for *Green Team* working on the *Fox Service Desk* project:

![filter byt_eam and Project-.png](/cms_trial/assets/a67bad1e-5f0d-41cd-adb0-1a4c7b42a835.png)

### Break down SLA targets by team and project

If you want permanent views of specific data breakdowns that you find important, you can create these using rich filter statistics gadgets. Our reporting dashboard has three main breakdowns.

First of all, we show the issue count, TTR % breached, and customer satisfaction for each of our teams:

![satisfaction for each of our teams.png](/cms_trial/assets/a4a252e4-dc95-43ed-87f4-ec0ea457462a.png)

We can also show a two-dimensional breakdown—in the next statistic gadget; we show the TTFR % met for each combination of team and customer request type, so we can see how each team is performing in each kind of request and where potential weaknesses are. The customer request types are ordered, ascending from lowest performance to highest.

![contentId-783942775](/cms_trial/assets/2b7dbbbb-e250-45cf-a3df-047e7f1ae9d0.png)

Finally, we show a two-dimensional breakdown of the TTR % breached for each organization and service management project combination.

![contentId-783942775](/cms_trial/assets/7598fb07-3b8d-4fdf-b17e-9d68b77ba9cb.png)

You can create data breakdowns based on whatever statistics you wish, and you can also filter any of them using the quick filters in your controller.

### Generating quick charts

You can dynamically create a quick chart to summarize the data in any statistics gadget by clicking the **Switch to quick chart view** button in the bottom-right-hand-corner:

![Switch quick chart view .png](/cms_trial/assets/9afd8e2d-98d7-4ed0-b58c-f448ca7cf61f.png)

Clicking the button displays a chart summarizing the data in the statistics table. For example:

![chart summarizing the data .png](/cms_trial/assets/b35dbf4b-b149-43cf-85d4-1a3d4ac8332c.png)

Note that chart gadgets (e.g., Rich Filter Flexi Charts, Rich Filter Time Series Chart) have a Show table button in the bottom-right-hand corner to generate quick tables from charts.

### Show historical progress against targets.

Our last category of gadgets in this dashboard provides breakdowns and views of historical data from various time series — a powerful way to check on trends and progress.

First, we've got another statistics gadget showing columns for several useful statistic types: number of created issues, TTFR % met, TTFR average, TTR % met, TTR average, and customer satisfaction. We show historic monthly totals for each statistic type in each row, with the most recent month at the top.

![show historic monthly totals.png](/cms_trial/assets/584edd4d-a152-4b14-a160-2258561bbe8d.png)

We can also provide charts to summarize our data. In a flexi chart gadget, we show the TTR % met by the team and TTR over historic weeks.

![TTRs  met by the team .png.png](/cms_trial/assets/9d015a85-6001-49da-ac5b-2fb03bc45d77.png)

Finally, we use a dedicated time series chart to show the historic weekly trends for the TTFR and TTR average in hours.

![dedicated time series.png](/cms_trial/assets/87b228a0-7297-4ad2-926a-0e6ed4e52b5a.png)

## Rich filter features resources.

The following links provide information on the fundamentals of each rich filter feature used in this dashboard in case you need more information:

- [Rich Filter Simple Gauges](/cms_trial/space/RFCDOC/783942638/Use+rich+filter+counters+and+gauges+in+your+dashboards/) will provide at-a-glance summaries of your SLA targets.
- [Rich Filter Statistics gadgets](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/) to provide one- and two-dimensional breakdowns based on configurable statistic types, including date ranges.
- [Rich Filter Flexi Charts gadgets](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/) to effectively summarize your data and show trends in a visual format.
- [Rich Filter Time Series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) allows you to precisely define custom time series (such as SLA averages) based on existing date fields, and a Rich Filter Time Series Chart gadget efficiently displays them.
- A [Rich Filter Controller gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) containing [static](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), [dynamic](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/), and [smart filters](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) enables you to filter your reporting gadgets by different dimensions.

## Start building the *Support request reporting* dashboard

Now that we've explained what our solution can do let's go ahead and build it.

In this section, you'll create a new rich filter and a dashboard with minimal configuration. If you need any instructions on creating rich filters and dashboard basics, you can find them in Get Started [with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

1. Create a new rich filter based on a Jira filter that returns all the support request issues you want to report on with your dashboard (see [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) for guidance if needed). Call it something appropriate like "Support request reporting". Remember that your Jira filter can return support request issues from multiple Service Management projects, therefore this solution has the advantage that it is cross-project.
2. Create a new dashboard with the *Left sidebar layout*, called something appropriate like "Support request reporting dashboard".
3. Add a Rich Filter Controller gadget to your dashboard.
4. Select your *Support request reporting* rich filter as the *Rich filter* value, then click *Submit*:
5. Press the *Done* button at the top of the UI to exit dashboard edit mode.

You should now have a basic dashboard that contains a single Rich Filter Controller gadget:

![single Rich Filter Controller .png](/cms_trial/assets/b5ba4785-0c0b-43c9-a2d6-a80e6a902312.png)

Important time-saving tips:

1. When you need to further configure an existing gadget, don't do it via dashboard edit mode—you can do it more quickly and with fewer dashboard refreshes using the [*rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) available on each rich filter gadget.
2. The *Rich filter menu* also contains an option to open the config for the rich filter the gadget is based on. For convenience, we recommend keeping the dashboard open in one browser tab, keeping the rich filter configuration open in another tab, and moving between the two as needed.
3. When you've changed the rich filter config in one tab and want to see those changes reflected in the dashboard in the other tab, refresh your dashboard quickly and conveniently using your controller's [*Optimized refresh*](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) [button](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Set up your filters

In this section, you will create all the quick filters you'll use in your dashboard. The static and dynamic filters will be usable from your controller and provide a lot of power — they filter the content shown in all other rich filter gadgets based on the same rich filter as the controller (for more information on static and dynamic filters, have a look at [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) and [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/)).

1. Go to the *Static Filters* tab of your rich filter config (accessed via the [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)) and create a new static filter called "Assigned to me", with the *JQL* "`assignee = currentUser()`".
2. Go to the Dynamic Filters tab and add dynamic filters based on the Jira fields — *Created*, *Priority*, *Customer Request Type*, *Organizations*, *Assignee*, *Issue Type*, and *Project.*

In our scenario, we have two support teams. Let's create a "Team" smart filter to allow you to display a quick filter in your controller to filter by team (for more information on configuring and using smart filters, see our [Use custom smart filters and smart columns on your dashboard](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/)article).

1. Go to the *Smart Filters* tab.
2. Create a new smart filter called "Team".
3. Create a separate smart clause for each team in the Team config screen. We've included two, but you might want to include more:

   1. "Green Team": Give it a green color and JQL to filter by members of that team, for example "`assignee in membersOf("green-team")`".
   2. "Orange Team": Give it an orange color and JQL to filter by members of that team, for example, "`assignee in membersOf("orange-team")`"

As an alternative to the above JQL, you might want to filter each team's JIRA issues using JQL like "`assignee in (a,b,c)`", where the letters are different assignee IDs.

Go back to your dashboard and refresh it; your controller should look like this:

![your controller .png](/cms_trial/assets/019e4aa9-92f9-4735-b888-93fa4f4e8232.png)

## Set up your time series

In this section, you'll create some custom time series that you can use in your gadgets to easily display trends over time as desired (see [Configuring Time Series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) for more information).

1. Go to the *Time Series* tab in your rich filter configuration.
2. Create a new time series called "Created", with a custom pink color.
3. Choose the **Created field** to show the Series.
4. Choose **Issue Count** for the **Base value**. This series will provide an issue count for created issues over time.
5. Click **Create**.

Repeat the process to create five more time series; choose a custom color for each one:

1. "Satisfaction": Show customer satisfaction for resolved issues over time.

   1. Color: yellow.
   2. **Series**: *Resolved*.
   3. *Base value*: *Satisfaction*.
2. "TTFR - Avg": Show average TTFR over time.

   1. Color: mid blue.
   2. *Series*: *Time to first response (completion date)*.
   3. *Base value*: *Time to first response - Average*.
3. "TTR - Avg": Show average TTR over time.

   1. Color: sky blue.
   2. *Series*: *Time to resolution (completion date)*.
   3. *Base value*: *Time to resolution - Average*.
4. "Time to first response - % Met": Show TTFR met/total over time.

   1. Color: green.
   2. *Series*: *Time to first response (completion date)*.
   3. *Base value*: *Time to first response - % Met*.
5. "Time to resolution - % Met": Show TTR met/total over time.

   1. Color: green.
   2. *Series*: *Time to resolution (completion date)*.
   3. *Base value*: *Time to resolution - % Met*.

Your *Time Series* tab should now look like this:

![Your Time Series tab.png](/cms_trial/assets/ede42e4d-5a10-4034-b6ac-912dd8328944.png)

## Set up the Rich Filter Simple Gauges gadget

Let's get your dashboard set up! You'll start by adding the Rich Filter Simple Gauges gadget (for more information on gauges, see our [Use rich filter counters and gauges in your dashboards](/cms_trial/space/RFCDOC/783942638/Use+rich+filter+counters+and+gauges+in+your+dashboards/) article).

1. Go to dashboard edit mode and add a Rich Filter Simple Gauges gadget to your dashboard.
2. Position it below your controller in the left-hand column.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. Add the following SLA ratios to the **Gauge filters and values** list by choosing them from the **Pick a filter** dropdown.

   1. **Time to first response - % Met**
   2. **Time to resolution - % Met**
5. Click **Submit**.

Your Rich Filter Simple Gauges gadget will now look like this:

![time to first response (TTFR).png](/cms_trial/assets/f46696ed-1467-4657-bcb1-4a6f846945df.png)

## Set up the first Rich Filter Statistics gadget

Next, you'll add a Rich Filter Statistics gadget, which provides a simple breakdown of issue count, TTR % breached, and customer satisfaction by team (for further information on one- and two-dimensional statistics, see [Display statistics and quick charts on your dashboard](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/)).

1. Go to dashboard edit mode and add a Rich Filter Statistics gadget to your dashboard.
2. Position it below your Rich Filter Simple Gauges gadget in the left-hand column.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. In **Breakdown by** > **Statistic type**, select your **Team** smart filter.
5. Choose the following *Values* in the **Pick a value** dropdown:

   1. **Issue Count**
   2. **Time to resolution - % Breached**
   3. **Satisfaction**
6. Click **Submit**.

Your left-hand Rich Filter Statistics gadget should look like this:

![satisfaction for each of our teams.png](/cms_trial/assets/a4a252e4-dc95-43ed-87f4-ec0ea457462a.png)

## Set up the first Rich Filter Two Dimensional Statistics gadget

Now, you'll add a Rich Filter Two-Dimensional Statistics gadget, which will provide a breakdown of TTFR (met) by team and customer request type.

1. Go to dashboard edit mode and add a Rich Filter Two-Dimensional Statistics gadget to your dashboard.
2. Position it below your Rich Filter Statistics gadget in the left-hand column.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. In **Horizontal breakdown** > **Statistic type**, select your **Team** smart filter.
5. In **Vertical breakdown** > **Statistic type**, select **Customer Request Type**.
6. In **Vertical breakdown** > **Sort by**, select **Total**.
7. Check the **Vertical breakdown** > **Reverse sort order checkbox** to see the customer request types with the worst performance (lowest totals) at the top of the list.
8. In the **Value** dropdown, select **Time to first response - % Met**.
9. Click **Submit**.

Your left-hand Rich Filter Two-Dimensional Statistics gadget should look like this:

![contentId-783942775](/cms_trial/assets/2b7dbbbb-e250-45cf-a3df-047e7f1ae9d0.png)

## Set up the second Rich Filter Two Dimensional Statistics gadget

To provide useful variety in reporting, you will now add another Rich Filter Two Dimensional Statistics gadget. This gadget will provide a breakdown of TTR % breached by organization and project.

1. Go to dashboard edit mode and add another Rich Filter Two-Dimensional Statistics gadget to your dashboard.
2. Position it at the top of the right-hand column.
3. In the gadget config form, select your *Support request reporting* rich filter in the *Rich filter* dropdown.
4. In **Horizontal breakdown** > **Statistic type**, select **Organizations**.
5. Check the **Horizontal breakdown** > **Filter out None** checkbox. In this case, it is not useful to see information on issues irrelevant to any organization.
6. In **Vertical breakdown** > **Statistic type**, select *Project*.
7. In the **Value** dropdown, select **Time to resolution - % Breached**.
8. Click **Submit**.

Your right-hand Rich Filter Two-Dimensional Statistics gadget should look like this:

![contentId-783942775](/cms_trial/assets/7598fb07-3b8d-4fdf-b17e-9d68b77ba9cb.png)

## Set up the second Rich Filter Statistics gadget

Your next gadget will be another Rich Filter Statistics gadget. With this, you'll see how powerful rich filters can be for showing trends over time: let's play with some time series. This gadget will provide a breakdown over time of created issues, TTFR % met, average TTFR, TTR % met, average TTR, and customer satisfaction — all by month.

1. Go to dashboard edit mode and add another Rich Filter Statistics gadget to your dashboard.
2. Position it in the right-hand column below the Rich Filter Two-Dimensional Statistics gadget.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. In **Breakdown by** > **Statistic type**, select **Time series**. This means you'll choose a time series to display trends over time in this gadget.
5. Select Months for Aggregation periods — we want to show a data breakdown by each month.
6. In the fields below, select **Time range: Number of months, Number: 6, Direction: Past**. We want to show totals for each of the last six months.
7. Check the **Reverse sort order** checkbox so that the most recent month appears at the top of the list.
8. Choose the following **Time series** in the **Pick a time series***...* dropdown:

   1. **Created**
   2. **Time to first response - % Met**
   3. **TTFR - Avg**
   4. **Time to resolution - % Met**
   5. **TTR - Avg**
   6. **Satisfaction**
9. Click **Submit**.

Your right-hand Rich Filter Statistics gadget should look like this:

![show historic monthly totals.png](/cms_trial/assets/584edd4d-a152-4b14-a160-2258561bbe8d.png)

## Set up the Rich Filter Flexi Charts gadget

Now, you'll add a Rich Filter Flexi Charts gadget; you'll use this to create a clustered bar graph showing the percentage of issues that the TTR met over a historical series of weeks for each team. If you need more guidance on setting up flexi charts, look at [Display custom charts and quick tables on your dashboard](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/).

1. Go to dashboard edit mode and add a Rich Filter Flexi Charts gadget to your dashboard.
2. Position it in the right-hand column below the Rich Filter Statistics gadget.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. For the **Chart type**, choose the **Clustered** *bar*.
5. In **Primary Breakdown** > **Statistic type**, select **Time to resolution (completion date)**.
6. For **Aggregation periods**, select **Weeks**.
7. In the fields below, select **Time range: Between dates**, then choose **From** and **To** dates that encapsulate your data range nicely.
8. In **Secondary Breakdown** > **Statistic type**, select **Team**.
9. For **Value**, choose **Time to resolution - % Met**.
10. Click **Submit**.

Your Rich Filter Flexi Charts gadget should look like this:

![TTRs  met by the team .png.png](/cms_trial/assets/9d015a85-6001-49da-ac5b-2fb03bc45d77.png)

## Set up the Rich Filter Time Series Chart gadget

Finally, you'll add a Rich Filter Time Series Chart gadget. This will show a handy line graph of the historical average TTFR and TTR trends (for more information on configuring time series gadgets, see [The Rich Filter Time Series Chart Gadget](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/)).

1. Go to dashboard edit mode and add a Rich Filter Time Series Charts gadget to your dashboard.
2. Position it in the right-hand column below the Rich Filter Flexi Charts gadget.
3. In the gadget config form, select your **Support request reporting** rich filter in the **Rich filter** dropdown.
4. For **Aggregation periods**, select **Weeks**.
5. In the fields below, select *the* **Time range**, **Number of weeks**, **Number 12**, and **Direction**, **Past**.
6. For **Time series**, select **TTFR - Avg and TTR - Avg**.
7. Click **Submit**.

Your Rich Filter Time Series Chart gadget should look like this:

![dedicated time series.png](/cms_trial/assets/87b228a0-7297-4ad2-926a-0e6ed4e52b5a.png)

Time series gadgets allow you to report on multiple date fields in the same chart, as seen in this example.

## Final result

![Final result service management reports.png](/cms_trial/assets/47f3e12c-9f67-4e29-b6fa-51ef958769a4.png)