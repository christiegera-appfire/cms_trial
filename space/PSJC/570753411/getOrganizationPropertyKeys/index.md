# getOrganizationPropertyKeys

## Description

Get the organization properties keys the provided organization id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getOrganizationPropertyKeys(organizationId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizationId | number | Yes | Id of the organization for which to get properties keys. |

## Return Type

**string []**

Returns null if the organization can not be found.

## Example

```javascript
return getOrganizationPropertyKeys(13);
```

Result: The string [] "TestProperty1|TestProperty2" will be return.

## See also