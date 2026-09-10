# getTimeSpent

## Description

Gets the time spent (logged) on an issue by a certain user or group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getTimeSpent(issueKey, user\_or\_group) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issuekey | String | Yes | Key of the issue. |
| user\_or\_group | String | Yes | Username or group name. |

## Return Type

**Interval**

Returns an interval that represents the sum of all the worklogs of the specified user or members of the specified group on the issue.

## Examples

### Example 1

```javascript
getTimeSpent("PRJ-32", "jira-users");
```

Returns: The sum of the worklogs of all the members of "jira-users" on issue PRJ-32: 4d 5h.

### Example 2

```javascript
getTimeSpent("PRJ-32", "testuser");
```

Returns: The sum of the worklogs of the user "testuser" on issue PRJ-32: 2h.

## See also