# Budget overruns - fixed costs

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

### Use Case: Identifying Budget Overruns Caused by Unforeseen Fixed Costs

This use case demonstrates how a Portfolio Manager can use the Financials module to pinpoint a portfolio's budget overruns, specifically those driven by unforecasted **fixed costs**, and report on the financial impact.

---

### Scenario

You are the Portfolio Manager for the "Q3 Product Launches" portfolio, which includes projects like "Mobile App V2," "Cloud Infrastructure Upgrade," and "Marketing Campaign." Your team has been diligently logging time, but the overall portfolio is showing a significant overrun variance in the Financials module. Your stakeholders are questioning why the budget is being exceeded so early. After reviewing the project dashboards, you suspect the cause isn't labor-related but rather due to a large, unexpected payment for a software license and a new consulting contract that were not accounted for in the initial plan. Your objective is to use BigPicture to isolate these fixed costs, prove they are the source of the overspend, and explain the financial situation clearly to leadership.

---

### How the Financials Module Helps

The Financials module provides the necessary tools for this situation:

- **Real-time Cost Tracking:** It lets you see the immediate financial impact of all costs, as soon as they are entered.
- **Cost Breakdowns:** The module enables you to separate and analyze costs by type. This means you can distinguish between variable labor costs (calculated from time logs) and the fixed costs you manually enter.
- **Data Aggregation:** It automatically aggregates all costs—both labor and fixed—from individual projects to the portfolio level, providing a single, unified view of the financial status.
- The **Custom Expenses** function lets you track fixed, recurring costs.

## **Walk-Through: Setting it up**

Follow these steps to manage the portfolio's budget and analyze the overruns:

**1. Set the Initial Budget**

- First, navigate to the Financials module in your "Q3 Product Launches" portfolio box.
- Locate the Budget input field and enter the original approved budget for the entire portfolio (for example, $1,500,000). This is your initial financial target.

**2. Configure cost drivers (task estimates, rates, and fixed costs)**

- **Task details**: Ensure that all the tasks to be considered are configured correctly, in accordance with [the task preparation manual](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695356/Initial+setup+bringing+your+financial+data+into+BigPicture#Prepare-tasks-for-the-Financials-module).
- **Rate:** To handle the hourly rates, ensure your rates (either Team or flat - one rate for a box) are accurately configured. Check the [Assign hourly rates to boxes/teams](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695356/Initial+setup+bringing+your+financial+data+into+BigPicture#Assign-hourly-rates-to-boxes%2Fteams) documentation section for more information. As team members log time against their tasks, the system will automatically use this rate to calculate actual costs.
- **Fixed Costs:** Fixed costs are separate from task-based spending. You can add them to the Financials module using [the Custom Expenses function](https://appfire.atlassian.net/wiki/x/e4T8hg). Let’s say someone created new entries for your third-party vendor contracts. For example, added a fixed cost of "$50,000" for "External Design Agency" under the "Mobile App V2" project. It can be made a recurring cost to automatically add it periodically, for example, for the cost of a software subscription.

## Track Real-Time Performance and Identify Overspend

Now, anyone with access to the box can identify the overspend cause:

- As the teams log time on their Jira tasks, the Financials module automatically calculates the **Actual Costs** for each project and aggregates them to the portfolio level.
- Check the Total Cost in the **Actual vs. Planned** view for the portfolio and specific initiatives. A red highlight means the project is over the budget.
- You can set a recurring **Custom Cost** and then check it for any period.

### Analyze the Cost Breakdown

- To find the root cause, use the module's reporting or breakdown features:

  - **Filter by Project:** Review the cost variance for each project. You will likely see that the "Mobile App V2" project is the primary driver of the negative variance, while "Cloud Infrastructure Upgrade" and "Marketing Campaign" are on track.
  - **Drill Down into Cost Types:** Within the problem project, you can break down the costs further. You will find that a significant portion of the cost is attributed to the fixed expenses you added, confirming your initial suspicions.

**5. Update the Plan**

- After identifying the issues, you can create a new, more realistic budget. Update the Budget value for the projects and the portfolio to reflect the new total.