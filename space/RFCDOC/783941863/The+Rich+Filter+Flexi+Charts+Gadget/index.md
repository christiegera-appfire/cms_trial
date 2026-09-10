# The Rich Filter Flexi Charts Gadget

## About the Rich Filter Flexi Charts gadget

The *Rich Filter Flexi Charts* gadget displays a chart with data computed from a collection of issues. This gadget is highly customizable, providing multiple options for the type of chart and the way the data is computed and displayed. It is also based on a rich filter instead of a Jira saved filter, thus providing the following features:

- the collection of issues used by the gadget can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the result type displayed by the chart can be *Issue Count*, a numeric or time-tracking field, or a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/);
- each chart type has either one or two breakdowns (the charts are referred to as *1D charts* and *2D charts* respectively) and each breakdown is based on an issue field or a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/). The primary breakdown can also be based on a date or date time field;
- the gadget can display [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) and [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/);
- the gadget can display average age reports;
- the gadget can also display the values from charts in a tabular format;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

Example 1: *Donut chart* of Issue Count by Project:

![ Donut chart of Issue Count by Project.png](/cms_trial/assets/125b9937-c17a-4431-acbc-1f8e70032dd5.png)

Example 2: *Clustered bar chart* of Story Points by Status and a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) named Team:

![Clustered bar chart of Story Points by Status and Team.png](/cms_trial/assets/57a4fea2-0514-4965-86a4-60a3b955ae65.png)

## Configuring the Rich Filter Flexi Charts gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Flexi Charts*gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed.

- For 1D charts – donut, pie, gauge, bar, line, treemap, word cloud:

![contentId-783941863](/cms_trial/assets/ec11f413-d025-4c50-8ea3-ace1acb6c013.png)

- For 2D charts – clustered bar, stacked bar, multi-line:

![contentId-783941863](/cms_trial/assets/9e8d8091-6699-4ae2-b320-eb995be8f000.png)

When using Rich Filters across multiple projects with different types (for example, Jira Software, Jira Product Discovery, JWM), you can encounter duplicate field names for the **Statistics type**, such as multiple *Customer* fields, in dropdown menus.

To help you distinguish between fields with the same name, Rich Filters shows additional information in tooltips when you hold the pointer over any field in dropdown menus:

- Field type appears in brackets (for example, *Customer* [text])
- Custom field ID is added when duplicates still exist (for example, *Customer [text] cf[12345]*)

Edit the gadget configuration as described below:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click on the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the filter you need.  The gadgets’ configuration forms only show the rich filters you are allowed to view. For more details, see the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page. |
| **Working Query** | The working query is an additional JQL query which is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Chart type** | Select one of the available chart types:   - 1D charts:    - Donut chart   - Pie chart   - Gauge chart   - Sliced bar chart   - Treemap chart   - Percentage bar   - Bar chart   - Line chart   - Word cloud chart - 2D charts:    - Clustered bar chart   - Stacked bar chart   - Multi-line chart |
| **For** ***2D charts*****, two breakdowns need to be configured, one primary and one secondary. Below we describe the breakdown settings only once.** |
| **Statistic type** | Select the criteria on which the issues will be grouped. In addition to issue fields, the drop-down list includes the smart filters and the time series defined in the selected rich filter, as well as options for special reports: contentId-783941863 For the breakdown of 1D charts and for the primary breakdown of 2D charts, there are several types of configuration, depending on the selected *Statistic type*:  a. Statistics on option fields (e.g. Priority, Status, select custom fields, etc.) or smart filters  b. Statistics on date or date time fields  c. Statistics on time series  d. Special statistics  The secondary breakdown of 2D charts can only be based on options fields or smart filters.  These options are further detailed in the sections below. |

### Statistics on option fields or smart filters

The following settings are applicable when the selected *Statistic type* is an option field (e.g. Priority, Status, select custom fields, etc.) or a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/):

| **Setting** | **Description** |
| --- | --- |
| **Sort by** | Select the order in which the values are displayed in the chart. The following options are available:   - **Total:** this will sort by the value computed for each *Statistic type* group. - **Alphabetical:** this will use alphabetical order for the *Statistic type* groups. - **Natural:** this will use the native sorting order of the issue field or smart filter selected as Statistic type, i.e. the order that has been configured for the options of the field or smart filter. This sorting option is available only for the issue fields Priority, Status, and Issue Type and for smart filters. |
| **Reverse sort order** | If checked, the sort order is reversed. |
| **Maximum slices / bars etc.** | These settings limit the number of slices / bars etc. to display. In the case of slices, the ones which are not individually displayed due to this limit are represented by one slice called Other.  The user can still display all the computed slices / bars etc. by clicking on the numbers in rounded rectangles located at the bottom right of the gadget. |
| **Value** | Select the value to be computed for each *Statistic type* group. There are four kinds of possible values:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e. *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, when using Jira Software, the gadget can show how many *Story Points* there are for each *Statistic type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) as configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios:** displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) as configured in the rich filter (percentage or ratio).  contentId-783941863 |

