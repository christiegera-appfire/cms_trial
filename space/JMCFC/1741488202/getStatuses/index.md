# getStatuses

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.jira.getStatuses(ids) | **Category** | jira |

## Description

Get Status information using a Status ID.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| ids | Array of strings | Yes | IDs of the Status objects to be returned. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of Status objects.

## Examples

Return Status data for the Status values with IDs of `10000` and `10001`.

```text
await api.jira.getStatuses(["10000","10001"]) // Returns Status objects.
```

You are viewing the documentation for **Jira Cloud**.