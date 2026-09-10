# How to manually create your Dataplane reports in Dashboard Hub Pro Cloud

## Overview

Dashboard Hub is the Cloud partner to Dataplane Reports for Jira. This page explains how to manually recreate Dataplane reports in Dashboard Hub.

If you migrate app data using Jira’s Cloud Migration Assistant (JCMA), your reports are mapped to Dashboard Hub reports best matched to the original report. See [Migrate from Dataplane Reports to Dashboard Hub](/cms_trial/space/RDD/438796295/Migrate+from+Dataplane+Reports+to+Dashboard+Hub+Pro+Cloud/) to migrate with JCMA.

Refer to the [feature comparison page](/cms_trial/space/RDD/438796304/Feature+comparison+for+Dataplane+Data+Center+vs+Dashboard+Hub+Pro+Cloud/) to learn more about the gadgets used to support your migrations. If you have any questions, contact our [support team](https://appf.re/support).

## Build your reports in Dashboard Hub

The following steps explain how to configure any Dataplane report type in the Dashboard Hub Pro Cloud.

1. Navigate to **Apps**>**Dashboard Hub**.

You can find the *Dashboard Hub* app in the Apps menu once your Jira administrator has installed it.

1. Create a dashboard if you haven’t created one yet. At the top-right, click **More** (**…**) and then select **Create Dashboard**.
2. Enter the *Name*and *Description*,and set the accessrestriction for the Dashboard. For more information, refer to [Create a Dashboard](https://appfire.atlassian.net/wiki/x/coO4C#Create-a-dashboard).
3. Create a blank dashboard or use one of the provided templates. To choose a template, click **Change Template**. For more information about templates, refer to [Use a template](/cms_trial/space/RDD/146310002/How+to+create%2C+edit%2C+clone%2C+delete%2C+and+export+your+dashboard/).
4. Click **Create**.
5. The *Welcome to your Dashboard* screen appears. Click **Add Gadget**to open the gadgets catalog menu. For more information about gadgets, refer to [Gadgets](/cms_trial/space/RDD/2116747794/Gadgets/).

![Dashboard Hub adding a Dataplane report gadget](/cms_trial/assets/f8e86cd2-9d49-48e6-a00b-3f8ee0f937b0.gif)

1. To configure the required Dataplane report under the Jira product, select the corresponding gadget to add to the current dashboard. To review the feature parity for both products and identify the gadget to use, refer to [Feature comparison for Dataplane Reports and Dashboard Hub](/cms_trial/space/RDD/438796304/Feature+comparison+for+Dataplane+Data+Center+vs+Dashboard+Hub+Pro+Cloud/).
2. Configure the gadget similar to the Dataplane report you want to recreate and click **Add**.
3. To save the Dashboard, click **Save**.

### **Example scenarios**

*Current Issue Assignees in Dataplane*

**Dataplane report use case:** Consider the current metrics Dataplane report showing the data from the JQL query "status = Open", broken down by Assignee.

- **Dataplane Report**: Current Issue Assignees
- **JQL**: `status = Open`
- **Chart Type**: Pie chart

![Dashboard Hub How to manually create your Dataplane reports in Dashboard Hub Pro Cloud report preview](/cms_trial/assets/1e23488b-6fca-40a1-908a-93dfcd3fb9c3.jpg)

**Rendered report:**

![Dashboard Hub How to manually create your Dataplane reports in Dashboard Hub Pro Cloud report preview](/cms_trial/assets/8f71d0b6-aaaa-4d62-bac3-5edbb7c5b7ff.jpg)

*Create a similar report type with the Jira Custom Charts gadget in Dashboard Hub Pro Cloud*

1. Open your dashboard in Dashboard Hub, then click **Edit**. To create a new Dashboard, refer to [Create Dashboard](https://appfire.atlassian.net/wiki/x/coO4C#Create-a-dashboard).
2. Click **Add Gadget**.
3. Select the Jira Custom Charts gadget. Refer to the [feature parity page](/cms_trial/space/RDD/438796304/Feature+comparison+for+Dataplane+Data+Center+vs+Dashboard+Hub+Pro+Cloud/) to determine the gadget to choose.
4. Configure the gadget to match the Dataplane report you want to replicate.

   1. **Name**: Current Issue Assignees\_StatusOpe
   2. **Datasource**: Use `This Jira Instance` in this example. Learn more about the options for connecting to other Jira instances in [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/).
   3. **JQL** : `status = “To Do”`.
   4. **View Type**: Pie chart
   5. Customize the chart by selecting the appropriate field values for *Chart By*, *Aggregation,* and *Field*. For more information refer to [Jira Custom Charts](https://appfire.atlassian.net/wiki/x/N4G4C).

![Dashboard Hub How to manually create your Dataplane reports in Dashboard Hub Pro Cloud Dashboard Hub GadgetConfig1](/cms_trial/assets/1464f68d-84c0-44a4-9eff-7b44d288dc1b.jpg)

**Report preview:**

Once you enter all the configuration details, the report is generated. To add the gadget to the Dashboard, click **Add**.

![Dashboard Hub How to manually create your Dataplane reports in Dashboard Hub Pro Cloud dashboard preview](/cms_trial/assets/79465e07-7f71-434f-bf8f-44fbcb0c4d1a.jpg)

To save the Dashboard configurations, click **Save**.

![Dashboard Hub How to manually create your Dataplane reports in Dashboard Hub Pro Cloud dashboard preview](/cms_trial/assets/4a48808e-f34c-4569-ad05-054e0223b822.jpg)

You see that a similar report is configured in Dashboard Hub Pro Cloud. Similarly, you can add more gadgets and configure the other report types in the Dashboard.

The reports might look different based on the configurations and app templates.

The reports generated in Dataplane Reports and Dashboard Hub Pro Cloud are based on the Jira data available in the instance. To create the dashboard reports with the same data, migrate your Jira Data Center data to Jira Cloud. To migrate, refer to [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?hosting=server&tab=overview) or [Configuration Manager for Jira](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview).

If you have any questions about converting your Dataplane reports with Dashboard Hub Pro Cloud, contact our [support team](https://appf.re/support).

To review the user documentation for the source reports configured in Dataplane Reports, see [Configure reports](https://appfire.atlassian.net/wiki/spaces/dataplane/pages/455934863).

## Historical values reports

To facilitate your migrations from Dataplane to Dashboard Hub, you can map your **historical** values reports in Dashboard Hub using the Jira Custom Charts and Historical Insights gadgets.

### When to use Historical Insights

The Historical Insights gadget aligns with the following Dataplane reports:

- Issue Values By Date
- Issue Values Snapshots By Date
- Issue Values Snapshots Sum By Date

See [Historical Insights](/cms_trial/space/RDD/3058532407/Historical+Insights/) to learn how to display your data in Dashboard Hub.

### When to use Jira Custom Charts

If you are manually recreating your reports in Dashboard Hub, the Jira Custom Charts gadget can be configured to suit a wide range of use cases. See [Jira Custom Charts](/cms_trial/space/RDD/146309431/Jira+Custom+Charts/) to learn more.

### Key mapping concepts

| **Dataplane Reports** | **Dashboard Hub Pro** | **Mapping notes** |
| --- | --- | --- |
| Summary (Search) | JQL query | In Dataplane, the **Summary** displays work items using the *Projects / Categories / Boards / Filters* tab or the *JQL* tab. In Jira Custom Charts, select **JQL** to enter a query directly, or select **Filter** to use a saved Jira filter. |
| Time period | JQL date clause | In Dataplane, you select a **Time Period** from preset ranges (e.g., Last 3 Months) or set explicit **Start Date** / **End Date** values. In Jira Custom Charts, add a date clause to your JQL (e.g., `created >= -3m`). Only time periods supported by JQL are possible. |
| Segment By | Group By | In Dataplane, **Segment By** breaks down results by one or more Jira fields. In Jira Custom Charts, use **Group By** (available when you select a grouped, stacked, or multi-chart view type). |

Example Dataplane gadget configuration

![Screenshot 2024-01-30 at 15.28.12.png](/cms_trial/assets/c9d22af7-7297-4583-be37-6d596a56ce5b.png)

Example Dashboard Hub gadget configuration

![DH-example-config.png](/cms_trial/assets/355e57ef-c678-45af-991b-7a8cc08d922c.png)

When you migrate Dataplane Reports to Dashboard Hub, the following historical reports are mapped to the Jira Custom Charts gadget. For each report, a corresponding Jira Custom Charts report is created in Dashboard Hub. If you need help recreating Dataplane historical values reports with the Jira Custom Charts gadget, refer to the individual reports below.

### **Issues Created By Date**

This Dataplane report displays the number of work items that were created on a specific date.

View Issues Created By Date example mappings for Dashboard Hub:

| **Setting** | **Dataplane** | **Dashboard Hub** | **Notes** |
| --- | --- | --- | --- |
| **Report/Gadget** | Issues Created by Date | Jira Custom Charts |  |
| **Datasource** | Configured Jira instance | Selected datasource: This Jira instance | The datasource is the Jira instance to connect to. Select a different datasource if your data is on another instance. See [Datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources). |
| **Query** | **Summary:** Use the *JQL* tab or *Projects / Categories / Boards / Filters* tab `project = "ACME"` | Select **JQL**, then enter  `project = "ACME" AND created >= -3m ORDER BY created DESC` | Select **Filter** to use a saved Jira filter instead. The JQL date clause (`created >= -3m`) replaces Dataplane's Time Period. Adjust as needed: `-30d` |
| **Time Period** | Start Date / End Date | Controlled by the JQL query date clause |  |
| **Chart Type** | Column chart example for historic reports | **View type**: Bar chart | Dataplane's Column Chart (vertical bars) corresponds to the Custom Charts Bar chart. |
| **Interval** | Preset dropdown. Controls whether the results are aggregated on a daily, weekly, monthly, quarterly, or annual basis. | **Chart by**: Created, grouped by week or month. | Select the time grouping when you choose a date field in Chart By. Replaces Dataplane's Interval control. |
| **Value Of** | Work item (issue) count | **Aggregation Field**: Work Items  **Aggregation**: Count |  |
| **Segment By** | Group results by the value of one or more Jira fields or properties, for example, *Priority* | **Group by**:*Priority* | Change View Type to **Stacked bar chart** or **Grouped bar chart** to enable Group By. |
| **Trend line** | Not available | **Show trend line**: On | Use the **Show trend line** toggle. To change the color, click the default line color and select a different color. |

### **Issues By Date**

Dataplane’s Issue By Date report displays the number of work items that reference a specific date, known as the **Date Basis**. You can select a Date Basis of Targeted Release Date to see how many work items were scheduled for release in a given date range.

View Issues By Date example mappings for Dashboard Hub:

| **Setting** | **Dataplane** | **Dashboard Hub** | **Notes** |
| --- | --- | --- | --- |
| **Report/Gadget** | Issues By Date | Jira Custom Charts |  |
| **Datasource** | Configured Jira instance | Selected datasource: This Jira instance | The datasource is the Jira instance to connect to. Select a different datasource if your data is on another instance. See [Datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources). |
| **Query** | **Summary:** Use the *JQL* tab or *Projects / Categories / Boards / Filters* tab `project = "ACME"` | Select **JQL**, then enter  `project = "ACME" AND "Target Release Date" >= "2026-01-01" AND "Target Release Date" < "2026-07-01"` | Select **Filter** to use a saved Jira filter instead. The JQL date clause replaces Dataplane's Time Period. |
| **Time Period** | Start Date / End Date | Controlled by the JQL query date clause |  |
| **Chart Type** | Column chart example for historic reports | **View type**: Bar chart | Dataplane's Column Chart (vertical bars) corresponds to the Custom Charts Bar chart. |
| **Interval** | Preset dropdown. Controls whether the results are aggregated on a daily, weekly, monthly, quarterly, or annual basis. | **Chart by**: Due date | Replaces Dataplane's Interval control. |
| **Value Of** | Work item (issue) count | **Aggregation Field**: Work Items  **Aggregation**: Count |  |
| **Segment By** | Group results by the value of one or more Jira fields or properties, for example, Priority | **Group by**:Priority | Change View Type to **Stacked bar chart** or **Grouped bar chart** to enable Group By. |
| **Trend line** | Not available | **Show trend line**: On | Use the **Show trend line** toggle. To change the color, click the default line color and select a different color. |

### **Issue Reporters By Date**

This report displays the number of work items created on specific dates, broken down by the issue Reporter.

View Issue Reporters By Date example mappings for Dashboard Hub:

| **Setting** | **Dataplane** | **Dashboard Hub** | **Notes** |
| --- | --- | --- | --- |
| **Report/Gadget** | Issue Reporters By Date | Jira Custom Charts |  |
| **Datasource** | Configured Jira instance | Selected datasource: This Jira instance | The datasource is the Jira instance to connect to. Select a different datasource if your data is on another instance. See [Datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources). |
| **Query** | **Summary:** Use the *JQL* tab or *Projects / Categories / Boards / Filters* tab `project = "ACME"` | Select **JQL**, then enter  `project = "ACME" AND created >= "2026-01-01" AND created < "2026-07-01"` | Select **Filter** to use a saved Jira filter instead. The JQL date clause replaces Dataplane's Time Period. |
| **Time Period** | Start Date / End Date | Controlled by the JQL query date clause |  |
| **Chart Type** | Column chart example for historic reports | **View type**: Bar chart | Dataplane's Column Chart (vertical bars) corresponds to the Custom Charts Bar chart. |
| **Interval** | Preset dropdown. Controls whether the results are aggregated on a daily, weekly, monthly, quarterly, or annual basis. | **Chart by**: Created | Select the time grouping when you choose a date field in Chart By. Replaces Dataplane's Interval control. |
| **Value Of** | Work item (issue) count | **Aggregation Field**: Work Items  **Aggregation**: Count |  |
| **Segment By** | Group results by the value of one or more Jira fields or properties, for example, *Priority* | **Group by**:Reporter | Each reporter’s work items are plotted as a separate series. Change View Type to **Stacked bar chart** or **Grouped bar chart** to enable Group By. |
| **Trend line** | Not available | **Show trend line**: On | Use the **Show trend line** toggle. To change the color, click the default line color and select a different color. |

### **Issues Resolved By Date**

This report displays the number of work items that were resolved on a specific date.

View Issues Resolved By Date example mappings for Dashboard Hub:

| **Setting** | **Dataplane** | **Dashboard Hub** | **Notes** |
| --- | --- | --- | --- |
| **Report/Gadget** | Issue Resolved By Date | Jira Custom Charts |  |
| **Datasource** | Configured Jira instance | Selected datasource: This Jira instance | The datasource is the Jira instance to connect to. Select a different datasource if your data is on another instance. See [Datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources). |
| **Query** | **Summary:** Use the *JQL* tab or *Projects / Categories / Boards / Filters* tab `project = "ACME"` | Select **JQL**, then enter  `project = "ACME" AND resolved >= -6m ORDER BY resolved DESC` | Select **Filter** to use a saved Jira filter instead. Use resolved `>=` to filter by resolution date, replacing Dataplane's Time Period. |
| **Time Period** | Start Date / End Date | Controlled by the JQL query date clause |  |
| **Chart Type** | Column chart example for historic reports | **View type**: Stacked Bar chart | Dataplane's Column Chart (vertical bars) corresponds to the Custom Charts Bar chart. |
| **Interval** | Preset dropdown. Controls whether the results are aggregated on a daily, weekly, monthly, quarterly, or annual basis. | **Chart by**: Resolved | Select the time grouping when you choose a date field in Chart By. Replaces Dataplane's Interval control. |
| **Value of** | Work item (issue) count | **Aggregation Field**: Work Items  **Aggregation**: Count |  |
| **Segment By** | Group results by the value of one or more Jira fields or properties, for example, *Priority* | **Group by**:Assignee | Each assignee appears as a colored segment in thte stacked bar. Change View Type to **Stacked bar chart** or **Grouped bar chart** to enable Group By. |
| **Trend line** | Not available | **Show trend line**: On | Use the **Show trend line** toggle. To change the color, click the default line color and select a different color. |

### **Sum Numeric Field By Date**

This report calculates the sum of the current values of a specified numeric field in Jira for all work items included in the search.

Sum Numeric Field By Date example mappings for Dashboard Hub:

| **Setting** | **Dataplane** | **Dashboard Hub** | **Notes** |
| --- | --- | --- | --- |
| **Report/Gadget** | Sum Numeric Field By Date | Jira Custom Charts |  |
| **Datasource** | Configured Jira instance | Selected datasource: This Jira instance | The datasource is the Jira instance to connect to. Select a different datasource if your data is on another instance. See [Datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources). |
| **Query** | **Summary:** Use the *JQL* tab or *Projects / Categories / Boards / Filters* tab `project = "ACME"` | Select **JQL**, then enter  `project = "ACME" AND type = Story AND created >= -6m ORDER BY created DESC` | Select **Filter** to use a saved Jira filter instead. The JQL date clause replaces Dataplane's Time Period. |
| **Time Period** | Start Date / End Date | Controlled by the JQL query date clause |  |
| **Date Basis** | Created Date (dropdown) | **Chart By**: Bar chart | Dataplane's Column Chart (vertical bars) corresponds to the Custom Charts Bar chart. |
| **Interval** | Preset dropdown. Controls whether the results are aggregated on a daily, weekly, monthly, quarterly, or annual basis. | **Chart by**: Created | Select the time grouping when you choose a date field in Chart By. Replaces Dataplane's Interval control. |
| **Value Of** | Story points | **Aggregation Field**: Story points  **Aggregation**: Sum |  |
| **Segment By** | Group results by the value of one or more Jira fields or properties, for example, *Priority* | **Group by**:Reporter | Each reporter’s work items are plotted as a separate series. Change View Type to **Stacked bar chart** or **Grouped bar chart** to enable Group By. |