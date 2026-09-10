# JMCF for Jira Cloud 2.1

This version, released on July 2, 2024, includes the following changes:

## Scheduled recalculations!

Custom fields can now be scheduled to (re)calculate on demand! For scenarios where custom fields take a long time to recalculate or when updated data is critical, you can now schedule individual custom fields to recalculate on a set interval. See [Scheduled recalculations](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/1100611586) for more details.

## Enable and Disable custom fields

Custom fields can now be enabled or disabled from the [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) page. Disabling a custom field will not remove it from issue screens, but the field will not recalculate, including any scheduled calculations in the future.

![Jira Misc Custom Fields (JMCF) Cloud schedule calculation button](/cms_trial/assets/9c2de278-2d8b-40e7-8077-8ab5845d3810.png)

## Documentation Changes

**Starting with the release of JMCF for Jira Cloud 2.1**, Release Notes will now be moved to the new [Changelog](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/1097859485) page; this page will include summary information on each release, and is sorted by date of release instead of release number. This change enables more frequent communication of changes to JMCF Cloud and better supports the intended release plans moving into the future.

**Tip**: You can use the **Watch** feature on the Changelog page to stay up to date on all release information! Just click the eye icon ( [eye icon] ) in the page toolbar to add the page to your Watch list and you will receive email notification when the page has been updated.

### Scripted Fields autodetect dependent fields

When entering a script for a Scripted field, JMCF for Jira Cloud will now autodetect any issue fields or issue properties that are accessed in the script and will add them to the list of dependencies. Dependencies enable triggering an automatic recalculation of the scripted field when its underlying data is updated. See [Scripted Field Dependencies](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/713588743/Scripted+Field#Dependencies) section for more details.

### Improved return data validation for Scripted Fields

The Scripted fields code editor now include additional feedback for the expected output data type of your script, and whether or not that type matches the configured data type for your field (e.g. string, datetime, number, etc.).

### ‘Status Entered’ fields now support multiple status values

The [Status Entered Time](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/318275598) and [Status Entered by User](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/317653018) custom field types now support selecting multiple status values to be monitored. When selecting multiple status values, a change in status to any of the selected values will trigger an update to the custom field.

### Custom domain support

JMCF for Jira Cloud is now supported when running Jira on custom domains.

## Other Improvements

This release includes other updates and improvements:

- JQL support for ‘Time in Status’ fields has been improved to support a variety of representations of time (e.g. `2days3hours42minutes17seconds` or `2d3h42m17s`), as opposed to searching only by seconds.
- Several UI fixes have been implemented to improve consistency, clarity, and performance.

## Bug Fixes

[Unmapped block: blockCard]