# admUpdateIssueTypeScheme

## Description

Updates an issue type scheme. To add / remove issue types from a scheme use addIssueTypeToScheme / removeIssueTypeFromScheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateIssueTypeScheme(id, name, description, defaultIssueTypeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateIssueTypeScheme(id, name, description, defaultIssueTypeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| id | int | Yes | Id of the issue type scheme. |
| name | string | Yes | Name of the issue type scheme. |
| description | string | Yes | Description of the issue type scheme. May be null |
| defaultIssueTypeId | int | Yes | Default issue type id. |

## Return Type

[**JIssueTypeScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the issue type scheme.

## Example

```javascript
JIssueTypeScheme sch = updateIssueTypeScheme(10204, "TT new scheme", "A copy of TT scheme", 10000);
```

## See also