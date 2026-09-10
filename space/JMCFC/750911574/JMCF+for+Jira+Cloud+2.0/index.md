# JMCF for Jira Cloud 2.0

This version, released on February 12, 2024, includes the following changes:

## Scripted Fields!

This version of **JMCF for Jira Cloud** includes the release of Scripted Fields! Scripted fields are a new custom field that return values using JavaScript to calculate their output. Your JavaScript can access the values in other fields as well as the Jira APIs. Scripted fields can also be created with dependencies, triggering automatic recalculations if those fields are updated!

Scripted fields currently support a limited set of data types, including:

- **Strings**
- **Datetimes**
- **Numbers**
- **Users** - Returns an Atlassian account ID or a user object.
- **Groups** - Returns a group ID or a Group object.
- **String collection** - Returns a collection of string values.
- **User collection** - Returns a collection of user IDs or user objects.
- **Group collection** - Returns a collection of Group IDs or Group objects.

**Note**: Scripted Fields are currently in limited release. Full availability will occur in a future release.

![Jira Misc Custom Fields (JMCF) Cloud scripted field editor interface](/cms_trial/assets/9f8bd947-a351-45d1-be53-ad5e180bce66.png)

## Other Improvements

This release includes other updates and improvements:

- The **Action menu** in [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) page now includes a **Recalculate** option for individual fields.
- [Time in Status](/cms_trial/space/JMCFC/465633373/Time+in+Status/) custom fields will now update when an issue is opened for viewing, resulting in more accurate updates to those fields.
- Checking the **All** checkbox in the [Create Custom Field](/cms_trial/space/JMCFC/465405703/Create+Custom+Field/) screen selection when the list of screens is filtered will on select the visible screens.
- Custom field names can now include up to 255 characters.

## Bug Fixes

[Unmapped block: blockCard]