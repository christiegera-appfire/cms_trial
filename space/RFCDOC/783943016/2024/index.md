# 2024

## December 18, 2024

## Icons column in views

You can now configure views with a new type of column called *Icons*, designed to display data in a compact format. An Icons column can contain up to six subcolumns, each displaying the values of an issue field as an icon. For example, you can define an Icons column that displays icons for *Issue Type*, *Priority, Project*, and *Assignee*. The Icons option is available in the *Special columns* section of the *Add a column* dropdown. You can add several Icons columns to the same view, each configured with the subcolumns of your choice, for maximum flexibility.

## New chart type: Percentage bar

We have added a new 1D chart type called *Percentage bar* chart. It has a layout similar to the *Bar* chart layout, but its y-axis ranges from 0% to 100%. This means that each bar functions like a gauge. Similar to the percentage bars in 1D statistics tables, each bar of a *Percentage bar* chart represents the percentage of the total value, or the value itself when it is a ratio. The pie chart and its variations (donut, gauge, treemap) do not accept overlapping categories (categories overlap when there is at least one issue that belongs to two or more categories). The *Percentage bar* chart type is the best alternative to pie charts in these cases.

## Option to hide empty periods in date-based statistics and charts

Previously, date-based statistics and charts displayed each period in the time range, including periods with no issues. For instance, a flexi chart configured to display a weekly bar chart of Story Points by the issues' Created date would show a bar for each week, even if no issues were created during some weeks. The gadget configuration now includes an option to hide these empty periods, so you only see periods with meaningful data. The new checkbox, called *Show empty periods*, is checked by default, so the default behavior remains unchanged. Simply uncheck it when you want the gadget to hide the empty periods.

## Improvements in smart filter and view lists

The configuration of smart filters and views is accessed in two screens: a screen with the list of smart filters/views, and one with the details of a particular smart filter/view. You can now see and edit more of the configuration directly from the first screen. For instance, from the smart filter list screen you can now:

- see the color and JQL of each smart clause,
- edit or delete any clause or add a new one,
- make a copy of an existing clause (using the right-click menu),
- copy to the clipboard the name and JQL of a clause.

These features should reduce the need for going back and forth between the two screens, thus making the configuration changes easier and faster.

## Options for dynamic filter name

In the rich filter configuration, you can now customize the label displayed by a dynamic filter in the controller. The options are similar to the ones already available for column headers in views. You can choose between the *Field name* (default option), the *Field initials*, or a custom label. This can be particularly useful if the field name is too long or otherwise inadequate for your dashboard.

## Other improvements and fixes

- In the *Issue Activity Stream* gadget, don't include issue transitions in the *Issue edited* activity type, so that transitions and edits can be separated with the *Items filtering* setting in the gadget config.
- More compact layout for stacked bar charts with many stacks
- In stacked bar charts, use a fading effect instead of the slice widening effect for highlighting slices.
- In the *Rich Filter Results* gadget, display asset names (instead of IDs) also for users who don't have a Jira Service Management license.

## September 18, 2024

## New starring feature for rich filters

You can now star your favorite rich filter objects. In the rich filters configuration, your starred rich filters will appear at the top of the list by default (i.e., the list is sorted by *Starred*, then *Name*). However, you can click on the *Name* column header to sort the list alphabetically. When configuring a gadget, starred rich filters are displayed in a dedicated section within the *Rich filter* dropdown. This feature makes accessing your favorite rich filters much faster and more convenient.

## Date formatting can be customized for each rich filter

Previously, rich filter gadgets displayed date and date-time values based on the format set in the Jira *Look and feel* configuration. Now, a similar (optional) setting is available in the rich filters configuration under a new tab called *Misc settings*. For each rich filter, you can either retain the Jira *Look and feel* format or customize it with a different format that will apply to all gadgets using that rich filter.

## Custom colors for quick filters in the controller

You can now customize the colors of quick filter buttons in the controller. When configuring controller gadgets, you can assign a color to each quick filter in the list, including options like *All static*. The selected color will be used to display the corresponding buttons, allowing you to tailor the look to your aesthetic preferences or to make quick filters easier to distinguish based on your criteria.

## Improved permalinks

