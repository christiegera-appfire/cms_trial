# Display date/time statistics and charts on your dashboard

In this article, you will explore the usage of date and datetime fields in rich filter [statistics](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/) and [chart](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/) gadgets. After you finish the basics, you will learn about the rich filter **Time Series** feature. Time series are based on date/datetime fields, allowing you to compare trends and hint at correlations efficiently. Once defined, time series can be reused across different gadgets — including statistics and chart gadgets and the **Rich Filter Time Series Chart** gadget. Finally, you'll look at the **Rich Filter Created vs Resolved Chart** gadget.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of [statistics](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/) and [charts](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/) gadgets.

## Final result

Once you've worked through the steps in this tutorial, you should have a dashboard that contains examples of all the rich filter gadget types that can display statistics and charts based on date and DateTime fields:

- Rich Filter Statistics gadget
- Rich Filter Two-Dimensional Statistics gadget
- Rich Filter Flexi Charts gadget
- Rich Filter Time Series Chart gadget
- Rich Filter Created vs. Resolved Chart gadget

![contentId-783942921](/cms_trial/assets/932ca92b-eb7b-4c5e-acc2-4ddc0c55f6f5.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in our [Learning Center](/cms_trial/space/RFCDOC/783942482/User+guides/), you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters linked at **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the **Left sidebar** layout. You can set this using the **Change layout** menu at the top of the dashboard.

   ![Left sidebar.png](/cms_trial/assets/ee9e6f6f-d565-48de-b9d3-883dae48848c.png)
4. Based on your rich filter, add a Rich Filter Controller gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving your gadget's configuration, make sure the controller is in the left-hand column; drag and drop it if necessary.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Recap: Use "option-based fields" in gadgets

When you configure a Rich Filter Statistics or Flexi Charts gadget to display statistics based on an "option-based field" (meaning a field with a specific finite number of options, such as *Assignee,* *Status,* or *Labels*) or a [smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/), the config options specific to those field types are pretty straightforward, including *Sort By* (e.g., *Alphabetical*) and Maximum rows/columns to display. You can find many examples of statistics and chart gadgets using "option-based fields" in [Display statistics and quick charts on your dashboard](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/) and [Display custom charts and quick tables on your dashboard](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/).

## Use dates in statistics and charts

Statistics and charts based on date and datetime fields (e.g., *Created*, *Resolved*, or custom date and datetime fields) work differently from those using "option-based" fields.

In all gadgets displaying statistics and charts based on dates, rich filters provide a powerful, flexible, and intuitive configuration mechanism that allows you to easily pick the aggregation periods (days, weeks, months, etc.), the time range to be displayed as a fixed or relative time window, and rules for displaying and aggregating data over time.

Let's walk through a demo to show you how this works.

1. Add a **Rich Filter Statistics gadget** to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)), and position it underneath your controller.
2. Set your new gadget's *Rich filter* field to the same Rich filter that your controller is based on.
3. In the **Statistic type** dropdown, choose **Created.** Since this is a date field, you have the following options to configure it.

   ![breakdown by.png](/cms_trial/assets/be170bde-0a9b-4c7d-a1d4-c757f15a97aa.png)
4. Let's explore each option in turn:

   1. **Aggregation periods**: This allows you to choose whether you want to show value totals per day, week, month, quarter, or year. There is also a special value, *Auto*, which leaves it up to the rich filters app to choose the most suitable *Aggregation periods* and *Time range* values to show a granular-but-complete statistic set for your data.
   2. **Time range**: This allows you to set the time range over which you want to show your aggregation periods. The options are as follows:

      1. **Number of <aggregation-period>**: Choose a set number of aggregation periods to display, for example the option will be *Number of days* if your chosen *Aggregation period* is *Days*. When this option is selected, two additional fields appear, which also need to be configured:

         - **Number**: The number of aggregation periods you want to display. You can choose to display up to 100 periods at once.
         - **Direction**: Whether you want to show aggregation periods in the *Past* (from the present date backward), *Future* (from the present date forward), or *Past & future* (backward and forward, with the present date in the middle).
      2. **Between dates**: Choose a specific start and end date for the time range you wish to display. When this option is selected, two additional fields appear, which also need to be configured:

         - **From**: The start date.
         - **To**: The end date.
      3. **All dates**: Dynamically display aggregation periods of the chosen type that span a time range covering all the existing values in the date/datetime field used as the breakdown (i.e. the *Statistic type*; *Created in this example*). This is particularly powerful when combined with a dynamic filter based on the same date field in the controller; it allows you to dynamically change the displayed time range.
      4. **This <aggregation-period>** and **Last <aggregation-period>**: For convenience, you can also display data over contextual predefined time ranges. For example, when *Months* is chosen as the *Aggregation period*, the options provided in the *Time range* dropdown are *This quarter*, *This year*, *Last quarter*, and *Last year*.
   3. **Reverse sort order**: This checkbox controls whether you want to display the data going forwards with the oldest date at the start (unchecked, the default), or going backwards with the newest date at the start (checked).
   4. **Show empty periods**: This checkbox controls whether you want to display periods when no items were created.
   5. **Show percentage bars**: This checkbox controls whether percentage bars are shown in the resulting statistics gadget alongside the values for each aggregation period.
   6. **Show totals**: This checkbox controls whether a *Total* row is shown at the bottom of the statistics table.
