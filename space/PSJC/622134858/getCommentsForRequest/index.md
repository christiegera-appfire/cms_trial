# getCommentsForRequest

## Description

Returns a list of comments structures

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCommentsForRequest(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request for which the comments will be retrieved |

## Return Type

[**JSMComment[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getCommentsForRequest("SM-1");
```

Returns a list of JSMComment structures.

## See also