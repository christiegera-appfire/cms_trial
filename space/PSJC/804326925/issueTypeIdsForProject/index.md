# issueTypeIdsForProject

## Description

Retrieves the issue type ids for the project with the given key. Returns an array of integers

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueTypeIdsForProject(projectKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | Project key |

## Return Type

**int[]**

The return value is a array containing all the issue type ids available for the given project.

## Example

```javascript
return issueTypeIdsForProject("TST");
```

Result: 10001|10002|10010

## See also