# copyAttachmentById

## Description

Copies the attachment for the provided id from one issue to another.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | copyAttachmentById(attachmentId, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attachmentId | Number | Yes | Attachment id. |
| issueKey | String | Yes | Issue key where you want to copy the attachment. |

## Return Type

**Boolean (true/false)**

Returns "true" if the attachment was copied successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## Example

```javascript
copyAttachmentById(10205, "TEST-2");
```

## See also