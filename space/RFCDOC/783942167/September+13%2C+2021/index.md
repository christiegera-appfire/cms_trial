# September 13, 2021

## More Customizations in Rich Filter Results Views

In a recent release, we introduced [display options for columns](/cms_trial/space/RFCDOC/783942111/August+28%2C+2021/) configured in the views of the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets. We have continued this effort and now these options include new settings.

Value formatting options and custom aggregation formulas were already available in rich filter gadgets using [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/). Creating a custom value is very useful when you want to reuse it in several gadgets (e.g., Rich Filter Results, Rich Filters Statistics, etc.). However, if you only need to customize these settings in a given view, you can now do this directly from the [view configuration](/cms_trial/space/RFCDOC/783941729/Configure+views/), without creating a custom value. This speeds up and simplifies the configuration process for such use cases.

The new settings, available when configuring columns in views, are:

- for columns based on numeric and time-tracking fields, you can choose the format of the values (including the total if enabled) among the following options:

  - For numeric fields:

    - Thousand separators on/off
    - Number of decimals: none or maximum 3, 2 or 1 or exactly 3, 2 or 1
  - For time-tracking fields:

    - Jira's time display format
    - Days, hours, minutes or seconds
- for columns supporting totals, you now have four more options for the aggregation formula (in addition to sum): none, average, minimum, and maximum.
- for columns based on [smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) configured to display the labels of the smart filter clauses (colored or not), you now have the additional option to display the labels in rectangles of the same width.

For more information about these new settings have a look at the [Configuring views](/cms_trial/space/RFCDOC/783941729/Configure+views/) documentation page.

Example of configuration for a column based on a numeric field named Story Points:

![contentId-783942167](/cms_trial/assets/695d48e0-6376-4f4f-acf9-90df3c8d5238.png)