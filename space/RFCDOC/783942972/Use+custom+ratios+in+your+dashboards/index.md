# Use custom ratios in your dashboards

[Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) enables you to define **custom ratios**. These advanced user-defined ratios provide power and flexibility that can be pre-packaged and used in [gauge](/cms_trial/space/RFCDOC/783942638/Use+rich+filter+counters+and+gauges+in+your+dashboards/), [statistics](/cms_trial/space/RFCDOC/783942568/Display+statistics+and+quick+charts+on+your+dashboard/), [flexi charts](/cms_trial/space/RFCDOC/783942604/Display+custom+charts+and+quick+tables+on+your+dashboard/), and [time series](/cms_trial/space/RFCDOC/783942921/Display+date%2Ftime+statistics+and+charts+on+your+dashboard/) gadgets. When defining a custom ratio, you can specify custom base values, including JQL filter queries for the numerator and denominator, and custom display options for the results, including label, color, and format. This article tells you all you need to know about using custom ratios.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942972).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## Final result

Once you've followed the steps in this tutorial, you can see your issues, such as completion rate and work ratios, broken down by interesting measures like team, priority, and project.

The dashboard will contain:

- All the rich filter gadget types that can display issue data based on custom ratios:

  - Rich Filter Simple Gauges gadget
  - Rich Filter Smart Gauges gadget
  - Rich Filter Flexi Charts gadget
  - Rich Filter Statistics gadget
  - Rich Filter Two-Dimensional Statistics gadget
  - Rich Filter Time Series Chart gadget
- A Rich Filter Controller gadget containing quick filters to refine your dashboard view dynamically.

![Use custom ratios in your dashboards.png](/cms_trial/assets/694ebe5a-e721-4412-afb3-d1206f130234.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in our [Learning Center](/cms_trial/space/RFCDOC/783942482/User+guides/), you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942972) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the **left sidebar l**ayout. You can set this using the Change layout menu at the top of the dashboard.

   ![Left sidebar.png](/cms_trial/assets/ae42ebc4-afad-49bc-8fb0-cff8c22f65ab.png)
4. Based on your rich filter, add a Rich Filter Controller gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving your gadgets' configuration, ensure the controller is in the left column; you can drag and drop it if necessary.

## Custom ratios versus "on the fly" ratios

We’ve already discussed the ratios in the “[Use rich filter counters and gauges in your dashboards](/cms_trial/space/RFCDOC/783942638/Use+rich+filter+counters+and+gauges+in+your+dashboards/)” page. We define ratios "on the fly" in Rich Filter Simple Gauges and Rich Filter Smart Gauges by selecting a filter for the gauge level and an aggregate value.

![Smart Gaugesresolved issues.png](/cms_trial/assets/70f0a5df-b7c3-4d92-9b75-9f1a6d147fba.png)

Custom ratios are similar in concept to the ratios created on the fly in gauge gadgets, but they provide a lot more power and flexibility:

- They are created as standalone entities in your rich filter config. After being defined once, they can be reused in multiple places.
- They can be used in various gadget types, including gauges, statistics, and charts.
- You can create ratios of a wide variety of different value types.
- You can specify JQL queries for the ratio level (numerator) and total (denominator).
- You can set custom display options for the results, including label, color, and format.

## Your first custom ratios

Let's create a custom ratio so you can see how they work.

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Go to the *Custom Ratios* tab and click **Create custom ratio.**

   ![Create Custom Ratio.png](/cms_trial/assets/7f524c47-4583-4854-986e-b6d5e516966e.png)
3. You'll create a custom ratio of completed story points versus total story points in the resulting dialog box. Enter the following values:

   1. **Name**: This label for your custom ratio will denote it when you use it inside gadgets. For this example, enter `Completion rate`.
   2. **Color**: Use the color picker to give your custom ratio a nice green color.
   3. **Numerator**: This defines the ratio level: the number on the top.

      - You can choose between *Issue Count*, numeric, and time tracking fields forthe **Base value**. You want to define a ratio of story points, so select **Story Points**.
      - For the numerator's **JQL** filter, enter `status in (Resolved, Closed)`. You define a ratio of resolved/closed story points versus the total number of story points.
   4. **Denominator**: This defines the ratio total: the number on the bottom.

      1. For Base value, choose the **Same as the numerator** for this example; we'll see examples of the other choices later. An explanation of the different available choices follows:

         1. The numerator is the same as the denominator, which is obvious; in this case, it will set the base value to Story Points.
         2. A constant, which means the denominator will always be the same, is useful to show progress against a set target.
         3. Another **compatible** field type. If the numerator and denominator are the same type, you can select different value fields for them. For example, if the numerator is based on story points—a numeric field—then the denominator can be based on story points or any other numeric field.
      2. Leave the denominator's JQL filter blank. In this case, we don't want to add additional filtering for the denominator — we want it to include all the story points.
   5. **Display format**: This allows you to choose the display format of your ratio. The options are *Percentage* or *Ratio*; if you choose *Ratio,* you'll be shown an additional *Decimals* field, which allows you to choose several decimal places to show in your ratio with choices ranging from 0 to 3. Leave **Percentage** selected.

      ![image-20240507-135144.png](/cms_trial/assets/59cd58f1-1ad5-45eb-a8b7-65383e98c0d3.png)
