# Scripted Custom Field Triggers

It is important to understand how the scripts for the Scripted Custom Fields are triggered. The scripts are not simply executed every time the field is viewed, a change must occur to let the field know (trigger) that it should be re-executed and the values recalculated.

## Events

The following events/triggers will cause a custom field script to be executed:

- attachment created
- attachment deleted
- comment created
- comment updated
- comment deleted
- issue created
- issue updated
- link created (if links trigger is selected in configuration)
- link deleted (if links trigger is selected in configuration)
- subtask created
- worklog created
- worklog updated
- worklog deleted

This means that almost any change to the issue will cause the script to be executed and the field re calculated.

## Relationship Triggers

Not only that but updates to issues with certain relationship will trigger fields to trigger. The following types of relationships will cause scripts to be executed.

- If one of the above triggers is activated for a sub-task, the Scripted Custom Field will also be triggered for the parent issue.
- If one of the above triggers is activated for a regular issue type that belongs to an Epic, the Scripted Custom Field will also be triggered for that parent Epic.
- If one of the above triggers is activated for an issue that has links, the Scripted Custom Field will also be triggered for the linked issues as well

These special relationship triggers ensure that scripted fields on the related issues will contain accurate data in the event that the scripts use data from the updated issue.

## Things to consider

When adding new Scripted Custom Fields the values may not be calculated right away. A change to the issue or a related issue must occur in order for the value to be populate.