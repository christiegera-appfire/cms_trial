# getIssueLinksDetail

## Description

Returns all the details about the links of an issue key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueLinksDetail(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Issue key. |

## Return Type

[**JIssueLink []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Examples

### Example 1

```javascript
return getIssueLinksDetail("TEST-1");
```

### Example 2

```javascript
JIssueLink[] jIssueLinks = getIssueLinksDetail("TEST-1");
for(JIssueLink jIssueLink in jIssueLinks){
    runnerLog("The linked issue " + jIssueLink.issue + " it has the following properties: "); 
    runnerLog("- link id : " + jIssueLink.id); 
    runnerLog("- link name : " +  jIssueLink.name);
    runnerLog("- direction : " + jIssueLink.direction);
    runnerLog("- description : " + jIssueLink.description);
}
```

## See also