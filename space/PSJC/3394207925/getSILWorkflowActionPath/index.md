# getSILWorkflowActionPath

## Description

Returns the SIL script path registered for a workflow post function action, identified by its action id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getSILWorkflowActionPath(actionId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| actionId | string | Yes | The id of the workflow post function action (the pfid configured for the SIL post function). |

## Return Type

**String**

Returns the path to the SIL script registered for the given action id. Returns an empty string if no post function is registered for the specified action id.

## Examples

### Example 1

```javascript
string scriptPath = getSILWorkflowActionPath("f890c814-a23b-4f0e-8db5-b95429906cc2");
return scriptPath;
```

Returns the SIL script path registered for the specified workflow post function action id.

## See also