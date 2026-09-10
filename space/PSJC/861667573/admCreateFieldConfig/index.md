# admCreateFieldConfig

## Description

Creates a field configuration

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateFieldConfig(name, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [createFieldConfig(name, description)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the field configuration |
| description | string | Yes | Description. May be null, in which case will be an empty string |

## Return Type

[**JFieldConfiguration**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the field configuration struct, or a null (empty) struct if it cannot be created

## See also