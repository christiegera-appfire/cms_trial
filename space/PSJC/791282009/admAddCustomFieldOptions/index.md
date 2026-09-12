# admAddCustomFieldOptions

## Description

Adds new custom field options (JCustomFieldOption[]) to options list for the specified context. If the context does not exist, it will NOT be created. This function only handles custom fields of the following types: single select, multi select, radio buttons and checkboxes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddCustomFieldOption(fieldNameOrId, options[, projectIssueTypesNames][, context]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addCFOption(fieldNameOrId, options[, projectIssueTypesNames][, context]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldNameOrId | String | Yes | Name or id of the custom field. |
| options | JCustomFieldOption[] | Yes | Options to be added, as a JCustomFieldOption array. The id parameter is not needed and will be ignored, value can't be empty. |
| projectIssueTypesNames | JProjectIssueTypes [] | No | An array of JProjectIssueTypes structures, representing project keys/issue types mappings. (The context where to add the options) - to be used alternatively with “context” parameter |
| context | String | No | The name or id of the context - to be used alternatively with the “projectIssueTypesNames” parameter |

## Return Type

[**JCustomFieldOption[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JCustomFieldOption structures representing the options added to the specified custom field.

## Example

### Example

Adding an option to the checkbox custom field, using the context for project with key TP and issue types Bug and Task.

```javascript
JProjectIssueTypes[] projectIssueTypesNames;
JProjectIssueTypes map;
map.projectKey = "TP";
map.issueTypesNames = {"Task", "Bug"};
projectIssueTypesNames = arrayAddElement(projectIssueTypesNames, map);
JCustomFieldOption[] optionsToBeAdded;
JCustomFieldOption option;
option.value = "added from SIL";
optionsToBeAdded = arrayAddElement(optionsToBeAdded, option);
JCustomFieldOption[] customFieldOptions = admAddCustomFieldOptions("checkbox", optionsToBeAdded, projectIssueTypesNames);
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
JCustomFieldOption[] optionsToBeAdded;
JCustomFieldOption option;
option.value = "added from SIL";
optionsToBeAdded = arrayAddElement(optionsToBeAdded, option);
JCustomFieldOption[] customFieldOptions = admAddCustomFieldOptions("checkbox", optionsToBeAdded, context);
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

The result will contain the options added, now with ID's.

## See also