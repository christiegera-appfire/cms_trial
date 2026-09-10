# admGetAllActiveAccounts

## Description

Gets all the users accounts, active only. Care should be exercised because it might return a large number of objects.
NOTE: Requires admin token to be set!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllActiveAccounts() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use "adm"; allActiveAccounts();] |

## Return Type

[**JUser []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JUser [] users = admGetAllActiveAccounts();
```

Returns all accounts, active

## See also