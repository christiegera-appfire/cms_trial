# February 16, 2022

## Support for filtering modes in dynamic filters

The [Rich Filter Controller](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) gadget now provides additional filtering modes for the [dynamic filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/) that display dropdowns (e.g., Assignee, Components, Status, Labels). The filtering modes correspond to the logical operators used to combine the selected values when generating the JQL filtering condition:

- **OR**: this is the default filtering mode (and the only mode previously available) – when multiple values are selected in a dynamic filter, they are combined with OR, which means that the filter returns the issues that match any (at least one) of the selected values;
- **AND**: this filtering mode is available for fields that can have several values simultaneously (e.g., Labels, multiple selection fields) – when multiple values are selected in a dynamic filter, they are combined with AND, which means that the filter returns the issues that match all the selected values simultaneously;
- **NOT**: This option is available for all fields. The selected values are negated and combined with AND, which means that the filter returns issues that don't match any of the selected values.

![contentId-783942336](/cms_trial/assets/58dd2402-126b-45ab-b41d-99d30fe7e43d.png)![contentId-783942336](/cms_trial/assets/7e22002f-4982-40eb-b529-143116c084e8.png)

For more information about the *Rich Filter Controller* gadget, have a look at its [documentation page](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/).

For more information about *dynamic filters*, have a look at [Configuring Dynamic Filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/).