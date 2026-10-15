# admGetAllFieldSchemes

## Description

Retrieves all new-model field schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllFieldSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [allFieldSchemes()] |

## Parameters

This routine has no parameters.

## Return Type

[**JFieldConfigurationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of [**JFieldConfigurationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/) values.

This routine returns only new-model field schemes. Use `admGetAllFieldConfigSchemes` to retrieve legacy field configuration schemes.

## Example

```sil
JFieldConfigurationScheme [] schemes = allFieldSchemes();

for(JFieldConfigurationScheme fs in schemes) {
    runnerLog("Id: " + fs.id);
    runnerLog("Name: " + fs.name);
}
```

## See also