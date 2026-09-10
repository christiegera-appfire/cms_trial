# admGetWorkflowsFromScheme

## Description

Retrieves a list of workflows associated to a workflow scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetWorkflowsFromScheme(workflowSchemeNameOrId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | workflowsFromScheme(workflowSchemeNameOrId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workflowSchemeNameOrId | string | Yes | The name or id of the workflow scheme. |

## Return Type

[**JWorkflow[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a list of workflow objects representing workflows associated to a given workflow scheme.

## Example 1

```javascript
string workflowSchemeName = "TEST: Software Workflow Scheme";
JWorkflow[] workflows = admGetWorkflowsFromScheme(workflowSchemeName);

return workflows;

// String representation
// 753856cf-e50b-4d4b-bc96-0c68a0f773cb|REAS: Service Request Fulfilment workflow|10008|10006|10007|6|10004|10008|3|5|10005|Respond to support|Respond to customer|Back to in progress|Pending|Resolve this issue|Close|Escalate this issue|Escalate
```

## Example 2

```javascript
JWorkflow[] workflows = admGetWorkflowsFromScheme(10002);

return workflows;
```

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]