# getCommentForRequest

## Description

Returns a comment structure with extra information (attachments and renderedBody), those are not get when using getCommentsForRequest

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCommentForRequest(requestId\_or\_Key, commentId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request for which the comment will be retrieved |
| commentId | Integer | Yes | The ID of the comment to be re returned |

## Return Type

[**JSMComment[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getCommentForRequest("SM-1", 10072);
```

Returns a list of JSMComment structures.

## See also