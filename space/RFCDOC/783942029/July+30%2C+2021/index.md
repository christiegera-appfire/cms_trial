# July 30, 2021

## Custom Values in Rich Filter Gadgets

This release introduces *custom values*, a set a features that considerably extends the capabilities of the rich filter gadgets.

Defined in the rich filter configuration, *custom values* are available as columns in views and as values in gadgets, alongside the Jira fields, providing support for *custom aggregation formulas* (sum, average, minimum and maximum, with optional JQL filtering of contributing issues) and *custom results display* (label, color and format). *Custom values* can be based on Issue Count or numeric and time-tracking fields.

All the rich filter gadgets that display results based on issue data benefit from this enhancement, including the [flexi charts gadget](/cms_trial/space/RFCDOC/783941863/The+Rich+Filter+Flexi+Charts+Gadget/).

For more information about this new set of features have a look at the [Configuring Custom Values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) documentation page.

### Examples of rich filter gadgets configured to display *custom values*

In the examples below we've used four custom values defined as follows:

- Resolved Story Points – the sum of the story points of the resolved issues (uses a JQL query to limit the contributing issues to the resolved ones)
- Support Time Spent – the sum of the time spent for support issues, displayed in days (uses a JQL query to limit the contributing issues to bugs)
- Avg Time Spent (h) – the average time spent, displayed in hours
- Max Rem. Estimate – the maximum remaining estimate for the unresolved issues, displayed in days (uses a JQL query to limit the contributing issues to the unresolved ones)

Rich Filter Simple Counter gadget displaying the four custom values:

![contentId-783942029](/cms_trial/assets/f3d9ba36-b2bc-4542-a28d-bb9b4145c7d3.png)

Rich Filter Statistics gadget displaying the four custom values aggregated by assignee:

![contentId-783942029](/cms_trial/assets/7b2444ca-e497-45c3-bfe4-71708cb0f171.png)

Rich Filter Flexi Charts gadget displaying a treemap chart of the custom value Support Time Spent aggregated by assignee:

![contentId-783942029](/cms_trial/assets/5e3a5d59-f383-44b8-8b66-be07063353de.png)