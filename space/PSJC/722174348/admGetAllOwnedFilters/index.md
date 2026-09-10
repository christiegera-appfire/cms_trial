# admGetAllOwnedFilters

## Description

Gets all the filters for an user. The user provided there is the owner of the filters

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllOwnedFilters(userId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; ownedFilters(userId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The user |

## Return Type

[**JFilter []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter [] ownedFilter = admGetAllOwnedFilters(currentUser());
```

Gets all the possible filters from the system belonging to the user

## See also