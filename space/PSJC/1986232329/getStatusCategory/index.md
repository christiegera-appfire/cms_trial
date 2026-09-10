# getStatusCategory

## Description

Gets the category of the status for the given issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getStatusCategory(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | string | Yes | Issue to retrieve status information for. |

## Return Type

**String**

Returns the status category name for the issue.

## Example

```javascript
return getStatusCategory("TST-123");
```

## See also