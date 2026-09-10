# downloadAttachmentById

## Description

Downloads an attachment from an issue and saves it in the destination file

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | downloadAttachmentById(key, attachmentId, destinationFile) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |
| attachmentId | int | Yes | Attachment id. |
| destinationFile | string | Yes | Path to save the file. |

## Return Type

**boolean**

Returns "true" if the attachment was downloaded successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## See also