# admGetAllFieldConfigSchemes

## Description

Retrieves all field configuration schemes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllFieldConfigSchemes() | **Package** | adm |
| **Alias** |  | **Pkg Usage** | allFieldConfigSchemes() |

## Return Type

[**JFieldConfgurationScheme []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFieldConfigurationScheme [] allFcSchemes = admGetAllFieldConfigurationSchemes();
for(JFieldConfigurationScheme fcs in allFcSchemes) {
    runnerLog("Id: " + fcs.id);
    runnerLog("Name: " + fcs.name);
}
```

## See also