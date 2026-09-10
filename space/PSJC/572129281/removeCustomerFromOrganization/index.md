# removeCustomerFromOrganization

## Description

Removes a customer or a list of customers from a specified organization.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeCustomerFromOrganization(customer, organization) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customer | String [] | Yes | The customers' username/s (or id/s for cloud) |
| organization | String | Yes | The organization name. |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Example

```text
return removeCustomerFromOrganization({"customer1@email.com", "customer2@email.com"}, "My Organization");
```

## See also