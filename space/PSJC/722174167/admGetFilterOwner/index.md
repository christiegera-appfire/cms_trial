# admGetFilterOwner

## Description

Gets the owner of a given filter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFilterOwner(filterId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; filterOwner(filterId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |

## Return Type

**string**

## Example

```javascript
string owner = admGetFilterOwner(10017);
```

Gets the owner of the filter with the id 10017

## See also