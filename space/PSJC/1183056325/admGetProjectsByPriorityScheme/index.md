# admGetProjectsByPriorityScheme

## Description

Returns a list of project keys by the given priority scheme name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectsByPriorityScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getProjectsByPriorityScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The priority scheme name. |

## Return Type

**string []**

Returns a list of project keys.

## Example

### Example 1

Returns project keys from the priority scheme "New priority scheme"

```javascript
return admGetProjectsByPriorityScheme("New priority scheme");
```

DEMO|ITSD|TEST

## See also