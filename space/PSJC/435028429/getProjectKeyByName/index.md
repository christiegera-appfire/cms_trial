# getProjectKeyByName

## Description

Retrieves the key for the project with the given name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectKeyByName(projectName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectName | String | Yes | Project name. |

## Return Type

**String**

The return value is a string representing the project key.

## Example

Project with key "DEMO" has the name "Demonstration Project".

```javascript
return getProjectKeyByName("Demonstration Project");
```

Result: DEMO

## See also