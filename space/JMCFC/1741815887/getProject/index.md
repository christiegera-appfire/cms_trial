# getProject

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getProject(idOrKey) | **Category** | jira |

## Description

Get the details for a project using its ID or Key.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| idOrKey | String | Yes | Project ID or key. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns a Project object.

## Examples

Return information about the **DEV** project.

```text
await api.jira.getProject("DEV") //Returns Project object.
```

Return information about project with the ID of **10115**.

```text
await api.jira.getProject("10115") // Returns Project object.
```

You are viewing the documentation for **Jira Cloud**.