# Use rich filter counters and gauges in your dashboards

This article introduces you to the counter and gauges gadgets available in [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview). Counters sum values you are interested in (for example, total issue count or story points), whereas gauges report proportions (for example, the percentage of issues that have been resolved). **Rich Filter Simple Counters** gadgets and **Rich Filter Simple Gauges** gadgets are based on issue counts or value fields such as story points or time spent. **Rich Filter Smart Counters** gadgets and Rich Filter Smart Gauges gadgets, in addition, use smart filters to split the values as a custom breakdown.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of smart filters, as explained in [using custom smart filters and smart columns on your dashboard](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).

## Final result

Once you've worked through the steps in this tutorial, you should have a dashboard that contains six rich filter gadgets:

- A Rich Filter Controller gadget containing some filters to provide interactive filtering across the entire dashboard.
- A Rich Filter Simple Counters gadget showing the total issue count, story points, and time spent.
- A Rich Filter Smart Counters gadget shows the number of issues assigned to different [teams](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) in the organization and those not assigned to any team.
- A Rich Filter, Simple Gauges gadget, showing the proportion of issues that have been resolved (both in terms of the issue count and the story points value of those issues) and the proportion of issues assigned to the current user.
- A Rich Filter Smart Gauges gadget showing the proportion of issues assigned to them each of the [custom warnings](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) we defined as examples — *Top priority*, *Past due date*, and *No due date*.
- A second Rich Filter Smart Gauges gadget shows the proportion of resolved issues for each team member.

