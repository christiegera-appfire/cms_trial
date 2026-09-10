# admGetAvailablePrioritiesForScheme

## Description

Returns a list of priorities names available for adding to a given priority scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAvailablePrioritiesForScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getAvailablePrioritiesForScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The name of the priority scheme. |

## Return Type

**string []**

Returns the list of the priority names available to be added.

## Example

### Example 1

Returns all the priority names that can be added to the scheme

```javascript
return admGetAvailablePrioritiesForScheme("New priority scheme");
```

Very Important|Not Important

## See also