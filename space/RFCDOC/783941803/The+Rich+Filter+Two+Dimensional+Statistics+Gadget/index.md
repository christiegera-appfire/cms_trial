# The Rich Filter Two Dimensional Statistics Gadget

## About the Rich Filter Two Dimensional Statistics gadget

The *Rich Filter Two-Dimensional Statistics* gadget is a two-dimensional version of the [Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/). It allows grouping issues on two criteria, and computes statistics for combinations of statistic types. It resembles Jira’s built-in *Two Dimensional Filter Statistics* gadget, but it is based on a rich filter instead of a Jira saved search and thus adds several new features:

- the collection of issues used for the statistics can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the gadget can group the issues by an issue field or by a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/);
- the gadget can group the issues by the values of a date or date time field to compute daily, weekly, monthly, quarterly or yearly statistics;
- the result type displayed by the gadget can be customized (for instance, to show the sum of *Story Points* instead of the *Issue Count*);
- the gadget can display [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/);
- the gadget can display [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/);
- the user can change the sorting order by clicking on an icon next to the column or row name;
- the gadget can also display the data as a chart; the user can switch between the table view and the chart view by clicking on an icon;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

**Example**: Story Points aggregated by the issue field Priority and a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) named High-Level Status:

![Story Points aggregated by field Priority.png](/cms_trial/assets/19de6849-177f-4ad9-affd-072f4c364470.png)

The labels and the colors displayed for High Level Status come from the clauses defined in the [configuration](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) of this smart filter.

## **2. Configuring the Rich Filter Two Dimensional Statistics gadget**

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Two Dimensional Statistics*gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![configuration form.png](/cms_trial/assets/6046eb61-bc99-4af2-bf84-9101b35effb5.png)

When using Rich Filters across multiple projects with different types (e.g., Jira Software, Jira Product Discovery, JWM), you can encounter duplicate field names for the **Statistics type**, such as multiple *Customer* fields, in dropdown menus.

To help you distinguish between fields with the same name, Rich Filters shows additional information in tooltips when you hold the pointer over any field in dropdown menus:

- Field type appears in brackets (for example, *Customer* [text])
- Custom field ID is added when duplicates still exist (for example, *Customer [text] cf[12345]*)

Edit the gadget configuration as described below:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click on the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the filter you need.  The gadgets’ configuration forms only show the rich filters you can view. See the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) documentation page for details. |
| **Working query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Two breakdowns, one horizontal and one vertical, need to be configured. Below, we describe the breakdown settings only once.** |
| **Statistic type** | Select the issue field or the [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) on which the issues will be grouped. The drop-down list includes the smart filters defined in the selected rich filter: High-level Status.png For each of the two breakdowns (horizontal and vertical), there are several types of configuration, depending on the selected *Statistic type*:  a. Statistics on option fields (e.g., Priority, Status, select custom fields, etc.) or smart filters  b. Statistics on date or date time fields  c. Statistics on time series  These options are further detailed in the sections below. |

### 2.a. Statistics on option fields or smart filters

The following settings are applicable when the selected *Statistic type* is an option field (e.g., Priority, Status, select custom fields, etc.) or a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/):

| **Setting** | **Description** |
| --- | --- |
| **Sort by** | Select how to sort the values of your *Statistic type*:   - **Total:** this will sort by the result computed for each *Statistic type* group for the corresponding breakdown. - **Alphabetical:** this will use alphabetical order for the *Statistic type* groups. - **Natural:** this will use the native sorting order of the issue field or smart filter selected as Statistic type, i.e., the order that has been configured for the options of the field or smart filter. This sorting option is available only for the issue fields Priority, Status, and Issue Type and for smart filters. |
| **Reverse sort order** | If checked, the sort order is reversed. |
| **Maximum rows/cols** | These settings limit the number of rows and columns to display.  The user can still display all the computed rows/columns by clicking on the numbers of rows/columns in rounded rectangles located at the bottom right of the gadget. |
| **Show percentage bars** | If checked, the gadget displays a bar chart for each statistic value:   - for all value types other than [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion of each value relative to the total; - for [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), the proportion corresponding to the ratio. |
| **Show totals** | If checked, the gadget displays the total values for the corresponding breakdown. |
| **Value** | Select the value to be computed for each *Statistic type* group. The following value types are available:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e. *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, if using Jira Software, the gadget can show how many *Story Points* there are for each*Statistic type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios**: displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) configured in the rich filter (percentage or ratio).  contentId-783941803 |

### Statistics on date fields

