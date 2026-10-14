# admProjectUsesFieldSchemeModel

## Description

Returns whether a project uses the new field scheme model.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admProjectUsesFieldSchemeModel(projKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [projectUsesFieldSchemeModel(projKey)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projKey | string | Yes | The project key. |

## Return Type

**boolean**

Returns a boolean value.

Returns true if the project uses the new field scheme model. Returns false if the project was not found or the project key is null.

## Example

```sil
boolean usesNewModel = projectUsesFieldSchemeModel("DEMO");
```

## See also