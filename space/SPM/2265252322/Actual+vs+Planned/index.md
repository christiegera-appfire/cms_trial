# Actual vs Planned

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The Actual vs Planned costs panel for the portfolio displays the effort costs for all tasks in the portfolio, broken down into specific initiatives.

![financials-portfolio-new-nav.png](/cms_trial/assets/4c9453e9-9a6c-485c-93f1-b7da4be6cea6.png)

## Top bar

### Period

Here, you can change the period of the chart. Choose one of the periods or set a custom period by entering the start and end dates. The shortest period you can choose is one week, and the longest is one year. Periods can be in the past or in the future (they are not constrained to a current year).

![financials-period-new-nav.png](/cms_trial/assets/16fbc972-0d42-4147-a42b-22ee702b582c.png)

Calculations

Here, you can check the calculation settings for the initiatives in the portfolio:

![calculations-details.png](/cms_trial/assets/36536af8-62f5-4cda-8121-b2e1d6c25cc4.png)

## Cost summary

Here, you can find a summary of the costs in this portfolio.

![portfolio-details.png](/cms_trial/assets/6cc7a7a6-2cca-4ebb-b998-03bd75e15bce.png)

### Budget

The amount of money planned for a specific portfolio of initiatives.

Click **Edit** ▢next to the amount to edit it.

Hover over **Info** ▢next to the Budget to check the date of the last edit and the editor.

### **Total Cost**

The total cost of all tasks of initiatives in the portfolio, both already performed and planned. The second displayed amount is the remaining budget amount. If the total cost is within the budget, the amount is green. If the total cost exceeds the budget, the amount is red.

### Actual cost

The cost of the effort in tasks is already recorded at this moment.

### **Remaining cost**

The cost of planned, future effort in tasks.

### Progress bar

Under the actual and remaining costs, you can see a percentage value and a bar representing the percentage of the total cost already spent.

## Cost over time chart

![cost-over-time-general.png](/cms_trial/assets/acfafb63-5baf-477f-9a12-62f3d4e78211.png)

In the chart, with one axis representing cost and the other time, you can check a visual representation of the cost of initiatives that change over time.

The period setting determines the timeframe and can be changed in the upper left corner of the Planned vs Actual costs panel.

### Current date

The purple vertical line represents the current date.

### Total cost line

The dashed horizontal line represents the Total cost. You can see if the costs stay within the budget. If the total cost is within the budget, the line is green. If the total cost exceeds the budget, the line is red.

### Budget line

The blue horizontal line represents the budget.

### Total cost tooltip

If you hold the pointer over the chart, a tooltip with the Total cost (along with its percentage value compared to the budget) for the given period is displayed. There is also a percentage value of the total cost for the period compared to the budget. The period starts at the beginning of the chart period and ends at the end of the month, marked by your cursor.

![cost-over-time.png](/cms_trial/assets/4a027d87-0d07-4ccb-bd72-41b7c61c1cf2.png)

When you click a specific period, you can see the data from the tooltip broken down by initiative:

![cost-over-time-initiative-details.png](/cms_trial/assets/08116eaf-3f49-4a58-9d78-698ecfa2beab.png)

### Budget milestones

Budget milestones are key financial checkpoints for your project. They're specific dates where you set expected spending goals, helping you to plan ahead and proactively manage your budget.

When you define a milestone on the **Administration > Financials > Budget milestones** page, it appears on the chart as a red line.

You can right-click a red line (milestone) to open a context menu for it.

From the menu, you can select:

- **Delete milestone** to delete a selected budget milestone.
- **Manage milestones** to go directly to the *Budget milestones* page.

![A context menu for a budget milestone.](/cms_trial/assets/082fdc59-5293-4008-b7fe-cb91cfd12156.png)

For more information

## CapEx vs. OpEx

To use this widget, you have to activate it in [the CapEx vs.OpEx settings](/cms_trial/space/SPM/1918830158/Financials+(Administration)/).

![capex-opex-panel.png](/cms_trial/assets/198b5eab-e826-4a8d-b5f1-85ab57d03529.png)

**CapEx** and **OpEx** are two primary categories for classifying a company's expenses.

- **CapEx** stands for **Capital Expenditure**. It's the money a company spends to buy, improve, or maintain long-term assets that will be used for longer periods
- **OpEx** stands for **Operational Expenditure**. This is the cost of a company's day-to-day business operations. These are recurring costs that are necessary to keep the business running.

In the Financials module, you can track CapEx and OpEx expenses by assigning tasks to one of these groups based either on a custom field or Jira filters. Check the settings page for more details.

### All tab

![capex-opex-panel.png](/cms_trial/assets/198b5eab-e826-4a8d-b5f1-85ab57d03529.png)

This is the main tab where you can check CapEx and Uncategorized (not assigned to either of those groups) costs. You can also check the source of the cost classification. Click Manage to go to the CapEx vs. OpEx settings.

#### Source

This indicates the source of the cost classification. For more information, check the CapEx vs OpEx settings.

#### Manage

Click Manage to go to the CappEx vs. OpEx settings.

### CapEx

![CapEx tab.png](/cms_trial/assets/96f71c4e-38ea-4f74-8805-84a445f044a7.png)

In this tab, you can check all the costs assigned to the CapEx category, divided into initiatives in the current portfolio, along with the corresponding number of logged hours.

### OpEx tab

![opex-tab.png](/cms_trial/assets/a60c0f53-15cf-43be-8186-1c85c2517263.png)

Here, you can check all the costs assigned to the OpEx category, divided into initiatives in the current portfolio, along with the corresponding number of logged hours.

### Uncategorized tab

![uncategorized.png](/cms_trial/assets/d1d1bf00-35ae-4427-b671-6895cf12137a.png)

In this tab you can check all the cost that is not categorized under one of the cost categories (CapEx/OpEx) divided into initiatives in the current portfolio, along with corresponding number of logged hours.

## Cost distribution by Initiatives

![cost-distribution-by-initiative.png](/cms_trial/assets/a4b4c172-3f7f-4d70-9135-eda2dc7dc9ca.png)

This chart lets you see the Total cost of a specific initiative as a percentage share of the portfolio’s total cost.

## Initiatives cost and budgets

In this table, you can find more detailed information about initiatives in the portfolio.

All initiatives from the portfolio are displayed here - even if they do not have sufficient data for cost calculation. Initiatives like that are marked with a warning icon. Hold the pointer over it to check why the initiative is not taken into consideration in the calculations:

![portfolio-initiative-error.png](/cms_trial/assets/de90b780-c09e-411b-8ae9-02b26c2a420f.png)

### Name

You can click the initiative name to go to its own Planned vs Actual costs panel (to get more information on tests in the initiative).

### Budget, Actual cost, Remaining cost, Total cost

Costs related to a specific initiative.

You can edit the Budget cost directly in the table.

Hold the pointer over the info icon to check the calculation settings for a specific initiative.

### Cost progress

The percentage value of Actual versus Remaining cost in the initiative.

### Cost distribution

A percentage value of the Total cost of this initiative against the Total cost of the chosen portfolio.