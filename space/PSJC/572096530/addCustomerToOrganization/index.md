# addCustomerToOrganization

## Description

Adds an existing customer or a list of customers to a specified organization.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addCustomerToOrganization(customer, organization) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customer | String [] | Yes | The customers' id/s. |
| organization | String | Yes | The organization name. |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Examples

```text
return addCustomerToOrganization({"customer1","customer2"}, "My Organization");
```

```text
return addCustomerToOrganization("customer", "My Organization");
```

## See also