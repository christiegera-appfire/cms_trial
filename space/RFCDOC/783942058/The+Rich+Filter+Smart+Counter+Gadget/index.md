# The Rich Filter Smart Counter Gadget

## About the Rich Filter Smart Counter gadget

The *Rich Filter Smart Counter* gadget displays aggregated issue data in a counter-type layout. The gadget is based on a rich filter and provides, among others, the following features:

- the collection of issues used for the aggregation can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- smart filters can do the aggregation;
- the results can be based on Issue Count, numeric and time-tracking fields, or [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/);
- the results are displayed as counts, labeled and colored according to the [smart filter configuration](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/);
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

![Rich Filter Smart Counter gadget display.png](/cms_trial/assets/67057197-102d-4245-8324-f003a7c1fe53.png)

## Configuring the Rich Filter Smart Counter gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Smart Counter* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783942058](/cms_trial/assets/6bfcbf88-5f62-4be3-b9db-0074b11b5713.png)

Edit the gadget configuration as described in the following table:

| **Setting** | **Description** |
| --- | --- |
| **Rich Filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. For more details, see the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page. |
| **Working Query** | The working query is an additional JQL query, which is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Smart Filter** | Select the smart filter on which the issues will be grouped. The drop-down list shows the smart filters defined in the selected rich filter. |
| **Show none** | If checked, the gadget displays the result corresponding to the issues that don't match any of the clauses of the selected smart filter. |
| **Value** | Select the value to be computed for each smart filter clause. There are four kinds of possible values:   - **Issue Count:** displays the number of issues in each group. - **Time Tracking:**displays the sum of one of the time-tracking fields (i.e., *Original Estimate, Remaining Estimate, Time Spent*) for the issues in each group. - **Numeric:**displays the sum of a numeric field for the issues in each group. For instance, using Jira Software, the gadget can show each group*’s* sum of *Story Points*. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), as configured in the rich filter (aggregation formula, display options, etc.).  contentId-783942058 |