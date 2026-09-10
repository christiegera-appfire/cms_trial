# January 17, 2022

In this release:

## Statistics, charts, and metrics based on Service Management SLA values

This release introduces statistics, metrics and charts based on the *SLA fields* provided by Jira Service Management(formerly known as *Jira Service Desk*). More precisely, the rich filters gadgets can now compute results based on the following properties of SLA fields: SLA *Met*, *Breached*, *%Met*, *%Breached*, *average duration*, and *completion date*.

## Statistics based on SLA fields

[The Rich Filter Statistics Gadget](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/) and [The Rich Filter Two Dimensional Statistics Gadget](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) can be configured with new values and new statistic types:

- For each SLA field, the options *Completed*, *Met*, *Breached*, *%Met*, *%Breached* and *Average* are available as values in the configuration form of the gadgets.

  ![contentId-783942310](/cms_trial/assets/633d8379-af03-47f2-904d-b8bc33fbad75.png)![contentId-783942310](/cms_trial/assets/4967af85-7777-4ae1-b7c1-693a3dba6709.png)
- The *completion date* of each SLA field is available as a *date statistic type*. This can be particularly useful when combined with SLA-related values.

  ![contentId-783942310](/cms_trial/assets/122f6cbb-9da7-4f08-8ccb-317dfd2d0ad9.png)

## Flexi charts based on SLA fields

[The Rich Filter Flexi Charts Gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) can be configured with new values and new statistic types:

- For each SLA field, the options *Completed*, *Met*, *Breached* and *Average* are available as values in the configuration form of the gadget.

  ![contentId-783942310](/cms_trial/assets/1a351ce0-e669-4098-bb11-a386714fdce1.png)
- The *completion date* of each SLA field is available as a *date statistic type*. This is particularly useful when combined with SLA-related values.

  ![contentId-783942310](/cms_trial/assets/2b277309-08e2-4193-b8b4-7faad23ecc45.png)
- For 2D flexi charts, when the completion date of an SLA field is selected on the primary breakdown, a predefined option is added to the statistic type options of the secondary breakdown: *SLA Met/Breached*.

  ![contentId-783942310](/cms_trial/assets/45fb7a4e-fa45-4cf4-b525-8d92e0f6bbdf.png)

## Counters based on SLA fields

[The Rich Filter Simple Counter Gadget](/cms_trial/space/RFCDOC/783941825/The+Rich+Filter+Simple+Counter+Gadget/) and [The Rich Filter Smart Counter Gadget](/cms_trial/space/RFCDOC/783942058/The+Rich+Filter+Smart+Counter+Gadget/) can be configured with new values. For each SLA field, the options *Completed*, *Met*, *Breached* and *Average* are available as values in the configuration form of the gadgets.  

[Unmapped macro: inline-media-image — no content to fall back on]

  

[Unmapped macro: inline-media-image — no content to fall back on]

## Gauges based on SLA fields

[The Rich Filter Simple Gauges Gadget](/cms_trial/space/RFCDOC/783942228/The+Rich+Filter+Simple+Gauges+Gadget/) and [The Rich Filter Smart Gauges Gadget](/cms_trial/space/RFCDOC/783942246/The+Rich+Filter+Smart+Gauges+Gadget/) can be configured with new ratios. For each SLA field, the options *%Met and* *%Breached* are available as predefined ratios in the configuration form of the gadgets.  

[Unmapped macro: inline-media-image — no content to fall back on]

  

[Unmapped macro: inline-media-image — no content to fall back on]

## Support for statistics by numeric fields

[The Rich Filter Statistics](/cms_trial/space/RFCDOC/783941781/The+Rich+Filter+Statistics+Gadget/), [Two Dimensional Statistics](/cms_trial/space/RFCDOC/783941803/The+Rich+Filter+Two+Dimensional+Statistics+Gadget/) and [Flexi Charts](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/) gadgets now support numeric fields as statistic type. All the existing features of these gadgets (sorting, totals, *quick charts* etc.) are compatible with statistics by numeric fields.

![contentId-783942310](/cms_trial/assets/b4ab7eae-dabb-4e62-beaa-70cd7ce4fbf6.png)