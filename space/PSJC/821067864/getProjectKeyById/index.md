# getProjectKeyById

## Description

Retrieves the key for the project with the given id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectKeyById(projectId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectId | String | Yes | Project id. |

## Return Type

**String**

The return value is a string representing the project key.

## Example

Project with key "DEMO" has the id "10000".

```javascript
return getProjectKeyById("10000");
```

Result: DEMO

## See also