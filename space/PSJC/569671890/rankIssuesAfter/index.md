# rankIssuesAfter

## Description

Used to adjust the prioritization or ranking of issues or tasks after a specified issue, helping to control the order in which work is addressed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | rankIssuesAfter(array\_of\_issue\_keys, key) | **Package** |  |
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
string [] issues = "TEST-6|TEST-7|TEST-8|";
return rankIssuesAfter(issues, "TEST-5");
```

Returns true if successful, false if otherwise.

## See also