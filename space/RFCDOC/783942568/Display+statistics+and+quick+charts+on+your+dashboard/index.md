# Display statistics and quick charts on your dashboard

A key feature of Jira dashboards is displaying your data through statistics and charts for effective, at-a-glance reporting. This article demonstrates related features available in Rich Filters for Jira Dashboards, namely statistics gadgets. You'll use **Rich Filter Statistics** and **Rich Filter Two-Dimensional Statistics** gadgets to generate statistics on your dashboard and display **quick charts** on the fly.

## Before you start

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Final result

When you've worked through all the steps in this tutorial, you should have a dashboard that contains two statistics gadgets:

- A Rich Filter Statistics gadget shows each Assignee's issue count and story points.
- A Rich Filter Two-Dimensional Statistics gadget that shows the time spent for each combination of Priority and Status.

The two statistics gadgets, which are the focus of this tutorial, can be seen on the right of the image below. The gadgets on the left (Rich Filter Controller and Rich Filter Results) have already been covered in previous tutorials.

![2026-02-19_09-04-14.png](/cms_trial/assets/c2ef1646-0e1d-481f-8286-96bc0301d98e.png)

Both statistics gadgets can also display quick charts, giving you easy access to a visual summary of the data: these are accessed by clicking the chart button in the bottom-right corner of the statistics gadgets. The image below shows some examples:

