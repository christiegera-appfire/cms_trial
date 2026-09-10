# projectObject

## Description

Returns the project properties.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | projectObject(pkey) | **Package** | adm |
| **Alias** | projectProps(pkey) //deprecated  admProjectProperties(pkey) //deprecated | **Pkg Usage** | projectObject(pkey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |

## Return Type

[**JProject**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The properties of the project.

## Example

```javascript
use "adm";
JProject p = projectObject("TSTPRJ");
```

## See also