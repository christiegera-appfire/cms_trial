# createCustomer

## Description

Creates a Service Desk customer. The newly created customer is not added to any JSD project, however he/she can raise request against unrestricted JSD projects.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createCustomer(displayName, email) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| displayName | String | Yes | The displayed name of the customer. |
| email | String | Yes | The email address of the customer. |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Example

```javascript
return createCustomer("John Doe", "john.doe@email.com");
```

## See also