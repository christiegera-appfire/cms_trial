# admGetProjectWorkflowScheme

## Description

Returns the name of workflow workflow scheme name for the given project key or id

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectWorkflowScheme(projectKeyOrId) | **Package** | adm |
| **Alias** | getProjectWorkflowScheme | **Pkg Usage** | projectWFScheme(projectKeyOrId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKeyOrId | string | Yes | The key or the id of the project |

## Return Type

**string**

Returns the name of the workflow scheme for the project.

## Example

```javascript
return admGetProjectWorkflowScheme("TEST");
```

Jira Service Management IT Support Workflow Scheme generated for Project TEST

## See also