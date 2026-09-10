# getIssueTypesInTheSameContext

## Description

Returns the list of issue types that are included in the same context as the given issue for a certain custom field

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueKey, customFieldId | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | The key of the issue |
| customfieldId | String | Yes | The id of the custom field (format: customfield\_xxxxx) |

## Return Type

**String []**

## Examples

```javascript
getIssueTypesInTheSameContext("ITSD-1", "customfield_10065")
```

Bug|Task|Epic

```javascript
//global, should return []
 return getIssueTypesInTheSameContext("ITSD-1", "customfield_10040");
```

## See also