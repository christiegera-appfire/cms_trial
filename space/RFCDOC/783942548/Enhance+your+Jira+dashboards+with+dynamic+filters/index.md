# Enhance your Jira dashboards with dynamic filters

This article focuses on another powerful feature of [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview): **dynamic filters**. These filters allow for fine-grained filtering of issues by individual values available in different fields. For example, you could filter for issues with a particular assignee, status, or label.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- An understanding of [static filters](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## The final result of this tutorial

When you've worked through all the steps in this tutorial, you should have:

- This is a Rich Filter Controller gadget with several dynamic filters. These filters allow you to filter the issues displayed in other rich filter gadgets by individual values.
- This is a Rich Filter Results gadget that displays the list of issues and allows you to see the effect of the filtering.

![Enhace result.png](/cms_trial/assets/f0124651-3ea2-41af-818e-26530283694b.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the Two-column layout. This is usually the default setting, but you can select it if required using the **Change layout** menu at the top of the dashboard.

   ![Newly created dashboard with Change layout option selected and two columns option highlighted](/cms_trial/assets/a8900e05-ff50-4460-ac6d-72c72706d609.png)

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Add dynamic filters to a Rich Filter Controller gadget

Dynamic filters allow for more granular filtering than static filters. [Static filters](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) take a [JQL query](https://www.atlassian.com/software/jira/guides/expand-jira/jql) as input and create a button in your controller to toggle that query on and off. On the other hand, dynamic filters take a Jira field as input and create a control allowing you to filter by individual values available to that field.

Let's start by adding dynamic filters to a Rich Filter Controller gadget.

1. Add a Rich Filter Controller gadget to your dashboard and configure it based on your rich filter ([Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) explaining how to do this).
2. Ensure your new gadget is in the left-hand column of your dashboard; you can drag and drop it if necessary.
3. Open your rich filter page (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
4. Select the *Dynamic Filters* tab.

   ![Dynamic filters.png](/cms_trial/assets/ce45e0a7-3f2d-49b9-93c6-1cbcd88d0e6a.png)
5. Add a dynamic filter based on the Assignee field.

   1. Start typing "Assignee" into the *Pick a field...* text input.
   2. Select *Assignee* from the list of options presented to you.
   3. An Assignee dynamic filter will appear above the text input.

      ![Dynamic filters config with a single dynamic filter created for assignee](/cms_trial/assets/dff17c68-af1e-451c-9d1f-74658c0b2dfe.png)
6. In the same way as before, add dynamic filters based on the *Priority*, *Status*, *Labels*, and *Resolution* fields.

   ![Dynamic filters config with dynamic filters created for assignee, priority, status, labels, and resolution](/cms_trial/assets/0bfd60fa-cb54-4c45-9ac2-a900dcd9240f.png)
7. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/); you should now see the dynamic filters on your controller.

   ![see the dynamic filters .png](/cms_trial/assets/d80bfbe0-6f3c-4fbc-873e-4b12130de159.png)

## Filter the issues in a Rich Filter Results gadget.

Now we've got a controller with some dynamic filters, and we need another gadget to filter. Let's add a Rich Filter Results gadget to our dashboard and see what effect the filters have on it.

1. Add a Rich Filter Results gadget to your dashboard.
2. Ensure your new gadget is in the right-hand column of your dashboard; you can drag and drop it if necessary.
3. In the gadget config form, ensure the *Rich filter* is set to the same rich filter as your controller, then click *Submit*.
4. Try clicking some of the dynamic filters in the controller, selecting a few values, clicking **Apply**, and seeing how the list of issues displayed in your Rich Filter Results gadget changes based on your selections. Note also how the dynamic filters display a number to tell you how many values you have selected inside each one.

   ![apply filtr.png](/cms_trial/assets/96e64c6b-84bf-42b3-ad58-9270ee701e18.png)

Unlike static filters, which apply automatically when toggled on or off, dynamic filter changes aren't used to your dashboard until you click the **Apply filters** button in the controller when changes have been made.

This is because dynamic filter settings usually involve selecting several options; the controller allows you to wait until you are happy with your filter selections before applying them.

1. Clear the filters by clicking the X button in the bottom-right corner of the controller.

![clear filters.png](/cms_trial/assets/61e23e87-6e58-4735-baaf-38af0c79c322.png)

It's also worth knowing that once a selection or value has been chosen in a dynamic filter, you can clear the individual selection by clicking the x button on the right-hand side when the pointer hovers over the number of selections.

![contentId-783942548](/cms_trial/assets/b0a6cda2-8e73-4214-a410-04dc46c64307.png)

If you select multiple options inside a single dynamic filter, the issues displayed will match **any** specified values (i.e., the values are ORed) by default. However, you can use the control buttons in the filter dropdown menu to change that behavior to NOT (match all values but the selected ones) and AND (match issues with all the selected values simultaneously) where appropriate.

![contentId-783942548](/cms_trial/assets/d59b0dc9-40b8-49b3-ba8d-edde7c798128.png)

## Searching and range selection of filter options

Before moving on, you should be aware of two more power-user features that can enhance your usage of dynamic filters (and smart filters — see [Use custom smart filters and smart columns on your dashboard](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) for more information on those).

First, when you click on a dynamic or smart filter, in addition to displaying the available options, the filter box becomes a text field into which you can type search terms to filter those options. This is useful if you have a filter containing many options and want to focus on a smaller group that interests you.

![contentId-783942548](/cms_trial/assets/32ebced1-becc-4e1b-8473-774199a18265.png)

Second, you can Shift + click the displayed options to select or deselect a range of options:

- Shift + click the bottom option in the list to select *all* options.
- Click to select one option, then Shift + click another option further up or down the list to select both and all options.
- The above functionality also works in reverse: you can Shift + click to deselect existing selected ranges.

Search and range selection are powerful in combination. You can filter the displayed options to a subset that interests you and then select all with one click.

Search and range selection is powerful in combination — you can filter the displayed options down to a subset that interests you and then select all of them with one click.

## Other dynamic filter types

The dynamic filters you've seen so far are **option dynamic filters**. There are four different types of dynamic filter control available in total; which type is created depends on the type of data stored in the chosen field:

- **Option dynamic filters** result from fields that can contain a finite number of specific values (such as Assignee, Status, Labels, or custom select fields) and take the form of a dropdown menu containing a checkbox for each value, allowing you to filter by one or more of them.
- **Date dynamic filters** result from fields that can contain a date/datetime value (such as Created or Due Date) and take the form of a date picker. They allow you to filter for dates before or after a specified date or between two dates.
- **Text dynamic filters** result from free text fields (such as Summary or Description), and take the form of a text input allowing you to type in a text search query to filter by.
- **Number dynamic filters** result from numeric fields (such as Story Points), and take the form of a text input allowing you to type in a numeric search query to filter by.

In this section, you'll make your controller more powerful by adding a dynamic filter for each type you've not already used.

### Add a date dynamic filter.

1. Open your rich filter config and select the *Dynamic Filters* tab.
2. Add a dynamic filter based on the Created field (or another appropriate date/datetime field).
3. Return to your dashboard, [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), and play with your new dynamic filter to see how it updates the listed issues.

   ![Created field .png](/cms_trial/assets/1f9973b6-0c22-4d7e-a44a-6d4b0db4b4c0.png)
4. Clear all the filters by clicking the X button in the bottom-right corner of the controller.

The selected date values are inclusive, meaning that they are included in the filter range.

**Advanced syntax details about date dynamic filters:**

- If only a *From* date is entered, the filter matches issues on or after that date.
- If only a *To* date is entered, the filter matches issues on or before that date.
- If the *From* and *To* dates are entered, the filter will match the issues between those two dates.
- You can enter date values in several different ways:

  - Select a day from the date picker that appears when you click the *From* or *To* fields.
  - Directly as a calendar date (e.g., "`yyyy/MM/dd`" or "`yyyy-MM-dd`")
  - Directly as relative time notation (e.g., "`5d`" meaning "5 days after now", or "-`4w 2d`" meaning "4 weeks and two days before now").

    - If you want to use *now* as a value in *From* or *To*, enter "`0d`".

### Add a text dynamic filter

1. Open your rich filter config and select the *Dynamic Filters* tab.
2. Add a dynamic filter based on the Summary field (or another appropriate text field).
3. Return to your dashboard, [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), and play with your new dynamic filter to see how it updates the listed issues.

   ![summary field.png](/cms_trial/assets/9ce71471-3190-4ff7-8156-99887d0dd917.png)
4. Clear all the filters by clicking the X button in the bottom-right corner of the controller.

**Advanced syntax details about text dynamic filters:**

- Jira has two text searchers, one for exact string search and one for full-text search. Each dynamic filter will use the searcher associated with the underlying field.
- Advanced full-text search features such as wildcard searches

### Add a dynamic filter

1. Open your rich filter config and select the *Dynamic Filters* tab.
2. Add a dynamic filter based on an appropriate numeric field like Story Points.
3. Return to your dashboard, [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), and play with your new dynamic filter to see how it updates the listed issues.

   ![Story points.png](/cms_trial/assets/9c6e09cd-7ee7-4968-b262-a1c9154d75ab.png)
4. Clear all the filters by clicking the X button in the bottom-right corner of the controller.

**Advanced syntax details about number dynamic filters:**

- You can enter numeric filter terms in several different ways:

  - Enter one or several space-separated values, e.g., enter "`1 2 3`" to filter for the values 1, 2, or 3.
  - The comparison operators "`<, "">," "<=," and ">=" are accepted, e.g., enter ">=1`" to filter for values greater than or equal to 1.
  - Use the form "`a:b`" to filter for a range of values; e.g., enter "`1:10`" to filter for values between 1 and 10.
  - Enter "`empty`" to filter for issues where this field is empty or "`!empty`" to filter for issues where this field is not empty.

Refer to our [Dynamic Filter Types](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/) reference documentation for more information on each dynamic filter type.

## Final result

Your final result should look like this:

![Enhace result.png](/cms_trial/assets/f0124651-3ea2-41af-818e-26530283694b.png)

## Next steps

You can work through the [Fundamentals](/cms_trial/space/RFCDOC/783942482/User+guides/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.