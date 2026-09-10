# getRequestTypeByIdForServiceDesk

## Description

Returns a JSMRequestType structure for the provided request type id, from the service desk mentioned.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestTypeByIdForServiceDesk(serviceDeskId, requestTypeId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk id. |
| requestTypeId | Integer | Yes | The request type id |

## Return Type

[**JSMRequestType**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a JSMRequestType structure containing information about the request type.

## Example

```javascript
JSMRequestType requestType = getRequestTypeByIdForServiceDesk(1, 25);
return requestType;
```

## See also