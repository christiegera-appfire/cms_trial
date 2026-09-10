# The Rich Filter Simple Gauges Gadget

## About the Rich Filter Simple Gauges gadget

The *Rich Filter, Simple Gauges* gadget, displays proportions from issue counts, numeric and time-tracking issue fields, [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), and [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/). The gadget is based on a rich filter and provides, among others, the following features:

- the collection of issues used for the calculations can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- the proportions can be displayed in one of three ways: as a gauge, as a percentage and fraction, or as a percentage only (for simplicity, called gauges, regardless of the way they are displayed);
- for the same collection of issues, the gadget can display multiple gauges at the same time;
- each gauge can be configured in one of two ways:

  - with a *filter & value* pair – the *filter* can be a predefined filter or any [static filter](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/); the *value* can be the number of issues (*Issue Count*), a numeric or time-tracking field (such as *Story Points* or *Original Estimate*), or a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/); the proportion is computed as the sum of the *values* of the issues that satisfy the filter divided by the sum of the *values* of all the issues in the collection used by the gadget;
  - with a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) – a dedicated configuration object for ratio definitions.
- The content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

![Smart Gaugesresolved issues.png](/cms_trial/assets/8973ac93-79ab-4b90-aa35-f762e7a9426b.png)

## Configuring the Rich Filter Simple Gauges gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Simple Gauges* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783942228](/cms_trial/assets/566d9798-e45e-47cc-8f88-be7c31c3e338.png)

Edit the gadget configuration as described in the following table:

| **Setting** | **Description** |
| --- | --- |
| **Rich filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. For more details, check the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page. |
| **Working Query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Gauge filters & values** | Configure the definition of each of the gauges to be displayed. You can configure up to 10 gauges in each gadget.  Each gauge can be configured using a filter and value pair or a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/).  Two dropdowns are used to configure the gauges:   1. The first dropdown contains:     - Three predefined filters: *Resolved Issues* (`resolution is not EMPTY`), *Unresolved Issues* (`resolution = Unresolved`), *Status category: Done* (`statusCategory = Done`)    - The [static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/) defined in the selected rich filter    - The [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) defined in the selected rich filter contentId-783942228 2. The second dropdown is displayed only if a filter (predefined or static) is selected in the first dropdown. The second dropdown contains four kinds of possible values:     - **Issue Count:** the gauge is based on the number of issues.    - **Numeric:** the gauge is based on a numeric field (e.g., *Story Points* or *Votes*).    - **Time Tracking:** the gauge is based on one of the time-tracking fields (i.e., *Original Estimate, Remaining Estimate, Time Spent*).    - **Custom values:**  the gauge is based on a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/). contentId-783942228   To sum up, to configure a gauge:   1. First, select a *filter* or a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/). If a *custom ratio* is selected, the gauge definition is complete and is added to the list. 2. If a *filter* was selected in step 1, select a *value* to complete the gauge definition – the gauge definition is added to the list. contentId-783942228 |
| **Layout** | Select one of the following display options:   - Gauge: Smart Gaugesresolved issues.png - Percentage & fraction: Percentage and fraction.png - Percentage only: Percentage only.png |
| **Decimals for percentage** | Select how you want to display decimals for percentages   - **None**: default setting (for example, `2%`, `26%`, `100%`) for clean, high-level overviews. - **Maximum 1**:(for example, `2.4%`, `25.6%`, `100%`) for precision tracking and nuanced KPIs. Values above 100% always display without decimals to save space. Decimals for percentag |