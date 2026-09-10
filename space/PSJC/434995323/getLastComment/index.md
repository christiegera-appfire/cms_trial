# getLastComment

## Description

Gets all the comment properties for the last issue comment.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getLastComment(issueKey); | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Issue key. |

## Return Type

[**JComment**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JComment cmt = getLastComment("DEMO-1");
runnerLog("Got comment:" + cmt["text"]);
```

## See also