# isIssueContext

## Description

Verifies if the script is running in an [Contexts](/cms_trial/space/PSJC/434995375/isIssueContext/).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isIssueContext() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**Boolean**

A "true" return value means that the script is running in an issue context and that the [standard variables and custom fields](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) are available for use.

## Example

```javascript
if(isIssueContext()){
    return usersInGroups({"jira-users"}) - reporter;
} else {
    return usersInGroups({"jira-users"}) - currentUser();
}
```

## See also