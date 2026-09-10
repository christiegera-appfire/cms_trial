# getProjectIdByKey

## Description

Retrieves the id for the project with the given key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getProjectIdByKey(projectId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |

## Return Type

**String**

The return value is a string representing the project id.

## Example

Project with id "10000" has the key "DEMO".

```javascript
return getProjectIdByKey("DEMO");
```

Result: 10000

## See also