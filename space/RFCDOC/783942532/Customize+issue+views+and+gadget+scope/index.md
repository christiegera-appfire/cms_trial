# Customize issue views and gadget scope

This article explains how to use a couple of features provided by [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) to create custom issue displays for multiple purposes or roles. **Views** allow you to customize the columns displayed when listing issues in Rich Filter Results gadgets. **Working queries** enable you to refine the scope of individual gadgets by applying a permanent JQL query at the gadget level.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get Started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## The final result of this tutorial

When you've worked through all the steps in this tutorial, you should have:

- There are two Rich Filter Results gadgets with tabs available to display separate views, each showing a different set of issues.
- A Rich Filter Controller gadget containing filters that can be used to filter the issues shown in both results gadgets.

![Customize issue views.png](/cms_trial/assets/ed39ac25-d71c-46af-a9ed-f344e49193ca.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get Started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard in Jira (**Dashboards** > **Create dashboard**).
3. Make sure it uses the Two-column layout. It’s a default setting, but you can select it if required using the **Change layout** menu at the top of the dashboard.

   ![Two columns.png](/cms_trial/assets/619070e0-89c5-4072-9617-915f3daab0f9.png)
4. Add **Rich Filter Results** gadget to your dashboard and configure it based on your rich filter (Learn more about [creating a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving your gadget's configuration, you can move it to the right-hand column of your dashboard by dragging and dropping it.
6. Click **Done** to exit dashboard edit mode.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Create a custom view of an issue list

You won't want to see the same columns in your results at all times. For example, a manager might want to see a simplified view for status checking, while two different team members might rely on different sets of fields to do their jobs. You can create a different rich filter view for each purpose.

Let's create a more useful default view to show some issue details and who reported them.

1. Go to your rich filter config screen.
2. Select the **Views** tab and click **Create View** in the top-right corner.

   ![Create view.png](/cms_trial/assets/eba156df-f052-4f6f-8502-503f4ca81bab.png)
3. In the resulting dialog box, enter `Requester` and click **Create**.
4. In the resulting *Requester* view config screen:

   1. Add the *Issue Type* column.

      1. Click the**Add a column***…* dropdown menu.
      2. Start typing `Issue Type` to filter for it in the available options.
      3. Select the *Issue Type*option that appears to add it to the list.
   2. Add the columns *Key, Priority, Summary, Reporter, and Status* in the same way as above.

      ![2025-08-01_14-09-07.png](/cms_trial/assets/60188f18-5235-470b-a86e-44b90a32df92.png)
5. Click the **Views** tab to go back to the main views config screen, and you will find your Requester view available there (which is helpful if you want to edit it later on).
6. To see your new view in your Rich Filter Results gadget, return to your dashboard and click the [*Optimized refresh*](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) button in the controller.

## Add a second view

Now, let's add a second view to allow you to look at Jira issues according to their delivery status.

1. Return to the *Views* tab of your rich filter config screen, as before.
2. Add another *Delivery* view with the columns *Issue Type, Key, Priority, Summary, Assignee, Status, and Resolution*.
3. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). The Rich Filter Results gadget should now show a separate tab for each view — select them to move between the two.

   ![Delivery view.png](/cms_trial/assets/6436c7bb-660a-4764-a907-09b66d30a33b.png)

## Choose the views to display inside your gadget.

You might not want to access all views in all Rich Filter Results gadgets all of the time. For each results gadget, you can select a particular set of views relevant to its intended use.

To configure this:

1. Go to your dashboard and click the **Edit** button at the top-right corner if the dashboard is not already in edit mode.
2. Go to your results gadget and select **Configure** from the **Menu** (▢) in the top-right corner.

   ![Configure_results.png](/cms_trial/assets/0b7c389e-6cdc-4cc1-937d-b097ad301237.png)
3. In the *Views* section of the resulting gadget form, you'll see that **All views** are currently selected and are being shown.

   ![image-20240506-160947.png](/cms_trial/assets/39b5a05a-1cc2-48eb-bcf8-1eaf705b4eba.png)
4. To show only a subset, click the **Customize shown views** radio button.   
   This will cause an **Add a view** dropdown to appear. As with other dropdowns in rich filters, you can type in some text to filter the available options before selecting the ones you want.
5. Select **Requester** from the dropdown and then **Delivery**. They will both appear in a vertical list.

   ![image-20240506-161022.png](/cms_trial/assets/5428c63b-9d02-4de7-ab10-853dc574db5e.png)
6. Try dragging and dropping the two views (you can also Tab to a view to focus it, press Space, and then use the up and down cursor keys to adjust its position). Change the order here to change the order in which the view tabs appear in the Rich Filter Results gadget.
7. Click the trash can icon next to one of the views and **Submit**. You'll see that the gadget now only shows one single view with no tabs.
8. Update the config form so the Rich Filter Results gadget shows both views again.
9. After saving the configuration of your gadget, click **Done** to exit dashboard edit mode.

## Easier configuration with the Menu

In the previous section, we showed you how to configure your Rich Filter Results gadget. This was quite an involved process — entering dashboard edit mode, entering the config form for the gadget by selecting **Configure** from the **Menu** (▢) in the top-right corner, updating your config details, clicking **Submit** to exit the config, and clicking **Done** to exit edit mode. Entering and exiting dashboard edit mode both trigger a reload of all your gadgets, which makes it take even longer.

Rich filters provide an easier way to update your configuration information. In every rich filter gadget footer, you can click the **Menu** (▢) icon to access the **Rich filter menu.**

This menu provides two very useful options for much quicker configuration:

![Configure gadget](/cms_trial/assets/82f4a877-5e4e-4208-8a73-affa71cb65e7.png)

- **Configure gadget**: Opens the config form for that gadget without entering dashboard edit mode.
- **Open rich filter config***:* This opens the config screen for the rich filter the gadget is based on in a new tab.

We advise you to use this menu to edit your configs in the future wherever possible (as you'll see later, renaming and gadget color highlighting are currently only available through dashboard edit mode).

## Use working queries to limit the scope of displayed issues in rich filter gadgets.

It is possible to apply a specific additional JQL query to each rich filter gadget, adding a permanent filter to the issues processed by the gadget — i.e., the gadget's scope — changing the data displayed in just that gadget. This is a powerful and versatile mechanism for customizing your gadgets. In Rich Filter Results gadgets, you can customize the issues shown in each gadget for different purposes.

This is a **working query** edited in the config form for each gadget. In this example, we will create a Rich Filter Results gadget showing canceled issues and another one showing non-canceled issues.

You can set a working query on any rich filter gadget, except the Rich Filter Controller and Text Panel gadgets.

### Create a "not canceled" results gadget

1. Open the configuration form for the Rich Filter Results gadget you already have on your dashboard.
2. Find the *Working query* field near the top. This is where your working query JQL goes.
3. Enter "`resolution in (EMPTY, Fixed, Done)`." This JQL filtering condition will always be combined (ANDed) with the base JQL filter that feeds the gadget. This gadget will display only issues with no resolution or the resolution **Fixed** or **Done** (this is what we consider to mean "not canceled" in this example).

   ![image-20240506-161133.png](/cms_trial/assets/5da6e8f0-c976-4ea1-9968-2cfc53e6d229.png)
4. Click **Submit**.
5. Rename the gadget to `Not canceled` so its purpose is easy to understand. Just click the name and start typing. Click the **Check** icon when ready.

   ![rename not cancelled.png](/cms_trial/assets/0970f2be-6c88-45b6-967a-1fc042e68ffc.png)

The Rich Filter Results gadget will now show only the not canceled issues (i.e., issues with resolution either *EMPTY* (Unresolved) or *Fixed*or*Done*). You can check this by switching to the *Delivery* view and looking at the *Resolution* column.

![Fixed or done.png](/cms_trial/assets/da892f8b-e4b1-4236-a866-8afcd1397326.png)

We define canceled issues as issues with a non-empty resolution other than *Fixed* and *Done*. Depending on your Jira configuration, you might have different resolutions and conventions.

### Create a canceled results gadget.

1. Add another Rich Filter Results gadget to your dashboard based on the same rich filter as the first one.
2. Make sure it is in the left-hand column; drag and drop it if needed.
3. Add the working query `resolution not in (EMPTY, Fixed, Done)`
4. Click **Submit**.
5. Rename it to `Canceled`**.**
6. Give it a different highlight color to stand out from the other one. The**Highlight color**options are available in dashboard edit mode, as shown below.

![Change color.png](/cms_trial/assets/6d9879c1-7bab-4911-9502-b2b6c8eefe04.png)

You should end up with two Rich Filter Results gadgets that look like this:

![result.png](/cms_trial/assets/2c3901a1-95dc-4f37-8cfc-f9a0beaa5777.png)

Rich Filters for Jira Dashboards also provides a dedicated feature for managing customized lists of issues specific to Rich Filter Results gadgets. This is called [Queues](/cms_trial/space/RFCDOC/783942406/Configure+queues/) and is covered elsewhere.

Using the "ORDER BY" clause in a working query will take precedence over the "`ORDER BY`" clause of the base filter, allowing you to customize the default sorting of issues for that gadget.

## **Freeze columns**

When your views contain many columns that extend beyond the width of your *Rich Filter Results* gadget, you can freeze important columns to keep them visible while users scroll horizontally. This ensures that key information like **Issue Type**, **Key,** and **Summary** columns remains in view at all times.

Let's freeze some columns in your *Delivery* view to see how this works:

1. Go to your rich filter configuration screen and select the *Views* tab.
2. Click your **Delivery** view to open its configuration.
3. Click the **Freeze** (▢) icon for the **Issue Type**, **Key,** and **Summary** columns to freeze them.

   ![2025-08-01_14-34-48.png](/cms_trial/assets/f022a6f3-54af-4002-b45f-73dbaa97e468.png)
4. Go back to your dashboard and click the **Optimized refresh** button in the controller to see the changes.

Now, when you switch to the *Delivery* view in your *Rich Filter Results* gadget, start scrolling horizontally. You'll see that the **Issue Type**, **Key,** and **Summary** columns remain fixed on the left side while other columns scroll past them.

![result view.gif](/cms_trial/assets/9d25f96c-854c-4543-a852-c351d1c4d18d.gif)

Freeze your most important columns to ensure users can always identify which issues they're looking at, even when exploring additional details in other columns.

## Further exercises

To add further power to the dashboard, we used a Rich Filter Controller gadget in the left-hand column above the Canceled Results gadget in our final example. To complete the tutorial, we'd like you to do the following:

1. Add a Rich Filter Controller gadget to your dashboard using the *Add a Gadget* side panel.
2. Drag and drop it to the top of the left-hand column of the dashboard if it isn't already placed there.
3. In the controller config form, set the *Rich filter* to the same Rich filter your other gadgets are based on, and click *Submit*.

If you use a rich filter from a previous tutorial, you may already have some filters on your controller. If you created a fresh new rich filter for this tutorial:

- Try creating some static filters, as shown in [Add some static filters to your controller](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- Try creating some dynamic filters. You can find out how to [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).

Try applying some filters in the controller. You'll see that both Rich Filter Results gadgets update live to add these extra filtering criteria over the top of the working queries active in each one. **Controllers use the same rich filter to filter the information shown in all the gadgets.**

![Controllers.png](/cms_trial/assets/235c70af-d8eb-4f09-816d-42a645ee3c2a.png)

## Next steps

You can work through the [Fundamentals](/cms_trial/space/RFCDOC/783942482/User+guides/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.