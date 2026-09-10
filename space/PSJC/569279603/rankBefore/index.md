# rankBefore

## Description

Used to adjust the prioritization or ranking of issues or tasks before a specified point or issue, controlling their order within a particular context.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | rankBefore(key\_to\_rank, key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key\_to\_rank | String | Yes | The issue key you want to rank |
| key | String | Yes | the pivot issue key |

## Return Type

**Boolean**

True if the rank is ok

## Example

```javascript
return rankIssuesBefore("TEST-4", "TEST-5");
```

Returns true if successful, false if otherwise.

## See also