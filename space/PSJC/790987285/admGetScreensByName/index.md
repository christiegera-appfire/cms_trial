# admGetScreensByName

## Description

Returns an array of screens filtered by name. If name is null, all screens are returned

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetScreensByName(partName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; screensByName(partName);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| partName | string | Yes | The partial match string. Filtering is done on Jira side |

## Return Type

[**JScreen []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JScreen [] screens = admGetScreensByName("Demo");
```

Returns the JScreen objects matching 'Demo' in the name

## See also