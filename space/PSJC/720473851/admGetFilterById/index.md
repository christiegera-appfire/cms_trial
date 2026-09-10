# admGetFilterById

## Description

Gets the filter specified by that id.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFilterById(filterId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; filterById(filterId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filterId | int | Yes | The filter id |

## Return Type

[**JFilter**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter filter = admGetFilterById(10037);
```

Gets the filter for id 10037

## See also