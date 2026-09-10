# October 25, 2021

In this release:

## Dynamic filters based on dates

Dynamic filtering, one mechanism by which [Rich Filter Controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) gadgets allow dashboard users to easily filter issues, now supports date and date time fields.

The configuration is as easy as any other field – in the rich filter configuration, simply add dynamic filters based on the date or date time fields you want to filter.

For dashboard users, filtering on dates is easy and intuitive: a click on the date dynamic filter in the controller reveals the From and To fields for the date limits. One or both of these fields can be filled with a calendar date by selecting it in a date picker or typing it in the field. It is also possible to type a time relative to the present, using the format accepted by the JQL (e.g., "3d", "-2w 3d 4h").

![contentId-783942200](/cms_trial/assets/7d61ae12-000d-4402-8a55-fdd5d69d9b62.png)

For more information about *dynamic filters*, have a look at [Configuring Dynamic Filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/).

## Statistics and charts based on dates

The [Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/), [Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/), and [Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadgets can now aggregate issue data by date and date time fields.

The configuration is flexible, with multiple options for the *aggregation periods* (from days to years) and for the *time range*:

Image — asset pipeline pending  
Image

An *auto* mode is also available, which dynamically adjusts the parameters to produce the most granular yet complete statistics (i.e., with the appropriate aggregation period so that all the relevant issues are included).

As with any other breakdown, date-based statistics and charts can compute results based on Issue Count, numeric & time-tracking fields, and [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/).

![contentId-783942200](/cms_trial/assets/6b639afa-1c29-4b6b-aa12-55b806f4141b.png)

The *Two Dimensional Statistics* gadgets can be configured with a date or date time statistic type for one or both breakdowns.

![contentId-783942200](/cms_trial/assets/a0d4ae4e-3b38-4a34-a93a-39485d5ef378.png)

In the *Flexi Charts* gadgets, date-based breakdowns can be configured for the following chart types:

- 1D: *bar charts*
- 2D: *clustered bar charts* and *stacked bar charts*.

![contentId-783942200](/cms_trial/assets/5d4c1c1b-1193-4320-9956-08b229c8d98a.png)