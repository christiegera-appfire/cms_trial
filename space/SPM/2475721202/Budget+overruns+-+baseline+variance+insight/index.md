# Budget overruns - baseline variance insight

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

This use case demonstrates how a Portfolio Manager can use the Financials module to identify why a portfolio is over budget, pinpoint the specific cost drivers, and use the Baseline feature to track changes from the original plan.

---

## **Scenario**

You are the Portfolio Manager for "Strategic Growth Initiatives," a portfolio that includes three major projects: "Product Redesign," "Market Expansion," and "Platform Integration." Your stakeholders have expressed concern that the portfolio is trending significantly over its initial budget. Through initial conversations, you suspect the issue is a higher-than-expected workload for a key development project. Your goal is to use BigPicture to confirm these suspicions, identify which specific projects are the source of the problem, and present a clear picture of how the financial plan has changed since its approval.

## How the Financials Module Helps

The Financials module provides the tools to address this scenario directly.

- **Budget Baselining:** [The Baseline feature](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695747/Set+up+your+project+budget#Baseline) lets you save a snapshot of your original estimations. By saving this baseline, you can always compare your current, updated financial plan against the initial approved plan, demonstrating the variance and rationale for any changes.
- **Real-time Cost Tracking:** It automatically calculates and aggregates costs from the individual tasks within your projects, giving you an immediate view of the total actual spending at the portfolio level.
- **Cost Breakdowns:** You can drill down to see costs by project, team, and different cost types to isolate the source of the overspend.

## **Walk-Through: Setting it Up in BigPicture**

Follow these steps to manage the portfolio's budget and analyze the overruns:

### Configure Cost Drivers

- **Estimate work**: Ensure that all the tasks to be considered are configured correctly, per [the task preparation manual](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695356/Initial+setup+bringing+your+financial+data+into+BigPicture#Prepare-tasks-for-the-Financials-module), and have estimates set.
- **Rate:** To handle the hourly rates, ensure your rates (either Team or flat - one rate for a box) are accurately configured. Check the [Assign hourly rates to boxes/teams](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695356/Initial+setup+bringing+your+financial+data+into+BigPicture#Assign-hourly-rates-to-boxes%2Fteams) documentation section for more information. As team members log time against their tasks, the system will automatically use this rate to calculate actual costs.

### Set the Initial Budget and Save the Baseline

- Navigate to the Financials module in your "Strategic Growth Initiatives" portfolio box.
- Locate the Budget field and enter the original approved budget for the entire portfolio (for example, $1,500,000). This is your initial financial target.
- To preserve this plan, go to [the Baseline feature](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695747/Set+up+your+project+budget#Baseline). Take a snapshot and name it **"Initial Plan"**. This action captures a snapshot of your initial estimations of the tasks.

### Track Real-Time Performance and Identify Overspend

- Let’s imagine the development hours increased in “Product redesign” and you want to see the updated cost calculations. Check [the Cost Variance](https://appfire.atlassian.net/wiki/spaces/DLPDRAFT/pages/2264695551) reportto see how the current costs compare to the original estimations.
- As the teams log time on their Jira tasks, the Financials module automatically calculates the **Actual Costs** for each project and aggregates them to the portfolio level.
- Check the Total Cost in the **Actual vs. Planned** view for the portfolio and specific initiatives. A red highlight means the project is over the budget.

### Analyze the Cost Breakdown

- **Drill Down into Cost Types:** You can further break down costs within the problem projects. You will find that a significant portion of the cost is attributed to the high-rate development project, confirming your initial suspicions.
- **Filter by Project:** Review the cost variance for each project. You will likely see that "Product Redesign" is the primary driver of the negative variance, while "Market Expansion" is on track.

### Update the Plan and Compare with the Baseline

- After identifying the issues, you can create a new, more realistic budget. Update the Budget value for the projects and the portfolio to reflect the new total.