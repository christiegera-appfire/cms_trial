# admSetPriorityScheme

## Description

Updates the project priority scheme to the given one.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetPriorityScheme(projectKey, schemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setPriorityScheme(projectKey, schemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key |
| schemeName | string | Yes | The name of the priority scheme |

## Return Type

**boolean**

Returns true if the scheme was set, false otherwise.

## Example

### Example 1

Sets the "New priority scheme" as the priority scheme of project "TEST".

```javascript
admSetPriorityScheme("TEST", "New priority scheme")
```

## See also