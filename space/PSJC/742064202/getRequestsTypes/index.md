# getRequestsTypes

## Description

Returns an array of JSMRequestType containing all the Request Type data, or only those that ar matching the provided searchQuery and sericeDesksIds.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestsTypes([searchQuery[, serviceDesksIds]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| searchQuery | String | No | The string to be used to filter the results. |
| serviceDesksIds | String[] | No | The service desks ids for which to get the results. |

## Return Type

[**JSMRequestType []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of JSMRequestType containing information about the request types.

## Example

Use the following code to get ALL request types.

```javascript
JSMRequestType[] requestTypes = getRequestsTypes(); 
 return requestTypes;
```

## See also