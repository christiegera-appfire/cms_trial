# getIssueTypesInCustomFieldContext

## Description

Returns the list of issue types for a certain custom field context

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueTypesInCustomFieldContext(customFieldId, context) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customfieldId | String | Yes | The id of the custom field (format: customfield\_xxxxx) |
| context | String | Yes | The id or the name of the custom field context |

## Return Type

**String []**

## Examples

```javascript
runnerLog(getIssueTypesInCustomFieldContext("customfield_10041", "10169"));
```

Bug|Task|Epic

```javascript
//global, should return []
 return getIssueTypesInCustomFieldContext("customfield_10040", "10167");
```

## See also