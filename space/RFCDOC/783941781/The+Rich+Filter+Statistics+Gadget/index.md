# The Rich Filter Statistics Gadget

## About the Rich Filter Statistics gadget

The *Rich Filter Statistics* gadget displays the collection of issues grouped by a specific field/criteria. It resembles Jira’s built-in *Issue Statistics* gadget, but it is based on a rich filter instead of a Jira saved search and thus adds several new features:

- the collection of issues used for the statistics can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the gadget can group the issues by an issue field or by a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/);
- the gadget can group the issues by the values of a date or date time field to compute daily, weekly, monthly, quarterly, or yearly statistics;
- the gadget can display multiple result types at the same time (such as *Issue Count* and *Story Points*);
- the gadget can display [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/);
- the gadget can display one or more [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/);
- the user can change the sorting order by clicking on a column name;
- the gadget can display the data as a chart; the user can switch between the table view and the chart view by clicking on an icon;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

**Example 1**: Issue Count and Story Points aggregated by the issue field Priority:

![2026-02-19_11-10-17.png](/cms_trial/assets/9b4c2385-b119-4977-b6a8-ae49005a8bc3.png)

**Example 2**: Issue Count and Story Points aggregated by a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) named High-level Status:

![contentId-783941781](/cms_trial/assets/c3608c44-94de-413c-8eb6-3951be5bf828.png)

The labels and colors displayed for High Level Status come from the clauses defined in this smart filter's configuration.

## Configuring the Rich Filter Statistics gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Statistics* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783941781](/cms_trial/assets/498bad75-4c23-4a7e-8ee6-125795aec027.png)

When using Rich Filters across multiple projects with different types (e.g., Jira Software, Jira Product Discovery, JWM), you can encounter duplicate field names for the **Statistics type**, such as multiple *Customer* fields, in dropdown menus.

To help you distinguish between fields with the same name, Rich Filters shows additional information in tooltips when you hold the pointer over any field in dropdown menus:

- Field type appears in brackets (for example, *Customer* [text])
- Custom field ID is added when duplicates still exist (for example, *Customer [text] cf[12345]*)

Edit the gadget configuration as described below:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. For more details, check the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page. |
| **Working Query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Statistic type** | Select the issue field or the [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) on which the issues will be grouped. The drop-down list includes the smart filters defined in the selected rich filter: High-level Status.png The gadget supports several types of breakdown configuration, depending on the selected *Statistic type*:   - Statistics on option fields (e.g., Priority, Status, select custom fields, etc.) or smart filters - Statistics on date or date time fields - Statistics on time series   These options are further detailed in the sections below. |

### Statistics on option fields or smart filters

The following settings are applicable when the selected *Statistic type* is an option field (e.g., Priority, Status, select custom fields, etc.) or a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/):

