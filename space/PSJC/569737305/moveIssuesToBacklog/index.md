# moveIssuesToBacklog

## Description

Moves issues or tasks back to the backlog from their current state or sprint, typically done when they are reprioritized or postponed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | moveIssuesToBacklog(array\_of\_issue\_keys, boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array\_of\_issue\_keys | String [] | Yes | The issue keys you want to move |
| boardId | Integer | Yes | Board id |

## Return Type

**Boolean**

True if the move is ok

## Example

```javascript
string [] issues = "TEST-1|TEST-2|TEST-3|";
return moveIssuesToBacklog(issues, 12345);
```

Returns true if successful, false if otherwise.

## See also