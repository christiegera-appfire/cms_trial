# addSILWorkflowAction

## Description

Adds a SIL post function to the specified workflow transition. The routine creates a unique action id, adds the SIL post function to the transition, saves the workflow, and registers the script path. Returns true if the post function was added successfully.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addSILWorkflowAction(workflowName, transitionNameOrId, pathToSil [, async]) | **Package** |  |
| **Alias** | addSilPostfunction(workflowName, transitionNameOrId, pathToSil [, async]) | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workflowName | string | Yes | Name of the workflow to modify. |
| transitionNameOrId | string | Yes | Name or id of the transition where the SIL post function will be added. |
| pathToSil | string | Yes | Path to the SIL script file, relative to the SIL storage directory. |
| async | boolean | No | When true, the post function is registered to run asynchronously. Defaults to false. |

## Return Type

**Boolean (true/false)**

Returns true if the SIL post function was added and registered successfully. Returns false if the workflow was not found, is not editable, the script path could not be resolved, or adding the post function to the transition failed.

## Examples

### Example 1

```javascript
boolean added = addSILWorkflowAction("Software Simplified Workflow for Project TEST", "Done", "scripts/my-postfunction.sil", true);
```

Returns true if the SIL post function was added to the "Done" transition of the specified workflow.

### Example 2

```javascript
boolean added = addSilPostfunction("Software Simplified Workflow for Project TEST", "Done", "scripts/my-postfunction.sil");
return added;
```

Same as addSILWorkflowAction, but will run synchronously.

## See also