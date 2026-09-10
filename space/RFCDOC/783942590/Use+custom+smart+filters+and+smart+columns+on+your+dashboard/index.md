# Use custom smart filters and smart columns on your dashboard

In this article, you will explore two features of [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) — **smart filters**, which allow you to filter and group your issues using configurable smart clauses based on JQL, and **smart columns**, which will enable you to include computed columns in Rich Filter Results gadgets to highlight information in your issues. You'll also learn how smart filters can be used in other contexts, such as statistics and quick charts.

Smart filters behave like computed fields, but you don't need Jira administrator privileges to define and use them. Smart filters give this power to all users.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## The final result of this tutorial

When you've worked through all the steps in this tutorial, you should have:

- A Rich Filter Controller gadget containing three smart filters.
- A Rich Filter Results gadget view includes custom smart columns highlighting your issues.
- A Rich Filter Statistics gadget displaying a breakdown of team stats based on a smart filter.

![custom smart filters result.png](/cms_trial/assets/249cf001-2d79-4ee3-92e2-18050b9ecff7.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in this series, you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942590) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it uses the **Left sidebar** layout. You can set this using the **Change layout** menu at the top of the dashboard.

   ![Left sidebar.png](/cms_trial/assets/0cfeaec5-b85c-4dee-9a3e-e3ef4820ab95.png)
4. Add a Rich Filter Controller gadget and a Rich Filter Results gadget to your dashboard, both based on your Rich filter ([Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) that explains how to do this).
5. After saving the configuration of your gadgets, drag and drop them to move the controller to the left-hand column of your dashboard and the results gadget to the right-hand column.
6. Click **Done** to exit dashboard edit mode.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Add a smart filter to your controller

