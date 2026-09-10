# getGroupUsers

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getGroupUsers(idOrName) | **Category** | jira |

## Description

Get the users of a Jira Group.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| idOrName | String | Yes | The ID or the name of the group to be returned. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of Jira User objects.

## Examples

Return the details of the **jira-servicedesk-users** group.

```text
await api.jira.getGroupUsers("jira-servicedesk-users")

// Returns an array of User objects.
 [
 {
    "self":"https://api.atlassian.com/ex/jira/xxx/rest/api/2/user?accountId=xxx",
    "accountId":"xxx",
    "avatarUrls":{
      ...
    },
    "displayName":"Jess Smith",
    "active":true,
    "timeZone":"America/Los_Angeles",
    "accountType":"atlassian"
  },
  {
    "self":"https://api.atlassian.com/ex/jira/xxx/rest/api/2/user?accountId=xxx",
    "accountId":"xx",
    "avatarUrls":{
      ...
    },
    "displayName":"Michael Jones",
    "active":true,
    "timeZone":"America/Los_Angeles",
    "accountType":"atlassian"
    },
    ...  
  ]
```

You are viewing the documentation for **Jira Cloud**.