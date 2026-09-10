# admUpdateFilter

## Description

Updates a filter. Returns the updated JFilter structure. Owner cannot be changed

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateFilter(filter) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; updateFilter(filter);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| filter | JFilter | Yes | The filter to be updated |

## Return Type

[**JFilter**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter f = admGetFilterById(10017);
f.description = "Modified description";
    f.name="anothername";admUpdateFilter(f);
```

Returns the JFilter object, if correctly updated.

## See also