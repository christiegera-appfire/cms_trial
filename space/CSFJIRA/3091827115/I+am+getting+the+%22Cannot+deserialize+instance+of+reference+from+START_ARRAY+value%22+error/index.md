# I am getting the "Cannot deserialize instance of reference from START_ARRAY value" error

## Summary

When creating a Salesforce Record from Jira, the user gets the "Error when trying to create Case: Cannot deserialize instance of reference from START\_ARRAY value [line:1, column:38]" error.

![contentId-3091827115](/cms_trial/assets/9e069e69-4b96-45e0-88cf-0dcbb8c25cbd.png)

## Environment

- Jira DC
- Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

After a Salesforce record is created, mapping a multi-picklist Jira field (array <option>) with a Salesforce Id field (reference) triggers this error as both fields are not compatible with each other.

## Workaround

Not applicable.

## Resolution

Review the compatibility of all the mapped fields on the issue type that you are experiencing the error.

1. Go to **Apps** > **Salesforce** > **Bindings** > **Mappings**.
2. Click **Mappings** on the affected Issue type.
3. Open the [Compatibility Matrix](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754374/Jira+Field+Type+to+Salesforce+Field+Type+compatibility) documentation in a new tab.
4. Ensure all the field mappings fulfill the compatibility matrix documentation rulings.
5. The error will be resolved once the incompatible fields are edited or deleted.