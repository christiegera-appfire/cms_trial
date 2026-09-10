# admAddProjectsToPriorityScheme

## Description

Adds the given list of project keys to the given priority scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddProjectsToPriorityScheme(schemeName, projectKeys) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addProjectsToPriorityScheme(schemeName, projectKeys) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeName | string | Yes | The name of the priority scheme |
| projectKeys | string [] | Yes | The list of project keys to be added |

## Return Type

**boolean**

Returns true if the projects were added, false otherwise.

## Example

### Example 1

Adds projects with keys "DEMO" and "ITSD" to the priority scheme named "Default priority scheme"

```javascript
admAddProjectsToPriorityScheme("Default priority scheme", {"DEMO", "ITSD"});
```

## See also