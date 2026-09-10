# addIssuesToEpic

## Description

Links multiple issues to a specific epic, making it clear that these issues are part of the epic's scope and objectives.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addIssuesToEpic(array\_of\_issue\_keys, epicId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array\_of\_issue\_keys | String [] | Yes | issues you want added on the epic |
| epicId | Integer | Yes | The epic id |

## Return Type

**Boolean**

True of operation succeeded

## Example

```javascript
string [] issues = "TEST-1|TEST-2|TEST-3";
return addIssuesToEpic(issues, "TEST-123");
```

Returns true if successful, false if otherwise.

## See also