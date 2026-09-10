# 2023

## December 12, 2023

## Improvements and fixes for fields Parent and Team

Following recent changes in Jira related to the issue fields *Parent* and *Team*, the app's support for these fields had to be adapted. This release delivers this adaptation and also extends the support for the field *Parent* to include dynamic filters. In the controller gadgets, dynamic filters on *Parent* work the same as the already available dynamic filters on *Epic Link*.

## November 8, 2023

## Choose your default layout in views

In a recent release we have introduced the option to display the issues in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadgets with one line per row (compact layout). The default layout remained the variable-row-height layout. In this release, we have made the default layout configurable at the level of the [views](/cms_trial/space/RFCDOC/783941729/Configure+views/). If you want a particular view to be displayed by default with one line per row, you can toggle a switch in the view configuration. Of course, users can still switch between the two layouts in the *Rich Filter Results* gadgets.

## September 29, 2023

## Support for read-only access to gadget configuration

Users who don't have edit rights on a dashboard can now access the configuration of its rich filter gadgets in read-only mode. This makes it easier for such users to better understand the results displayed by the gadgets and the way the app works in general. To access this feature, click on the Rich Filters icon situated in the bottom-left corner of any gadget and select the new *View gadget config* option in the drop-up menu.

## Optimized gadget refresh

Previously, the only way to refresh the rich filter gadgets in an optimized way was to use the dedicated button at the bottom-right of the Rich Filter Controller gadgets. If you clicked on the Jira-managed refresh buttons at the top-right of every gadget, or on the dashboard refresh button at the top-right of the dashboard, the rich filter gadgets were recreated from scratch. We have now made these two refresh options also perform an optimized refresh. Each user can now use the refresh buttons they prefer and everyone benefits from high responsiveness in the rich filter dashboards.

## August 24, 2023

## Customize Gantt chart colors

Previously, the color of the bars in the [Gantt charts](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) was based on the issues' *status category*. Now, the bar colors can also be [customized](/cms_trial/space/RFCDOC/783941729/Configure+views/) by using a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/)*.*

## July 31, 2023

## Automatic app data deletion after uninstall

In the previous release we have introduced [Delete all app data](/cms_trial/space/RFCDOC/783943002/App+configuration/), a feature that allows you to *manually* request the deletion of all your data in the *Rich Filters for Jira Dashboards* app. We have now added an *automated* scheduling for app data deletion after the app is uninstalled. This means that, if you haven't manually requested the app data deletion, after you uninstall the app your data will be stored for a limited period of time (between 4 and 6 months), after which it will be automatically deleted. If you re-install the app during this period you will still find your data (the rich filter objects and the permissions configured in the app) and will be able to continue to use the app normally.

## Support for filtering issue activity

The [Rich Filter Issue Activity Stream](/cms_trial/space/RFCDOC/783942442/The+Rich+Filter+Issue+Activity+Stream+Gadget/) gadget now supports filtering the activity items at the gadget level. The filters are defined in the gadget configuration and allow you to show or hide activity performed by certain users, or to show or hide certain types of events (like *Issue created*, *Issue transitioned, etc.*).

## July 12, 2023

## Delete all app data

This new feature allows you to easily delete all your data in the *Rich Filters for Jira Dashboards* app. This covers the rich filter objects and the permissions configured in the app. You may wish to do this before uninstalling the app, for instance after a trial on a temporary instance, or in order to reset the app and start over.

To learn more about this feature, have a look at [Delete all app data](/cms_trial/space/RFCDOC/783943002/App+configuration/).

## Support for third-party app fields

We have added support for custom fields provided by the following third-party apps:

- *STAGIL Traffic Lights*
- *Timesheets by Tempo - Jira Time Tracking*

To learn more about third-party app support, have a look at [Third-Party App Support](/cms_trial/space/RFCDOC/783942998/Third-Party+app+support/).

## June 15, 2023

This release adds several new features and improvements to the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadget.

## Display Gantt charts (beta)