5. For now, choose:

   - **Aggregation periods** value of **Weeks**
   - **Time range** of **Number of weeks**.

     - **Number** of **6**
     - **Direction** of **Past**.   
       This will cause the statistics gadget to display the last 6 weeks of data.
6. Check the **Reverse sort order** checkbox.   
   This will display the data in reverse chronological order, with the most recent week in the top row.
7. In the **Values** section, choose **Issue Count** and **Story Points** from the **Pick a value ...** dropdown.   
   The configuration of your gadget should look like this:

   ![breakdown setup.png](/cms_trial/assets/7190fcb2-817d-4bce-aa76-26e004f9246d.png)
8. Click **Submit**. Your gadget should look like this:

   ![created statistics.png](/cms_trial/assets/81604d06-02eb-496f-a13b-f5f3d159e180.png)

This looks good so far. You've generated a table of created issue count and story point values for each of the last six weeks.

## Use dates in two-dimensional statistics

Date and DateTime fields can be used in Rich Filter Two-Dimensional Statistics gadgets in much the same way as above to provide a useful breakdown of your data across a specified time range. Let's look at an example.

1. Add a **Rich Filter Two-Dimensional Statistics** gadget to your dashboard and place it at the top of the right-hand column.
2. Base it on the same rich filter as your other gadgets.
3. For the **Horizontal breakdown**, select a **Statistic** type of **Assignee**.
4. For the **Vertical breakdown**, choose **Resolved** (the resolution time of the issues) as the **Statistic type**.
5. For **Resolved's Aggregation periods** value, choose **Months**.

   1. Choose a **Time range** of **Between dates**, and select the last three months using yours From and To inputs.
6. Again, check the **Reverse sort order** checkbox.
7. For **Values**, choose **Story Points**.
8. Click **Submit**. Your gadget should look like this:

   ![resolved two dimentional statistics.png](/cms_trial/assets/a4edca79-5a23-4b92-8040-dc4b4575d11d.png)

This is a useful follow-up to the previous example. You can review the resolved story points for each team member during a specific time period—Q1 2023 in our example screenshot. The *Between dates* time range is useful for selecting a specific fixed time period to show data for.

## Use dates in flexi charts

You can use date/datetime fields in Rich Filter Flexi Charts gadgets in much the same way as in statistics gadgets to provide informative visual summaries of trends over time. Let's take a look.

1. Add a **Rich Filter Flexi Charts** gadget to your dashboard and place it in the left-hand column at the bottom.
2. Base it on the same rich filter as your other gadgets.
3. For the **Chart type**, select **Stacked bar**.
4. Select **Due date** for **Primary breakdown** > **Statistic type**.
5. The date-related settings are mostly the same as for the statistics gadget types. Select the following:

   1. **Aggregation periods**: **Months**
   2. **Time range**: **All dates**
6. There is one setting particular to chart gadget types, hence you've not seen it before: Aggregation type. Let's explain the possible values:

   - **Period value**: The default — for each aggregation period shows the individual value.
   - **Cumulative trend**: For each aggregation period, show the total value from the start of the time range displayed in your gadget up until the end of the period.
   - **Cumulative total**: For each aggregation period, show the total value from the start of your data up until the end of the period.
