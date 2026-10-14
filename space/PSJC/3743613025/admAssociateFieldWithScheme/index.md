# admAssociateFieldWithScheme

## Description

Associates a field with a new-model field scheme. The field must be specified using its internal Jira name, such as 'summary' or 'customfield\_12345'. When `workTypeIds` is provided, the association is restricted to the specified work types (issue types).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAssociateFieldWithScheme(schemeId, fieldId, workTypeIds) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [associateFieldWithScheme(schemeId, fieldId, workTypeIds)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the new-model config scheme |
| fieldId | string | Yes | The internal name of the field, such as ‘summary', 'fixVersion', or 'customfield\_12345’ |
| workTypeIds | string[] | No | Array of work type (issue type) ids to restrict the field association to. |

## Return Type

**boolean**

Returns a boolean value.

Returns `true` if the field was associated with the scheme.

This routine applies only to new-model field schemes.

## See also