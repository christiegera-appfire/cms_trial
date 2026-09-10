# rankAfter

## Description

Used to adjust the prioritization or ranking of issues or tasks after a specified point or issue, influencing the order in which work is addressed within a sprint or board.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | rankAfter(key\_to\_rank, key) | **Package** |  |
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
return rankAfter("TEST-6", "TEST-5");
```

Returns true if successful, false if otherwise.

## See also