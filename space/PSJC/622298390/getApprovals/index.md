# getApprovals

## Description

Returns a list of approvals structures

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getApprovals(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request for which the approvals will be retrieved |

## Return Type

[**JSMApproval[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getApprovals("SM-1");
```

Returns a list of JSMApproval structures.

## See also