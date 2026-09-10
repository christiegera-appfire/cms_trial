# getOrganizationNameById

## Description

Sends an invitation to a customer or a list of customers for a specified Service Desk project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getOrganizationNameById(id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Organization Id | Number | Yes | Id of the organization for which to get the name. |

## Return Type

**String**

Returns null if the organization can not be found.

## Example

```javascript
return getOrganizationNameById(101);
```

Result: The string "Test Organization" will be return.

## See also