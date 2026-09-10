# November 9, 2022

## New flexi chart type: Word cloud

[Flexi charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) now have a new *Chart type* option for 1D charts named *Word Cloud*. Like *Bar* and *Line* charts, *Word cloud* charts support overlapping and non-overlapping groups of issues but have a non-sequential layout, similar to the layout of *Treemap* charts. This means that you can use *Word cloud* as an alternative to *Bar* and *Line* types for charts by labels or other multiple-selection fields (*Treemap* charts, as well as *Donut*, *Pie* and *Gauge* charts, don't support these fields since they display slices, which must not overlap).

## Quick tables in Time Series Chart and Created vs Resolved Chart gadgets

In statistics gadgets, quick *charts* allow you to easily display charts for a visual representation of your statistics values. Similarly, in charts gadgets, *quick tables* allow you to easily display tables with all the values used in the charts. In this release we have added quick tables in two rich filter chart gadgets: [Time Series Chart](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/) and [Created vs Resolved Chart](/cms_trial/space/RFCDOC/783942386/The+Rich+Filter+Created+vs+Resolved+Chart+Gadget/) (very soon we will add quick tables in the [Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadget as well). Click on the corresponding icon at the bottom-right of the gadget to toggle the quick table on and off.

## Support for Assets objects fields in Rich Filter Results views, statistics, and dynamic filters

The custom fields of type [*Assets objects*](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-the-assets-objects-field/), which link issues to objects in [Assets for Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-assets-in-jira-service-management-cloud/), are now available:

- as columns in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets;
- as *Statistic type* in the statistics and flexi charts gadgets: [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/), [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/), and [Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/);
- as [dynamic filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/), allowing you to filter the issues on your dashboard.