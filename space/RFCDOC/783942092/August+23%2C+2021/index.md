# August 23, 2021

## Working Queries in Rich Filter Gadgets

The rich filter gadgets can optionally be configured to use a gadget-specific issue-filtering JQL condition referred to as *working query*.

Defined in the gadget's configuration form, the working query is an *additional JQL query* which is permanently applied on top of the base Jira filter and any active quick filters in the controller to further filter the issues the gadget will work with. In other words, while all the linked rich filter gadgets on a dashboard have access to the same collection of issues (which is dynamically controlled by the [controller gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/)), each individual gadget can also be configured to work with a subset of this issues collection.

This powerful feature allows you to configure each gadget to be precisely tailored to the intended use, while keeping the benefit of interactive and coherent dashboards.

![contentId-783942092](/cms_trial/assets/10b9519b-d8ad-4a58-91ae-f2c89a8af829.png)

## Totals in Rich Filter Results Views

The [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) displayed by the [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets can now be configured to optionally show a row with the totals. The total values are computed and displayed for the columns corresponding to numeric and time-tracking fields and to [custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/).

This feature provides an easy and convenient way to access aggregated issue data directly in the Rich Filter Results gadgets.

![contentId-783942092](/cms_trial/assets/c4bb7c6e-a3aa-4cae-bd5c-4575e30a7ee5.png)