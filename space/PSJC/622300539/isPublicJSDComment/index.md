# isPublicJSDComment

## Description

This function returns the type of comment, if the comment is public, the function will return "true"otherwise it will return "false".

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isPublicJSDComment(requestId\_or\_Key, commentId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request from which the comment will be retrieved |
| commentId | Integer | Yes | The id of the JSD comment |

## Return Type

**Boolean**

If the comment is public, the function will return "true" otherwise it will return "false".

## Example

Th following code will return "true" if the comment with the provied id is public and "false" otherwise.

```javascript
isPublicJSDComment("SM-1", 10072);
```

## See also