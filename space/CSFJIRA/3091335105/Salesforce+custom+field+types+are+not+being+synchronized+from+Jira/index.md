# Salesforce custom field types are not being synchronized from Jira

## Summary

Salesforce custom fields are not being synchronized from Jira.

## Environment

- All Jira versions
- All Connector versions

## Diagnostics Steps

Not applicable.

## Cause

This is happening most likely because when you synchronize the Jira field to a Salesforce custom field, the value of the field is hitting or exceeding their length limit for the respective Salesforce custom field type.

We are currently working on an improvement to provide a better context when this happens.

## Workaround

Not applicable.

## Resolution

Different Salesforce custom field types have different length limits.

Consult the following table for a selected list of custom field types and their length limits:

| Salesforce Custom Field Type | Length Limit |
| --- | --- |
| **Text** | Up to 255 characters |
| **Text (Encrypted)** | Up to 175 characters |
| **Text Area** | Up to 255 characters |
| **Text Area (Long)** | The default is set to 32,768 characters, but the administrator can change the limit to any length between 256 to 131,072. |
| **URL** | Up to 255 characters |
| **Email** | Up to 80 characters |
| **Phone** | Up to 40 characters |

For more information and for more custom field types and their length limits, check the [Salesforce Documentation on Custom Field Types](https://help.salesforce.com/articleView?id=custom_field_types.htm&type=5).

extension