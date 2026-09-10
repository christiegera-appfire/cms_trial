# createCustomerRequest

## Description

Creates a customer request and returns the newly created request as a structure.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createCustomerRequest(serviceDeskId, requestTypeId, summary, [description [,requestFieldValues [,requestParticipants [,raiseOnBehalfOf [,channel]]]]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | String | Yes | The service desk id. |
| requestTypeId | String | Yes | The request type id. |
| summary | String | Yes | The summary of the new request. |
| description | String | No | The description of the new request. |
| requestFieldValues |  | No | Mappings for the custom fields of the issue that will be created. If you provide a new summary/description here, it will overwrite the parameters already provided. |
| requestParticipants | String[] | No | Users account ids for the user that will participate on the newly created request. Is not available to Users who have the customer permission only or if the feature is turned off for customers. |
| raiseOnBehalfOf | String | No | Create the request in the name of another user (user account id should be used). Is not available to Users who have the customer permission only. |
| channel | String | No | Shows extra information for the request channel. |

## Return Type

[**JSMCustomerRequest**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JSMCustomerRequest customerRequest = createCustomerRequest(1, 6, "Request JSD help via Power Scripts", "I need a new *mouse* for my PC");
return customerRequest;
```

Creates a customer request and returns the newly created request as a structure.

## See also