# May 17, 2022

In this release:

## Support for duration (computed) custom values

This release introduces a new type of [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) that computes duration, i.e., the time elapsed between two dates. These computed custom values can be found under the section *DURATION (COMPUTED)* in the *Base value* dropdown of the custom values dialog. There are two entries under this section:

- *Issue age / resolution time*: this is a predefined duration value which computes:

  - for unresolved issues – the time elapsed between now and the created date (issue age),
  - for resolved issues – the time elapsed between the resolution date and the created date (resolution time).
- *Custom duration*: With this base value, you can compute the time elapsed between any two date fields or between a date field and now by selecting a date field or *Current time* in the *Start* and *End* dropdowns.

Duration custom values can be used in views and most rich filter gadgets, just like the other custom values.

## New gadget: Rich Filter Text Panel

The Rich Filter Text Panel gadget lets you display configurable rich text directly on dashboards. You can use it to inform and guide users and give your dashboards context.

For more information about the Rich Filter Text Panel gadget, look at its [documentation page](/cms_trial/space/RFCDOC/783942398/The+Rich+Filter+Text+Panel+Gadget/).

## New settings for custom ratios: display format

You can now configure a display format for your custom ratios: in the dialog, there is a new dropdown labeled Display format with two options: Percentage and Ratio. If you select *Ratio*, a second dropdown appears where you can select the number of decimals to display your ratio. For example, for a value of 3/10, the gadgets would display 30% if you select the Percentage format and 0.30 if you select the Ratio format with Exactly 2 decimals.

## Support for date / time formats

The rich filter gadgets now display date and date-time values according to the Date / time formats configured in your Jira instance on the Look and Feel page under System settings.