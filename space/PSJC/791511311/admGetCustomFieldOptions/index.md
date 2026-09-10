# admGetCustomFieldOptions

## Description

Retrieves the JCustomFieldOption array of a custom field. If projectIssueTypesNames is empty or is not provided, the global context is going to be used. If the filterDisabled parameter is used set to true, all disabled options are excluded from the result. In case of cascade selects, the optionId represents the id of the parent option. This function only handles custom fields of the following types: single select, multi select, radio buttons, checkboxes and cascading selects.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetCustomFieldOptions(fieldNameOrId[, projectIssueTypesNames[, filterDisabled]][, context, [, filterDisabled]]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getCFOptions(fieldNameorId[, projectIssueTypesNames[, filterDisabled]][, context, [, filterDisabled]]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldNameOrId | String | Yes | Name or id of the custom field. |
| projectIssueTypesNames | JProjectIssueTypes [] | No | An array of JProjectIssueTypes structures, representing project keys/issue types mappings. (The context from which to get the options) - to be used alternatively with “context” parameter |
| context | String | No | The name or id of the context - to be used alternatively with the “projectIssueTypesNames” parameter |
| filterDisabled | Boolean | No | Filter for disabled options. |

## Return Type

[**JCustomFieldOption[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JCustomFieldOption structures representing the options of the specified custom field.

## Example

### Example

Get the options of the checkbox custom field, using the context for project with key TP and issue types Bug and Task.

```javascript
JProjectIssueTypes[] projectIssueTypesNames;
JProjectIssueTypes map;
map.projectKey = "TP";
map.issueTypesNames = {"Task", "Bug"};
projectIssueTypesNames = arrayAddElement(projectIssueTypesNames, map);
JCustomFieldOption[] customFieldOptions = admGetCustomFieldOptions("checkbox", projectIssueTypesNames);
int indexCC = 1;
for(JCustomFieldOption option in customFieldOptions) {
    runnerLog("---option " + indexCC + "---");    
    runnerLog("id = " + option.id);
    runnerLog("optionId = " + option.optionId);
    runnerLog("value = " + option.value);    
    runnerLog("disabled = " + option.disabled);    
    indexCC = indexCC + 1;
}
runnerLog("_________________________________________________");
```

Alternatively, the context can be used:

```javascript
JProjectIssueTypes[] projectIssueTypesNames;
string context = "TP_Context";
JCustomFieldOption[] customFieldOptions = admGetCustomFieldOptions("checkbox", context);
int indexCC = 1;
for(JCustomFieldOption option in customFieldOptions) {
    runnerLog("---option " + indexCC + "---");    
    runnerLog("id = " + option.id);
    runnerLog("optionId = " + option.optionId);
    runnerLog("value = " + option.value);    
    runnerLog("disabled = " + option.disabled);    
    indexCC = indexCC + 1;
}
runnerLog("_________________________________________________");
```

Possible result as a string:

```javascript
---option 1---
id = 10044
optionId = 
value = option1
disabled = false
---option 2---
id = 10045
optionId = 
value = option2
disabled = true
```

## See also