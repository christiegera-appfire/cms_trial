# admGetProjectPropertyValues

## Description

Returns an array of indexed property keys. You may use the property names to navigate the array i.e. it is indexed by property names

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectPropertyValues(projectKey, propertyKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getProjectPropertyValues(projectKey, propertyKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| propertyKey | String | Yes | Property key. |

## Return Type

**string []**

Returns an array of indexed property keys.

## Example

```javascript
admGetProjectPropertyValues("TEST", "myprop")
```

## See also