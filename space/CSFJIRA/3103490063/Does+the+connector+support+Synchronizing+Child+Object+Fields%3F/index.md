# Does the connector support Synchronizing Child Object Fields?

## Purpose

In Salesforce you may sometimes find the need to create a custom formula field in order to return specific data from a Child Object. A formula that returns related fields from a Child Object may look like this:

“Case\_\_r.CaseNumber”

This would return the Case Number of the related Child Case object. Also, please note that a custom "relationship" field ends in "\_\_r" and not "\_\_c" as most custom fields.

## Answer

Although the connector does support custom fields, it **does not support** custom "relationship" fields.

- Custom fields whose API names end in "\_\_c" are standard custom fields whose values pulled directly from the parent record which the connector is able to provide to Jira without issues.
- Custom fields whose API names end in "\_\_r" are custom "relationship" fields. These fields cannot be synched as the field where the information is being pulled is a field from a different object altogether and not part of the current associated field.