# getProjectsInCustomFieldContext

## Description

Returns the list of projects for a certain custom field context

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectsInCustomFieldContext(customFieldId, context) | **Package** |  |
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
return getProjectsInCustomFieldContext("customfield_10041", "10169");
```

ITSD|TEST

```javascript
//global, should return []
 return getProjectsInCustomFieldContext("customfield_10040", "10167");
```

## See also