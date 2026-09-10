# March 28, 2022

## New Gadgets: Rich Filter Created vs. Resolved Chart and Rich Filter Time Series Chart

This release introduces two new gadgets that display multi-line charts based on date & date-time fields.

### Rich Filter Created vs. Resolved Chart

The *Rich Filter Created vs. Resolved Chart* gadget displays values based on the issues created versus the issues resolved over a given period of time. It allows users to monitor the relative evolution of created and resolved issues.

The gadget is configured with a time range and an aggregation period (similar to date-based flexi charts) and with a value, which can be Issue Count or a numeric field. The gadget is compatible with the three aggregation types introduced in the [previous release](/cms_trial/space/RFCDOC/783942344/February+28%2C+2022/).

Example of gadget configured to display the created versus the resolved Story Points with unresolved trend sub-plot and *cumulative trend* aggregation:

![contentId-783942426](/cms_trial/assets/04cc124a-5da8-447b-bc34-fba34824ba71.png)

For more information about the Rich Filter Created vs. Resolved Chartgadget, have a look at its [documentation page](/cms_trial/space/RFCDOC/783942386/The+Rich+Filter+Created+vs+Resolved+Chart+Gadget/).

### Rich Filter Time Series Chart

The *Rich Filter Time Series Chart* gadget displays one or several series of values as a line or multi-line chart. For maximum flexibility and reusability, these series of values are defined in the rich filter configuration as a new type of configuration object called [time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/). A time series is based on a date or date-time field and a value, which can be Issue Count, a numeric or time-tracking field, a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/), a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) or an SLA field. An optional JQL filtering condition can be used to filter the issues which contribute to the time series.

The *Rich Filter Time Series Chart* gadget is configured with a time range and an aggregation period (similar to date-based flexi charts) and with one or several *time series*. The gadget is compatible with the three aggregation types introduced in the [previous release](/cms_trial/space/RFCDOC/783942344/February+28%2C+2022/).

This chart is particularly useful when configured to display two or more time series, allowing users to make comparisons and identify trends and correlations between series.

Example of gadget configured to display four time series:

![contentId-783942426](/cms_trial/assets/58503983-c069-43b1-b19a-87feccb5ffcc.png)

The four time series, as defined in the rich filter:

![contentId-783942426](/cms_trial/assets/3ac94942-2d9e-4c5d-95af-864bc2fd8daa.png)

For more information about the Rich Filter Time Series Chartgadget, look at its [documentation page](/cms_trial/space/RFCDOC/783942364/The+Rich+Filter+Time+Series+Chart+Gadget/).