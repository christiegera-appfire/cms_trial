# getCustomerRequests

## Description

Returns a string array of customer requests keys that match the provided parameters. More information about the parameters can be found on Atlassian's rest API: https://developer.atlassian.com/cloud/jira/service-desk/rest/api-group-request/#api-rest-servicedeskapi-request-get

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomerRequests([searchTerm[, requestOwnership[, requestStatus[, approvalStatus[, organizationId[, serviceDeskId, requestTypeId]]]]]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| searchTerm | String | No | Filters customer requests where the request summary matches the searchTerm |
| requestOwnership | String[] | No | Can be "OWNED\_REQUESTS", "PARTICIPATED\_REQUESTS", "ORGANIZATION", "ALL\_ORGANIZATIONS", "APPROVER" |
| requestStatus | String | No | Can be "CLOSED\_REQUESTS", "OPEN\_REQUESTS", "ALL\_REQUESTS" |
| approvalStatus | String | No | Can be "MY\_PENDING\_APPROVAL", "MY\_HISTORY\_APPROVAL" |
| organizationId | Integer | No | Valid only when used with requestOwnership is "ORGANIZATION". |
| serviceDeskId | Integer | No | Filters customer requests by service desk. |
| requestTypeId | Integer | No | Filters customer requests by request type. Note that the serviceDeskId must be specified for the service desk in which the request type belongs. |

## Return Type

**String []**

## Example

```javascript
return getCustomerRequests();
```

Returns a list of keys of all the customer requests.

## See also