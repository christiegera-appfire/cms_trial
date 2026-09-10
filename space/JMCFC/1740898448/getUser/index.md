# getUser

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getUser(accountId) | **Category** | jira |

## Description

Get User data with an Account ID.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| accountId | String | Yes | The user’s Atlassian Account ID. See Determining a User ID, below. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns a User object.

## Examples

Return a string of the **Summary** field value of the current issue.

```text
await api.jira.getUser("632xxxxxxxxxxxxx1c6") // Returns a User object
```

You are viewing the documentation for **Jira Cloud**.

## Determining a User ID

In Jira, there is a distinct difference between a User’s public name and their User ID; a User’s ID is unique identifier associated with their Atlassian account and is unique across all Atlassian products and instances. The best way to find a User’s ID is to check the URL of the User when viewing their details through the User Management tools. To find the ID of a User:

1. Log into Jira as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **User Management**.
3. This will open a new window displaying the Atlassian Administration tools. In the list of **Users**, click the name of the user for whom you need an ID.
4. Check the URL of the page that opens (figure, immediately right). The User’s ID is the last part of the URL, after ‘/users/’.

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud user ID determination guide