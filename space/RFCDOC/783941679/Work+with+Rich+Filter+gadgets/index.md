# Work with Rich Filter gadgets

The gadgets provided by the**Rich Filters for Jira Dashboards**app are called *Rich Filter* gadgets. All rich filter gadgets are based on rich filters and have one particular property—two or more rich filter gadgets on a dashboard are linked together if they share the same rich filter.

The first rich filter gadget described in this section is the *Rich Filter Controller*. This gadget displays buttons controlling which issues the other rich filter gadgets display. All the other rich filter gadgets display results based on issue data. This section presents all the rich filter gadgets and how they can be configured.

You don’t need to do anything to connect the gadgets: when placed on the same dashboard, all gadgets configured to use the same rich filter are automatically connected. When you enable or disable quick filters (static, dynamic, or smart filters) in the controller, the new filtering configuration defines a new collection of issues, and all the other gadgets automatically reload their data based on this new issue collection.

You can have gadgets that use two (or more) rich filters on the same dashboard. They will not affect each other, even if the two rich filters have quick filters with the same name.

You can also use any other Jira gadgets on the same dashboard with rich filter gadgets; however, the quick filters will not affect these other gadgets.

## The gadgets

- [The Rich Filter Controller Gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) - displays buttons for a rich filter's quick filters (static, dynamic, or smart), letting users control which issues the other connected gadgets on the dashboard display.
- [The Rich Filter Results Gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) - displays the filtered issue list using one or more configured views and queues, with support for tabs, sorting, totals, and Gantt charts.
- [The Rich Filter Issue Activity Stream Gadget](/cms_trial/space/RFCDOC/783942442/The+Rich+Filter+Issue+Activity+Stream+Gadget/) - shows a chronological feed of recent activity (comments, status changes, etc.) across the issues returned by the rich filter.
- [The Rich Filter Simple Counter Gadget](/cms_trial/space/RFCDOC/783941825/The+Rich+Filter+Simple+Counter+Gadget/) - displays one or more single numeric counters, based on issue count or custom values, for the filtered issue collection.
- [The Rich Filter Smart Counter Gadget](/cms_trial/space/RFCDOC/783942058/The+Rich+Filter+Smart+Counter+Gadget/) - displays aggregated issue data (or custom values) broken down by a smart filter's clauses, shown as labeled, colored counters
- [The Rich Filter Simple Gauges Gadget](/cms_trial/space/RFCDOC/783942228/The+Rich+Filter+Simple+Gauges+Gadget/) - displays gauges representing custom ratios (for example, completion rate, work ratio) as percentage-based visual indicators.
- [The Rich Filter Smart Gauges Gadget](/cms_trial/space/RFCDOC/783942246/The+Rich+Filter+Smart+Gauges+Gadget/) - displays a gauge for each clause of a smart filter (for example, one per team), each representing a custom ratio.
- [The Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) - displays issue counts, custom values, custom ratios, or time series in a table, aggregated by an issue field or smart filter.
- [The Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) - A two-dimensional version of the Statistics gadget that groups issues by two criteria (issue fields, smart filters, or date fields) and displays computed statistics—including custom values, custom ratios, and time series—as a sortable table or chart
- [The Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) - displays a chart with data computed from a collection of issues. This gadget is highly customizable, offering multiple options for chart types and how data is computed and displayed.
- [The Rich Filter Created vs Resolved Chart Gadget](/cms_trial/space/RFCDOC/783942386/The+Rich+Filter+Created+vs+Resolved+Chart+Gadget/) - displays the number of issues created versus the number of resolved over a given period
- [The Rich Filter Time Series Chart Gadget](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) - plots one or more configured time series as line charts, useful for comparing trends such as issue counts or SLA metrics over time.
- [The Rich Filter Text Panel Gadget](/cms_trial/space/RFCDOC/783942398/The+Rich+Filter+Text+Panel+Gadget/) - displays configurable rich text directly on dashboards to inform and guide users and to give context to dashboards.