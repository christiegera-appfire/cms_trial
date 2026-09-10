# getContextsForCustomField

## Description

Returns the list of contexts for a certain custom field

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getContextsForCustomField(customfieldId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customfieldId | String | Yes | The id of the custom field (format: customfield\_xxxxx) |

## Return Type

**String []**

## Example

```javascript
getContextsForCustomField("customfield_10041")
```

Default Configuration Scheme for cb cf|ctx1|ctx2

## See also