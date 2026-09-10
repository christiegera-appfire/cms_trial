# getAllCommentIds

## Description

Gets all the comment ids that are already entered on an issue. Gets all the comment ids that are already entered on an issue. Unlike the [getCommentById()](/cms_trial/space/PSJC/434930021/getCommentById/) function, this function returns what is already entered on the issue. Comments are guaranteed to be sorted from the oldest to the newest one. For instance the last comment is at the end of the array, first comment is the first in the list.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllCommentIds(key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | String | Yes | Key of the issue. |

## Return Type

**Number []**

Ids of the comments on the issue represented by key parameter.

## Example

```javascript
number [] arr = getAllCommentIds(key);
for(number x in arr) {
   string [] cmt = getCommentById(x);
   runnerLog("Got comment:" + cmt["text"]);
}
```

## See also