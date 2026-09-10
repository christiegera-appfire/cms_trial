# getIssuesInQueueRoutine

## Description

Returns an array of issue keys for queueId from the provided service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssuesInQueueFunction(serviceDeskId, queueId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk from where to take the issues. |
| queueId | Integer | Yes | The queue from where to take the issues |

## Return Type

**string []**

Returns null if the service desk or the queue can not be found.

## Example

```javascript
return getIssuesInQueueFunction(1, 1);
```

## See also