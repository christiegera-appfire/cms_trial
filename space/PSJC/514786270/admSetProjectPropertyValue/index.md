# admSetProjectPropertyValue

## Description

Saves a property with the specified name and value under the property key
value may be an integer or a string.
The property name will be used to index the array on the return of getProjectPropertyValues
Returns true if that one is saved.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectPropertyValue(projectKey, propertyKey, propertyName, value) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setProjectPropertyValue(projectKey, propertyKey, propertyName, value) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| propertyKey | String | Yes | Property key. |
| propertyName | String | Yes | Property name. |
| value | String / Integer | Yes | The value set for the property on the provided project. |

## Return Type

**Boolean (true/false)**

Returns true if the property is saved and false otherwise.

## Examples

```javascript
admSetProjectPropertyValue("TEST", "myprop", "custom_int", 23)
```

```javascript
admSetProjectPropertyValue("TEST", "myprop", "custom_str", "test_value")
```

## See also