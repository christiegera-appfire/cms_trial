# getProjects

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getProjects(idsOrKeys) | **Category** | jira |

## Description

Get the value of a field for the given Jira issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| idsOrKeys | Array of strings | Yes | One or more Project IDs or keys. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of Project objects.

## Examples

Return the details of requested projects.

```text
await api.jira.getProjects(["SPA","EPA"]) // Returns an array of Project objects.
```

You are viewing the documentation for **Jira Cloud**.