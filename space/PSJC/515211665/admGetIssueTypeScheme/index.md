# admGetIssueTypeScheme

## Description

Returns a specific issue type scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetIssueTypeScheme(name, id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | issueTypeScheme(name, id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the scheme. |
| id | integer | Yes | The ID of the scheme. |

## Return Type

[**JIssueTypeScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a specific issue type scheme.

## Example

```javascript
JIssueTypeScheme itScheme = admGetIssueTypeScheme("Default Issue Type Scheme", 11000);
runnerLog("Id: " + itScheme.id);
runnerLog("Name: " + itScheme.name);
runnerLog("Description: " + itScheme.description );
```

## See also