You can now visualize your work schedule directly on your dashboard with Gantt charts. The [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) displayed by [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadgets can be configured to display a [Gantt chart](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/), in addition to the normal columns like *Key* and *Summary*. Gantt charts support colored bars, badge-style dependencies, scroll by dragging and multiple zoom levels.

This feature is still in beta – we are planning to add improvements in the future and your feedback is welcome and appreciated.

## Display issues with one line per row

Previously, [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadgets could only display issues with variable row height, i.e. the table rows are displayed on one or several lines, depending on the content and on the horizontal space available in the gadget. This is still the default behavior, but now you also have the option to display the issues with one line per row. This mode results in a more compact and consistent layout, at the cost of hiding some content when the available horizontal space is insufficient. This option can be toggled on and off in a new settings dropdown situated in the top-right corner of the issues table.

## Support for floating headers and custom column width

Similar to frozen header lines in spreadsheets, the floating header is practical when [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadgets display many lines. This means the table header is always visible when you scroll down the dashboard page.

The custom column width is a simple but very useful feature that allows each user to customize the layout of the [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/)gadgets. Simply drag the edge of the column header to reduce or increase the width of the column. The customization is remembered at the browser level and does not impact other users of the same dashboard. You can reset the column width at any time from the new settings dropdown situated in the top-right corner of the issues table.

## May 16, 2023

## Support for average age reporting in flexi charts

The [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadget now offers support for a new type of report: *average age*. This report can be displayed as a *Bar, Line, Clustered bar, and Multi-line chart and shows how long issues have been unresolved,* on average, during each aggregation period. In order to configure the gadget to display the average age, select the *Average age* as the *Statistic type*, along with the desired time range and aggregation periods.

## Improved options selection in drop-downs

The selectors for values and statistic types in gadgets' configuration are now enhanced with shortcuts to the sections available in the list. This makes it easier to find and select the desired options in the list – simply click the shortcuts to jump between categories of available statistic types and values.

## April 27, 2023

## Trash for rich filters

We have implemented a trash mechanism for rich filters – if you want to delete a rich filter, you now need to start by moving it to the trash. Once in the trash, the rich filter cannot be edited or used in gadgets anymore. Trashed rich filters are automatically deleted after 60 days, but can still be viewed, restored, or deleted manually before then. You can access the trash from the  `...`  menu at the top-right of the active rich filters list.

Together with the *Last used date* information on the rich filters and the *automatic archiving* of unused rich filters that we have added recently, the trash mechanism will considerably simplify the management of your rich filters.

## New Last comment columns in views for Service Management

In the [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) displayed by [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets, four new columns, available for issues in Service Management projects, allow you to follow the conversations in the comments. You can find these columns in the *Special columns* section of the *Add a column* dropdown.

- *Last external comment* – the most recent external comment added either by a Service Management agent or by a customer
- *Last internal comment* – the most recent comment added internally
- *Last reply from customer* – the most recent comment added by the customer
- *Last reply to customer* – the most recent external comment added by a Service Management agent

## April 7, 2023

## Improved support for satisfaction feedback

The customer satisfaction feedback available in Jira Service Management contains a rating, a date and an optional comment. The satisfaction rating was already available in the Rich Filters app. In this release we have added support for the satisfaction date and comment.

- The *satisfaction date* can be used like any other issue field of type date time:

  - as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets;
  - as *Statistic type* in the statistics and flexi charts gadgets: [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/), [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) and [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/);
  - as [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/), allowing you to filter the issues on your dashboard;
  - as a basis for configuring [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/).
- The feedback comment can be viewed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets – if your [view](/cms_trial/space/RFCDOC/783941729/Configure+views/) contains the column *Satisfaction* (i.e. the rating), you can hover over the rating to see the satisfaction date and click to see the feedback comment in a tooltip.

## Support for dynamic filtering on the issue key

You can now add [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/)s on the issue key, which allow you to filter your dashboard on one or several specific issues. In the [controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/), the dynamic filter on *Key* allows you to search for the issues by their keys, but also by words in their summaries. Once the issues you're interested in appear in the dropdown, you simply select them and apply the filters, as with any other dynamic filter.

## March 30, 2023

## Support for themes

The themes recently added in Jira are now supported by the Rich Filters app, both in dashboards and in the rich filters configuration pages. When you change your current theme in Jira, the app's UI reflects that change – there is no separate setting for the app.

## UI improvements

There are two UI improvements added in this release that we would like to mention:

- In the [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) configuration, in the *Add a column* dropdown, the available options are organized in sections (*Issue fields*, *Special columns*, *Static filters*, *Smart filters* and *Custom values*). It is now easier to find the options you're looking for, thanks to the buttons we have added at the top of the options list. There is a button for each section and, when you click on one, the list scrolls automatically to the beginning of the corresponding section.
- [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) can display a quick table below the chart, with a tabular representation of the chart data. The quick tables of flexi charts configured with the *Word cloud* chart type are now also displaying the icons for priorities and issue types, to match the way these are displayed in the chart itself.

## Additional informative tooltips in charts

In [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/), the name of the value of the chart (e.g. Issue Count or Story Points) is displayed in the footer of the gadget and, for chart types that have x and y axes (bar, line, clustered bar etc.), also in the y axis label. When you hover over the value name in any of these places, you now get a tooltip showing:

- the total value over the whole chart,
- when the value is a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) or a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), its JQL query, if any.

## March 22, 2023

## New instance-level configuration for the app

The new *App configuration* page gives access to instance-level settings for the Rich Filters app. Site admins and [Jira admins](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) can access this page from Jira’s *Apps* administration menu, in the left sidebar under the section *Rich Filters*.

Currently two permission settings are available on this page: *Creating rich filters* and *Exporting rich filter gadget results*. Have a look at [*App configuration*](/cms_trial/space/RFCDOC/783943002/App+configuration/) for details about these settings.

## Support for the field Category

The issue field [Category](https://support.atlassian.com/jira-work-management/docs/categorize-items-in-your-list-view/), available in business projects in Jira Work Management, is now available:

- as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets;
- as *Statistic type* in the statistics and flexi charts gadgets: [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/), [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) and [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/);
- as [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/), allowing you to filter the issues on your dashboard.

## More flexibility for dynamic filters

In [Rich Filter Controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) gadgets, [dynamic filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/) on option-based fields (like *Priority* or *Assignee*) display a dropdown with a list of options to choose from in order to filter your issues. It is now possible to have these options displayed in reverse order for specific dynamic filters for which the reverse order is preferred. The *Reverse options order* setting is available in the rich filter configuration, in the dynamic filter edit dialog.

## March 14, 2023

## UX improvements in quick tables

The rich filter gadgets that display charts – [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/), [Rich Filter Time Series Chart](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) and [Rich Filter Created vs Resolved Chart](/cms_trial/space/RFCDOC/783942386/The+Rich+Filter+Created+vs+Resolved+Chart+Gadget/) – can display a quick table below the chart, with a tabular representation of the chart data. We have made the understanding of this data easier by adding highlighting interactions between the chart and the quick table to help you quickly identify the correspondence between the two. For example, when you hover in the chart, the corresponding line or cell of the quick table is highlighted, and when you hover over a cell in the table, the corresponding bar or slice in the chart is highlighted.

## Support for Jira themes

We have been working behind the scenes to add support for themes in the Rich Filters app to match the new themes in Jira. We expect to be ready to release this feature as soon as Atlassian makes the theming framework available for third party apps.

## February 23, 2023

## New types of columns in Rich Filter Results views

When configuring [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in  [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets, you now have new options in the *Add a column* dropdown:

- The  [static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/) configured in your rich filter are available to be added as columns, allowing you to highlight issues with colors and labels. Static filter columns behave as ON/OFF markers – issues that match the JQL of the static filter will display the marker.
- A new option named *Last comment* is available under the section *SPECIAL COLUMNS*. You can use this column to display, for each issue, the last comment that you have access to.

## Automatic archiving of unused rich filters

This is a new feature that will simplify the management of your rich filters by automatically identifying the unused rich filters and moving them to a separate list – the rich filters archive.

Rich filters that are not used for 180 days are automatically archived. A rich filter is considered “used” when a gadget based on it is loaded in a dashboard, or when the rich filter’s configuration is changed.

Once archived, rich filters cannot be edited or selected anymore in the configuration of rich filter gadgets. However, if an existing dashboard based on an archived rich filter is loaded, the rich filter is automatically unarchived. You can also manually unarchive a rich filter from its configuration page.

## January 23, 2023

## Export gadgets to PDF, Excel and CSV

In a previous release we have added support for export to PDF, Excel and CSV in the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/), [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) and [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) gadgets. In this release we have added this feature in the remaining rich filter gadgets. The [Rich Filter Controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) gadget is special in this regard: it allows you to export to one PDF or Excel file all the rich filter gadgets on the same dashboard that are linked to that controller gadget (reminder: rich filter gadgets on a dashboard are linked together if they use the same rich filter in their configuration). The gadgets are exported as they are at the time the export is initiated, thus reflecting any active filtering in the controller, current [view](/cms_trial/space/RFCDOC/783941729/Configure+views/) in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/), sorting of columns etc.

To sum up, in one click you can export any rich filter gadget individually or all the rich filter gadgets of a dashboard.

## Support for Unresolved (computed) time series

This release introduces a new type of [t](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/)[ime series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) called *Unresolved*, which you can find under the section *Computed* in the *Series* dropdown of the time series dialog. Unlike the other time series which are based on a date field, unresolved time series are computed as the difference between *Created* and *Resolved* time series. Unresolved time series allow you to easily monitor the size of your backlog.

## Support for time series in additional gadgets

[Time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) were already supported in the [Rich Filter Time Series Chart](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) and the [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) gadgets. This release adds support for time series in two additional gadgets: the [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) and the [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadgets. This new feature can be very useful if you need to display a *time series dynamically split* by the values of an issue field or the clauses of a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/). For instance, you can track in a multi-line flexi chart the unresolved Story Points (time series of type *Unresolved*) for each of your teams (defined with a smart filter).