7. Choose **Cumulative total** for the **Aggregation type**.
8. Select **Status Category** for **Secondary breakdown** > **Statistic type**.
9. Select **Issue Count** for the **Value**.
10. Click Submit. Your gadget should look like this:

    ![flexi charts.png](/cms_trial/assets/ac106667-3f4a-4258-8f37-a98dfbf0fccf.png)

The chart displays issues based on their *Due date*; for each aggregation period, you can see the number of issues in each status category — *To Do*, *In Progress*, and *Done*. The above screenshot was taken in April 2023 — you can see how many of the issues due in April were done, in progress, or still in the backlog. If you look at the previous aggregation period — March 2023 — you'll see issues still not due in March; hence, they are overdue. The target is always to complete all the due issues so that nothing remains overdue by the end of each month.

The gadget uses the *Cumulative total* setting, hence the total displayed for April contains the issues due in all previous periods. Similarly, in May, you'll see all the issues due until the end of May, including those from previous months.

You can use any [static](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), [dynamic](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/), or [smart filters](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) present in your controller to filter other gadgets based on the same rich filter as the controller. For example, you could filter by team or assignee to pinpoint the source of the overdue issues.

## Create time series

Rich filters provide the Time Series feature, which allows you to predefine custom time series that can then be used in multiple relevant gadgets as desired, and also provides some useful customization options such as custom color and per-time series JQL filter.

Time series can be used in Rich Filter Statistics, Rich Filter Two Dimensional Statistics, Rich Filter Flexi Charts, and Rich Filter Time Series Chart gadgets.

You'll start by creating "Due features", "Resolved features", and "Created bugs" time series — these will provide interesting tracking data for different types of work you are interested in and their evolution over time. Later, you'll use them to create a chart to study potential correlations between them.

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Select the *Time Series* tab and click the **Create Time Series** button.
3. In the resulting dialog box, you'll see a series of settings:

   - **Name**: An identifying name for your time series. Enter `Due features`.
   - **Color**: A custom color. Choose one that suits you. We chose a light blue color.
   - **Series**: A date/datetime field on which the time series will be based. Choose the **Due date**.
   - **Base value**: The value that will be counted for this time series in each aggregation period. Choose **Issue Count**.
   - **JQL**: A specific JQL query that filters the data for this time series. Enter`type = "New Feature"`.
4. Click **Create**.
5. Create two more time series:

   - `Resolved features`

     - **Color**: Choose a green color
     - **Series**: Choose **Resolved**
     - **Base value**: Choose **Issue Count**
     - **JQL**: Enter `type = "New Feature"`.
   - `Created bugs`

     - **Color**: Choose red.
     - **Series**: Choose **Created**.
     - **Base value**: Choose **Issue Count**.
     - **JQL**: Enter `type = Bug`.
6. Your *Time Series* tab should now look like this. Check it before you move on.

   ![time series.png](/cms_trial/assets/f9b3a739-86ab-46a4-8f78-3e02d7d1124c.png)