| **Setting** | **Description** |
| --- | --- |
| **Sort by** | Select how to sort the values of your *Statistic type*:   - **Total:** This will be sorted by the value computed for each *statistical type* group (if multiple value columns exist, the first one will be used for sorting). - **Alphabetical:** This will use alphabetical order for the statistical *type* groups. - **Natural:** This will use the native sorting order of the issue field or smart filter selected as Statistic type, i.e., the order configured for the field or smart filter's options. This sorting option is available only for the issue fields Priority, Status, and Issue Type and for smart filters. |
| **Reverse sort order** | If checked, the sort order is reversed. |
| **Maximum rows** | If set, limit the number of result rows to display.  The user can still display all the computed rows by clicking on the number of rows in a rounded rectangle at the bottom right of the gadget. |
| **Show percentage bars** | If checked, the gadget displays a bar chart for each statistic value:   - for all value types other than [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion of each value relative to the total; - for [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion corresponding to the ratio. |
| **Show totals** | If checked, the gadget displays a row with the totals for each selected value. |
| **Values** | Select the values to be computed for each *Statistic type* group. You can select up to 10 values at a time.  The following value types are available:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e., *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, when using Jira Software, the gadget can show the number of *Story Points* for each *Statistical type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios**: displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) configured in the rich filter (percentage or ratio). contentId-783941781 |

### Statistics on date fields

The following settings are applicable when the selected *Statistic type* is a date or a date time field:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to their values for the date or date time field selected as *Statistic type*.  The available options are *Days*, *Weeks*, *Months*, *Quarters*, *Years*, and *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e., with the appropriate aggregation period so that all the relevant issues are included). |
| **Time Range** | Together with its sub-settings, this specifies the total time span for which the statistics should be computed.  The time range sub-settings depend on the option selected in the *Time range* drop-down as described below. |
| **Time Range** | **Time range subsetting** | **Description** |
| **Number of periods** | **Number of days / weeks, etc.** | Enter a number of periods. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain past values. Therefore, you should always select Past for these fields, as you will never find any issues created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and the future. For this field, it is more useful to select Future to see statistics for issues that are due soon or Past & Future to see statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date in the issues' values).  *All dates* are the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options that depend on the selected *Aggregation period.*  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Reverse sort order** | If checked, the default chronological order is reversed. |
| **Show percentage bars** | If checked, the gadget displays a bar chart for each statistic value:   - for all value types other than [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion of each value relative to the total; - for [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion corresponding to the ratio. |
| **Show totals** | If checked, the gadget displays a row with the totals for each selected value. |
| **Values** | Select the values to be computed for each *Statistic type* group. You can select up to 10 values at a time.  The following value types are available:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e., *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, when using Jira Software, the gadget can show the number of *Story Points* for each *Statistical type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios**: displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) configured in the rich filter (percentage or ratio). contentId-783941781 |

### Statistics on time series

The gadget can also be configured to display one or more [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/). To do so, select the Time series option in the *Statistic type* setting.

![contentId-783941781](/cms_trial/assets/3bfc634f-af19-4505-9329-5149b39a9310.png)

The following settings are applicable when the selected *Statistic type* is *Time series*:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to the date or date time fields on which the selected time series are based.  The available options are *Days, Weeks, Months, Quarters, Years, and Auto.*  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e., with the appropriate aggregation period so that all the relevant issues are included). |
| **Time Range** | Together with its sub-settings, this specifies the total time span for which the statistics should be computed.  The time range sub-settings depend on the option selected in the *Time range* drop-down as described below. |
| **Time Range** | **Time range subsetting** | **Description** |
| **Number of periods** | **Number of days / weeks, etc.** | Enter a number of periods. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values from the past. Therefore, you should always select Past for time series based on these fields, as you will never find any issues created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For a time series based on this field, it is more useful to select Future to see statistics for issues that are due soon or Past & Future to see statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date in the issues' values).  *All dates* are the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options, which depend on the selected *Aggregation period.*  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Reverse sort order** | If checked, the default chronological order is reversed. |
| **Show percentage bars** | If checked, the gadget displays a bar chart for each of the selected time series:   - for time series based on all value types other than *custom ratios*, the proportion of each value relative to the total; - for time series based on [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion corresponding to the ratio. |
| **Show totals** | If checked, the gadget displays a row with the totals for each selected time series. |
| **Time series** | You can select one or several time series to display. The gadget displays a new column for each selected time series with the values computed from the given time series. contentId-783941781 |

## Quick charts in the Rich Filter Statistics gadget

In addition to the main table view, the *Rich Filter Statistics* gadget offers a chart view, which displays the results as a chart. This chart, referred to as a *quick chart*, requires no additional configuration. You can switch between the table view and the chart view by clicking on the corresponding icon at the gadget's bottom right.

By default, a donut chart based on the first column of the table is displayed. You can choose the chart type and statisticsvalues by selecting them in the corresponding fields at the bottom right of the gadget. The following chart types are currently available:

- donut chart
- pie chart
- gauge chart
- bar chart
- treemap chart

You can also change the statistic value in your quick chart. The values available depend on your configuration.

**Show values** tooggle is available in the **Three-dot menu** (▢) in the footer of quick charts. When enabled, numeric values appear directly on the chart when space allows.

Supported chart types:

- Percentage bar
- Bar
- Line
- Clustered bar chart
- Stacked bar (shows both slice percentages and stack totals)
- Multi-line chart

![image-20260213-092302.png](/cms_trial/assets/61284b00-2046-4c77-8d0e-579fdb49640a.png)

The order of the slices or bars in the *quick charts* is the same as in the table.

The *maximum rows*setting applies to the *quick charts* as well.

### Examples of *quick charts*:

Donut chart of Issue Count by Project:

![Donut chart of Issue Count by Project.png](/cms_trial/assets/b695a121-4941-42af-9a80-cc0b0bd639c6.png)

Pie chart of Story Points by Priority:

![Pie chart of Story Points by Priority.png](/cms_trial/assets/021ae5fe-fbc5-4386-b93a-b60b9cff36a7.png)

Gauge chart of Time Spent by Status:

![Gauge chart of Time Spent by Status.png](/cms_trial/assets/fa5e962a-3fd5-4d2d-b3a8-91aa8a49e283.png)

Bar chart of Issue Count by Issue Type:

![Bar chart of Issue Count by Issue Type.png](/cms_trial/assets/fd9bbd5c-8639-41cd-9469-88e71544ac1d.png)

Treemap chart of Story Points by Status:

![Treemap chart of Story Points by Status.png](/cms_trial/assets/4bd5f9f8-6316-4cc7-97de-eabcd614e8ba.png)