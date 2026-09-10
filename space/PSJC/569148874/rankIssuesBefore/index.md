# rankIssuesBefore

## Description

Used to adjust the prioritization or ranking of issues or tasks before a specified issue, controlling the order in which work is addressed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | rankIssuesBefore(array\_of\_issue\_keys, key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array\_of\_issue\_keys | String [] | Yes | The issue keys you want to rank |
| key | String | Yes | the issue key |

## Return Type

**Boolean**

True if the rank is ok

## Example

```javascript
string [] issues = "TEST-1|TEST-2|TEST-3|";
return rankIssuesBefore(issues, "TEST-5");
```

Returns true if successful, false if otherwise.

## See also