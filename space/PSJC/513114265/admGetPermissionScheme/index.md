# admGetPermissionScheme

## Description

Retrieves a list of actions and corresponding permissions for a permission scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetPermissionScheme(name, id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | permissionScheme(name, id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the scheme. |
| id | integer | Yes | The ID of the scheme. |

## Return Type

[**JPermissionScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JPermissionScheme permScheme = admGetPermissionScheme("Default Permission Scheme", 11000);
runnerLog("Id: " + permScheme.id);
runnerLog("Name: " + permScheme.name);
runnerLog("Description: " + permScheme.description );
```

## See also