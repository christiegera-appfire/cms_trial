# admDeleteProject

## Description

Deletes the project indicated in the project\_key parameter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeleteProject(project\_key) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deleteProject(project\_key) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project\_key | string | Yes | The project key. The value must be unique. |

## Return Type

**Boolean**

Returns true if the project has been deleted.

## Examples

### Example 1

```javascript
string key_basic = "B"+ count++;
deleteProject(key_basic);
```

### Example 2

```javascript
string key_cmpl = "C"+ count;
deleteProject(key_cmpl);
```

## See also