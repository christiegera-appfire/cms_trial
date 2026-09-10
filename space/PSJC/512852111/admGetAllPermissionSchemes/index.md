# admGetAllPermissionSchemes

## Description

Retrieves a list of actions and corresponding permissions for all permission schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPermissionSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allPermissionSchemes() |

## Return Type

[**JPermissionScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of key/value pairs representing the values of all permission schemes, where the key is the permission and the value is the associated permission grants for each permission. Each value can be composed of multiple permission grant values separated by "|". Each permission grant is composed of an ID and a type. The type is in parentheses.

## Example

```javascript
JPermissionScheme [] allPermsSchemes = admGetAllPermissionSchemes();
for(JPermissionScheme jps in allPermsSchemes) {
    runnerLog("Id: " + jps.id);
    runnerLog("Name: " + jps.name);
}
```

## See also