4. Click **Create**.

At this point, your *Custom Ratios* tab should display a summary of the custom ratio you just created. You can edit or delete it using the pen and trash can buttons at the right-hand end of the row.

Now, we'd like you to create more custom ratios to get more practice and demonstrate some of the other options discussed above.

1. Work ratio defines a ratio of the time you spent resolving issues versus the original time estimate you gave for resolving those issues. This is very useful for monitoring whether the estimates given are too low or high or investigating inefficiencies in your process that may be increasing the time spent.

   - **Name**: `Work ratio`, give it a dark blue color.
   - **Numerator**:

     - **Base value**: **Time Spent**
     - **JQL**: **Leave blank**
   - **Denominator**:

     - **Base value**: **Original estimate**, here, we are computing a ratio with different base values for the numerator and denominator. The two are both time-tracking fields and are therefore compatible.
     - **JQL**: Leave blank.
   - **Display format**: **Percentage**.
2. Target completion will define a ratio that shows how many story points' worth of issues have been resolved in the previous three months versus a target number. This is useful for showing progress and trends on work targets.

   - **Name**: `Target completion`, give it a lighter blue color.
   - **Numerator**:

     - **Base value**: **Story Points**.
     - **JQL**: `resolutiondate > startOfMonth(-90d)`
   - **Denominator**:

     1. **Base value**: Choose **Constant** and, in the Type a number field that appears, enter **200**. This will be our story point target for three months.
     2. **JQL**: Leave blank.
   - **Display format**: **Percentage**.

Your *Custom Ratios* tab should now look like this:

![Custom ratio.png](/cms_trial/assets/78be3e10-7ac7-4130-bf0b-a891f161a152.png)

## Using custom ratios in a Rich Filter Simple Gauges gadget

Now that you've created these custom ratios, let's use them in the dashboard.

First, you'll use a Rich Filter Simple Gauges gadget to display your Completion rate and Work ratio so you can monitor them at a glance.

