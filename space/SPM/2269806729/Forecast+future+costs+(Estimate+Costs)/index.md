# Forecast future costs (Estimate Costs)

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Beyond tracking what you've already spent, the Financials module in BigPicture provides the capability to **forecast future costs**, often referred to as **remaining cost**. This crucial feature lets you anticipate upcoming expenditures based on the remaining work, helping you manage your budget proactively and make informed decisions about resource allocation and project trajectory.

BigPicture automatically calculates remaining costs using a formula similar to actual costs, but focused on the work yet to be completed:

> The remaining cost is calculated by subtracting the actual cost from the total cost.

- **Remaining Effort:** This value is primarily derived from the **"Remaining Estimate" field in your Jira issues**. As tasks progress and time is logged, the remaining estimate in Jira should be updated to reflect the effort still required. BigPicture pulls this dynamic data.
- **Team/Box Rate:** If no specific user or job role rate is defined.

This continuous calculation provides a dynamic forecast that adjusts as your project evolves and remaining work is re-estimated.

## Influencing and Viewing Estimated Costs

To ensure accurate forecasting, it's vital to maintain up-to-date "Remaining Estimate" values in your Jira tasks. Project managers and team members should regularly review and adjust these estimates as new information becomes available or as work progresses.

You can view these estimated costs at various levels within the Financials module:

- **Task Level:** See the projected cost to complete individual Jira issues.
- **Project Level:** The estimated costs from all tasks within a project "Box" are aggregated, providing a total projected cost to finish that project.
- **Portfolio/Program Level:** Estimated costs roll up further to give you a comprehensive forecast for entire programs or portfolios, allowing for high-level financial planning and risk assessment.

These estimated costs are typically displayed in dedicated columns within the Financials module grid. By actively managing and reviewing these figures, you can anticipate future financial demands, identify potential budget shortfalls before they occur, and adjust your plans to ensure financial viability.