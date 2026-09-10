# admGetProjectPropertyKeys

## Description

Returns an array of property keys available on the project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectPropertyKeys(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | projectPropertyKeys(projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |

## Return Type

**string []**

Returns all project property keys for a project.

## Example

```javascript
admGetProjectPropertyKeys("TEST");
```

## See also