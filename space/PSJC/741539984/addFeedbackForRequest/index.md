# addFeedbackForRequest

## Description

Add feedback to the provided requestId\_or\_Key

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addFeedbackForRequest(requestId\_or\_Key, rating [,comment]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the selected request. |
| rating | number | Yes | Rating must be between 1 and 5. |
| comment | String | No | Comment for the rating. |

## Return Type

[**JSMFeedback**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JSMFeedback feedback = addFeedbackForRequest("SM-1","5","Thanks for help.");
 return feedback;}
```

Adds the feedback and returns the feedback structure if the feed was added successfully

## See also