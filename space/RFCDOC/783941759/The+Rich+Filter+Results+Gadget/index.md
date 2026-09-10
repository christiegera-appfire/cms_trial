# The Rich Filter Results Gadget

## About the Rich Filter Results gadget

The *Rich Filter Results* gadget displays one or multiple lists of issues. It resembles Jira’s built-in *Filter Results* gadget, but it is based on a rich filter instead of a Jira saved search and thus adds several new features:

- the content displayed can be further filtered by using *Rich Filter Controller* gadgets;
- the gadget itself can further refine the results by applying a gadget-specific JQL query called a *working query*;
- the gadget can display multiple [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) defined in the rich filter (which can include computed columns and color coding);
- the gadget can display all the issues (the default behavior) or one or multiple [queues](/cms_trial/space/RFCDOC/783942406/Configure+queues/); queues are custom lists of issues configured in the rich filter;
- the gadget allows the users to edit the issues directly from the dashboard using the issue dialog;
- the gadget gives easy access to Jira's bulk operations on the displayed issues;
- end-users can customize the layout of each view;
- the content of the gadget can be [exported](/cms_trial/space/RFCDOC/783942966/Export+data/) to PDF, Excel (.xlsx), and CSV formats.

**Example 1**: gadget configured to display the issues using three [views](/cms_trial/space/RFCDOC/783941729/Configure+views/):

![Results view dashboard](/cms_trial/assets/60741b99-814f-48d7-9fe5-d90d2124a6c1.png)

**Example 2**: gadget configured to display three support [queues](/cms_trial/space/RFCDOC/783942406/Configure+queues/):

![queues dashboard](/cms_trial/assets/f05cad53-7770-4448-981d-9a25ef5b1c95.png)

**Example 3**: the selected view displays a Gantt chart:

![2026-04-09_15-34-48.png](/cms_trial/assets/9414177e-140d-4c24-aa6c-2c74c8ec1654.png)

## Configure the Rich Filter Results gadget

