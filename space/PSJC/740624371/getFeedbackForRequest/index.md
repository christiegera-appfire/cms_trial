# getFeedbackForRequest

## Description

Returns a JSMFeedback structure for the provided requestId\_or\_Key

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getFeedbackForRequest(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the selected request. |

## Return Type

[**JSMFeedback**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JSMFeedback feedback = getFeedbackForRequest("SM-1");
 return feedback;}
```

Returns the feedback structure for the request "SM-1"

## See also