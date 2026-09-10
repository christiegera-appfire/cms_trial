# getRequestTypesForServiceDesk

## Description

Returns an array of JSMRequestType containing all the Request Type data for the provided parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestTypesForServiceDesk(serviceDeskId [,searchQuery [, groupId]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | Integer | Yes | The service desk id. |
| searchQuery | String | No | The string to be used to filter the results. |
| groupId | integer | No | Filters results to those in a customer request type group. |

## Return Type

[**JSMRequestType []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JSMRequestType containing information about the request types.

## Example

```javascript
JSMRequestType[] requestTypes = getRequestTypesForServiceDesk(1);
return requestTypes;
```

## See also