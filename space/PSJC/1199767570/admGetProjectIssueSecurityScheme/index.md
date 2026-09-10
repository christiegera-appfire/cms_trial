# admGetProjectIssueSecurityScheme

## Description

Returns the name of the issue priority scheme name for the given project key or id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectIssueSecurityScheme(projectKeyOrId) | **Package** | adm |
| **Alias** | getProjectIssueSecurityScheme | **Pkg Usage** | projectIssSecScheme(projectKeyOrId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKeyOrId | string | Yes | The key or the id of the project |

## Return Type

**string**

Returns the name of the issue priority scheme for the project.

## Example

```javascript
return admGetProjectIssueSecurityScheme("TEST");
```

Security scheme

## See also