### Statistics on date fields

The following settings are applicable when the selected *Statistic type* is a date or a date time field:

![contentId-783941863](/cms_trial/assets/17f50fa4-48df-4f49-8976-56908e53b477.png)

Please note that date fields can be used as breakdown only in *Bar*, *Clustered*/*Stacked bar*, and *Line*/*Multi-line* charts. The other chart types are not compatible with date field configurations.

The following settings are applicable when the selected *Statistic type* is a date or a date time field:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to the their values for the date or date time field selected as *Statistic type*.  The available options are: *Days*, *Weeks*, *Months*, *Quarters*, *Years*, *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e. with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time Range** | **Time range subsetting** | **Description** |
| **Number of days / weeks etc.** | **Number** | Enter the number of aggregation periods to be displayed. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values that are in the past. Therefore you should always select *Past* for these fields as you will never find any issue created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For this field it is more useful to select *Future* in order to see statistics for the issues that are due soon, or *Past & Future* to also see the statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* is the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options which depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Aggregation type** | Select one of the following aggregation type options:   - **Period value**: this is the default option – the chart displays the values of each individual aggregation period; - **Cumulative trend**: progressively adds the values from the previous periods, including only the issues starting with the first period of the chart; - **Cumulative total**: progressively adds the values from the previous periods, also including the issues before the first period.  Period value.pngCumulative trend.pngCumulative total-.png |
| **Value** | Select the value to be computed for each *Statistic type* group. There are four kinds of possible values:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e. *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, when using Jira Software, the gadget can show how many *Story Points* there are for each *Statistic type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) as configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios:** displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) as configured in the rich filter (percentage or ratio).  contentId-783941863 |

### Statistics on time series

The gadget can also be configured to display [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/). In order to do so, you need to select a *time series* in the *Statistic type* setting in the primary breakdown. The following image provides an example:

![contentId-783941863](/cms_trial/assets/bd54bfb4-b992-4fb2-af7a-9305e3bde22d.png)

Please note that time series can be used as breakdown only in *Bar*, *Clustered*/*Stacked bar*, and *Line*/*Multi-line* charts. The other chart types are not compatible with time series configurations.

The following settings are applicable when the selected *Statistic type* is a time series:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to the date or date time field on which the selected time series is based.  The available options are: *Days*, *Weeks*, *Months*, *Quarters*, *Years*, *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e. with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time range** | **Time range subsetting** | **Description** |
| **Number of days / weeks etc.** | **Number** | Enter the number of aggregation periods to be displayed. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values that are in the past. Therefore you should always select *Past* for time series based on these fields as you will never find any issue created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For time series based on this field it is more useful to select *Future* in order to see statistics for the issues that are due soon, or *Past & Future* to also see the statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* is the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options which depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Aggregation type** | Select one of the following aggregation type options:   - **Period value**: this is the default option – the chart displays the values of each individual aggregation period; - **Cumulative trend**: progressively adds the values from the previous periods, including only the issues starting with the first period of the chart; - **Cumulative total**: progressively adds the values from the previous periods, also including the issues before the first period. |
| **Value** | The gadget automatically fills-in the *Value* field with the base value of the selected time series. contentId-783941863 |

### **Special statistics**

The gadget can also be configured to display *average age* reports, which show how long issues have been unresolved on average, during each aggregation period in a time range.

![average age reports,.png](/cms_trial/assets/fe8d0468-18f6-44b8-95bf-43f3ba6a0436.png)

### How is the average age chart computed?

The way the average age algorithm works is that, for each aggregation period **(1)** it identifies all issues that are relevant for that aggregation period, **(2)** computes and sums their ages and then **(3)** divides the sum of ages by the number of relevant issues in that aggregation period.

**(1)** An issue is relevant for an aggregation period if the following two conditions are both met at the same time:

- the issue was created before or during the aggregation period (i.e. created before the end of the aggregation period)
- the issue has not been resolved before the start of the aggregation period (i.e. it has been resolved during or after the aggregation period, or it is still unresolved)

**(2)** During each aggregation period, the age of a relevant issue is calculated as:

