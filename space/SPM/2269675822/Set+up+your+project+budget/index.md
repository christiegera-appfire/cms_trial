# Set up your project budget

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The first step in effective financial tracking is to define a clear and realistic budget for your project or initiative. The Financials module in BigPicture lets you establish this, providing a fixed reference point against which you can measure performance throughout the project lifecycle.

## Budget

You can define a budget for portfolio and initiative levels. In both cases, the budget field is available in the Actual vs Planned view, top-left section:

![budget.png](/cms_trial/assets/273b4e11-a460-426f-a1f9-df45d59de95b.png)

Click the edit icon and set the value. Now, the budget line is also visible in the chart.

Hold the pointer over the info icon to check the date, time, and editor name of the last update.

In the portfolio view, you can also change a budget for an initiative using an inline edit in the Initiatives costs and budgets:

![initiative-budget.png](/cms_trial/assets/ee889dd9-fe2a-4199-ba09-b17b0ca1e8ed.png)

## Baseline

Baseline is a snapshot of your budget at a specific point in time, typically at the start of the project or a major phase. You can compare many snapshot to a baseline using the Cost Variance tab, giving you insight into cost deviations from the baseline.

Keeping your project's budget on track can be tricky, especially when plans change over time. With the simplified budget-setting feature, you can quickly **set up a cost baseline** and **take snapshots along the way**. This makes it simple to compare your original planned costs with your actual or current cost estimates. By regularly checking these baselines, program and portfolio managers can stay in control, spot issues early, and make smarter decisions from start to finish.

![financials-module-cost-variance-tab.png](/cms_trial/assets/e1dd3b1f-7be1-422c-8824-a38521c21d06.png)

### About the snapshots

Snapshots of the financial information are **taken for the entire app** (all boxes). The first snapshot you take automatically becomes the **baseline**.

- Snapshots can be taken **manually** or **automatically**. The automatic frequency of snapshots is based on configuration.
- Snapshots can be removed.
- The baseline snapshot can be changed.

**Limitations**: You can keep up to 15 snapshots.

You can manage snapshots in the Financials section of the app Administration.

### Security and access

| **Role** | **Cost variance tab access** | **Configuration access** |
| --- | --- | --- |
| Financial Viewer | ✅ | ❌ |
| Financial Admin | ✅ | ✅ |
| Box Admin | ✅ | ❌ |
| App Admin | ✅ | ✅ |
| Jira Admin | ✅ | ✅ |

### Cost variance tab

#### Availability

The Cost Variance tab is available ONLY in **portfolio boxes**.

#### How to access

In the Financials module:

1. Go to the *Cost variance* tab in the side panel.

![financials-module-switch-to-cost-variance-tab.png](/cms_trial/assets/bdd074b5-8cc0-4cc6-9cb9-a342ce1d69c1.png)

#### How to interpret the data

The app compares each snapshot with the current data.

On the left, you see the current information based on project boxes in a portfolio. On the right, you see data from the selected snapshots.

![financials-module-cost-variance-box-data-vs-baseline.png](/cms_trial/assets/b22882d0-f2e7-49bb-a2a9-e96363df2f33.png)

| **Cost variance** | **Description** |
| --- | --- |
| Negative cost variance negative-variance-red.pngnegative-cost-variance-yellow.png | Costs increased compared to the snapshot. |
| Positive cost variance positive-cost-variance-green.png | Costs decreased compared to the snapshot. |
| Grey icon without numbers no-cost-varicance-grey.png | No discrepancy between the snapshot and current data. |

#### Select snapshots for cost variance calculation

You can select **multiple snapshots** for comparison.

![financials-module-cost-variance-multiple-snapshots.png](/cms_trial/assets/d4976f0e-a24b-414d-b15a-bd7ac3a55211.png)

#### Add snapshots to the view

In the *Cost variance* tab of the Financials module:

1. Click the plus button to open the view adjustment menu.
2. In the **Snapshots to compare** section, click **Add snapshot** to open the dropdown.
3. Select a snapshot from the list.

#### Remove snapshots from the view

In the *Cost variance* tab of the Financials module:

1. Click the plus button to adjust the view.
2. In the **Snapshots to compare** section, click the bin icon.

![financials-module-cost-variance-remove-snapshots-from-view.png](/cms_trial/assets/882bf18e-44a5-4ea3-b9b0-3a4739d8714a.png)

### Configuration

#### Initial setup

To set a baseline:

1. Go to the **Cost Variance** tab in the side panel.
2. Click **Configure.**
3. Adjust the automation settings.
4. Take the first snapshot to establish the baseline.

#### How to access the configuration page

Snapshot information and automation settings can be found in **App Administration** > **Financials** tab > **Baselines**.

![image-20250402-095623.png](/cms_trial/assets/6e980255-7386-4f52-adff-95aefe9ca7e0.png)

#### Automation settings

You can set up the app to take the snapshots automatically:

- At the end of **each quarter**
- At the start of **each month**
- **Never**