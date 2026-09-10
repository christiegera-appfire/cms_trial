# admSetProjectWorkflowScheme

## Description

Updates the workflow scheme to the given one. Return true if success, false otherwise

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetProjectWorkflowScheme(projectKey, propertyKey, propertyName, value) | **Package** | adm |
| **Alias** | setProjectWorkflowScheme | **Pkg Usage** | setProjectWFScheme(projectKey, propertyKey, propertyName, value) |

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
admSetProjectWorkflowScheme("ITSD","WF sch");
```

## See also