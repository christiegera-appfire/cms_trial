# Display custom charts and quick tables on your dashboard

A key feature of Jira dashboards is displaying your data through statistics and charts for effective, at-a-glance reporting. This article demonstrates a related feature available in [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview), namely the **Rich Filter Flexi Charts** gadget. This lets you generate detailed charts on your dashboard and display **quick tables** on the fly.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Final result

When you've worked through all the steps in this tutorial, you should have a dashboard that contains two flexi chart gadgets:

- One contains a donut chart showing the number of story points worth of issues reported by each reporter.
- One contains a stacked bar chart showing resolved and unresolved issues for each priority.

The two flexi chart gadgets, which are the focus of this tutorial, can be seen on the right of the image below. The gadgets on the left (Rich Filter Controller and Rich Filter Results) have already been covered in previous tutorials.

![dashboard with flexi charts.png](/cms_trial/assets/86af6bc9-8e90-4144-ae88-4751b80f9caa.png)

Both flexi chart gadgets can also display quick tables that provide details of the data summarized in the charts: these are accessed by clicking the **Show table** button in the bottom-right corner of the flexi chart gadgets. The below image shows an example:

![Reporter flexi chart1.png](/cms_trial/assets/c4ae7d09-6648-4f2d-895d-a72b6ed3cbe1.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the **Left sidebar** layout. We'll put our charts in the right-hand column, as they benefit from having more display space than other gadget types. You can set this using the **Change layout** menu at the top of the dashboard.

![Left sidebar.png](/cms_trial/assets/d999e4d5-2008-4d8b-9093-1ab079ee20b6.png)

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Your first Flexi Chart

Rich Filter Flexi Charts gadgets allow you to show one-dimensional charts (single statistic type) or two-dimensional charts (two statistic types), with data points of your choice displayed for each value.

Let's create a simple one-dimensional chart showing each reporter's story points.

1. Add a **Rich Filter Flexi Charts** gadget to your dashboard (Learn more on how to [create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. Move the gadget to the right-hand column of your dashboard by dragging and dropping it.
3. There are several fields you should configure in the gadget config form (for the moment, we'll leave the *Chart type* as the default *Donut* type):

   1. **Rich filter**: Set this to your rich filter.
   2. **Breakdown by** > **Statistic type**: We'll get this chart to show a breakdown by reporters, so select **Reporter** in the Statistic type dropdown.
   3. **Value**: For each reporter, let's show the number of story points' worth of issues they have reported. Choose **Story Points**.
4. Your gadget config form should look like the following image. Check it is correct, then click **Submit**.

   ![image-20240507-064417.png](/cms_trial/assets/dccf87fe-2c11-4901-a1ca-293d464ae4ed.png)
5. Your Rich Filter Flexi Charts gadget should look like the following image.

   ![Reporter flexi chart.png](/cms_trial/assets/ba93ee79-1e5a-44bd-b3fe-4dbca73b70c8.png)

Suppose the selected Statistic type has options for which the matching issues are equal to zero for the selected Value. In that case, those options are still greyed out in the legend (and quick tables, as you'll see later) but are not included in the chart. For example, in the donut chart above, Chris and Will have no story points for their issues.

## Manipulate your chart display

The Rich Filter Flexi Charts gadget config form offers several options for changing the default display.

1. Return to your *Rich Filter Flexi Charts* gadget config form (see [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. We haven't discussed the following options previously. Update them as described below:

   1. **Filter out None**: If this option is selected, issues with the statistic type empty won't be included in the chart (in the Reporter's case*,* this may have no effect, as empty values are unlikely). Check this box if you wish.
   2. **Sort by**: This dropdown offers different values depending on the chosen statistic type. Select the **Total** option. This will sort the chart data in descending order by the number of story points rather than ascending reporter names in alphabetical order. In the case of donut/pie charts, the data runs clockwise from the top.
   3. **Reverse sort order**: reverses the default sort order of the option chosen in Sort by. In this case, checking the box would sort the chart data by the number of story points in ascending order. We've kept the box unchecked.
3. Your config form should look like the following image. Check they are correct, then click **Submit**.

   ![image-20240507-064609.png](/cms_trial/assets/f2458b8b-7d96-4fcb-93c5-007695548cb9.png)
4. You should end up with a different display in your chart gadget. Feel free to play around with these settings until you get a display that you are happy with.

   ![Reporter flexi chart2.png](/cms_trial/assets/b7a6668e-fae7-4417-b663-964267741f8e.png)
5. Go back into your gadget config form and look at the different chart types available in the *Chart type* dropdown. The Rich Filter Flexi Charts gadget provides a variety of one—and two-dimensional charts to cover all your needs.

**One-dimensional chart types:**

- Donut
- Pie
- Gauge
- Bar
- Line
- Treemap
- Word cloud

**Two-dimensional chart types:**

- Clustered bar
- Stacked bar
- Multi-line

6. Try out a few types of one-dimensional charts to see the variety.

![custom smart filters .png](/cms_trial/assets/fe63bcce-bf08-43ff-a2e4-deac16d64c30.png)

You can find more information on the configuration options available for different gadgets in our Working with Rich Filter Gadgets reference articles, such as [The Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/).

## Chart interactive features

The different chart types all have interactive features. For example:

- You can hover over the columns/slices to display exact values as tooltips. This can be especially useful in donut charts when the gadget display is too narrow to show the labels seen in previous screenshots.
- You can click the values or their bars/slices to load lists of all the associated issues in a separate tab.

  ![Values view.png](/cms_trial/assets/77359eb6-d478-4251-964e-626f3fcb9151.png)

## Create two-dimensional charts

Let's create a two-dimensional chart. In this case, we'll create a stacked bar graph showing the number of resolved and unresolved issues for each priority.

1. Add another Rich Filter Flexi Charts gadget to your dashboard (Click [here](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to learn more on how to add gadgets).
2. Drag and drop the gadget to the right column of your dashboard. Later, we'll add other features to the left column.
3. Set the following field values in the gadget config form:

   1. **Rich filter**: Set this to the same rich filter your other Flexi chart gadget uses.
   2. **Chart type**: Choose a Stacked bar.
   3. **Primary breakdown** > **Statistic type**: Choose **Priority** in this dropdown.
   4. **Secondary breakdown** > **Statistic type**: choose **Resolved/Unresolved** in this dropdown.
   5. **Value**: We'll show the number of issues for each priority and resolved/unresolved combination. Choose **Issue Count** in this dropdown.
4. Your Rich Filter Flexi Charts gadget config form should look like the following image. Check it is correct, then click **Submit**.

   ![image-20240507-072224.png](/cms_trial/assets/bc97ab62-cf56-44e4-a63a-ef339762f854.png)
5. Your gadget should look like this.

   ![two-dimensional chart.png](/cms_trial/assets/44740f69-7e3e-4531-8079-a44e8c07f6bb.png)

## Filter charts using your controller

You'll notice how connected everything is as you use Rich Filters for Jira Dashboards more. With this in mind, let's look at filtering your chart display using a Rich Filter Controller gadget.

1. Add a **Rich Filter Controller** gadget to your dashboard using the **Add a Gadget** side panel.
2. Drag and drop it to the left-hand column of the dashboard if it hasn't already been placed there.
3. In the controller config form, set the *Rich filter* to the same Rich filter your other gadgets are based on, and click **Submit**.

If you use a rich filter from a previous tutorial, you may already have some filters on your controller. If you created a fresh new rich filter for this tutorial:

- Try creating some static filters, as shown in [Add some static filters to your controller](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- Try creating some dynamic filters. You can find out how to [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).

Try applying some filters in the controller. Note how they filter issues inboth flexi chart gadgets.

![dashboard with flexi charts.png](/cms_trial/assets/86af6bc9-8e90-4144-ae88-4751b80f9caa.png)

Bear in mind that controllers filter the information shown in *all* gadgets using the same rich filter!

## Display quick tables

Flexi charts have quick tables available to provide details of the data summarized in the chart. Quick tables are displayed by clicking the **Show table** button in the bottom-right corner of the gadget.

![show table.png](/cms_trial/assets/c017c7f7-802a-4f72-8684-c4714fdcd406.png)

1. Click the **Show table** button to display a tabular representation of your data.

   ![Reporter flexi chart1.png](/cms_trial/assets/c4ae7d09-6648-4f2d-895d-a72b6ed3cbe1.png)

Click the **Show Table** button again to hide the quick table.

As with any other table in rich filters, you can sort the data in a quick table by different columns by clicking the column headings. Click a heading multiple times to toggle between ascending and descending order.

![Quick table showing story points by reporter, with column sorting control highlighted, sorted ascending by reporter](/cms_trial/assets/52c23c5f-0fe2-4be6-a3e8-222a48d22554.png)

Tables generated from two-dimensional charts can be sorted by ascending and descending column values, row values, and totals by clicking the arrow controls in the relevant column and row headings.

![Sort by total.png](/cms_trial/assets/ab513f7d-0b6a-442c-b4e4-9eefce852492.png)

After sorting has been applied, you can clear all the applied sorting in a two-dimensional quick table by clicking the x button in the top-left corner. Similar to the charts from which the quick tables are generated, you can click the header and cell values to load lists of all the associated issues in a separate tab.

## Further exercises

To add further power to the dashboard, in our final example, we added a Rich Filter Results gadget in the left-hand column, below the Rich Filter Controller gadget, based on the same Rich filter (Create a simple dashboard that explains how to do this). You can complete this step on your dashboard to complete the tutorial.

Your dashboard should look like this:

![dashboard with flexi charts.png](/cms_trial/assets/86af6bc9-8e90-4144-ae88-4751b80f9caa.png)

As a further exercise, we encourage you to explore using smart filters in flexi charts. [Smart filters](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) allow you to filter and group your issues using configurable smart clauses based on JQL and also have the advantage that, when defined, they become available for use in other places. This includes statistic types in [statistics](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/) and charts and columns in [views](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/). Use our [Smart filters in statistics and charts](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) exercise as a starting point, and try adding a smart filter as a statistic type in a new flexi chart gadget.

## Next steps

This is the last topic in the [Fundamentals](/cms_trial/space/RFCDOC/783942482/User+guides/) article series. Each one works as a standalone topic, so you can jump to specific topics of interest if you missed any or want to revisit ones you've already covered.

You can use the rich filter you created in this article as a starting point for other tutorials.