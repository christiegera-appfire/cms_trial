# getVersionsObjects

## Description

Returns all the project versions as an array of JVersion structures.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getVersionsObjects(pkey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pKey | String | Yes | Project key. |

## Return Type

[**JVersion []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JVersion [] verObjs = getVersionsObjects("TP"); //projectKey as parameter
for(JVersion ver in verObjs) {
    runnerLog(ver.name);
    runnerLog(ver.releaseDate);
}
```

Returns an array of JVersion structures containing all the project versions.

## See also