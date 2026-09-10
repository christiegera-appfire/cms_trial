# getCustomerObject

## Description

Returns a JUser structure or null

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomersObject(serviceDeskId, displayNameOrNameOrEmail, customerAccountId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The ID of the service desk for which the customers will be retrieved |
| displayNameOrNameOrEmail | string | No | A string that fully or partially describes the customer's name, or display name, or email - used to improve performance when searching for the customer |
| customerAccountId | string | Yes | The customer's account id |

## Return Type

[**JUser**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```text
return getCustomerObject(1, "John", "qm:1bf61d2c-45e8-4h07-a3c1-7d56421c41eb:d74883xd-61fb-4f43-8c02-a2f6cfe7d3f5");
```

Returns a JUser structure or null, if the customer having that specific account id is not found.

## See also