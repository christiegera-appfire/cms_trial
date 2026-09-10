# swapSprints

## Description

Facilitates the reordering or swapping of sprints within a Scrum board. It may be used to adjust the order of sprints based on project priorities or other considerations.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | swapSprints(sprint\_1\_Id, sprint\_2\_Id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprint\_1\_Id | Integer | Yes | The first sprint id |
| sprint\_2\_Id | Integer | Yes | The second sprint id |

## Return Type

**Boolean**

Returns true if the sprint are swapped.

## Example

This will switch the order that the sprints appear on the board for the two sprints below.

```javascript
return swapSprints(12345, 678910);
```

Returns true if successful, false if otherwise.

## See also