[Add](https://support.atlassian.com/jira-core-cloud/docs/add-and-customize-a-gadget/) a new or edit an existing *Rich Filter Results* gadget in your [Jira dashboard](https://support.atlassian.com/jira-core-cloud/docs/what-is-a-jira-dashboard/). The configuration form of the gadget will be displayed:

![contentId-783941759](/cms_trial/assets/8950adcc-dfac-4f7e-9165-10442c264435.png)

### **Rich Filter**

1. Select the rich filter on which the gadget will be based.
2. Click the *Rich Filter* selector to display the list of rich filters.  
   You can either scroll through or use the search box to find the filter you need.

The gadgets’ configuration forms only show the rich filters you can view. For details, see the [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) documentation page.

### **Working Query**

The working query is an additional JQL query that is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. The working query is optional: if left empty, only the base Jira filter and the quick filters affect the issues displayed by the gadget.

The working query can also contain an `ORDER BY` clause. If such a clause is present, it precedes the order defined by the base Jira filter. You can even have a working query that contains only the `ORDER BY` clause if you want to change only the default order of the displayed issues.

Note that the gadget can also display queues of issues (see below). In such a case, the order defined in queues takes precedence over all other orders by clauses.

### **Display**

There are two display options possible:

- **All issues**: The gadget displays the list of issues returned by the rich filter and any additional filtering at the dashboard level. With the "Views" setting (see below), you can then select the views that are used to display the issues.
- **Queues**:The gadget will display the [queues](/cms_trial/space/RFCDOC/783942406/Configure+queues/) selected in the **Queues** setting (see below). Each queue will use the views configured in the rich filter.

### **Views**

The **View** option is available when you select **All issues** for the **Display**.

You can select the views (among the views defined in the Rich Filter) displayed by the gadget. By default, all views are displayed (the option **Show all views** is selected).

Select the **Customize views** option to display only selected views. You can add, remove, or reorder the views to be displayed.

![2026-06-24_08-48-40.png](/cms_trial/assets/9d012a49-7420-49ad-a2a4-e5bef4bb99e9.png)

### **Queues**

The **Queues** option is available when you select **Queues** for the **Display**.

You can select to:

- **Show all queues**:to displayall the queues defined in the selected rich filter.
- **Customize queues:** to display only selected queues.   
  You can add, remove, or reorder the queues you want to be displayed.

The queues displayed in the same gadget are independent of the current view, page, and sort order.

![Customize queues](/cms_trial/assets/c207887a-e258-430e-94c0-1c8993507dea.png)

### **Maximum rows**

The **Maximum** **rows** option lets you set the number of issues the gadget displays per page. The default number of issues is 10. You can change it, but it cannot exceed 50.

You can view the maximum number of issues by clicking the range pill toggle at the bottom of the gadget.

![recult issue count.png](/cms_trial/assets/aaf8a0de-2009-49af-868e-83ce703bfb62.png)

## Customize view layout

The end users can customize the layout of each view in two ways:

- Adjusting the width of any column,
- Choosing how the rows are displayed – two options are available:

  - rows of variable height, i.e., the rows are displayed on one or several lines, depending on the content and the horizontal space available in the gadget – this is the default option;
  - rows of the same height, i.e., the rows are always displayed with one line per row (some content will be hidden when the available horizontal space is insufficient).

To adjust the width of a column, simply drag the edge of the column header to reduce or increase its size.

The settings dropdown situated in the top-right corner of the issues table lets you customize the layout of the current view further:

- **One-line rows***:* enable you to toggle between rows of variable height (one or multiple lines per row) and rows of the same height (one line per row)
- **Striped rows**: enable you to toggle between rows in one color and rows in stripes
- **Reset column**: If the width of at least one column has been customized, the option removes the customizations and reverts to the default column width

The customizations are remembered at the browser level and do not impact other users of the same dashboard.

![customizations](/cms_trial/assets/1e38be5a-22cd-417a-a56e-ada22c3c4e2d.png)

## Update issues using the issue dialog

You can update issues directly from the dashboard using the issue dialog accessible from the *Rich Filter Results* gadget. You'll find an **Open issue dialog** button on the gadget's right-hand side when hovering over an issue. Clicking this button will open the [issue dialog](https://support.atlassian.com/jira-software-cloud/docs/update-an-issues-details/) directly in the dashboard, allowing users to preview and/or update issues.

![Open issue dialog.png](/cms_trial/assets/0fcecd94-a7b8-434d-9b5c-9dd1555d7d14.png)

Once the user closes the *issue dialog*, the dashboard is automatically updated to reflect any changes made.

## Bulk change issues

The issues displayed in the *Rich Filter Results* gadget can be modified in bulk by using the **Bulk change issues...** button located in the gadget's footer.

![bulk change.png](/cms_trial/assets/c7d03447-07aa-4b98-b94a-75e0506742d6.png)

When clicking *Bulk Change Issues, the* button redirects you to [Jira's Bulk Operation screen](https://support.atlassian.com/jira-service-management-cloud/docs/edit-multiple-issues-at-the-same-time/). This allows you to edit, move, transition, delete, watch, or stop watching multiple issues in one operation.

## Use Gantt charts

A Gantt *chart* is a bar chart that illustrates a project schedule. Any [view](/cms_trial/space/RFCDOC/783941729/Configure+views/) can be configured to display a Gantt chart in addition to normal columns like *Key* and *Summary*.

In the view configuration (see [Enable Gantt chart](/cms_trial/space/RFCDOC/783941729/Configure+views/) for details), the Gantt chart is configured with:

- a start and an end date based on issue fields,
- optionally, a list of dependencies based on *issue link types*,
- a choice for bar colors: predefined based on the issues' *status category* or customized based on a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/).

In *Rich Filter Results* gadgets, views with a Gantt chart are displayed like any other view: they can be used in queues, sorting, pagination, issue dialog, switching between views, etc., and work normally. The only particularity of views with a Gantt chart is that they can only be displayed with the one-line layout.

Below are the main things to know when using Gantt charts:

- The dependencies are represented with badges showing the number of the corresponding issues, placed to the left or the right of the bar, depending on the order of precedence.
- You can hover over a bar to see a tooltip with the start and end dates and the bar's duration.
- You can quickly scroll the chart by dragging the background or using the top and bottom scroll bars.
- When the bar of issues is present in the chart but not currently visible, an arrow at the left edge allows you to scroll the chart to see that bar automatically.

![2026-04-09_15-34-48.png](/cms_trial/assets/9414177e-140d-4c24-aa6c-2c74c8ec1654.png)

The settings icon (▢) situated in the top-right of the issues table gives access to the following Gantt-specific features:

- Click **Go to today** to scroll the chart to the current period automatically.
- Hold the pointer over the **GANTT** lozenge to see which date fields the Gantt is based on.
- You can change the chart zoom level. The available options are **D**, **W**, **M**, and **Q**, which represent days, weeks, months, and quarters, respectively.

![gant options.png](/cms_trial/assets/b054baaf-8007-423f-91df-ab6d4a88ce0a.png)