The following settings are applicable when the selected *Statistic type* is a date or a date time field:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to the their values for the date or date time field selected as *Statistic type*.  The available options are: *Days*, *Weeks*, *Months*, *Quarters*, *Years*, *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e. with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time range** | **Time range subsetting** | **Description** |
| **Number of periods** | **Number of days / weeks etc.** | Enter a number of periods. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values that are in the past. Therefore you should always select *Past* for these fields as you will never find any issue created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For this field it is more useful to select *Future* in order to see statistics for the issues that are due soon, or *Past & Future* to also see the statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* is the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options which depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Reverse sort order** | If checked, the default chronological order is reversed. |
| **Show totals** | If checked, the gadget displays the total values for the corresponding breakdown. |
| **Value** | Select the value to be computed for each *Statistic type* group. The following value types are available:   - **Issue Count:** computes the number of issues in each group. - **Time Tracking:**computes the sum of one of the time-tracking fields (i.e. *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**computes the sum of a numeric field for the issues in each group. For instance, if using Jira Software, the gadget can show how many *Story Points* there are for each*Statistic type* group. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) as configured in the rich filter (aggregation formula, display options, etc.). - **Custom ratios**: displays a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) as configured in the rich filter (percentage or ratio).  contentId-783941803 |

### **2.c. Statistics on time series**

The gadget can also be configured to display [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/). In order to do so, you need to select a *time series* in the *Statistic type* setting. The selection can be done either on the horizontal breakdown or on the vertical one. The following image provides an example where the time series is selected on the horizontal breakdown:

![image-20250728-130857.png](/cms_trial/assets/fe6ad63d-00a5-4f4f-89bc-6b8815846a8d.png)

The following settings are applicable when the selected *Statistic type* is a time series:

| **Setting** | **Description** |
| --- | --- |
| **Aggregation periods** | Select the periods on which the issues will be grouped, according to the date or date time field on which the selected time series is based.  The available options are: *Days*, *Weeks*, *Months*, *Quarters*, *Years*, *Auto*.  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e. with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time range** | **Time range subsetting** | **Description** |
| **Number of periods** | **Number of days / weeks etc.** | Enter a number of periods. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Direction** | Select how the periods are positioned relative to the current period. The possible options are:   - **Past** – the time range includes past periods and the current period - **Future** – the time range includes the current period and future periods - **Past & Future** – the time range includes past periods, the current period, and future periods, with the current period in the middle of the range   Fields like *Created* or *Resolved* always contain values that are in the past. Therefore you should always select *Past* for time series based on these fields as you will never find any issue created or resolved in the future.  Fields like *Due Date* contain values that can be both in the past and in the future. For time series based on this field it is more useful to select *Future* in order to see statistics for the issues that are due soon, or *Past & Future* to also see the statistics for overdue issues. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date occurring in the values of the issues).  *All dates* is the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options which depend on the selected *Aggregation period*.  Possible options are: This year, Last year, This quarter, Last quarter, This month, Last month. |
| **Reverse sort order** | If checked, the default chronological order is reversed. |
| **Show totals** | If checked, the gadget displays the total values for the corresponding breakdown. |
| **Value** | The gadget automatically fills-in the *Value* field with the base value of the selected time series. contentId-783941803 |

## **3. Quick charts in the Rich Filter Two Dimensional Statistics gadget**

In addition to the main table view, the *Rich Filter Two Dimensional Statistics* gadget offers a chart view which displays the results as a chart. This chart, referred to as a *quick chart*, requires no additional configuration. You can switch between the table view and the chart view by clicking on the corresponding icon located at the bottom right of the gadget.

By default, a clustered bar chart is displayed. You can choose the chart type of the *quick chart* by selecting it in the corresponding field at the bottom of the gadget. You can also swap the primary and secondary breakdowns of the chart  by clicking on the <> icon located between the breakdowns, at the bottom of the gadget.

The following chart types are currently available:

- Clustered bar chart
- Stacked bar chart
- Multi-line chart

To display numeric values directly on the charts, enable the **Show values** toggle in the **Three-dot menu** (▢) in the footer of quick charts. When enabled, numeric values appear directly on the chart when space allows.

Supported chart types:

- Percentage bar
- Bar
- Line
- Clustered bar chart
- Stacked bar (shows both slice percentages and stack totals)
- Multi-line chart

  ![2026-02-13_13-27-26.png](/cms_trial/assets/7f5458b9-4924-44d5-ac50-76c29a75b880.png)

The *maximum rows/cols* setting applies to the *quick charts* as well.

### Examples of *2D quick charts*:

- Clustered bar chart of Issue Count by Project:

![bar chart of Issue Count by Project.png](/cms_trial/assets/12ec1967-0b42-4835-b825-7fb78eee3b09.png)

- Stacked bar chart of Time Spent by Issue Type and Priority:

![contentId-783941803](/cms_trial/assets/40f2337e-ca6b-45b8-bff3-4a162492e367.png)

- Multi-line chart of Story Points by Priority and Assignee:

![Story Points by Priority and Assignee.png](/cms_trial/assets/d352c725-aaf7-41a2-ba1d-fb584af8e1dd.png)