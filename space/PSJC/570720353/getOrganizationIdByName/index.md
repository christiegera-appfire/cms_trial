# getOrganizationIdByName

## Description

Get the organization id of the provided organization name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getOrganizationIdByName(organizationName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizationName | string | Yes | The name of the organization for which to get the id. |

## Return Type

**number**

Returns null if the organization can not be found.

## Example

```javascript
return getOrganizationIdByName("Test Organization");
```

Result: The string "Test Organization" will be return.

## See also