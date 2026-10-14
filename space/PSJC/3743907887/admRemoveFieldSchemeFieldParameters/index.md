# admRemoveFieldSchemeFieldParameters

## Description

Removes field parameter overrides for a field in a new-model field scheme. The field must be specified using its internal Jira name, such as 'summary' or 'customfield\_12345'.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveFieldSchemeFieldParameters(schemeId, fieldId, parameterNames, workTypeIds) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [removeFieldSchemeFieldParameters(schemeId, fieldId, parameterNames, workTypeIds)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the new-model field scheme. |
| fieldId | string | Yes | The internal name of the field, such as 'summary', 'fixVersion', or 'customfield\_12345'. |
| parameterNames | string[] | Yes | Array of parameter names to remove, such as 'isRequired', 'isHidden', 'description', or 'rendererType'. |
| workTypeIds | string[] | Yes | Array of work type (issue type) ids for which the parameter overrides should be removed. |

## Return Type

**boolean**

Returns a boolean value.

Returns true if the field parameter overrides were removed.

**Note**: This routine applies only to new-model field schemes.

## See also