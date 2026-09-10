# admChangeFilterOwner

## Description

Changes the owner of a given filter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admChangeFilterOwner(filterId, newOwner) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; changeFilterOwner(filterId, newOwner);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |
| newOwner | string | Yes | The new owner. Must be not null |

## Return Type

**string**

## Example

```javascript
admChangeFilterOwner(10017, newowner);
```

Gets the owner of the filter with the id 10017

## See also