# admSetProjectIssueSecurityScheme

## Description

Updates the issue security scheme to the given one. Return true if success, false otherwise

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectIssueSecurityScheme(projectKey, schemeName) | **Package** | adm |
| **Alias** | setProjectIssueSecurityScheme | **Pkg Usage** | setProjectIssSecScheme(projectKey, schemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key |
| schemeName | string | Yes | The name of the scheme to be set |

## Return Type

**Boolean (true/false)**

Returns true if the scheme was set and false otherwise.

## Example

```javascript
admSetProjectIssueSecurityScheme("ITSD","Security sch");
```

## See also