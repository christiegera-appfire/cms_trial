# admGetAllAccounts

## Description

Gets all the users accounts. Both active and inactive accounts. Care should be exercised because it might return a large number of objects.
NOTE: Requires admin token to be set!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllAccounts() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use "adm"; allAccounts();] |

## Return Type

[**JUser []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JUser [] users = admGetAllAccounts();
```

Returns all accounts

## See also