# admGetAllPrioritySchemes

## Description

Returns the list of priority scheme names that exist in the Jira environment. The routine is an alias for admGetAllPrioritiesScheme routine.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPrioritySchemes() | **Package** | adm |
| **Alias** | admGetAllPrioritiesScheme() | **Pkg Usage** | getAllPrioritySchemes() |

## Return Type

**string []**

Returns the list of the priority schemes names.

## Example

### Example 1

Returns all the priorities scheme names

```javascript
return admGetAllPrioritySchemes();
```

Default priority scheme|Test scheme|New scheme

## See also