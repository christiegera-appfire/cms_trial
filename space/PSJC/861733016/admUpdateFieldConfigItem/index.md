# admUpdateFieldConfigItem

## Description

Updates the description and flags for a field configuration item; field must be an internal field name, like 'summary' or 'customfield\_12345'

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateFieldConfigItem(fieldConfigId, field, description, required, hidden) or admUpdateFieldConfigItem(fieldConfigId, field, description, required, hidden, renderer) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [updateFieldConfigItem(fieldConfigId, field, description, required, hidden), updateFieldConfigItem(fieldConfigId, field, description, required, hidden, renderer)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldConfigId | int | Yes | Id of the field configuration |
| field | string | Yes | The name of the field, internal to Jira. 'summary', 'fixVersion', 'customfield\_12345' are a few examples |
| description | string | Yes | The description of the field. May be empty |
| required | boolean | Yes | If field is required in the Jira UI |
| hidden | boolean | Yes | If field is hidden in the Jira UI |

### Or

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldConfigId | int | Yes | Id of the field configuration |
| field | string | Yes | The name of the field, internal to Jira. 'summary', 'fixVersion', 'customfield\_12345' are a few examples |
| description | string | Yes | The description of the field. May be empty |
| required | boolean | Yes | If field is required in the Jira UI |
| hidden | boolean | Yes | If field is hidden in the Jira UI |
| renderer | string | Yes | Currently, it supports changing the text field types from 'wiki-renderer' to 'text-renderer' and the other way around - in certain cases. |

## Return Type

**boolean**

Returns true if the field configuration item is updated

## See also