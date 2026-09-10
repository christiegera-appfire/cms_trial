# admProjectExists

## Description

Returns 'true' if project with provided key exists and 'false' otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admProjectExists(project\_key) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | projectExists(project\_key) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| project\_key | string | Yes | The project key. The value must be unique. |

## Return Type

**Boolean**

Returns 'true' if project exists and 'false' otherwise.

## Examples

```javascript
boolean prjExist = admProjectExists("TEST");
```

```javascript
use "adm";
boolean pexists = projectExists("CX1");
```

## See also