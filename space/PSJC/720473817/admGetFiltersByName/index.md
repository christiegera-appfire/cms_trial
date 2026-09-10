# admGetFiltersByName

## Description

Gets all the filters matching a name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFiltersByName(name) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; filtersByName(name);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name |

## Return Type

[**JFilter []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter [] filters = admGetFiltersByName("importantfilter");
```

Gets all the filters with that name, partial match

## See also