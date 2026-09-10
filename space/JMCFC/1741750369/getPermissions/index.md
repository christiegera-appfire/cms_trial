# getPermissions

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getPermissions(string[permissionKey, ..]) | **Category** | jira |

## Description

Get the details for global, project, and app-created permissions using their permission key.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| permissionKeys | Array of strings | Yes | One or more permission keys.  To find all permission keys, output the results of [getAllPermissions](/cms_trial/space/JMCFC/1742045213/getAllPermissions/) to a custom field or the console. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of requested Permission objects.

## Examples

Return a string of the **Summary** field value of the current issue.

```text
await api.jira.getPermissions(["ADD_COMMENTS","ARCHIVE_ISSUES"])

//[
//    {
//      "key":"ADD_COMMENTS",
//      "name":"Add Comments",
//      "type":"PROJECT",
//      "description":"Ability to comment on issues."
//    },
//    {
//      "key":"ARCHIVE_ISSUES",
//      "name":"Archive Issues",
//      "type":"PROJECT",
//      "description":"Ability to archive issues."
//    }
//]
```

You are viewing the documentation for **Jira Cloud**.