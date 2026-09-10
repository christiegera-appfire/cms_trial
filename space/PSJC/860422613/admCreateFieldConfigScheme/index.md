# admCreateFieldConfigScheme

## Description

Creates a field config scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateFieldConfigScheme(name, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [createFieldConfigScheme(name, description)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the config scheme |
| description | string | Yes | Description. May be null, in which case will be an empty string |

## Return Type

[**JFieldConfigurationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the scheme, or a null (empty) struct if it cannot be created

## See also