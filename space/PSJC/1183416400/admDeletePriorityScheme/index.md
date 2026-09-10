# admDeletePriorityScheme

## Description

Deletes a priority scheme using its id. This operation is only available for priority schemes without any associated projects. Any associated projects must be removed from the priority scheme before this operation can be performed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admDeletePriorityScheme(prioritySchemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | deletePriorityScheme(prioritySchemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeId | number | Yes | The id of the priority scheme |

## Return Type

**boolean**

Returns true if the scheme was deleted, false otherwise.

## Example

### Example 1

Deletes the priority scheme with id 10301

```javascript
admDeletePriorityScheme(10301);
```

return true;

## See also