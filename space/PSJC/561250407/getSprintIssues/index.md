# getSprintIssues

## Description

Retrieves the list of issues or tasks associated with a specific sprint.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getSprintIssues(sprintId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprintId | integer | Yes | The sprint |

## Return Type

**String**

Array of issue keys

## Example

```javascript
string [] sprintIssues = getSprintIssues(12345);
```

## See also