You can also base your time series on date/datetime custom fields or define computed time series such as *Unresolved* (computed as the difference between two-time series: *Created* and *Resolved*). If you use [Jira Service Management](https://www.atlassian.com/software/jira/service-management), you can also use the completion date of SLA fields such as *Time to first response*. Your base value can be *Issue Count*, a *Numeric* or *Time Tracking* field, or a custom value.

## Display time series in a Rich Filter Time Series Chart gadget

To display our time series, as a first example, you will use a new type of gadget — the **Rich Filter Time Series Chart** gadget. This gadget allows you to compare time series based on multiple date/datetime fields, each time series potentially with its own JQL query applied; the results are displayed as (multi-)line graphs.

This demonstrates that the time series feature is an effective and convenient way to pre-package your configuration for date/datetime statistics and charts, which can be reused in multiple places. Comparing time series is a very commonly requested use case, and we wanted to make it as quick and easy as possible.

Let's create a chart comparing the cumulative trend of *Due features*, *Resolved features*, and *Created bugs* over 12 weeks.

1. Go back to your dashboard.
2. Add a **Rich Filter Time Series Chart** gadget to the bottom of the left-hand column of your dashboard.
3. Base it on the same rich filter as your other gadgets.
4. Choose **Aggregation periods** of **Weeks**, **Time range** of **Number of weeks**, and **Number** **12**.
5. Select **Cumulative trend** from the **Aggregation type** dropdown.
6. Choose your **Due features**, **Resolved features**, and **Created bugs** time series from the **Pick a time series...** dropdown.
7. Click **Submit**. Your time series chart should look like this:

   ![time series chart.png](/cms_trial/assets/85f9aeee-e6ca-4112-b67d-722bb8988193.png)

That was quick and easy, and you ended up with a chart that allows you to study the correlation between the different time series. For example, you can look for points where the number of resolved features became less than the number of due features and think about potential causes. One possible cause is that more work was done on fixing bugs in those periods, taking time away from developing new features. Maybe the created bugs time series can provide some answers?

As with other rich filter chart gadgets, you can hover over data points to get tooltips providing more details.

![chart details.png](/cms_trial/assets/c7f74841-7d98-4da6-a2d3-6fd7a026a0f4.png)

Rich Filter Time Series Chart gadgets also have a Show table button:

![show table.png](/cms_trial/assets/04bc6690-a806-4ed0-8a29-b87cefe09b4d.png)

Clicking this generates a quick table showing the chart data in detail, displayed at the bottom of the same gadget:

![Rich filter time series chart gadget quick table, showing exact numbers for Due features, Resolved features, and Created bugs, for 12 separate weeks](/cms_trial/assets/c2341d5a-3da6-47cb-8282-60e0ba531782.png)

The Rich Filter Time Series Chart gadget allows you to compare time series that return the same type of value, such as Issue Count or numeric, time tracking, or duration values.

## Use time series in statistics gadgets

Using time series is not limited to Rich Filter Time Series Chart gadgets; you can also use them in other gadget types. In this section, you'll create a Rich Filter Statistics gadget showing a number of time series indicating the count of created and unresolved issues each month over four months, along with the story point value of the unresolved issues, the average resolution time, and the average resolution time of bugs specifically.

A major advantage of using time series in Rich Filter Statistics gadgets is that you can display time series with different base values in the same gadget. You can pretty much compare anything against anything in the same aggregation periods.

To begin this section, you will create a [custom value](/cms_trial/space/RFCDOC/783942682/Use+custom+values+in+your+dashboards/) that will later be used as a base value for two of the time series you will create.

1. Open your rich filter config (described in [Easier configuration with the Rich filter menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Select the *Custom values* tab, and click **Create custom value**.
3. In the resulting dialog box, enter the following values:

   - **Name**: Enter `Resolution time`
   - **Color**: Choose a green color
   - **Base value**: Choose **Issue age / resolution time**
   - T**otal formula**: Choose **Average value**
   - **Duration display format**: choose **Days**
   - **JQL**: Enter `resolution is not EMPTY`
4. Click **Submit**. Your Custom values tab should now look like this:

   ![custom resolution time value.png](/cms_trial/assets/be60daff-aa07-41df-81d9-92c1259f30f8.png)

   Next, you'll create more time series for your statistics. Note how the *Res time (avg)* and *Bug res time (avg)* time series are based on the *Resolution time* custom value created above.
5. Go to your rich filter config *Time series* tab.
6. Create the following five-time series:

   - `Created`

     - **Color**: Orange.
     - **Series**: **Created**.
     - **Base value**: **Issue Count**.
     - **JQL**: Leave blank.
   - `Unresolved`

     - **Color**: Red.
     - **Series**: **Unresolved (created minus resolved issues)**
     - **Base value**: **Issue Count**
     - **JQL**: Leave blank
   - `Unresolved SP`

     - **Color**: Red.
     - **Series**: **Unresolved** **(created minus resolved issues)**
     - **Base value**: **Story Points**
     - **JQL**: Leave blank
   - `Res time (avg)`

     - **Color**: Green
     - **Series**: **Resolved**
     - **Base value**: Choose your **Resolution time** custom value
     - **JQL**: Leave blank
   - `Bug res time (avg)`

     - **Color**: Blue
     - **Series**: **Resolved**
     - **Base value**: Choose your **Resolution** time custom value
     - **JQL**: Enter `type = Bug`
7. Your *Time Series* tab should now look like this.

   ![time series set.png](/cms_trial/assets/e3eb2384-bb37-46c0-a5ac-6a342b65bcba.png)

Now, you'll use your new time series in a statistics gadget.

1. Go back to your dashboard.
2. Add a **Rich Filter Statistics** gadget to your dashboard and position it at the bottom of the right-hand column.
3. Set your new gadget's *Rich filter* field to the same Rich filter that your controller is based on.
4. In the **Statistic type** dropdown, choose the new **Time series** option, which appears when you have time series available to use.
5. You need to select the **Aggregation** periods over which you will show your time series. Enter the following:

   - **Aggregation periods**: **Months**
   - **Time range**: **Number of months**
   - **Number**: **4**
6. Check the **Reverse sort order** checkbox.
7. Instead of the Pick a value... dropdown at the bottom of the form, you'll now see a **Pick a time series...** dropdown. Select **Created**, **Unresolved**, **Unresolved SP**, **Res time (avg)**, and **Bug res time (avg)**.
8. Click **Submit**. Your gadget should now look like this:

   ![statistics time dashboard.png](/cms_trial/assets/1247af91-d7e6-4bce-ab18-ddaaf0ead90b.png)

   The custom time series names are used as column headings, and your chosen colors are used in the percentage bars.

It is also worth looking at how these custom time series are used in the associated quick chart view (click the *Switch to quick chart view* button in the bottom-right of the gadget).

## Use time series in flexi charts

You can also use time series in Rich Filter Flexi Charts gadgets. In this example, you will use a clustered bar graph to split the *Unresolved SP* time series, showing the number of unresolved story points for multiple teams separately over time.

1. First, create a Teams smart filter as shown in [Create a Teams smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).
2. Add a **Rich Filter Flexi Charts** gadget to your dashboard and position it at the bottom of the right-hand column.
3. Set your new gadget's *Rich filter* field to the same Rich filter that your controller is based on.
4. Choose the **Clustered bar** in the **Chart type** dropdown.
5. Select the **Unresolved SP** time series in the **Primary breakdown** > **Statistic type** dropdown.

Both Rich Filter Flexi Charts and Rich Filter Two-Dimensional Statistics gadgets allow you to select a time series as a breakdown and then use a second breakdown to split that time series.

1. Select the following values for the Aggregation periods fields:

   - **Aggregation periods**: **Weeks**
   - **Time range**: **Last quarter**, choosing this predefined value is a useful way of ensuring you will always see the last quarter of data, even as time progresses.
   - **Aggregation type**: **Cumulative** **total**
2. Select the **Teams** smart filter in the **Secondary breakdown** > **Statistic type** dropdown.
3. Click **Submit**. Your gadget should now look like this:

   ![teams chart.png](/cms_trial/assets/cef12b85-032b-47a7-8838-f311e263c3a5.png)

This shows the power of flexi charts in this context — you can create a single time series and then easily split it by another dimension, enabling it to do the job of many different time series.

You can also use time series in Rich Filter Two Dimensional Statistics gadgets, where the configuration is fairly similar to two-dimensional flexi charts.

## Rich Filter Created vs. Resolved Chart gadgets

To finish, you will look at another gadget type — the **Rich Filter Created vs Resolved Chart** gadget. This gadget displays a very specific type of time series chart to fulfill another common use case in reporting — showing created issues versus resolved issues over time. For this gadget, the time series are already built in.

Let's explore this to see how it works.

1. Add a Rich Filter Created vs Resolved Chart gadget to your dashboard and place it at the bottom of the right-hand column.
2. Base it on the same rich filter as your other gadgets.
3. Choose **Aggregation periods** of **Weeks**, a **Time range** of **Number of weeks**, and **Number 12**.
4. Choose **Cumulative total** for the **Aggregation type**.
5. Choose **Issue Count** for the **Value**.
6. Check the **Unresolved trend** checkbox. This displays an additional line graph underneath the main graph, showing the difference between created and resolved for each aggregation period.
7. Click **Submit**. Your created vs resolved chart should look like this:

   ![created vs resolved.png](/cms_trial/assets/5ffbb1cd-2394-4d46-9e51-dad14ea967b9.png)

   The Rich Filter Created vs Resolved Chart has other useful features. Most notably, the sections of the graph where *Created* > *Resolved* are colored red, and the sections where *Resolved* > *Created* are colored green, making it easy to analyze the trends.