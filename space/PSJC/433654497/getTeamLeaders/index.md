# getTeamLeaders

## Description

Returns the team leaders user keys on the specified project. All the component leads.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getTeamLeaders(project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project key | String | Yes | Key of the selected project. |

## Return Type

**String []**

Returns a list of all the component leads from all the components in the specified project.

## Example

```javascript
//team leaders of the current project are TL1, TL2
string[] team_leaders;
team_leaders = getTeamLeaders(project);
```

Result: |TL1|TL2|

## See also