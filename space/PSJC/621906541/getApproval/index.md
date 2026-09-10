# getApproval

## Description

Returns an approval structure

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getApproval(requestId\_or\_Key, approvalId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request for which the approval will be retrieved |
| approvalId | Integer | Yes | The ID of the approval to be re returned |

## Return Type

[**JSMApproval**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getApproval("SM-1", 5);
```

Returns a JSMApproval structure.

## See also