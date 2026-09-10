# admClearProjectPropertyValue

## Description

Clears a property with the specified name and value under the property key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admClearProjectPropertyValue(projectKey, propertyKey, propertyName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | clearProjectPropertyValue(projectKey, propertyKey, propertyName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| propertyKey | String | Yes | Property key. |
| propertyName | String | Yes | Property name. |

## Return Type

**Boolean (true/false)**

Returns true if the property value is cleared and false otherwise.

## Example

```javascript
admClearProjectPropertyValue("TEST", "myprop", "custom_int")
```

## See also