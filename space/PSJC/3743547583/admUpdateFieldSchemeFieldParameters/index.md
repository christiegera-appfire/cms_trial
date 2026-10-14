# admUpdateFieldSchemeFieldParameters

## Description

Updates field parameters for a field in a new-model field scheme.

Updates field parameters for a field in a new-model field scheme. The field must be specified using its internal Jira name, such as 'summary' or 'customfield\_12345'.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateFieldSchemeFieldParameters(schemeId, fieldId, required, hidden [, description [, rendererType]]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [updateFieldSchemeFieldParameters(schemeId, fieldId, required, hidden [, description [, rendererType]])] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the new-model field scheme. |
| fieldId | string | Yes | The internal name of the field, such as 'summary', 'fixVersion', or 'customfield\_12345'. |
| required | boolean | Yes | If the field is required in the Jira UI. |
| hidden | boolean | Yes | If the field is hidden in the Jira UI. |
| description | string | No | The description of the field. May be empty. |
| rendererType | string | No | The renderer type for the field, such as 'wiki-renderer' or 'text-renderer'. |

## Return Type

**boolean**

Returns a boolean value.

Returns true if the field parameters were updated.

This routine applies only to new-model field schemes.

## See also