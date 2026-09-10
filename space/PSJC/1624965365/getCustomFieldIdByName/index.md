# getCustomFieldIdByName

## Description

Returns a list of ids for all custom fields with the given name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomFieldIdByName(customfieldName); | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customfieldName | String | Yes | Name of custom field to retrieve ids for. |

## Return Type

**String []**

Returns an array of custom field ids.

## Examples

### Example

```javascript
return getCustomFieldIdByName("My Custom Field");
```

Returns: "customfield\_10101"

## See also