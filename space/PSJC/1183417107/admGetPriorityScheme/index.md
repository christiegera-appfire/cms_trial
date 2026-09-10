# admGetPriorityScheme

## Description

Returns the priority scheme name for the given project key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetPriorityScheme(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getPriorityScheme(projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key. |

## Return Type

**string**

Returns the priority scheme name.

## Example

### Example 1

Returns the priority scheme name for project "TEST"

```javascript
return admGetPriorityScheme("TEST");
```

New priority scheme

## See also