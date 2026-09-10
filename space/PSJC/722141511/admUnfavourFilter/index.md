# admUnfavourFilter

## Description

Un-favours a filter for the supplied account. Marks the filter as non-favourite for the account id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUnfavourFilter(filterId, accountId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; unfavourFilter(filterId, accountId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |
| accountId | string | Yes | The account id. Must be not null |

## Return Type

**boolean**

## Example

```javascript
admUnfavourFilter(10017, theuser);
```

The effect is as the newuser would click on the start icon on the filter, unselect

## See also