# admGetWorkflowScheme

## Description

Returns a specific workflow scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetWorkflowScheme(id\_or\_name) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | workflowScheme(id\_or\_name) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| id\_or\_name | integer or string | Yes | The ID or the Name of the scheme |

## Return Type

[**JWorkflowScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a workflow scheme.

## Example

```javascript
JWorkflowScheme workScheme = admGetWorkflowScheme(11000);
runnerLog("Id: " + workScheme.id);
runnerLog("Name: " + workScheme.name);
runnerLog("Description: " + workScheme.description );
```

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]