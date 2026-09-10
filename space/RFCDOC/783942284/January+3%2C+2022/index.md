# January 3, 2022

In this release:

## New Gadgets: Rich Filter Simple Gauges and Rich Filter Smart Gauges

This release introduces two new gadgets which display gauges: *Rich Filter Simple Gauges* and *Rich Filter Smart Gauges*. These gadgets are similar to the *Rich Filter Simple Counters* and *Rich Filter Smart Counters* gadgets but, while the counters gadgets display aggregated values, the gauges gadgets display proportions and ratios. These can be derived from Issue Count, numeric & time-tracking issue fields, [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) or [custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/), and can be displayed in one of three ways: as a gauge, as a percentage and fraction, or as a percentage only.

- The [Rich Filter Simple Gauges](/cms_trial/space/RFCDOC/783942228/The+Rich+Filter+Simple+Gauges+Gadget/) gadget can display up to 10 independent gauges. Each gauge can be configured with a *filter & value* pair or with a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) – a dedicated configuration object for ratio definitions. The *filter* determines the gauge level by filtering the contributing issues. The *value* can be the Issue Count, a numeric or time-tracking field, or a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/).

  ![contentId-783942284](/cms_trial/assets/2c9e2034-fe5b-4338-b9a6-51438725d5ba.png)![contentId-783942284](/cms_trial/assets/90c179e6-2079-4097-8abd-460bc38b3b73.png)![contentId-783942284](/cms_trial/assets/45697f02-f829-463a-97c8-c94adc99a12e.png)
- The [Rich Filter Smart Gauges](/cms_trial/space/RFCDOC/783942246/The+Rich+Filter+Smart+Gauges+Gadget/) gadget is based on a [smart filter](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) and displays one gauge for each of the smart filter's clauses. The *value* on which the gauges are based can be the Issue Count, a numeric or time-tracking field, or a [custom value](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/). Two computation modes are available:

- - *The smart clauses are used as gauge filters*, i.e. they are used to compute the gauge levels relative to all the issues included in the gadget (all the gauges have the same total value). In other words, the collection of issues included in the gadget is partitioned according to the smart clauses, and the gauges reflect this partitioning.

    ![contentId-783942284](/cms_trial/assets/977a10b5-7b32-4398-8cc7-27aaa279351e.png)
  - *The smart clauses are used to compute the gauge totals*. All the gauges use the same *gauge filter*, which needs to be selected separately. In other words, the collection of issues included in the gadget is partitioned according to the smart clauses, and each of the resulting sub-collections is used to compute a simple gauge.  
    For this computation mode, a [custom ratio](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) can be used instead of a *gauge filter* and a *value*.

    ![contentId-783942284](/cms_trial/assets/656f4d95-fba1-4261-95a4-987b1684671f.png)

## Custom Ratios in gauge gadgets

This release introduces *custom ratios*, a new type of configuration object – similar to [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) – which further extends the capabilities of the rich filter gadgets. *Custom ratios* are defined as ratios, with a numerator and a denominator which can be based on Issue Count or numeric & time tracking fields. Optional JQL filtering conditions can be used to filter the contributing issues for the numerator and/or the denominator. *Custom ratios* can thus be used to compute ratios of different values.

*Custom ratios* are defined in the rich filter configuration and are available in the new gauges gadgets as a way to define proportions, providing a reusable and more flexible alternative to *filter & value* pairs. In future releases, *custom ratios* will be made available in other rich filter gadgets as well.

In the example below, four custom ratios are defined in the rich filter:

![contentId-783942284](/cms_trial/assets/88cdafd6-93de-4c98-a59f-7e5e98845e71.png)

These *custom ratios* are used to configure four simple gauges, displayed as a percentage and fraction:

![contentId-783942284](/cms_trial/assets/b8ecffe1-ad69-44b5-944e-ba5f409d0026.png)

For more information about this new configuration object, have a look at the [Configuring Custom R](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/)[atios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) documentation page.

## Dynamic filtering and statistics

We extended the dynamic filtering and the statistic support with two more fields. It is now possible to add dynamic filters and to use as statistic type in statistics gadgets:

- Project Category
- Status Category