# getAttachmentsForRequest

## Description

Returns a list of attachments structures

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAttachmentsForRequest(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request for which the attachments will be retrieved |

## Return Type

[**JSMAttachment[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getAttachmentsForRequest("SM-1");
```

Returns a list of JSMAttachment structures.

## See also