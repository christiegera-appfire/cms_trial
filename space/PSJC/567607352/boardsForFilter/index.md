# boardsForFilter

## Description

Identifies the boards that use a particular filter for issue tracking, helping to understand which boards are based on specific criteria or conditions.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | boardsForFilter(filterId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | Integer | Yes | Filter id |

## Return Type

**Integer []**

Gets the boards created based on the filter

## Example

```javascript
integer [] boards = boardsForFilter(12345);
return boards;
```

## See also