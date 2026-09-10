# admUpdateFieldConfig

## Description

Updates a field configuration

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateFieldConfig(fieldConfigId, name, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [updateFieldConfig(fieldConfigId, name, description)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| fieldConfigId | int | Yes | Id of the configuration |
| name | string | Yes | Name of the field configuration |
| description | string | No | Description. May be null, in which case will be an empty string |

## Return Type

[**JFieldConfiguration**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the field configuration struct, or a null (empty) struct if it cannot be updated

## See also