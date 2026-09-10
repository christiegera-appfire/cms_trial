# admUnshareFilter

## Description

Un-shares a filter. Removes the share by id. You will find the shares in the filter structure (including their ids)

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUnshareFilter(filterId, sharePermId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; unshareFilter(filterId, sharePermId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |
| sharePermId | int | Yes | The share permission id. |

## Return Type

**boolean**

## Example

```javascript
admUnshareFilter(f.id, 10035);
```

Un-Shares the filter with some share perm given id

## See also