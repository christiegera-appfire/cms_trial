# isTeamLeader

## Description

Verifies if the specified user is a team leader on the project (if it is a component lead).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isTeamLeader(project, username) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project key | String | Yes | Key of the selected project. |
| user name | String | Yes | User name of user that is verified. |

## Return Type

**Boolean**

A "true" return value means that the specified user is component lead on at least one component of the specified project.

## Example

```javascript
//Team leaders of the current project are : TM1 and TM2
isTeamLeader(project, currentUser());
```

Returns "true" if the current user is TM1 or TM2 and "false" if the current user is other than TM1 or TM2.

## See also