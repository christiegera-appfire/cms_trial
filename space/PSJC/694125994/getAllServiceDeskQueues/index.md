# getAllServiceDeskQueues

## Description

Returns an array of JSMQueue structures.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllServiceDeskQueues(serviceDeskId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk id. |

## Return Type

[**JSMQueue []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JSMQueue structures.

## Example

```javascript
JSMQueue[] queues = getServiceDeskQueues(1);
return queues;
```

## See also