You are going to create a smart filter called `Warnings`, which will allow you to filter your issues based on three important criteria (as you'll see below, these are defined in the rich filter config as **Smart clauses**, each with its own JQL query):

- **Top priority**: The highest priority issues are open.
- **Past due date**: Unclosed issues that are overdue.
- **No due date**: Non-resolved/closed issues where the due date is empty.

Let's walk through adding this smart filter to your controller.

1. Open your rich filter configuration (described in the [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Select the **Smart Filters** tab and click the **Create Smart Filter** button.

   ![Smart filters.png](/cms_trial/assets/db42de31-7de1-4526-aea0-02ffeb62d3fd.png)
3. Enter the Name `Warnings` in the resulting dialog box, and click **Create**. |  
   You will be relocated to the *Warnings* smart filter config screen.
4. Click the **Create smart clause** button.

   ![Warning smart filter config, showing the default view - no smart clauses created yet. The create smart clause button is highlighted](/cms_trial/assets/5b7eb007-2cfa-4de3-b971-fb02651ea093.png)
5. In the resulting dialog box, enter the details required for the `Top priority` smart clause:

   1. **Name**: `Top priority`
   2. **JQL**: `priority in (1, 2) AND status = Open`

      ![Create a smart clause dialog box with top priority clause details filled out](/cms_trial/assets/12580b78-2e94-41a0-8668-d6c209bdb5a2.png)
   3. Click **Create** to finish creating it; you'll see it listed on the *Warnings* smart filter config screen.
6. Add two more smart clauses to the *Warning* smart filter:

   1. **Name**: `Past due date`  
      ***JQL***: `duedate < now() and status != Closed`
   2. **Name**: `No due date`  
      **JQL**: `duedate = EMPTY and status not in (Resolved, Closed)`

      ![Warning smart filter config, showing the top priotity, past due date, and no due date smart clauses](/cms_trial/assets/a717394b-26c2-4c42-b989-4574596b1ec6.png)
7. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/); you should now see the *Warnings* smart filter on your controller. Try selecting some different clauses, clicking **Apply**, and seeing how the list of issues displayed in your Rich Filter Results gadget changes based on your selections.

   ![apply top priority.png](/cms_trial/assets/fc79e658-9f0e-46fa-9a5b-449fbbcd5380.png)
8. Clear the filter by clicking the **X** button in the bottom-right corner of the controller.

   ![click to clear.png](/cms_trial/assets/a283ac0f-362c-4960-9ee3-e51b70e7d13c.png)

The smart filter displays a number to tell you how many clauses you have selected inside it. Once a value has been entered into a smart filter, you can clear the value by clicking the x button on the right-hand side of the filter.

## Highlight your issues with smart columns.

You can already see the value of smart filters. They build on what static and dynamic filters offer, allowing you to customize how you can filter your lists of Jira issues to provide more informative dashboards. But that's not all—you can also create new data columns in your Rich Filter Results gadgets based on your smart filters to easily highlight important information in your issues.

These are called smart columns. Let's add one to your dashboard.

1. Open your rich filter config.
2. Select the *Views* tab, then create a view called `Delivery` containing the columns *Issue Type, Key, Priority, Summary, Assignee, Status, and Resolution* (for more guidance, see [Create a custom view of an issue list](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).

   ![Delivery view config screen with columns shown of issue type, key, priority, summary, assignee, status, and resolution](/cms_trial/assets/f613f239-a16e-43fd-bd45-c1797a3d260a.png)
3. Now for the smart column. Start typing `Warnings` into the **Add a column…** dropdown — you'll find that the *Warnings* smart filter is listed as an available column!

   ![View config Add a column dropdown with warn typed into it, and autocomplete options showing the warnings smart filter ](/cms_trial/assets/fadf9d20-77ec-4d25-bbd4-e97f69e3ac5f.png)
4. Click *Warnings* to add it to the list of columns for your view.
5. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). You'll see the Rich Filter Results gadget update to the new view. This includes the new *Warnings* column, with the different clauses shown as colored tags on matching issues.

   ![result with priority.png](/cms_trial/assets/7847938d-ce8e-4edf-8f2f-233397369223.png)

## Customize your smart filter tag colors.

For example, you can change the colors of your smart filter tags to provide a clearer visual indication of where problem areas can be found in your issue lists.

1. Open your rich filter config.
2. Select the *Smart Filters* tab, and select **Warnings** to go to your smart filter's config screen.
3. If you click the colored boxes to the left of the smart clause titles, you'll be given a color picker to select new colors for your clauses. You can choose from presets and enter custom colors using the controls at the bottom of the picker.

   ![Warnings colors.png](/cms_trial/assets/9b9ece79-15aa-4756-a9d7-b023fff4c8e3.png)
4. We will choose orange for Top priority items, red for Past-due items*,* and gray for items with No due date. Feel free to choose different colors as you wish.
5. Go back to your dashboard, [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), and look at your new *Warnings* color scheme.

## Add a second smart filter with a customized smart column layout

The available smart column customizations go beyond just changing tag colors. You can further change the look of your smart columns, including the column headers and how the label text is shown. And, as with all column types, you can change the position of the column in the table.

Let's investigate this by creating a new smart filter that calls out high-risk items — those that are high priority but have no assignee — in a separate column.

1. Open your rich filter config.
2. Select the *Smart Filter* tab and click **Create Smart Filter**.
3. Call your new smart filter `Risk`.
4. In the resulting *Risk* smart filter config screen, click **Create smart clause** and create a single, smart clause with the following data:

   1. **Name**: `On`
   2. **JQL**: `Priority in (1,2) and assignee is EMPTY`
   3. **Color**: Red is just fine for a high-risk warning.

      ![Create a smart clause dialog box showing the details for the On clause](/cms_trial/assets/747622d4-987f-4f80-ae43-9a6b626fe99b.png)
5. Click **Create**.
6. Select the *Views* tab of the rich filter config, and select your *Delivery* view to go to its config screen.
7. Add a *Risk* smart column to the view using the **Add a column...** dropdown menu.
8. Drag and drop the *Risk* column to a more prominent position in the table, for example, just after the *Priority* column (you can also Tab to the column to focus it, press Space, and then use the up and down cursor keys to adjust its position).
9. Edit the *Risk* smart column by clicking its **Configure** icon.

   ![Requester view config showing Risk smart column with Configure this column button highlighted](/cms_trial/assets/e161211d-ea5f-4bef-b6cb-f9f6cc053f63.png)
10. In the resulting dialog box, you are presented with options for presenting the tags (color, label text, or both) and column headings (none, smart filter name or initials, or custom). Choose the following for your *Risk* column:

    1. **Show tags as**: **Colors only**.
    2. **Column heading**: **Smart filter initials**.

       ![Edit smart column Risk dialog box, showing options for colors only tags and smart filter initials column headings selected](/cms_trial/assets/9a9f6934-8306-40b5-96a4-cf22df25e445.png)
11. Click **Update**, then go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). You should now see your new column with header *R* and a colored red dot to highlight all the issues determined to be high-risk by the criteria specified above.

    ![results with warnings.png](/cms_trial/assets/9b378016-e3b3-427e-8d9e-12b0d91d754c.png)

## Further exercises — smart filters in statistics and charts

In our final example, we've further demonstrated the power of smart filters by creating a new smart filter that splits your data into two teams, each made up of different assignees, and shows their issue counts and story point totals in a Rich Filter Statistics gadget. As we've said before, everything is connected to rich filters, and smart filters are no exception. You can use smart filters anywhere, and you can use other value types.

To complete the tutorial, you must follow the steps below.

### Create a Teams smart filter

1. Create a new smart filter called Teams in the same manner as above.
2. In Inside Teams, create two smart clauses using the following data (replace the placeholder letters with your available assignee names, splitting them evenly between the two teams).

   1. **Name**: `Blue team`

      1. **JQL**: `assignee in (a,b,c)`
      2. **Color**: Blue.
   2. **Name**: `Green team`

      1. **JQL**: `assignee in (d,e,f)`
      2. **Color**: Green.

Alternatively, you could create Jira groups to represent your teams and filter them using the JQL function `membersOf("groupName")`. For example, "`assignee in membersOf("Blue team")`".

### Display team statistics

1. Add a new Rich Filter Statistics gadget to your dashboard.
2. Fill in the following fields as described in its config form:

   1. **Rich filter**: Set this to the same rich filter your other rich filter gadgets are based on.
   2. **Breakdown by** > **Statistic type**: When you click the *Statistic type* dropdown, you'll notice that your smart filters are available as values to choose from! Select **Teams**.
   3. **Values**: Choose **Issue Count** and **Story Points** from the **Pick a value...** dropdown.
3. Drag and drop the statistics gadget below the Rich Filter results gadget in the right-hand column.
4. Click **Submit**.

## Final result

Your final dashboard should look like the following image.

![custom smart filters result.png](/cms_trial/assets/249cf001-2d79-4ee3-92e2-18050b9ecff7.png)

You can try clicking the chart button in the bottom-right corner of the statistics gadget to view some charts based on your *Team's* statistics.

## Next steps

You are advised to work through the [Fundamentals](/cms_trial/space/RFCDOC/783942482/User+guides/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.