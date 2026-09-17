# admGetFieldConfigITMappings

## Description

Returns the issue type - field configuration mappings for a field configuration scheme

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFieldConfigITMappings(schemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [fieldConfigITMappings(schemeId)] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the config scheme |

## Return Type

[**JFieldConfigITMapping []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a list of issueTypeId - fieldConfigId for the scheme. If issueTypeId is 0 (zero) it means it's the default issue type

## See also