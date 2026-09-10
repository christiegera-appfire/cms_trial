# Unable to add/delete neither bindings nor mappings for a specific project

## Summary

Unable to add/delete either bindings or mappings. After clicking on the **Save** button, it just keeps loading without saving the changes:

## Environment

- Any JIRA version
- Any version of the connector

## Diagnostics Steps

Error (401) can be seen from the network console on Chrome when trying to save the changes.

## Cause

The current user does not have **Administer Projects** permission for the Jira project that is being added/deleted from the bindings or the mappings.

## Workaround

Not applicable.

## Resolution

Grant the **Administer Projects** permission to the user who needs to add the new binding or mapping.