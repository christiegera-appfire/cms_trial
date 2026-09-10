# admGetIssueTypesFromScheme

## Description

Returns an array of issue type ids for a scheme scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetIssueTypesFromScheme(id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | issueTypesFromScheme(id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| id | int | Yes | Id of the issue type scheme. |

## Return Type

**int []**

Returns the issue types from a scheme.

## Example

```javascript
return admGetIssueTypesFromScheme(10204);
```

## See also