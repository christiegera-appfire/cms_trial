# createRequestTypeInServiceDesk

## Description

Creates a new request type in the provided service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createRequestTypeInServiceDesk(serviceDeskId, name, issueTypeId[, description, helpText]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The ID of the service desk where the customer request type is to be created. |
| name | string | Yes | Name of the request type on the service desk. |
| issueTypeId | number | Yes | ID of the issue type of the request type. The issue type should already exists. |
| description | string | No | Description of the request type on the service desk. |
| helpText | string | No | Help text for the request type on the service desk. |

## Return Type

**string**

The id of the newly added request type if it gets created.

## Example

```javascript
return createRequestTypeInServiceDesk(1, "TestRequest", 10011);
```

## See also