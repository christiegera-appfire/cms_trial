# admUpdateFieldConfigScheme

## Description

Updates a field config scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateFieldConfigScheme(schemeId, name, description) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [updateFieldConfigScheme(schemeId, name, description)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the config scheme |
| name | string | Yes | Name of the config scheme |
| description | string | No | Description. May be null, in which case will be an empty string |

## Return Type

[**JFieldConfigurationScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the scheme, or a null (empty) struct if it cannot be updated

## See also