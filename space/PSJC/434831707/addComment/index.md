# addComment

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addComment(issue, username, comment[, securityLevel]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Posts a comment on the specified issue on behalf of the specified user. Returns a number representing the id of the comment.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |
| user name | String | Yes | User name of the selected user. |
| comment | String | Yes | Comment that will be posted on the selected issue. |
| securityLevel | String | No | Security level of comment. Only project roles are accepted for security level. |

## Return Type

**Number**

The returned number represents the id of the comment.

## Examples

### Example 1

```javascript
addComment(key, currentUser(), "I have executed a transition.");
```

Adds a comment on the current issue, on behalf of the current user.

### Example 2

```javascript
addComment(key, currentUser(), "you can't see me", "Administrators");
```

Adds a comment on the current issue, on behalf of the current user, viewable only by "Administrators".

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]