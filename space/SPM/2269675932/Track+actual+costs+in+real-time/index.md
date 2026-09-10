# Track actual costs in real-time

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Once a project is underway, the Financials module continuously tracks your spending against the budget you've set. The system's ability to provide **real-time actual costs** is a key benefit, offering an immediate and accurate view of your project's financial status based on the work being performed.

## Cost calculations

Here, you can find the formulas used for the cost calculations in the [Financials module](https://appfire.atlassian.net/wiki/spaces/SPM/pages/2269806655).

![cost-calculation.png](/cms_trial/assets/df06933c-c706-460d-b6d6-90b2af8f42d5.png)

### Total cost

| **Rate applied** | **Formula** | **Required settings** |
| --- | --- | --- |
| Box rate | Remaining estimate:  `sum of (box hourly rate) * task workload hours`  `for each task in a period`  [Story Points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/):  `sum of (box hourly rate) * Story Points for open tasks in a period * SP conversion ratio * AVG # working hours per day)` | 1. Box hourly rate 2. Tasks: estimates 3. Tasks: start or end date (at least one within the calculation period). |
| Team rates | Remaining estimate:  `sum of (team hourly rate) * task workload hours in a period`  `for each task in a period`  `and for each team`  [Story Points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/):  `sum of (team hourly rate) * Story Points for open tasks in a period * SP conversion ratio * AVG # working hours per day)`  `for each team` | 1. Team hourly rates. 2. Team allocation to box. 3. Tasks: estimates. 4. Tasks: start or end date (at least one within the calculation period). 5. Task - team assignment. |

### Actual cost

| Rate applied | **Formula** | **Required inputs** |
| --- | --- | --- |
| Box rate | Time Spent:  `sum of (time spent * hourly rate)`  [Story Points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/):  `sum of (box team rate) * (Story Points for completed tasks in a period * SP conversion ratio * AVG # of working hours per day)` | 1. Box hourly rate. 2. Tasks: time spent OR story points estimates. 3. Tasks: start or end date (at least one within the calculation period) |
| Team rates | Time Spent:  `sum of (time spent * hourly rate)`  [Story Points](/cms_trial/space/SPM/1918506126/Story+points+(Effort+mode)/):  `sum of (team rate) * (Story Points for completed tasks in a period * SP conversion ratio * AVG # of working hours per day)`  `for each team` | 1. Team hourly rates. 2. Team allocation to box. 3. Tasks: time spent OR story points estimates. 4. tasks: start or end date (at least one within the calculation period) 5. Task-team assignment. |

### Remaining cost

The remaining cost is calculated by subtracting actual cost from total cost.

## Viewing Actual Costs at Different Levels

The true power of the Financials module lies in its ability to aggregate and display actual costs at every level of your project hierarchy.

### Task level

You can view the actual cost for each individual Jira issue. This provides a granular understanding of what specific tasks are costing you.

1. Choose an initiative from the box switcher.
2. You can see actual cost for each task in initiative in the Work costs breakdown table:

![task-actual-cost.png](/cms_trial/assets/f3be3cd2-c12f-4268-8aaa-b97e72d5c156.png)

### Box level

All actual costs from tasks within a box are automatically rolled up to show the total actual cost for that entire box:

![actual-cost-initiative.png](/cms_trial/assets/f61076a4-cb41-4989-998a-4e984c205a20.png)

You can also check a box actual cost in portfolio’s Initiatives costs and budgets table:

![box-cost-initiatives.png](/cms_trial/assets/00d8d95e-b888-4130-aeff-413e08345748.png)

### Portfolio level

This aggregation continues up the hierarchy. By opening a higher-level box (like portfolio), you can see the total actual cost for all the projects contained within it, offering a top-level financial summary.

![portfolio-level-actual cos.png](/cms_trial/assets/3ba6a964-3fa3-4cb9-82e0-6eb620682b9c.png)