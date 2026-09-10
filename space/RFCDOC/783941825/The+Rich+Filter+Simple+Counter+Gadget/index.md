# The Rich Filter Simple Counter Gadget

## About the Rich Filter Simple Counter gadget

The *Rich Filter Simple Counter* gadget displays issue counts, field sums, and custom values for a collection of issues. The gadget is based on a rich filter and provides, among others, the following features:

- the collection of issues used for the counting can be further filtered using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL called *working query*;
- for the same collection of issues, the gadget can display multiple results at the same time – based on the number of issues (*Issue Count*), the sum of numeric and time-tracking fields (such as *Story Points* or *Original Estimate*), or on custom values;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

![custom value dashboard.png](/cms_trial/assets/63592193-ece4-4f1b-8fc1-7d117450f957.png)

## Configure the Rich Filter Simple Counter gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Simple Counter* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783941825](/cms_trial/assets/dc01813c-92b6-4aff-a559-09c4ec704cd8.png)

Edit the gadget configuration as described in the following table:

| **Setting** | **Description** |
| --- | --- |
| **Rich Filter** | Select the rich filter the gadget will use.  Click the *Rich Filter* button to display the list of rich filters; you can either scroll through or use the search box to find the desired filter.  The gadgets’ configuration forms only show the rich filters you can view. Check the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) page for more details. |
| **Working Query** | The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to filter further the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues used by the gadget. |
| **Values** | Select the values to be displayed. You can select up to 10 values at a time.  There are four kinds of possible values:   - **Issue Count:** displays the number of issues. - **Time Tracking:**displays the sum of one of the time-tracking fields (i.e., *Original Estimate, Remaining Estimate, Time Spent*) for the collection of issues. - **Numeric:**displays the sum of a numeric field for collecting issues. For instance, using Jira Software, the gadget can show the sum of *Story Points* for collecting issues. - **Custom values:** displays a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), as configured in the rich filter (aggregation formula, display options, etc.).  contentId-783941825 |