# getAllPermissions

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getAllPermissions() | **Category** | jira |

## Description

Get an array of all Jira Permissions for your instance.

## Parameters

None.

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of Permission objects.

## Examples

Return all permissions.

```text
await api.jira.getAllPermissions() 

//[
//   { "key":"ADD_COMMENTS",
//     "name":"Add Comments",
//     "type":"PROJECT",
//     "description":"Ability to comment on issues."
//   },
//   ...
//]
```

You are viewing the documentation for **Jira Cloud**.