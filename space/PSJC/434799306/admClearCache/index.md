# admClearCache

## Description

Clears the internal cache. Clears the cache after you have performed a modification directly into the Jira database (something which is **not** recommended!), allowing Jira to pick up the change.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admClearCache() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | clearCache() |

## Return Type

**Boolean (true/false)**

Always uninitialized (false). You can safely ignore the return value of this function.

## Example

```javascript
admClearCache();
```

## See also