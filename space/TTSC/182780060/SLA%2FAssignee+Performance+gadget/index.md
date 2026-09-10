# SLA/Assignee Performance gadget

The TTS - SLA/Assignee Performance hadget displays the number of SLAs that are met, breached, or in the critical zone based on the assignee or specific SLA, providing a visual representation of the performance.

This tutorial will walk you through the process of adding the SLA/Assignee Performance Gadget to your dashboard.

## How to add TTS - SLA/Assignee Performance gadget

### **Jira admins**

Jira admins can add the gadget directly to the system dashboard (Global dashboard) without creating a new dashboard.

### **For non-admins**

Follow these steps to add the gadget to a custom dashboard:

1. Open a custom dashboard, or create one following the [Jira documentation](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-dashboards/).
2. Click the **Edit** button. The *Add a gadget* side panel opens.
3. In the side panel, search for `TTS - Periodic Met vs Breached SLA`.
4. Click **Add**. The gadget configuration screen appears.
5. Configure the gadget:

   ![Time to SLA SLA Assignee Performance gadget configuration](/cms_trial/assets/e585d651-8910-44ec-a470-308bae1c01f5.png)
   - **Title:** Enter a title for the gadget.
   - **Group by:** Choose the grouping option based on SLA or assignee. The *Filter* and *Assignees*/*SLA* dropdowns appear.

     - **SLA:** If you choose to group by SLA, enter the filter as a scope of this gadget and the SLA that you want to see on it.
     - **Assignee:** If you choose to group by assignee, enter the assignee names that you want to see in this gadget and select filters to narrow down the displayed work items.

       - **Note:** The gadget is limited to a maximum of **2,000 work items**. If your filter exceeds this limit, only the first 2,000 work items will be displayed.
   - **Add remaining duration:** Check this box to see the SLAs based on the remaining duration.

     - Enabling this displays the **Remaining Duration** options. Choose the default value (8h, 24h, 48h) or add a custom one.
6. Click **Save**.

The gadget will now appear on the dashboard.

## Examples

Below are examples of the configuration results mentioned above. You can view the gadget’s output in two formats: **Panel View** and **Table View**.

![Time to SLA SLA Assignee Performance gadget preview](/cms_trial/assets/de9a0e95-a219-4f2b-86ce-5293d2512a4f.png)

![Time to SLA SLA Assignee Performance gadget settings panel](/cms_trial/assets/19f8a8db-90be-44c0-9eef-9557bb4301c1.png)

## Get reports from gadgets

Clicking on any of the bars in the gadget will redirect you to the **Reports** page. Based on the gadget’s configuration, Time to SLA automatically creates a filter for the selected data. You can then click **Generate** to view the detailed report.

When you click on a specific segment of a bar (for example, `Breached`), the filter will show:

- **SLA Indicator: Breached**

This means the report will display only the SLAs that were breached. You can modify this filter or adjust the configurations to customize the report further.