Permalinks generated from the controller now include the currently selected queues and views, as well as any custom sorting applied in the *Rich Filter Results* gadgets on the dashboard. This enhancement allows you to replicate the current state of the dashboard more accurately.

## September 2, 2024

## Collapsible sections in controller gadgets

Rich Filter Controller gadgets allow you to configure sections to group and organize your quick filters. Sections that have a title are now collapsible: you can click on their title to expand and collapse them at any time.

- When expanded, all the quick filters belonging to that section are displayed, as before.
- When collapsed, only the active quick filters (i.e. the ones that are currently applied) are displayed. This can make your controller simpler and more compact, and thus take less space on your dashboard. You can still interact with the active quick filters of your collapsed sections. If a collapsed section has no active quick filters, you can minimize it (i.e. send it to the right side of the gadget footer) to further declutter your controller. This means that even filters that are used very occasionally can now be made available (as part of a minimized section) and accessed with one click, without taking any space when not in use.

If you want to have access to many quick filters without sacrificing too much dashboard space, we encourage you to redesign your controllers to take advantage of these features.

## Support for several values in 2D statistics

When configuring *Rich Filter Two Dimensional Statistics* gadgets, you can now select up to 10 values (similar to 1D statistics). The gadget displays the table (or quick chart) for one value at a time, and you can switch the current value from the drop-up in the gadget footer (similar to quick charts in 1D statistics). For example, you can configure one 2D statistics gadget with three values: *Original Estimate*, *Time Spent* and *Remaining Estimate* to have all these values (sequentially) available on the dashboard, without taking space for extra gadgets.

## Striped rows and more sorting options in statistics

In the previous release we have added support for striped rows in Rich Filter Results gadgets. This release extends this feature to the statistics tables (1D and 2D). A new settings menu in the statistics gadgets allows you to turn this feature off. The same settings menu also contains entries to sort the table by the statistic type values, as well as an entry to reset the sorting order to the default.

## Miscellaneous UI and UX improvements

This release brings several UI and UX improvements:

- When using dynamic filters based on project fields, you can now filter the dropdown options by typing a project key, as an alternative to typing a project name.
- When configuring a gadget, in the rich filter dropdown, the rich filters that are used by other gadgets on the same dashboard are displayed at the top, so that you can select one directly, without searching. This will make building dashboards with many rich filter gadgets easier.
- In the Rich Filter Issue Activity Stream gadgets you can now expand the comments preview in order to see the full comments when they are long.
- In the rich filters configuration, the rich filter lists now display the first admin's full name instead of only the icon (any subsequent admins are still displayed as icons, with a tooltip showing their names). In addition, the visibility lozenges previously displayed as part of the *Jira filter* column are now displayed in a dedicated column called *Visibility*.

## July 2, 2024

## Striped rows in Rich Filter Results gadgets

By default, Rich Filter Results gadgets are now displayed with striped rows. You can turn this feature off for any particular view in the view settings menu of the gadget, similar to the "One-line rows" option. We are planning to add striped rows in statistics tables as well.

## More compact gadget UI

