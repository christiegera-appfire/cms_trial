# getServiceDeskQueue

## Description

Returns a JSMQueue structure.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getServiceDeskQueue(serviceDeskId, queueId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk id. |
| queueId | Integer | Yes | The queue id. |

## Return Type

[**JSMQueue**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a JSMQueue structure.

## Example

```javascript
JSMQueue queue = getServiceDeskQueue(1, 1);
return queue;
```

## See also