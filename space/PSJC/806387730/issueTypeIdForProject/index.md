# issueTypeIdForProject

## Description

Retrieves the issue type id for the project with the given key and issue type.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueTypeIdForProject(projectKey, issueTypeName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | Project key |

## Return Type

**int**

The return value is an integer, negative of not set if the issue type is not found.

## Example

```javascript
return issueTypeIdForProject("TST", "Feature Request");
```

Result: 10034

## See also