1. Add a Rich Filter Simple Gauges gadget to your dashboard (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
2. If required, move the gadget to just below your controller gadget by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   1. **Rich filter**: Set this to the same rich filter as your controller.
   2. **Gauge filters and values**: From the Pick a filter dropdown, choose your **Completion rate** and **Work ratio** custom ratios.

      ![Rich Filter Simple Gauges gadget config showing two gauge filters selected, Completion rate and Work ratio](/cms_trial/assets/02dcccdc-39f1-444e-82ea-55ceb8001727.png)
   3. Click **Submit**. Your Rich Filter Simple Gauges gadget should look like this:

      ![Rich Filter Simple Gauges gadget.png](/cms_trial/assets/e25cd3f6-d947-4b87-a7d1-d4f89b2451a2.png)

## Using custom ratios in a Rich Filter Smart Gauges gadget

Now, you'll create a Rich Filter Smart Gauges gadget that shows how close your teams are to meeting their target completion. Smart gauges are very similar to simple gauges, the difference being that they use a [smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) to provide a custom breakdown rather than being based on individual base values.

1. First, add a Teams smart filter to your rich filter, as described in [Create a Teams smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/).
2. Add a **Rich Filter Smart Gauges** gadget to your dashboard.
3. If required, move the gadget to just below your previous gadget by dragging and dropping it.
4. Configure the following fields in the gadget config form:

   - **Rich filter**: Set this to the same rich filter as your other gadgets.
   - **Smart filter**: Choose your **Teams** smart filter.
   - **Show None**: Make sure this checkbox is unchecked. We are not interested in target completion for issues not assigned to a team.
   - **Computation mode**: Select the **Use smart clauses as gauge totals** radio button.
   - **Gauge filter and value**: Choose your **Target completion** custom ratio.

     ![Rich Filter Simple Gauges gadget config showing the Show None checkbox uncheccked, Use smart clauses and gauge totals computation mode selected, and Target completion gauge filter selected](/cms_trial/assets/1d8be118-ba62-43d4-b514-5609c718de2a.png)
   - Click **Submit**. Your Rich Filter Smart Gauges gadget should look like this:

     ![Target completion custom ratio.png](/cms_trial/assets/28e66c64-de5d-446b-aeb6-025f5f1290a0.png)

## Using custom ratios in flexi charts

Custom ratios are also usable in Rich Filter Flexi Charts gadgets, providing useful summaries of your ratio breakdowns. In this section, you will create a bar chart showing each assignee's top priority ratio. The top priority ratio shows the ratio of highest and high priority issues. It is useful to know the percentage of top-priority issues that are assigned to each team member — ideally, you want the high-priority issues shared out evenly so that no one team member is put under too much pressure and you don't end up with a single point of failure.

First, let's create the *Top priority ratio*:

1. Return to your rich filter config, and open the *Custom ratios* tab.
2. Create a new custom ratio as follows:

   - **Name**: `Top priority ratio`, give it an orange color.
   - **Numerator**:

     - **Base value**: **Issue Count**
     - **JQL**:`priority in (Highest, High)`
   - **Denominator**:

     - **Base value**: **Issue Count**
     - **JQL**: Leave blank
   - **Display format**: **Percentage**

Now for the flexi chart:

1. Go back to your dashboard and add a **Rich Filter Flexi Charts** gadget.
2. Move the gadget to the bottom of the left-hand column by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   - **Rich filter**: Set this to the same rich filter as your other gadgets.
   - **Chart type**: **Bar**
   - **Breakdown by**:

     - **Statistic type**: **Assignee**
     - **Sort by**: **Total**
   - **Value**: **Top priority ratio** custom ratio

     ![image-20240507-135831.png](/cms_trial/assets/9b43c593-0bb8-457e-8250-aff0c371995d.png)
4. Click **Submit**. Your Rich Filter Flexi Charts gadget should look like this:

   ![custom ratios in flexi charts.png](/cms_trial/assets/1bcae2e1-7406-4b15-a5f6-ecdbe1b552f9.png)

## Displaying custom ratios in statistics

You can also display custom ratios broken down into one or two dimensions in rich filter statistics gadgets.

First, you'll create a one-dimensional breakdown of your Completion rate, Work ratio, and Target completion custom ratios by Priority. This is useful for verifying that your teams are prioritizing higher-priority work over lower-priority work, checking that the work ratio is not too high, and seeing what priority work contributes most towards the completion target.

1. Add a **Rich Filter Statistics** gadget to your dashboard.
2. Move the gadget to the top of the right-hand column by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   - **Rich filter**: Set this to the same rich filter as your other gadgets.
   - **Breakdown by** > **Statistic type**: **Choose Priority**
   - **Values**: Select your **Completion rate**, **Work ratio**, and **Target completion** custom ratios.

     ![image-20240507-135928.png](/cms_trial/assets/fc64575e-a8e5-41ec-abcf-8d54ef6d78ff.png)
4. Click **Submit**. Your Rich Filter Statistics gadget should look like this:

   ![custom ratios in statistics.png](/cms_trial/assets/ed67ea7a-36a6-42b5-bfbd-8b16917ff97c.png)

Now, let's look at a two-dimensional breakdown example. Here, you'll create a statistics table that breaks down the *Work ratio* by both *Project* and *Priority*.

1. Add a **Rich Filter Two-Dimensional Statistics** gadget to your dashboard.
2. Move the gadget to the bottom of the right-hand column by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   - **Rich filter**: Set this to the same rich filter as your other gadgets.
   - **Working query**: In this example, we want you to display this metric for a subset of available projects only; to filter for these, you'll use a working query (see Customize issue views and gadget scope for more information). Enter **JQL** similar to `project in ("Fox Service Desk", "Raven Service Desk", "Seal Service Desk"`. We chose service desk projects in our case, but you can choose different projects that are appropriate for your data.
   - **Horizontal breakdown** > **Statistic type**: **Project**
   - **Vertical breakdown** > **Statistic type**: **Priority**
   - **Value**: **Work ratio** custom ratio

     ![image-20240507-140032.png](/cms_trial/assets/bbaadc88-ae54-44d3-9715-20c02b321157.png)
4. Click **Submit**.Your Rich Filter Two-Dimensional Statistics gadget should look like this:

   ![custom ratios in statistics two dimentional.png](/cms_trial/assets/2c956d79-9325-403b-83b6-d8c4b043c0e3.png)

## Custom ratios in time series

Finally, for this article, we wanted to show you that custom ratios can be used in time series (see [Display date/time statistics and charts on your dashboard](/cms_trial/space/RFCDOC/783942921/Display+date%2Ftime+statistics+and+charts+on+your+dashboard/) for more information about time series). This particularly useful combination allows you to see how a ratio evolves over time.

Let's demonstrate with an example. You are going to create three different time series, then display them in a Rich Filter Time Series Chart gadget:

- **Work ratio**: This uses the Work ratio custom ratio as the base value, showing how the time spent completing work matches the original estimates for that work. The time series is based on Resolved, showing the work ratio of resolved issues over several aggregation periods. Ideally, the work ratio should stay near 100%; otherwise, there is a problem with your estimations, or your process is inefficient in some way.
- **Top priority ratio**: This uses the Top priority ratio custom ratio as the base value, which shows the ratio of issues that are the highest and highest priority. The time series is based on Created, so it shows the top priority ratio of created issues over several aggregation periods. Ideally, this should stay consistent and at an acceptable level; otherwise, your prioritization needs to be adjusted.
- **Due completion rate**: This uses the Completion rate custom ratio as the base value, showing the completed story point ratio. The time series is based on the *Due date*, so it shows the rate of issues due in each aggregation period that are completed. Ideally, this should stay at 100%; otherwise, some work was not completed by its due date and is overdue.

Let's begin by creating the required time series:

1. Go back to your rich filter config and open the *Time series* tab.
2. Create the following time series:

   - **Work ratio**:

     - **Name**: `Work ratio`; give it a mid-blue color
     - **Series**: **Resolved**
     - **Base value**: **Work ratio** custom ratio
     - **JQL**: Leave blank
   - **Top priority ratio**:

     - **Name**: `Top priority ratio`; color it orange
     - **Series**: **Created**
     - **Base value**: **Top priority ratio** custom ratio
     - **JQL**: Leave blank
   - **Due completion rate**:

     - **Name**: `Due completion rate`; color it pink
     - **Series**: **Due date**
     - **Base value**: **Completion** **rate** custom ratio
     - **JQL**: Leave blank

Your *Time series* tab should look like the following. Check that it is correct before moving on.

![ Time series tab.png](/cms_trial/assets/b3c7e580-d0b1-4c5c-9724-1c5df85a4f8d.png)

Now, let's display them in a time series chart:

1. Return to your dashboard and add a Rich Filter Time Series Chart gadget.
2. Move the gadget to the bottom of the right-hand column by dragging and dropping it.
3. Configure the following fields in the gadget config form:

   - **Rich filter**: Set this to the same rich filter as your other gadgets.
   - **Aggregation periods**: **Weeks**
   - **Time range**: **Number of weeks**
   - **Number**: 12
   - **Direction**: **Past**
   - **Aggregation type**: **Cumulative total**; this ensures that the ratio shown for each aggregation period is the average and all that came before it, not only the individual period.
   - **Time series**: Add your **Work ratio**, **Due completion rate**, and **Top priority ratio** time series to the list using the **Pick a time series...** dropdown.

     ![Rich filter time series gadget config showing the following sections - 12 weeks in the past for aggregation periods, Cumulative total aggregation type, and Work ratio, Due completion rate, and Top priority ratio Time series](/cms_trial/assets/5d97ce3c-35fc-4541-81dc-74256e82e4ee.png)
4. Click **Submit**. Your Rich Filter Time Series Chart gadget should look like this:

   ![Rich Filter Time Series Chart gadget .png](/cms_trial/assets/40c665fd-2d1f-4b81-a093-dacd2665f3e7.png)

In general, these trends look healthy, except for the due completion rate, which is starting to trend downward, indicating that some issues were not completed on time and are overdue.

## Further exercises

To complete this tutorial, we'd like you to create some quick filters to provide additional interactive filtering of the issues shown in your gadgets. Your controller will already display the *Teams* smart filter you created earlier. Now you should:

1. Add some static filters as described in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
2. Add some dynamic filters as described in [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).

Remember that applying a quick filter in your controller will filter *all* gadgets based on the same rich filter as the controller. For example, the image below shows part of a Jira dashboard with three rich filter gadgets, all being filtered by active quick filters in the controller. The dashboard is being filtered by *Assignee* and *Priority*.

![ additional interactive filtering .png](/cms_trial/assets/605168b0-5301-45ac-bd16-49c65406814f.png)