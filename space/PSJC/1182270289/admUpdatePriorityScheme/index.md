# admUpdatePriorityScheme

## Description

The basic updated of a priority scheme, we only set the name, description and priorities. You can also alter the priorities and projects in it by using the according routines.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdatePriorityScheme(schemeId, name, defaultPriorityId, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updatePriorityScheme(schemeId, name, defaultPriorityId, description) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | number | Yes | The id of the priority scheme to be updated |
| name | string | Yes | The new name of the priority scheme. Must be unique |
| defaultPriorityId | number | Yes | The new id of the default priority for the priority scheme. |
| description | string | No | The new description of the priority scheme. |

## Return Type

**boolean**

Returns true if the scheme was updated, false otherwise.

## Example

### Example 1

Updates a priority scheme

```javascript
admUpdatePriorityScheme(schId, "new name updated at " + currentDate(), 4, "description updated at " + currentDate());
```

## See also