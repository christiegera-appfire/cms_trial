# admGetAllInactiveAccounts

## Description

Gets all the users accounts, inactive only. Care should be exercised because it might return a large number of objects.
NOTE: Requires admin token to be set!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllInactiveAccounts() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use "adm"; allInactiveAccounts();] |

## Return Type

[**JUser []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JUser [] users = admGetAllInactiveAccounts();
```

Returns all accounts, inactive

## See also