- for issues resolved during the aggregation period: resolution date minus created date
- for issues resolved after the end of the aggregation period or for issues which are still unresolved: the end of the period minus the creation date.   
  **Note:** If an aggregation period starts in the past and ends in the future, then *Now* is used to calculate the age of an issue instead of the end of the period.

**(3)** The average age for an aggregation period is computed as the ratio between the sum of issue ages and the number of issues which are relevant for that aggregation period. The average age values are displayed in days with two decimals.

In order to display the issues average age in the *Flexi Chart gadget*, select the *Average age* option in the *Statistic type* setting in the primary breakdown. The following image provides an example:

![image-20240516-101808.png](/cms_trial/assets/28bbc92e-2d9c-4faf-8272-747921043e36.png)

Please note that the average age can only be displayed in *Bar*/*Clustered bar* and *Line*/*Multi-line* charts. The other chart types are not compatible with average age reporting.

The following settings are applicable when the selected *Statistic type* is the *Average age*:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped. The available options are: *Days*, *Weeks*, *Months*, *Quarters*, *Years*, *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e. with the appropriate aggregation period so that all the relevant issues are included). |
| **Time Range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time Range** | **Time range subsetting** | **Description** |
| **Number of days / weeks etc.** | **Number** | Enter the number of aggregation periods to be displayed. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* is the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options which depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Value** | The gadget automatically fills-in the *Value* field with the *Average issue age* value*.* image-20240516-100955.png |

## Examples of Flexi Charts

- Donut chart of Issue Count by Project:

![ Donut chart of Issue Count by Project.png](/cms_trial/assets/125b9937-c17a-4431-acbc-1f8e70032dd5.png)

- Pie chart of Story Points by Priority:

![flexichart of Story Points by Priority.png](/cms_trial/assets/6965cbbe-b8c1-4a2b-88be-7584955a06ec.png)

- Gauge chart of Time Spent by Status:

![Gauge chart of Time Spent by Statu.png](/cms_trial/assets/52003d35-49aa-4ee0-a198-bba25a802b43.png)

- Bar chart of Issue Count by Issue Type:

![flexi chart of Issue Count by Issue Type.png](/cms_trial/assets/dc4f440b-c68a-47ab-9a01-0195dabe2eda.png)

- Bar chart of Average age by weeks:

![Bar chart of Average age by weeks.png](/cms_trial/assets/641db639-5b70-4af1-bca3-b8b44dca27b9.png)

- Line chart of Issue Count by Created date:

![Line chart of Issue Count by Created date.png](/cms_trial/assets/ca6f99af-2daa-415b-8935-bf379711e94a.png)

- Treemap chart of Story Points by Status:

![Treemap chart  Story Points by Status.png](/cms_trial/assets/7d31a802-c663-4595-a4c5-1ebdec2b40f8.png)

- Percentage bar chart of Business value by Issue type:

  ![Percentage bar chart of Business value by Issue type.png](/cms_trial/assets/f147228d-f415-475e-bf44-450e40ab87b1.png)
- Word cloud chart of Issue Count by Organizations:

![Word cloud chart of Issue Count by Organizations.png](/cms_trial/assets/55a59a85-681e-4db8-8c89-169cdd2dc83f.png)

- Clustered bar chart of Story Points by Status and by a smart filter named Team:

![Clustered bar chart of Story Points by Status plus Team.png](/cms_trial/assets/54196df9-b32a-4fd7-8247-d2f666f3c11c.png)

- Stacked bar chart of Time Spent by Issue Type and Priority:

![Stacked bar chart of Time Spent by Issue Type and Priority](/cms_trial/assets/360f0bc5-94ca-4d65-ac8b-f8fb3c0bb447.png)

- Multi-line chart of Issue Count by Created and Team:

![Multi-line chart of Issue Count by Created and Team.png](/cms_trial/assets/676f9199-29e2-484e-8839-e4b1b8014894.png)

## Value display on charts

To display numeric values directly on the charts, enable **Show values** toggle in the **Three-dot menu** (▢). The numeric values appear directly on the chart when space allows.

Supported chart types:

- Percentage bar
- Bar
- Line
- Clustered bar chart
- Stacked bar (shows both slice percentages and stack totals)
- Multi-line chart

  ![2026-02-13_13-24-15.png](/cms_trial/assets/a6817bde-09d0-400e-a4ff-15d0d55a6e5f.png)

## Quick tables in the Flexi Charts gadget

*Quick tables* enable users to easily display the values from charts in a tabular format. To toggle the quick table on or off, simply click on the table icon located in the footer of the gadget.

![easily display the values from charts in a tabular format.png](/cms_trial/assets/a20f2d01-5ac8-4644-bb88-cbffe4abac9f.png)