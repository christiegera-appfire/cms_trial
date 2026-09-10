# setUserProperty

## Description

Sets properties of users. If the property does not exist, it will be created.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setUserProperty(user, propertyKey, propertyValue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or userkey to get the property for. |
| propertyKey | String | Yes | Key of the property. |
| propertyValue | String | Yes | Value to set for the property. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
setUserProperty("testuser", "phone", "987 654 3210");
```

## See also