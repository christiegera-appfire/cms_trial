# admGetFavouriteFilters

## Description

Gets all the filters for an user, favorited by the user. The user provided there is not necessarily the owner of the filters

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFavouriteFilters(userId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; favouriteFilters(userId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The user |

## Return Type

[**JFilter []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter [] ownedFilter = admGetFavouriteFilters(currentUser());
```

Gets all the favourite filters of the user

## See also