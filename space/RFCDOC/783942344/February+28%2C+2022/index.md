# February 28, 2022

## Support for cumulative aggregation in flexi charts based on dates

[Rich Filter Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadgets configured to display charts based on date & date-time fields are now enriched with options for cumulative aggregation of data. The following *aggregation types* are available:

- **Period value**: this is the default option (and the only one previously available) – the chart displays the values of each individual aggregation period;
- **Cumulative trend**: progressively adds the values from the previous periods, including only the issues starting with the first period of the chart;
- **Cumulative total**: progressively adds the values from the previous periods, including the issues before the first period.

This feature is compatible with 1D and 2D date-based charts (bar, clustered bar, and stacked bar).

Example of a bar chart of *Story Points* by *Due date* with *Cumulative trend* aggregation type:

![contentId-783942344](/cms_trial/assets/9118786a-923e-4667-a1d0-e64f70353801.png)

For more information about the *Rich Filter Flexi Charts* gadget, look at its [documentation page](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/).