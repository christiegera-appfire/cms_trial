# The Rich Filter Created vs Resolved Chart Gadget

## About the Rich Filter Created vs. Resolved Chart gadget

The *Rich Filter Created vs. Resolved Chart* gadget displays the number of issues created versus the number of resolved over a given period. It resembles Jira’s built-in *Created vs. Resolved Chart* gadget, but it is based on a rich filter instead of a Jira saved search and thus adds several new features:

- the collection of issues used by the gadget can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the values used by the gadget can be customized (for instance, to show the sum of *Story Points* instead of the *Issue Count*);
- an advanced configuration mode allows customizing the s*tart* and *finish* dates instead of the default *Created* and *Resolved* dates;
- the gadget can also display the values from charts in a tabular format;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

![Rich Filter Created vs. Resolved Chart gadget .png](/cms_trial/assets/8ff897d6-6a36-4900-9066-3cdadf1e7439.png)

## Configuring the Rich Filter Created vs. Resolved Chart gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Created vs. Resolved Chart* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed.

![contentId-783942386](/cms_trial/assets/f4134c99-93c6-43ae-93aa-e41b54167aaa.png)

### Configuring a simple Created vs Resolved chart

Edit the gadget configuration as described below:

Select one of the following aggregation-type options:

- **Period value**: this is the default option – the chart displays the values of each individual aggregation period;
- **Cumulative trend**: progressively adds the values from the previous periods, including only the issues starting with the first period of the chart;
- **Cumulative total**: progressively adds the values from the previous periods, including the issues before the first period.

![Period value Created vs. Resolved Chart gadget .png](/cms_trial/assets/1168bbc7-3575-4a77-945a-97bc375c9d26.png)![Cumulative trend Created vs. Resolved Chart gadget .png](/cms_trial/assets/22c3986f-895b-4ca7-b1ed-8931ac957dc8.png)![Cumulative total Created vs. Resolved Chart gadget .png](/cms_trial/assets/d35fc8fe-f237-4a29-8547-662066eb7aae.png)

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter. The gadgets’ configuration forms only show the rich filters you can view. For more details, see the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page. |
| **Working query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Configuration mode** | The available options are:   - **Created vs. Resolved** (default mode): The chart is based on the Created and Resolved date fields, displaying the created vs. resolved issues. This sub-chapter covers this option only. - **Custom Start vs. Finish** (advanced mode): You can customize the start and finish dates. See the next sub-chapter for more details about this configuration mode. |
| **Aggregation periods** | Select the periods on which the issues will be grouped. The available options are *Days, Weeks, Months, Quarters, Years, and Auto.*  If the *Auto* option is selected, the *aggregation periods* and *time range* are adjusted dynamically to produce the most granular yet complete statistics (i.e., with the appropriate aggregation period so that all the relevant issues are included). |
| **Time range** | Together with its subsettings, this specifies the total time span for which the statistics should be computed.  The time range subsettings depend on the option selected in the *Time range* drop-down as described below. |
| **Time range** | **Time range subsetting** | **Description** |
| **Number of days / weeks etc.** | **Number** | Enter the number of aggregation periods to be displayed. The time range corresponds to the specified number of consecutive aggregation periods. |
| **Between dates** | **From / To** | Enter the two dates that define the limits of the time range (both specified dates are inclusive).  The inputs can be selected from a date picker or entered manually as a calendar date ("`yyyy/MM/dd`" or "`yyyy-MM-dd`"). |
| **All dates** | If selected, the time range is determined dynamically to include all the relevant issues (from the first date to the last date in the issues' values).  *All dates* are the only possible *Time range* option if the selected *Aggregation period* is *Auto*. |
| **Contextual options** | These are predefined *Time range* options that depend on the selected *Aggregation period*.  Possible options are,*This year, Last year, This quarter, Last quarter, This month, Last month*. |
| **Aggregation type** | It can be:   - **Period value** – shows the number of issues created and resolved during each individual period. - **Cumulative trend** – starts from zero and progressively adds values to each period from the previous periods. It includes only the issues created or resolved after the first period represented on the graph. - **Cumulative total** – starts with the number of issues created or resolved before the first period and progressively adds values from the previous periods to each period. It includes all the issues returned by the filter, independently of their created or resolved dates. |
| **Value** | Select the value to be computed for each aggregation period. There are two kinds of possible values:   - **Issue Count:** computes the number of issues created/resolved in each aggregation period. - **Numeric:**computes the sum of a numeric field for the issues in each aggregation period. For instance, when using Jira Software, the gadget can show the number of Story Points for the issues created/resolved in each aggregation period.  contentId-783942386contentId-783942386 |
| **Unresolved trend** | If checked, the graph will also include a sub-plot with the trend of unresolved issues over time.  The unresolved trend is always cumulative—when the selected Aggregation type is Period value, the Unresolved trend is computed as a cumulative trend. |

### Advanced – customize the Start and Finish dates

If the selected **Configuration mode** is **Custom Start vs. Finish** (advanced), you can customize the start and finish dates on which the gadget is based. The other settings apply as already explained in the previous sub-chapter.

The configuration form of the gadget in advanced mode:

![contentId-783942386](/cms_trial/assets/8d4d02ab-3c54-4de6-be3d-9ef02b361466.png)

Additional settings for the advanced mode:

| **Setting** | **Description** |
| --- | --- |
| **Start date** and **Finish date**  Applies only if the configuration mode is *Custom Start vs. Finish* | Select the custom start and finish dates on which the chart is based. You can select any date fields for start and finish. contentId-783942386 |

Example of the chart showing the Story Points of the issues started vs. resolved:

![showing the Story Points of the issues started vs. resolved.png](/cms_trial/assets/79dc1a66-3a7a-4544-9eb6-4309f88c807c.png)

## **Quick tables in the Created vs. Resolved Chart gadget**

*Quick tables* enable users to display the values from charts in a tabular format easily. To toggle the quick table on or off, simply click the table icon in the gadget's footer.

![Quick tables.png](/cms_trial/assets/a93d97c8-c201-4ddd-81a4-f58af6cac0e9.png)![Quick table.png](/cms_trial/assets/4faf2a73-5d87-45ed-804c-1e6435b417ba.png)

To display numeric values directly on the charts, enable the **Show values** toggle in the **Three-dot menu**. The numeric values appear directly on the chart when space allows.

![2026-02-13_13-43-24.png](/cms_trial/assets/bf356813-dd38-4812-8d78-f877901df12f.png)

### Export to PDF, Excel, and CSV

Additionally, users can export the data displayed by the *Rich Filter Created vs Resolved gadget* to PDF, Excel, or CSV formats. For further information, please refer to the [Exporting data](/cms_trial/space/RFCDOC/783942966/Export+data/) documentation page.