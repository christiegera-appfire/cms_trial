# getAvailableTransitions

## Description

Retrieves all available transitions for the current user from the given issue state.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAvailableTransitions(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |

## Return Type

**String []**

The return value is an array of strings, containing the names of the available transitions for the current user from the given issue state.

## Example

Issue DEMO-1 has status Open and is assigned to test user. Currently logged in user is admin. Start Progress transition is restricted only to assignee, therefore it will be omitted.

```javascript
return getAvailableTransitions("DEMO-1");
```

Result: Resolve Issue|Close Issue.

## See also