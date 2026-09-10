# removeOrganization

## Description

Removes an organization or a list of organizations from a specified project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeOrganization(organization, project) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organization | String [] | Yes | The organizations name. |
| project | String | Yes | The key of the selected project. |

## Return Type

**Boolean**

Returns "true" if the operation succeeded.

## Example

```text
return removeOrganization({"First Organization", "Second Organization"}, "JSD");
```

## See also