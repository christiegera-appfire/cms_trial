# getCommentById

## Description

Gets all the comment properties for a given id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCommentById(issueKey, id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | No | The key of the issue. |
| commentId | Number | Yes | Id of the issue comment |

## Return Type

[**JComment**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
number [] arr = getAllCommentIds(argv["key"]);
for(number x in arr) {
 JComment cmt = getCommentById(x);
 runnerLog("Got comment:" + cmt["text"]);
}
```

## See also