![2026-02-19_08-30-20.png](/cms_trial/assets/667b9194-e49c-4028-bc62-6fe3ef607023.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the **Two-columns** layout. This is usually the default setting, but you can select it if required using the **Change layout** menu at the top of the dashboard.

![two column layout.png](/cms_trial/assets/04b6ec26-1ada-42da-bf0d-3355c6c486bd.png)

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Create one-dimensional statistics

Rich Filter Statistics gadgets allow you to display a table showing a breakdown based on a configurable statistic type.

Let's create a gadget showing each Assignee's issue count and story points.

1. Add a **Rich Filter Statistics** gadget to your dashboard ([Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) that explains how to add gadgets).
2. Move the gadget to the right-hand column of your dashboard by dragging and dropping it.
3. There are several fields you should configure in the gadget config form:

   1. **Rich filter**: Set this to your rich filter.
   2. **Breakdown by** > **Statistic type**: This statistics gadget will show a breakdown by assignees, so select **Assignee** in the *Statistic type* dropdown.
   3. **Values**: For each Assignee, let's show the number of issues assigned to them and the number of story points they have. Choose **Issue Count** and **Story Points**.
4. Click **Submit**.

   ![image-20240506-142231.png](/cms_trial/assets/3acf468d-8e07-49bc-b0a5-2a18652a5e2f.png)

   Your Rich Filter Statistics gadget shows each assignee's issue count and story points.

   ![2026-02-19_08-33-53.png](/cms_trial/assets/402be593-a077-4823-9acf-f8dfd5ba5b29.png)

At this point, you should be in dashboard edit mode. At any point, you can click the *Done* button at the top of the dashboard to exit dashboard edit mode and see the final layout of your dashboard. You can re-enter dashboard edit mode by clicking the **Edit** button at the top of the dashboard.

## Manipulate your statistics display

In this case, the rows are sorted alphabetically by **Assignee**. As with tables in rich filters, you can sort the statistics view by other columns by clicking the column heading.

![2026-02-19_08-35-05.png](/cms_trial/assets/5198f6a9-dbc7-4330-b30d-125adcbd3709.png)

You can toggle between descending and ascending order by clicking the column heading multiple times.

Be aware that the *Unassigned* row always appears at the end of the statistic table, regardless of sorting.

The Rich Filter Statistics gadget config form offers several options if you want to change the default display.

1. Return to your Rich Filter Statistics gadget config form (see [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Configure the more advanced following options, following the instructions:

   1. **Filter out None**: If this option is selected, issues with the statistic type empty (in this case, *Unassigned*) won't be included in the statistics. Check the box.
   2. **Sort by**: This dropdown offers different values depending on the chosen statistic type.   
      Select the **Total** option. This will sort the table in descending order by the first **Value** column available, which in our case is **Issue Count**.
   3. **Reverse sort order**: reverses the default sort order of the option chosen in **Sort by**. Check the box.
   4. **Show percentage bars:** Shows or hides the percentage bars in the display. Uncheck this box.
   5. **Show totals**: Shows or hides the **Total** row. Uncheck this box.
3. Your config options should look like the following image. Check they are correct, then click **Submit**.

   ![image-20240506-142400.png](/cms_trial/assets/dd04180d-0113-44f0-be90-d3afa37243ae.png)

   Your Rich Filter Statistics gadget should end up with a simpler, more compact display, which might be preferable in some situations, depending on what information you need. Feel free to play around with these settings until you get a data display that you are happy with.

![2026-02-19_08-36-26.png](/cms_trial/assets/125f31b6-044a-48da-80af-59d591e41208.png)

You can find more information on the configuration options available for different gadgets in our Working with Rich Filter Gadgets reference articles, such as [The Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/).

## Create two-dimensional statistics

Rich Filter and Two-Dimensional Statistics gadgets allow you to display a table showing a two-dimensional data breakdown based on two configurable statistic types.

In this case, we'll create a data table showing the time spent for each issue priority and status combination.

1. Add a **Rich Filter Two-Dimensional Statistics** gadget to your dashboard.
2. Move the gadget to the right-hand column of your dashboard, below the first statistics gadget, by dragging and dropping it. We'll add other features to the left-hand column later on.
3. There are several fields you should configure in the gadget config form:

   1. **Rich filter**: Set this to the same rich filter that your other statistics gadget is based on.
   2. **Horizontal breakdown** > **Statistic type**: We'll show the different statuses as columns in the table — select **Status** in this dropdown.
   3. **Vertical breakdown** > **Statistic type**: We'll show the different issue priorities as rows in the table — select **Priority** in this dropdown.
   4. **Value**: We'll show the time spent on each issue and the combination of Priority and Status. Choose **Time Spent** in this dropdown.
4. Your Rich Filter Two-Dimensional Statistics gadget config form should look like the following image. Check it is correct, then click **Submit**.

   ![image-20240506-142537.png](/cms_trial/assets/a5db0ebd-31da-4c51-ac75-51835672ef23.png)

   Your Rich Filter Two-Dimensional Statistics gadget displays a data table of time spent for each issue priority and status combination.

   ![2026-02-19_08-40-51.png](/cms_trial/assets/6bf5436d-7c89-495c-b444-ae26dc0290bb.png)

   Before you move on, you should note the following:

- Rich Filter Two-Dimensional Statistics gadgets can be sorted by ascending and descending column *and* row values by clicking the arrow controls in the column and row headings.

  ![2026-02-19_08-43-37.png](/cms_trial/assets/8a18cebd-4969-408a-8349-4ec035d2a0c6.png)
- Clicking the heading value brings up the list of issues corresponding to that column/row in a separate browser tab.
- You can clear all the applied sorting by clicking the x button that appears in the top-left corner of the table after sorting has been used.
- Rich Filter Two-Dimensional Statistics gadgets also have several options for manipulating the display of your data. We won't go through these in detail here, as they are very similar to the config options for one-dimensional Rich Filter Statistics gadgets. Still, we'd advise you to go back into your gadget config form, play around, and see how they affect the data display.

## Filter statistics using a controller

You'll notice how connected everything is as you use Rich Filters for Jira Dashboards more. With this in mind, let's look at filtering your statistics display using a Rich Filter Controller gadget.

1. Add a **Rich Filter Controller** gadget to your dashboard using the **Add a Gadget** side panel.
2. Drag it to the left-hand column of the dashboard if it hasn't already been placed there.
3. In the controller config form, set the **Rich filter** to match the Rich filter used by your other gadgets, and click **Submit**.

If you use a rich filter from a previous tutorial, you already have some filters on your controller. If you created a fresh new rich filter for this tutorial:

- Create some static filters, as shown in [Add some static filters to your controller](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- Creating some dynamic filters. You can find out how to [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).

Try applying some filters in the controller. Note how they filter issues inboth statistics gadgets.

![2026-02-19_08-45-09.png](/cms_trial/assets/96196468-bda0-48ac-955c-3ded5375998f.png)

Remember that controllers filter the information shown in *all* gadgets using the same rich filter!

## Display quick charts

Statistics gadgets have quick charts available. They are generated directly from the statistics without requiring any configuration. Quick charts are displayed by clicking the chart button in the bottom-right corner of the gadget.

Click the **Chart button** (▢) to display a donut chart showing the number of issues per Assignee.

![2026-02-19_08-46-42.png](/cms_trial/assets/da210def-3003-4245-987f-f33ee929c8a7.png)

When you click the chart button to display it, it turns into a table button, which can be clicked to return to the table view.

1. Click the **Donut chart** text at the bottom of the gadget to bring up several different chart options. You can also click the **Issue Count** text to change the data shown to one of the other values in the table. From these options, you can choose a Bar chart and Story Points.

   ![2026-02-19_08-47-30.png](/cms_trial/assets/b02a47c7-85de-4661-be15-3a9638109b39.png)
2. The different chart types all have interactive features. For example, in the bar chart, you can hover over the columns to display tooltips with exact values and click the assignee names or their bars/slices to load up lists of all the associated issues in a separate tab.

   ![bar chart story points.png](/cms_trial/assets/7fa3f713-d1b1-447b-9fd9-08b583dcded7.png)
3. Enable **Show values** in the **Three-dot menu** (▢) to display numeric values directly on the chart when space allows.

   ![2026-02-19_08-49-17.png](/cms_trial/assets/a1697820-2473-4094-b71a-b9889d5f2eaa.png)

The slices or bars are displayed in the same order as the table. If you want to change the order, switch to the table view, change the sort order by clicking on the column headers, and then switch back to the chart view.

The examples shown above are all taken from the Rich Filter Statistics gadget. Rich Filter Two-Dimensional Statistics quick charts work in the same way, with a couple of notable differences:

- The chart types are different, with types such as clustered bar charts that are relevant to two-dimensional statistics.
- The chart shows a breakdown by two statistic types — in our case, **Priority**and**Status** — and choosing which one appears across the x-axis and within the legend is possible. You can swap the two by clicking the **< >** button between the two statistic types. This is illustrated below.

![Click to swap.png](/cms_trial/assets/aff2b1e5-182c-4351-9386-f6b327a2d84d.png)

## Further exercises

To add further power to the dashboard, we put a Rich Filter Results gadget in our final example in the left-hand column below the Rich Filter Controller gadget. To complete the tutorial, we'd like you to do the following:

1. Add a Rich Filter Results gadget to your dashboard below your controller gadget based on the same rich filter (Create a simple dashboard explaining how to do this).
2. Add two views to your Rich Filter Results gadget as described in [Customize issue views and gadget scope](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/).

Your dashboard should look like this:

![2026-02-19_09-04-14.png](/cms_trial/assets/c2ef1646-0e1d-481f-8286-96bc0301d98e.png)

As a further exercise, we encourage you to explore using smart filters in your statistics. [Smart filters](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) allow you to filter and group your issues using configurable smart clauses based on JQL and also have the advantage that, when defined, they become available for use in other places. This includes statistic types in statistics and [charts](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/) and columns in [views](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/). See our [Smart filters in statistics and charts](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) exercise for specific guidance on adding a smart filter as a statistic type in a Rich Filter Statistics gadget.

## Next steps

You can work through the [Fundamentals](/cms_trial/space/RFCDOC/783942482/User+guides/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.