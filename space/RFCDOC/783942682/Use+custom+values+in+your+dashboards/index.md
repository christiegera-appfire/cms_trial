# Use custom values in your dashboards

[Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) allow you to define custom values—advanced user-defined values that can be used in rich filter gadgets. They can use custom formulas (sum, average, minimum, and maximum) when aggregating values, custom display options for the results, including label, color, and format, and JQL for further filtering. Custom values are available as columns in views and values in gadgets alongside Jira fields.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## Final result

Once you've worked through the steps in this tutorial, you should have a dashboard that contains five rich filter gadgets:

- A Rich Filter Controller gadget will provide interactive filtering on your dashboard.
- A Rich Filter Simple Counters Gadget to sum custom values.
- A Rich Filter Flexi Charts gadget based on custom values.
- A Rich Filter Statistics gadget based on custom values.
- A Rich Filter Results gadget showing custom value-based columns in action.

![custom values dashboard.png](/cms_trial/assets/0d5449dc-b69a-40f1-8a06-b32fcb4c34ff.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in our [Learning Center](/cms_trial/space/RFCDOC/783942482/User+guides/), you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the left**sidebar** layout. You can set this using the **Change layout** menu at the top of the dashboard.

   ![Left sidebar.png](/cms_trial/assets/1a007c73-42dd-47ea-a6c9-036246f8d8f7.png)
4. Based on your rich filter, add a Rich Filter Controller gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving the configuration of your gadgets, make sure the controller is in the left column; you can drag and drop it if necessary.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Your first custom value

Let's start by creating a custom value based on a time-tracking field. You'll create one called `Time Spent (h)` that sums the total time spent working on your issues based on the **Time Spent** Jira field, which has:

- A custom label and color.
- Custom formatting in hours (many people want an option to change Jira's default time formatting).

To do this:

1. Go back to your rich filter config and select the *Custom values* tab.
2. Click **Create custom value**.

   ![Custom Values .png](/cms_trial/assets/9721230e-61c3-43ba-9f81-6ffbb5a9a9d1.png)
3. In the resulting dialog box, enter the following values:

   1. **Name**: `Time Spent (h)`   
      Select a custom color from the color picker. We've chosen orange.
   2. **Base value**: This is the Jira field on which you are basing your custom value. Select **Time Spent** from the dropdown.
   3. **Total formula**: This is used to calculate the totals shown when aggregating this custom value in gadgets (for example, the values shown in statistics and charts). Select **Sum total** — we want to show the total number of hours.
   4. **Time display format**: This gives you options for displaying time tracking fields in days, hours, minutes, or seconds, in addition to Jira's display format. Select **Hours**.

      ![image-20240507-120154.png](/cms_trial/assets/16af92a2-1fac-4cca-9b64-a4c353726c4c.png)
4. Click **Create**.

At this point, your *Custom values* tab should display a summary of your created custom values. You can edit or delete it using the pen and trash can buttons at the right-hand end of the row.

## Numeric custom values

Now, let's look at a numeric custom value; here, you'll create a Resolved Story Points value based on the Story Points Jira field. This value uses a JQL query to provide the necessary filtering right inside the custom value itself.

1. Create a new custom value with the following configuration values:

   1. **Name**: `Resolved Story Points`. Give it a green color.
   2. **Base value**: Select **Story Points** from the dropdown.
   3. **Total formula**: Select **Sum total.**
   4. **Decimals**: This allows you to choose between showing no decimal portion in your values, a maximum number of decimal places, or an exact number of decimal places (with trailing zeros if required). Leave this at the default value.
   5. **JQL**: This is where you can enter a JQL query to filter the issues to which this custom value applies. Since we want to show resolved story points, this custom value should apply only to resolved issues. To achieve this, insert `resolution is not EMPTY` into this field.
2. Click **Create**.

   ![set Custom Values .png](/cms_trial/assets/acdc709f-c8e6-4a29-b87c-bed376b703f9.png)

## Display your custom value totals in counters and statistics gadgets.

Now you've created some custom values, you need to use them somewhere.

First, you'll use a Rich Filter Simple Counters gadget to display useful totals.

1. Add a **Rich Filter Simple Counters** gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. If required, move the gadget to just below your controller gadget by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   1. **Rich filter**: Set this to your rich filter.
   2. **Values**: From the **Pick a value...** dropdown, select the **Jira Issue Count** value and your custom **Time Spent (h)** and **Resolved Story Points** values.

      ![Rich Filter Simple Counters gadget config form with rich filter and three values selected, Issue Count, Time Spent (h), and Resolved Story Points](/cms_trial/assets/9605108a-6c43-4525-8934-c16372e7fc4e.png)
4. Click **Submit**. Your Rich Filter Simple Counters gadget should look like this:

   ![custom value dashboard.png](/cms_trial/assets/28e736af-fd4a-4e58-bc48-939b9b44ff00.png)

Now, let's use a Rich Filter Statistics gadget to break down the same data further and show each assignee's custom values.

1. Add a **Rich Filter Statistics** gadget to your dashboard.
2. Move the gadget to the right-hand column by dragging and dropping it.
3. There are several fields you should configure in the gadget config form:

   1. **Rich filter**: Set this to the same rich filter as your other gadgets.
   2. **Breakdown by** > **Statistic type**:  Select **Assignee** from the dropdown.
   3. **Values**: Again, select **Issue Count** value, **Time Spent (h)**, and **Resolved Story Points**.

      ![Rich Filter Statistics gadget config form with rich filter, Assignee Statistic type, and three values selected, Issue Count, Time Spent (h), and Resolved Story Points](/cms_trial/assets/474b2ae1-e69e-4f3b-9b28-fc5ac048276a.png)
4. Click **Submit**. Your Rich Filter Statistics gadget should look like this:

   ![custom statistics.png](/cms_trial/assets/4662ed1c-b755-4ba4-9b32-f0e97b1da5e0.png)

Before we move on, let's briefly consider what we just did. We defined a notion of *Time Spent (h)* and started using that instead of the native Time Spent field. This is preferable because it provides a custom time display in hours and a custom label and color. We then defined a notion of *Resolved Story Points* that provided a useful filter on top of the native Story Points field and used that in our gadgets.

This has started to give you a glimpse into the power of custom values — you can define a custom value to suit your needs and then use it everywhere. And you can do all this without being a Jira administrator. Let's continue.

## Duration-based custom values

Let's explore creating more advanced custom values based on computed durations provided by rich filters. We'll create new custom values based on the calculated duration value of the *Issue age / resolution time*. *Issue age / resolution time* brings two closely related values together in one. If an issue isn't resolved, the value will be *Issue Age — i.e., the time that has passed since the issue was created*. If it is resolved, the age will stop increasing on the resolution date, and the value will become a static *resolution time* value — i.e., **the time between the created date and the resolution date**.

We'll now create two new custom values based on *Issue age/resolution time*:

- *Age* will contain the age of issues, whether they have been resolved or not. You'll display this in a Rich Filter Results gadget view later on.
- *The Average Resolution Time will contain the resolution time of issues; hence,* it will only be shown for resolved issues. This can display each assignee’s average issue resolution time in your Rich Filter Statistics gadget.

![Create a custom value dialog box showing the Issue age resolution time base value](/cms_trial/assets/6eb7dbf2-400d-49ee-bc8b-f6380b304a5b.png)

Let's do this:

1. Go back to your rich filter config's *Custom values* tab.
2. Create a new custom value with the following configuration values (as illustrated in the picture above):

   1. **Name**: `Age` Give it a blue color.
   2. **Base value**: Select **Issue age / resolution time**.
   3. **Total formula**: Select **Average value**.
   4. **Duration display format**: Select **Days**.
3. Create another custom value with the following configuration values:

   1. **Name**: `Avg Resolution Time` Give it a gray color.
   2. **Base value**: Select **Issue age / resolution time**.
   3. **Total formula**: Select **Average** **value**.
   4. **Duration display format**: Select **Days**.
   5. **JQL**: Insert `resolution is not EMPTY` — we want this custom value to apply only to resolved issues.
4. Your *Custom values* tab should now look like this. Check it before moving on:

   ![Duration-based custom values.png](/cms_trial/assets/9c3ba19f-14f8-4cdc-bba5-a55f2364d61f.png)

## Add Avg Resolution Time to your statistics

1. On your dashboard, open your *Rich Filter Statistics* gadget config form (as described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Add your new **Avg Resolution Time** value in the *Values* section and click **Submit**.
3. Your *Rich Filter Statistics* gadget should now look like this:

   ![Rich Filter Statistics gadget .png](/cms_trial/assets/b8dbb0c0-7603-4b28-887e-6e4138aeaa66.png)

Now, the gadget also shows the average resolution time for each assignee. In this case, the percentage bar is not displayed — it does not make sense for values using the average aggregation formula.

## Display custom values in a results gadget.

In a Rich Filter Results gadget, let's display some custom values as columns.

To be able to do that, you'll first need to set up a [View](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) to display those columns.

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Select the *Views* tab.
3. Add a view called `Delivery status check`.
4. Inside the *Delivery status check*, add the columns *Issue Type*, *Key*, *Priority*, *Summary*, *Assignee*, *Time Spent (h)*, *Status*, *Resolution*, and *Age*. We've chosen custom values that make sense to display in Rich Filter Results gadget columns.
5. Turn your attention to the **Show totals row toggle** switch above the columns list. Click the toggle to turn this on. A Rich Filter Results gadget will now display this view with a *Total* row at the bottom containing the totals for all the value columns in the view, including the custom value columns.

Like the other columns, you can edit the display of your custom value columns using the edit (pen) icons on the right-hand side of the display, for example, to customize the column headings.

Your *Delivery status check* configuration should look like this:

![Delivery status check config.png](/cms_trial/assets/651b23c4-a7c9-4ecc-ba41-2de6f405de9e.png)

Now it's time to show your new view inside a Rich Filter Results gadget.

1. Add a **Rich Filter Results** gadget to your dashboard.
2. Move the gadget to the right-hand column below the Rich Filter Statistics gadget by dragging and dropping it.
3. In the gadget config form, set the *Rich filter* to the same rich filter as your other gadgets.
4. Set the **Display** to **All issues** and **Views** to **Customize shown views** and select the newly created **Delivery status check** todisplay the list of issues returned by the selected views.
5. Click **Submit**.   
   Your Rich Filter Results gadget should look like this:

   ![Delivery status check view.png](/cms_trial/assets/b74660de-e073-4082-8799-35aea2781725.png)

Have a look at the columns based on your custom values. Note the *Total* row, which displays totals for your custom values calculated according to the *Total formula* setting you specified for each one.

## Create a custom value based on a custom duration

Now, we will create a `Due In` custom value that shows how far away the deadline for each issue is. This will be based on *Custom duration*, a special advanced base value that allows you to select a start and an end time/date from a list of options (including the current time), with the final value being the computed duration between the two.

Let's look at how this works:

1. Go back to your rich filter config's *Custom values* tab.
2. Create another custom value with the following configuration values:

   1. ***Name***: `Due In`, give it a red color.
   2. **Base value**: Select **Custom duration** from the dropdown. This causes two additional dropdown fields to appear to allow you to specify your start and end values:

      1. **Start**: Select **Current time**.
      2. **End**: Select **Due date**.
   3. **Total formula**: Select **Minimum value**. When aggregating this custom value on multiple issues, we'd like to see the one due next: the minimum Due In value.
   4. **Duration display format**: For the chosen Start and End values, this field is fixed at **Days—non-fractional**.
   5. **JQL**: Insert `resolution is EMPTY`, it makes no sense to show Due In values for issues that have been resolved.

      ![image-20240507-121208.png](/cms_trial/assets/5d1d9f3d-3fdd-4bcf-aeea-60bb81526555.png)
3. Go back to your rich filter config's *Views* tab.
4. In the *Delivery status check* view, add a new *Due In* column and drag and drop it between the *Summary* and *Assignee* columns.
5. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). You should see your *Due In* column in action:

   ![due in.png](/cms_trial/assets/b4bee8e1-1efb-4db3-84c4-d5718b409b06.png)

The *Total* row value for *Due In* is particularly interesting. Because you selected the *Minimum Value* for the *Total formula*, this is a useful signal of when the next task is due for completion.

## Further exercises

To complete this tutorial, we'd like you to create a bar [flexi chart](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/) that shows the *Avg Resolution Time* for each *Priority*.

1. Configure Rich Filter Flexi Charts:

- **Rich filter**: Select the same rich filter you've been using for your other gadgets
- **Chart type**: Select **Bar chart** (to match the visualization shown in the image)
- **Breakdown by** > **Statistic type**: Select **Priority** from the dropdown
- **Values**: Select your custom **Avg Resolution Time** value from the dropdown

Your finished chart should look something like this:

![ avg resolution time chart .png](/cms_trial/assets/f05bd69e-0604-4194-baf1-85e0d07fd45e.png)

We'd also recommend that you add some filters to your controller to provide additional interactive filtering of the issues shown in your gadgets:

1. Add static filters as described in [Get Started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
2. Add dynamic filters as described in [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).
3. Add a *Teams* smart filter as described in [Create a Teams smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).
4. Update your previous flexi chart to use your new smart filter as the *Statistic type*. This will allow you to display the Average Resolution Time by Team.