We have made the gadget UI more compact by reducing the vertical spacing between elements, allowing you to fit more rich filter results on your screen. Your [feedback](http://appf.re/support) on these changes is welcome and appreciated.

## June 18, 2024

## New option for the base value of custom values and custom ratios: "Time Spent + Remaining Estimate"

A new option is now available in the base value dropdowns of custom values and custom ratios: *Time Spent + Remaining Estimate*. This is a calculated value that can be used as an alternative to the *Original Estimate* base value, for an up-to-date total estimate.

## Statistics support for Parent

The new issue field *Parent* is now supported as statistic type in the statistics and flexi charts gadgets. It works by aggregating the issues with the same direct parent, i.e. on only one level of the issue hierarchy. For statistics and dynamic filtering, you should use this field instead of the deprecated Epic Link field.

## Dynamic filtering support for "Security Level"

You can now filter in the controller on the security level of your issue. To access it, simply add the new *Security Level* dynamic filter in your rich filter configuration.

## Preview images embedded in text fields and comments

You can now click on the images displayed in the *Rich Filter Results* and *Rich Filter Issue Activity Stream* gadgets to open an image preview screen similar to the one displayed by Jira in the issue screen. Note that you will need to update the app in Jira's *Manage apps* screen for this feature to work.

## Enhanced JQL validation

Previously, JQL queries entered in the app (e.g., in the base Jira filter of a rich filter or in the configuration of a static filter) were validated only when the configuration was saved. Starting with this release, the app now also validates already-configured JQL queries when they are simply displayed. This helps you easily identify any JQL queries that have become invalid after being entered.

In dashboards, rich filter gadgets now display a warning icon in the footer if any part of the JQL query they use is invalid. As before, the gadget will still attempt to compute results by ignoring the invalid clause of the JQL query when possible. However, the new warning icon, along with its explanatory tooltip, allows you to make an informed decision about the validity of these results.

## May 17, 2024

## New chart type: Sliced bar chart

A new chart type named *Sliced bar chart* is now available in flexi charts and in quick charts. It is a 1D chart type similar to the Gauge chart but with a more compact layout.

## Longer JQL queries in rich filter config

When configuring rich filters, you can add JQL queries to many configuration objects, like static filters, smart filter clauses, custom values, etc. These JQL queries can now be longer than before, up to 1000 characters vs. up to 500 characters.

## March 8, 2024

## Open issue dialog from Rich Filter Issue Activity Stream

The feature that gives direct access to the issue dialog, which was already available in the Rich Filter Results gadgets, is now also available in the [Rich Filter Issue Activity Stream](/cms_trial/space/RFCDOC/783942442/The+Rich+Filter+Issue+Activity+Stream+Gadget/) gadget. An icon appearing on hover at the right of the line allows you to open a dialog where you can view and edit the issue, without leaving the dashboard.

## New dependencies dialog in Gantt charts

The [Gantt charts](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) displayed in the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets can represent dependencies between the issues. A badge with the number of dependent issues is displayed to the left or right of each issue's bar, representing the number of preceding or following issues respectively. If you click on these badges, the app now displays a dialog listing those dependent issues with their relevant details: dependency type, issue type, key, summary, start or end date and status. The scheduling consistency is automatically checked, and the result is represented with a color tag. Access to the issue dialog allows you to easily view and edit the issues, for instance to update start or end dates in order to fix the scheduling problems highlighted in the dialog.

## Option to reset the sort order in Rich Filter Results

The Rich Filter Results gadgets display issues in a default order, defined in the configuration. On top of the default order, users can apply custom sorting by clicking on column headers. It is now possible for users to reset the sort order to the default one. When custom sorting is active, the menu accessible through the settings icon displayed at the right of the header line of the table has a new entry labeled *Reset sort order*. This is similar to the *Reset column width* feature that was already available.

## Warning for links with very long URLs

The app generates many functional hyperlinks. Most of them open a new tab with the Jira issue navigator already filtering on the relevant issues. The URL of the links encodes the JQL of the filter that is applied in the issue navigator. If the JQL is very long, the URL is very long also, and might exceed the maximum limit supported by the user's browser (the limit depends on the browser and its version). When the URL of a particular link is longer than 2,000 characters, when you click on the link the app now shows a small dialog, warning you that the URL is very long and might not work in your browser. The dialog allows you to continue and open the link (you may know what the limit is for your browser and that this link will work), or cancel, or copy the JQL of the link to the clipboard. Copying the JQL allows you to paste it yourself in the issue navigator if needed, thus bypassing the browser limitation on the URL length.

## Bar and line charts y axis steps improvement

In some cases (when values are time-based), the steps of the y axis of bar and line charts were not round numbers. We have improved these charts to have y axis steps that are, for all types of values, as round as possible, given the other constraints.

## January 9, 2024

## Y axis badge for line charts

In the line and multi-line flexi charts, as well as in the *Rich Filters Time Series* and *Created vs. Resolved* gadgets (which also use the line/multi-line layouts), we have added a badge on the y axis showing the level of the current cursor vertical position in the chart. A horizontal line materializes this vertical position, allowing you to easily visually compare the values of several data points in the chart. This feature is also particularly useful for multi-line charts that display ratios, as well as for charts whose y axis unit is different from the unit of the values in the chart, because it allows you to see in the badge the precise value of any data point in the unit of the y axis.

![contentId-783943016](/cms_trial/assets/d5d7ab97-f4a2-41b9-9292-cc961f8b88c6.png)