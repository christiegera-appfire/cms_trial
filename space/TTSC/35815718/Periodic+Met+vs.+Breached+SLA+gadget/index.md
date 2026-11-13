# Periodic Met vs. Breached SLA gadget

The Periodic Met vs. Breached SLA gadget displays SLA performance as a **bar chart** grouped by status. The horizontal axis represents time, which can be displayed as either **weekly** or **monthly** periods.

This tutorial will guide you through adding and configuring the gadget on your Jira dashboard.

## How to add Periodic Met vs. Breached SLA gadget

### **Jira admins**

Jira admins can add the gadget directly to the **system dashboard** (Global dashboard) without creating a new dashboard.

### **For non-admins**

Follow these steps to add the gadget to a custom dashboard:

1. Open a custom dashboard, or create one following the [Jira documentation](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-dashboards/).
2. Click the **Edit** button. The *Add a gadget* side panel opens.
3. In the side panel, search for `TTS - Periodic Met vs Breached SLA`.
4. Click **Add**. The gadget configuration screen appears.
5. Configure the gadget:

   ![Time to SLA Periodic Met vs Breached SLA gadget configuration](/cms_trial/assets/69f42888-e5c9-4707-a265-fb157e898c8e.png)
   - **Title:** Enter a title for the gadget.
   - **Filter:** **Filter:** Start typing the name of a saved Jira filter, then select it from the matching results. You can also select an SLA to include specific work items. Leave this field blank to include all SLAs.

     - **Note:** The gadget is limited to a maximum of **2,000 work items**. If your filter exceeds this limit, only the first 2,000 work items will be displayed.
   - **Time Period:** Choose whether to display data **weekly** or **monthly.**
   - **Days Previously:** Enter the number of days in the past from which you want to collect SLA data. This sets the start date for SLAs.

     - For example, selecting **30 days** will show SLAs that started within the past 30 days.
   - **Refresh** period**:** (Optional) Set a refresh interval in minutes for the gadget to update automatically.

You can limit work items based on Created Date or Resolved Date using JQL in the **Filter** field. Alternatively, limit data by SLA Start Date using the Days Previously field.

1. Click **Save**.

The gadget will now appear on the dashboard.

This gadget displays the total number of SLA instances. If a work item has multiple SLAs in it, then each SLA will be counted separately.

## Examples

Let’s say you configure the gadget as follows:

- **Days Previously**: `30d` (SLAs that started within the last 30 days).
- **Filter**: A saved search that shows work items created or resolved in the past 7 days.

The resulting bar chart will display:

- SLAs from the last **30 days** on the X-axis.
- Work items scoped over the **last 7 days** based on your filter criteria.

This configuration answers the query: `Show me work items from the last 7 days whose SLAs started no more than 30 days ago.`

## Reports integration

When you click a bar in the gadget, you’ll be redirected to the **SLA Reports** page. Based on the gadget’s configuration, **Time to SLA** will automatically create a filter for the selected data.

You can click **Generate** to view the breakdown of the gadget’s components in a detailed report.