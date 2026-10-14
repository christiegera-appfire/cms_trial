# admDisassociateFieldFromScheme

## Description

Removes a field association from a new-model field scheme. The field must be specified using its internal Jira name, such as 'summary' or 'customfield\_12345'.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDisassociateFieldFromScheme(schemeId, fieldId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [disassociateFieldFromScheme(schemeId, fieldId)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the new-model field scheme. |
| fieldId | string | Yes | The internal name of the field, such as 'summary', 'fixVersion', or 'customfield\_12345'. |

## Return Type

**boolean**

Returns a boolean value.

Returns `true` if the field was disassociated from the scheme.

This routine applies only to new-model field schemes.

## See also