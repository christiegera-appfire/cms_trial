# admRemoveIssueTypeFromScheme

## Description

Removes an issue type ids for a scheme scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveIssueTypeFromScheme(schemeId, issueTypeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeIssueTypeFromScheme(schemeId, issueTypeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the issue type scheme. |
| issueTypeId | int | Yes | Id of the issue type. |

## Return Type

**boolean**

Returns true if the issue type was removed.

## Example

```javascript
admRemoveIssueTypeFromScheme(10204, 10008);
```

## See also