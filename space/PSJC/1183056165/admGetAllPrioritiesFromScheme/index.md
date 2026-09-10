# admGetAllPrioritiesFromScheme

## Description

Returns the list of priorities names that exist in the given priority scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPrioritiesFromScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getAllPrioritiesFromScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The name of the priority scheme. |

## Return Type

**string []**

Returns the list of priority names.

## Example

### Example 1

Returns all the priorities from scheme "Default priority scheme"

```javascript
return admGetAllPrioritiesFromScheme("Default priority scheme");
```

Highest|High|Medium|Low|Lowest

## See also