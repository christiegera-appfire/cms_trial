# uploadAttachment

## Description

Uploads an attachment to an issue

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | uploadAttachment(key, sourceFile) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |
| sourceFile | string | Yes | Path to the file. |

## Return Type

**boolean**

Returns "true" if the attachment was uploaded successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## Example

```javascript
return uploadAttachment("TP-222","C:\Pictures\embarassing_photo_of_uncle_jim.jpg");
```

## See also