# The Rich Filter Time Series Chart Gadget

## About the Rich Filter Time Series Chart gadget

The *Rich Filter Time Series Chart* gadget displays one or several [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) as line charts. The gadget is based on a rich filter and provides, among others, the following features:

- the collection of issues used by the gadget can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the gadget can plot together many [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) as a multi-line chart, allowing users to make comparisons and identify trends and correlations between series;
- the gadget supports all types of *time series* (such as issue counts, numeric & time tracking values, computed durations, and SLA fields);
- the gadget can also display the values from charts in a tabular format;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

![Time Series Chart gadget.png](/cms_trial/assets/0e319979-3465-4c5a-bf87-f1567e84221d.png)

## Configuring the Rich Filter Time Series Chart gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Time Series Chart*gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed.

![contentId-783942364](/cms_trial/assets/f3f62e11-ef8e-4155-a06e-801281b8dfd8.png)

Edit the gadget configuration as described below:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. See the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) documentation page for details. |
| **Working query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Aggregation periods** | Select the periods on which the issues will be grouped. The available options are *Days*, *Weeks*, *Months*, *Quarters*, *Years*, and *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e., with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time range** | **Time range subsetting** | **Description** |
| **Number of days / weeks etc.** | **Number** | Enter the number of aggregation periods to be displayed. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values from the past. Therefore, you should always select Past for time series based on these fields, as you will never find any issues created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For a time series based on this field, it is more useful to select Future to see statistics for issues that are due soon or Past & Future to see statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* are the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These predefined *Time range* options depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Aggregation type** | Select one of the following aggregation type options:   - **Period value**: this is the default option – the chart displays the values of each individual aggregation period; - **Cumulative trend**: progressively adds the values from the previous periods, including only the issues starting with the first period of the chart; - **Cumulative total**: progressively adds the values from the previous periods, including the issues before the first period.  period_time series.pngCumulative time series-.pngCumulative total time series-.png |
| **Time Series** | Select the time series you wish to display. You can select up to 10 time series at a time. contentId-783942364contentId-783942364 The gadget can display only time series with the same value type together. Once the first time series has been selected, only time series with the same value type can be added. |

## **Quick tables in the Times Series gadget**

*Quick tables* enable users to display the values from charts in a tabular format easily. To toggle the quick table on or off, click the table icon in the gadget’s footer.

![Quick tables time series.png](/cms_trial/assets/4e3d1d78-f614-4de0-9c99-02dbd70d4ed3.png)![Quick tables time_series.png](/cms_trial/assets/3a32fbee-c9b8-4566-941f-3e994dad3477.png)

To display numeric values directly on the charts, enable the **Show values** toggle in the **Three-dot menu**. The numeric values appear directly on the chart when space allows.

![2026-02-13_13-30-53.png](/cms_trial/assets/3e148101-a770-4f66-a2e5-890c7edbd135.png)

**Export to PDF, Excel, and CSV**

Additionally, users can export the data displayed by the *Rich Filter Time Series Chart gadget* to PDF, Excel, or CSV formats. For further information, please refer to the [Exporting data](/cms_trial/space/RFCDOC/783942966/Export+data/) documentation page.