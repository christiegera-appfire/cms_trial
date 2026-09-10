# April 13, 2022

In this release:

## Access bulk change operations from Rich Filter Results gadgets

You can now access Jira's bulk change operations directly from your Rich Filter Results gadgets. Just click on the corresponding icon in the gadget footer, and the bulk change will be initiated with the list of issues displayed by the gadget. This means that, in addition to the easy access, you benefit from the filtering capabilities of rich filter dashboards when doing bulk changes.

For more information about the Rich Filter Resultsgadget, look at its [documentation page](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/).

## Support for time series in Rich Filter Statistics gadgets

The Rich Filter Statistics gadget can now be configured to compute and display [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/). A new option labeled *Time series* was added at the bottom of the *Statistic type* dropdown under the *ADVANCED* section. When you select the *Time series* statistic type, the *Values* dropdown is replaced with a *Time series* dropdown so that you can select up to 10 time series for your gadget (you can select any time series defined in your rich filter, regardless of their value type). To finish the configuration of your gadget, select the *Aggregation periods* and *Time range*, as you would for a configuration of [statistics on date fields](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/).

For more information about the Rich Filter Statistics gadget, look at its [documentation page](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/).

## Support for dashboard permalinks

You can now generate *permalinks* for already filtered dashboards. Permalinks are URLs that encode the active filters in the controller gadgets on the dashboard. You can use a permalink to open the dashboard later, with the same filters already applied. Of course, permalinks can also be very useful for sharing a filtered dashboard with other users.

To generate a dashboard permalink, simply click on the corresponding icon in the footer of your Rich Filter Controller gadget. The permalink will be automatically copied to your clipboard.

For more information about the Rich Filter Controller gadget, look at its [documentation page](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/).

## Support for ratios in bar charts

Flexi charts now support ratios as values (both [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) and predefined SLA-based ratios). In the config form of your Rich Filter Flexi Charts gadget, the *Values* dropdown has a new section labelled *CUSTOM RATIOS* containing the custom ratios defined in your rich filter. If available, the SLA-based ratios are added under the section *SERVICE MANAGEMENT SLA FIELDS*. Ratio values are compatible with bar and clustered bar charts.

Of course, the quick charts available in the [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) and the [Rich Filter Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) gadgets also support ratios, without any additional configuration.

For more information about the Rich Filter Flexi Charts gadget, have a look at its [documentation page](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/).

## Support for dynamic filters on Epic Name

The field *Epic Name* is now available to add as [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/).

## Support for Project Category in Rich Filter Results gadgets

The field *Project Category* is now available to add as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in Rich Filter Results gadgets.