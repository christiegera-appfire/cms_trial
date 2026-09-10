# admDeleteProjectProperty

## Description

Simply deletes the property key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteProjectProperty(projectKey, propertyKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteProjectProperty(projectKey, propertyKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |
| propertyKey | String | Yes | Property key. |

## Return Type

**Boolean (true/false)**

Returns true if the property is deleted and false otherwise.

## Example

```javascript
admDeleteProjectProperty("TEST", "myprop")
```

## See also