# admDeleteCustomFieldOptions

## Description

Deletes options with the provided ids from the custom field. This function only handles custom fields of the following types: single select, multi select, radio buttons and checkboxes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteCustomFieldOptions(fieldNameOrId, optionsIds[, projectIssueTypesNames][, context]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | delCFOptions(fieldNameOrId, optionsIds[, projectIssueTypesNames][, context]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldNameOrId | String | Yes | Name or id of the custom field. |
| optionsIds | String[] | Yes | Ids of the options to be deleted. |
| projectIssueTypesNames | JProjectIssueTypes [] | No | An array of JProjectIssueTypes structures, representing project keys/issue types mappings. (The context from which to delete the options) - to be used alternatively with “context” parameter |
| context | String | No | The name or id of the context - to be used alternatively with the “projectIssueTypesNames” parameter |

## Return Type

**boolean**

The returned value has no meaning.

## Example

### Example

Deletes the option with id 10080 from checkbox custom field, using the context for project with key TP and issue types Bug and Task.

```javascript
JProjectIssueTypes[] projectIssueTypesNames;
JProjectIssueTypes map;
map.projectKey = "TP";
map.issueTypesNames = {"Task", "Bug"};
projectIssueTypesNames = arrayAddElement(projectIssueTypesNames, map);
return admDeleteCustomFieldOptions("checkbox", "10080", projectIssueTypesNames);
```

Alternatively, the context can be used:

```javascript
JProjectIssueTypes[] projectIssueTypesNames;
string context = "TP_Context";
return admDeleteCustomFieldOptions("checkbox", "10080", context);
```

## See also