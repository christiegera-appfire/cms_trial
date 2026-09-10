# getUsersFromOrganizations

## Description

Gets users from a specified organization or list of organizations.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUsersFromOrganizations(organizations) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| organizations | String [] | Yes | The organizations names. |

## Return Type

**String []**

Returns all the users from an organization.

## Examples

### Example 1

```text
return getUsersFromOrganizations({"First Organization", "Second Organization"});
```

### Example 2

```text
return getUsersFromOrganizations("My Organization");
```

## See also