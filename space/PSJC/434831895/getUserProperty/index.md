# getUserProperty

## Description

Retrieves properties of users.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUserProperty(user, property) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or userkey to get the property for. |
| property | String | Yes | Key of the property. |

## Return Type

**String**

Returns the value of the specified property. If the user does not have the property, it will return an empty string.

## Example

```javascript
return getUserProperty("testuser", "phone");
```

The look-up is first made after the userkey, then after the username.

## See also