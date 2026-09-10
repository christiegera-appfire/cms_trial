# getGroup

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getGroup(idOrName) | **Category** | jira |

## Description

Get the name and group ID of a Jira Group.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| idOrName | String | Yes | The ID or the name of the group to be returned. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array containing the name and ID of the group.

## Examples

Return the details of the **jira-administrators** group.

```text
await api.jira.getGroup("jira-administrators") // {"name":"jira-administrators","groupId":"xxx"}

// Returns an array with Group data:
//{"name":"jira-administrators","groupId":"3a753xxx-xxx-xxxx47d"}
```

You are viewing the documentation for **Jira Cloud**.