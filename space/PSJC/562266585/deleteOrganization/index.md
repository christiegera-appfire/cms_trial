# deleteOrganization

## Description

Removes a customer organization.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteOrganization(organization) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organization | String | Yes | The organization name. |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Example

```javascript
return deleteOrganization("My Organization");
```

## See also