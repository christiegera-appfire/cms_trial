# admGetIssueSecurityScheme

## Description

Retrieves the security scheme for a specific issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetIssueSecurityScheme(name, id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | issueSecurityScheme(name, id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the scheme. |
| id | integer | Yes | The ID of the scheme. |

## Return Type

[**JIssueSecurityScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JIssueSecurityScheme isScheme = admGetIssueSecurityScheme("Default Issue Security Scheme", 11000);
runnerLog("Id: " + isScheme.id);
runnerLog("Name: " + isScheme.name);
runnerLog("Description: " + isScheme.description );
```

## See also