# Cost Variance

## How does it work

Keeping your project's budget on track can be tricky, especially when plans change over time. Luckily, there's an easier way. With the simplified budget-setting feature, you can quickly **set up a cost baseline** and **take snapshots along the way**. This makes it simple to compare your original planned costs with your actual or current cost estimates. By regularly checking these baselines, program and portfolio managers can stay in control, spot issues early, and make smarter decisions from start to finish.

![financials-module-cost-variance-tab.png](/cms_trial/assets/6c1df60a-2a1a-4013-822f-454cd6343407.png)

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

## Cost variance tab

### Availability

The Cost Variance tab is available ONLY in **portfolio boxes**.

### How to access

In the Financials module:

1. Go to the *Cost variance* tab in the side panel.

![financials-module-switch-to-cost-variance-tab.png](/cms_trial/assets/bcc193c2-b512-4f19-8005-5a28b92c046c.png)

### How to interpret the data

The app compares each snapshot with the current data.

On the right, you see data from the selected snapshots. On the left, you see the current information based on project boxes in a portfolio.

![financials-module-cost-variance-box-data-vs-baseline.png](/cms_trial/assets/0193c029-bcc3-4ce8-9ed3-6508c2484ed6.png)

| **Cost variance** | **Description** |
| --- | --- |
| Negative cost variance negative-variance-red.pngnegative-cost-variance-yellow.png | Costs increased compared to the snapshot. |
| Positive cost variance positive-cost-variance-green.png | Costs decreased compared to the snapshot. |
| Grey icon without numbers no-cost-varicance-grey.png | No discrepancy between the snapshot and current data. |

### Select snapshots for cost variance calculation

You can select **multiple snapshots** for comparison.

![financials-module-cost-variance-multiple-snapshots.png](/cms_trial/assets/c9e1938f-ba09-41ba-bba3-41f6563c8a0f.png)

#### Add snapshots to the view

In the *Cost variance* tab of the Financials module:

1. Click the plus button to open the view adjustment menu.
2. In the **Snapshots to compare** section, click **Add snapshot** to open the dropdown.
3. Select a snapshot from the list.

#### Remove snapshots from the view

In the *Cost variance* tab of the Financials module:

1. Click the plus button to adjust the view.
2. In the **Snapshots to compare** section, click the bin icon.

![financials-module-cost-variance-remove-snapshots-from-view.png](/cms_trial/assets/6d604cf5-4fcb-4cce-bccb-646a62645074.png)

## Configuration

### Initial setup

To set a baseline:

1. Go to the **Cost Variance** tab in the side panel.
2. Click **Configure.**
3. Adjust the automation settings.
4. Take the first snapshot to establish the baseline.

### How to access the configuration page

Snapshot information and automation settings can be found in **App Administration** > **Financials** tab > **Baselines**.

![image-20250402-095623.png](/cms_trial/assets/713e3a55-6f52-41f4-bfae-71ced275200e.png)

### Automation settings

You can set up the app to take the snapshots automatically:

- At the end of **each quarter**
- At the start of **each month**
- **Never**