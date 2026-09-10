# admGetFieldConfigScheme

## Description

Retrieves a specific field configuration scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFieldConfigScheme(name, id) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | fieldConfigScheme(name, id) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the scheme. |
| id | integer | Yes | The ID of the scheme. |

## Return Type

[**JFieldConfgurationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFieldConfigurationScheme fcScheme = admGetfieldConfigScheme("Default Field Config Scheme", 11000);
runnerLog("Id: " + fcScheme.id);
runnerLog("Name: " + fcScheme.name);
runnerLog("Description: " + fcScheme.description );
```

## See also