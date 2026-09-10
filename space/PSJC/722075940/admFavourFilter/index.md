# admFavourFilter

## Description

Favours a filter for the supplied account. Marks the filter as favourite for the account id  
.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admFavourFilter(filterId, accountId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; favourFilter(filterId, accountId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |
| accountId | string | Yes | The account id. Must be not null |

## Return Type

**boolean**

## Example

```javascript
admFavourFilter(10017, theuser);
```

The effect is as the newuser would click on the start icon on the filter

## See also