![ich filter counters and gauges in your dashboards.png](/cms_trial/assets/bb67711c-c8df-4576-ad9b-086739c59066.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the left sidebar layout. You can set this using the **Change layout** menu at the top of the dashboard.

   ![Left sidebar.png](/cms_trial/assets/e373f1f5-be39-4a69-bb06-fdbd7714bf56.png)
4. Based on your rich filter, add a **Rich Filter Controller** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving the configuration of your gadget, move the controller to the left-hand column of your dashboard, if required, by dragging and dropping it.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Add simple counters

Start by adding a simple counter to your dashboard to summarize some core information about your issues. This can include issue count, sums of numeric or time-tracking fields, or even custom values (which we'll cover elsewhere).

1. Add a **Rich Filter Simple Counters** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. Ensure your new gadget is in the left-hand column of your dashboard, underneath your controller; drag and drop it if needed.
3. In the gadget config form, set the different fields as follows:

   1. **Rich filter**: Set this to your rich filter.
   2. **Values**: From the Pick a value... dropdown, select: *Issue Count*, *Story Points*, and *Time Spent*.
4. Your configuration form should look like this: Check it is correct, then click *Submit*.

   ![image-20240507-083448.png](/cms_trial/assets/88037ffe-07da-4941-a98d-a4eed4f71439.png)
5. Your Rich Filter Simple Counters gadget should look like this:

   ![Rich Filter Simple Counters.png](/cms_trial/assets/fce46c01-1a7c-4ffa-9d13-26e2dc4ac791.png)

You can click on any value shown in a counters gadget to open up a new browser tab containing a list of all the Jira issues contributing to that value.

## Add simple gauges

Next, let's add a set of simple gauges to report success in hitting work targets. A gauge computes a proportion from a total, for example, the proportion of issues resolved. The proportions shown in simple gauges can be derived from issue count, numeric or time-tracking fields, or custom values and custom ratios (we'll cover custom values and custom ratios elsewhere).

1. Add a **Rich Filter Simple Gauges** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. Ensure your new gadget is in the right-hand column of your dashboard; you can drag and drop it if necessary.
3. In the gadget config form, set the different fields as follows:

   1. **Rich filter**: Set this to your rich filter.
   2. **Gauge filters & values**: To configure a simple gauge, select a filter (predefined or [static](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)) and a value. The filter returns the issues that contribute to the gauge level. The value aggregates issues when computing the gauge level, total, and ratio. So, for example, you might want to show the resolved story points as a proportion of the total story points. For this example, we'll use one of the predefined filters with rich filters.

      1. From the **Pick a filter** dropdown, select **Resolved Issues**.
      2. From the **Pick a value** dropdown that appears next to the first dropdown, select **Issue Count**.
      3. Create a second gauge — this time, select **Resolved Issues** from **Pick a filter**, and **Story Points** from **Pick a value**.
4. Your configuration form should look like this: Check it is correct, then click **Submit**.

   ![image-20240507-083633.png](/cms_trial/assets/51fe711f-8beb-4d56-b0bc-08eb15f53aa5.png)
5. Your Rich Filter Simple Gauges gadget should look like this:

   ![Rich Filter Simple Gauges.png](/cms_trial/assets/f947b15a-e6c6-468f-b4d0-6462f854406e.png)

You will see that by default, the gauges display the percentage of the gauge level from the gauge total and the gauge level and total as numeric values in a gauge graphic format. So, in our cases:

- The percentage of resolved issues, the number of resolved issues, and the total number of issues.
- The percentage of resolved story points, the number of resolved story points, and the total story points.

You can also create a simple gauge based on a static filter. For example, you might want to create a gauge that shows the proportion of issues assigned to you.

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Go to the *Static Filters* tab and check whether you have the *Assigned to me* static filter available.
3. If you don't already have *Assigned to me*, add some static filters to your controller as described.
4. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
5. Return to your Rich Filter Simple Gauges gadget config form (as described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
6. Create a third gauge. This time, select your **Assigned to me** static filter from **Pick a filter** and **Issue Count** from **Pick a value**.
7. Click **Submit**.

You should now have a gauge based on your static filter. Note how its color matches the color set for the static filter in the rich filter configuration and that the predefined *Resolved Issues* filter has a predefined green color.

![Assigned to me .png](/cms_trial/assets/c38f2452-93e7-4260-a8f4-f328ff92b268.png)

You can click on any value shown in a gauges gadget (percentage or number) to open up a new browser tab containing a list of all the Jira issues contributing to that value.

## Change the gauge layout.

The Layout dropdown at the bottom of the gadget config form offers three different layout options for simple gauges.

- **Gauge**: This is the default we have been using so far. It shows the percentage of the gauge level from the gauge total and the gauge level and total in a gauge graphic format.

  ![Assigned to me .png](/cms_trial/assets/c38f2452-93e7-4260-a8f4-f328ff92b268.png)
- **Percentage and fraction:** This shows the percentage of the gauge level from the gauge total and the gauge level and total as a fraction.

  ![Percentage and fraction.png](/cms_trial/assets/07879060-c808-438f-b4d6-ea1b3b4ad184.png)
- **Percentage only**: This shows only the percentage of the gauge level from the gauge total.

  ![Percentage only.png](/cms_trial/assets/79967ef6-0f64-4548-bb19-de374e1620b1.png)

Have a play with these options now, and choose the one you like best:

1. Return to your Rich Filter Simple Gauges gadget config form.
2. Choose a new value from the **Layout** dropdown.
3. Click **Submit** to see your new layout.

## Add smart counters

Let's look at the smart versions of the two gadgets above, starting with the Rich Filter Smart Counters gadget. As mentioned earlier, this gadget displays values split by a smart filter as a custom breakdown. We'll display a count of the issues assigned to the different teams defined by the *Teams* smart filter we saw earlier in the article series.

First, let's make sure you have the *Teams* smart filter available:

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Go to the *Smart Filters* tab.
3. If you don't already have it available, create the *Teams* smart filter as described in [Create a Teams smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).
4. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

Now, let's add a counter to summarize our Team issue counts:

1. Add a **Rich Filter Smart Counters** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. Ensure your new gadget is in the left-hand column of your dashboard, underneath your Rich Filter Simple Counters gadget; drag and drop it if needed.
3. In the gadget config form, set the different fields as follows:

   1. **Rich filter**: Set this to your rich filter.
   2. **Smart filter**: Choose your smart filter as Teams.
   3. **Show None**: This checkbox controls whether a count is shown for issues that don't match any smart filter clause. Keep this box checked—it is useful to monitor the number of issues not assigned to any team.
   4. **Value**: Choose **Issue Count**.
4. Your configuration form should look like this: Check it is correct, then click *Submit*.

   ![image-20240507-084226.png](/cms_trial/assets/55a0b76f-4a8b-411d-b03f-78a634d28f19.png)
5. Your Rich Filter Smart Counters gadget should look like this:

   ![Rich Filter Smart Counters .png](/cms_trial/assets/7f07bbda-fb3d-45e1-bbac-33c00e56163c.png)

Note how the gadget shows a count of the issues matched by each smart clause in the smart filter, each also matching the smart clause's label and color.

## Add smart gauges

Similar to smart counters, smart gauges always use a smart filter to provide a custom breakdown. In this section, you'll add a Rich Filter Smart Gauges gadget showing the percentage of issues with different custom warnings, defined by the *Warnings* smart filter we saw earlier in the article series.

1. If you don't already have the Warnings smart filter available, add it to your rich filter as described on this page: [Add a smart filter to your controller](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).
2. Add a **Rich Filter Smart Gauges** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
3. Ensure your new gadget is in the right-hand column of your dashboard, underneath your Rich Filter Simple Gauges gadget; drag and drop it as needed.
4. In the gadget config form, set the different fields as follows:

- **Rich filter**: Set this to your rich filter.
- **Smart filter**: Choose your Warnings smart filter.
- **Show None**: This checkbox controls whether a gauge is shown for issues that don't match any smart filter clause. Uncheck this box.
- **Computation mode**: Keep the **Use smart clauses as gauge filters** radio button selected — this option creates a gauge for each smart clause showing the percentage of issues matching the smart clause (gauge level) from all the issues included in the gadget (gauge total). As a result, each gauge has the same total. The values are computed based on the **Value** field selection (the field below this one). In this case, we show the percentage of issues each warning has applied to them.

The other Computation mode value — *Using smart clauses as gauge totals* — also creates a gauge for each smart clause. In this case, however, each gauge's total is based on the total number of issues that match the smart clause, and you have to choose a filter that you want to show a proportion of in each gauge (for example, the number of issues resolved). You'll see an example of this in the next section.

- **Value**: Choose **Issue Count**.
- **Layout**: Choose **Percentage & fraction**.

1. Your configuration form should look like this: Check it is correct, then click **Submit**.

   ![image-20240507-084801.png](/cms_trial/assets/905021fd-f2ca-4018-9a47-c46cf655e760.png)
2. Your Rich Filter Smart Gauges gadget should look like this:

   ![Rich Filter Smart Gauges gadget .png](/cms_trial/assets/82f82e47-2791-4ee7-b87d-4724fd7ceb69.png)

This gadget shows a percentage of the issues that match each smart clause, the actual number of matching issues, and the total number of issues in each case.

## Explore the second smart gauge computation mode.

In this section, you'll add another Rich Filter Smart Gauges gadget, this time based on the *Teams* smart filter, showing the proportion of issues each team has resolved. This time, you'll use the second smart gauges computation mode to explore the difference between the two.

1. You can add another Rich Filter Smart Gauges gadget to your dashboard below the previous one in the right-hand column.
2. Use the following values in the config form:

   1. **Rich filter**: Set this to your rich filter.
   2. **Smart filter**: Choose your smart filter as **Teams**.
   3. **Show None**: Uncheck this box.
   4. **Computation mode**: Select the **Use smart clauses as gauge totals** radio button
   5. **Gauge filter and value**: Choose **Resolved Issues** from the **Pick a filter** dropdown and **Issue Count** from the **Value** dropdown.
3. Click **Submit**.

Your new gadget should look like this:

![Teams smart filter.png](/cms_trial/assets/8fb6866d-1059-4ed9-8858-00651ac14250.png)

Have a look at your two Rich Filter Smart Gauges gadgets and observe the difference between the first and second computation modes:

- In the first example, which uses the first mode, you show the percentage of issues that match each smart clause out of the total number of issues available. In this case, the smart clauses determine the gauge levels.
- In the second example, which uses the second mode, you show the percentage of resolved issues from the issues assigned to each team. In this case, the smart clauses determine the total for each gauge, and you had to select a separate filter (*Resolved Issues*) from which to derive the proportion.

## Further exercises

To complete this tutorial, we'd like you to add some dynamic filters to your controller, as explained in [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/), and explore how they can be used to filter further the information shown in your counters and gauges gadgets.

You don't need many dynamic filters for this example, and you should take care to choose ones that make sense to apply alongside the filtering already happening inside the counters and gauge gadgets. Priority and Reporter are reasonable choices. Try applying some filters in your controller and note the effect they have on your other gadgets.

![ich filter counters and gauges in your dashboards.png](/cms_trial/assets/bb67711c-c8df-4576-ad9b-086739c59066.png)