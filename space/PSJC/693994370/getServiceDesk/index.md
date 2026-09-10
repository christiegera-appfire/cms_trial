# getServiceDesk

## Description

Returns a JSMServiceDesk structure for the provided project key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getServiceDesk(projectKey) | **Package** |  |
| **Alias** | getServiceDeskByProjectKey | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key. |

## Return Type

[**JSMServiceDesk**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a JSMServiceDesk structure containing information about the service desk.

## Example

```javascript
JSMServiceDesk serviceDesk = getServiceDesk("SM");
return serviceDesk;
```

## See also