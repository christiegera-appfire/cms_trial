# answerApproval

## Description

Answer to an existing approval.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | answerApproval(requestId\_or\_Key, approvalId, decision) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The request key or id. |
| approvalId | String | Yes | The id of the approval to be answered. |
| decision | boolean | Yes | The decision can be 'true' if we want to approve of 'false' if we decline the approval. |

## Return Type

[**JSMApproval**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

### Example 1

```javascript
JSMApproval approval = answerApproval("SM-92", 23, true);  
return approval;
```

## See also