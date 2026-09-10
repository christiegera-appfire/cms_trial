# getAttachmentMediaId

## Description

Returns the media ID that can be used in ADF, for the specified issue and attachmentId

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAttachmentMediaId(key, attachmentId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |
| attachmentId | integer | Yes | The id of the attachment. |

## Return Type

**string**

Returns the media id for the provided parameters.

## Example

```javascript
string mediaId = getAttachmentMediaId("TEST-23", 10230);
return mediaId;
```

## See also