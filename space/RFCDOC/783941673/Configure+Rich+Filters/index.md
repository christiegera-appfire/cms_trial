# Configure Rich Filters

The rich filters extend the Jira native filters to include definitions for additional filtering capabilities (quick filters), issue highlighting, multiple views for the results, and other settings that can be used by rich filter gadgets. The rich filters greatly simplify the configuration of rich filter gadgets and allow these to coordinate and interact with one another to provide powerful interactive dashboards.

The principle is simple: all gadgets with a rich filter on the same dashboard are automatically connected. You can activate and deactivate quick filters in a gadget, and the other gadgets will automatically reload to reflect the filtering. You can edit the rich filter, and all gadgets that use it on any dashboard will be updated the next time they are loaded: new options appear, views or filters change, without needing to re-configure each gadget individually.

Each Rich Filter has the following key attributes:

- The **name** serves as an identifier for the rich filter.
- The **description** lets you store additional text information about the rich filter.
- Administrators are users who are allowed to edit the configuration of the rich filter. The user who creates a rich filter is automatically set as that filter’s administrator. However, it is possible to allow other users to edit the rich filter by adding them to the administrator’s list.
- The **Jira filter** is the base data source for every gadget that uses the rich filter.

  ![Details view](/cms_trial/assets/865680f0-bfff-4712-bd98-88d1db26d7f6.png)

[Jira administrators](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) can edit the configuration of any Rich Filter independently of the administrators' list.

## Contents

- [Manage Rich Filters](/cms_trial/space/RFCDOC/783941683/Manage+Rich+Filters/) - covers the lifecycle actions for rich filters themselves: creating, searching for, viewing/editing, duplicating, archiving, trashing, and permanently deleting them.

  - [Bulk operations](/cms_trial/space/RFCDOC/1723596949/Bulk+operations/) - perform actions like moving to trash, restoring, permanently deleting, downloading usage data, or exporting to backup across multiple rich filters at once, accessible using Bulk ops in the side navigation.
  - [Rich filter usage data](/cms_trial/space/RFCDOC/1723236446/Rich+filter+usage+data/) - download an Excel file tracking usage activity for their rich filters.
  - [Export and import of rich filters data](/cms_trial/space/RFCDOC/1723924660/Export+and+import+of+rich+filters+data/) - create backup files containing rich filter configurations.
- [Details configuration](/cms_trial/space/RFCDOC/783941695/Details+configuration/) – Define fixed quick filters based on preset JQL clauses that users can toggle on or off to narrow down the issues shown in gadgets.
- [Configure static filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/) - Define fixed quick filters based on preset JQL clauses that users can toggle on or off to narrow down the issues shown in gadgets.
- [Configure dynamic filters](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/) - Create quick filters whose selectable options are generated automatically from the values of a chosen issue field, so they stay current as data changes.
- [Configure smart filters](/cms_trial/space/RFCDOC/783941713/Configure+smart+filters/) - Build named sets of color-coded, JQL-based clauses that can filter issues, appear as tags/columns in results, or serve as grouping criteria in statistics and chart gadgets.
- [Configure views](/cms_trial/space/RFCDOC/783941729/Configure+views/) - Define the sets of columns (issue fields, custom values, tags, or a Gantt chart) that Rich Filter Results gadgets use to display issues.
- [Configure queues](/cms_trial/space/RFCDOC/783942406/Configure+queues/) - set up JQL-based, tab-displayed issue lists, each with its own views and sort order, for organizing work like support requests or triage queues.
- [Configure custom values](/cms_trial/space/RFCDOC/783942033/Configure+custom+values/) - create user-defined, aggregated metrics (sum, average, min, max) based on issue count or numeric/time-tracking fields, for use as columns or gadget values.
- [Configure custom ratios](/cms_trial/space/RFCDOC/783942266/Configure+custom+ratios/) - define numerator/denominator-based ratios (for example, completion rate, work ratio), optionally filtered by JQL, and display them as percentages or decimal ratios in gadgets.
- [Configure time series](/cms_trial/space/RFCDOC/783942356/Configure+time+series/) - build date-field-based data series (for example, issues created per week) that can be charted or tabulated to track trends over time.