# downloadAttachment

## Description

Downloads an attachment from an issue and saves it in the destination file

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | downloadAttachment(key, attachmentName, destinationFile) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |
| attachmentName | string | Yes | Attachment name. |
| destinationFile | string | Yes | Path to save the file. |

## Return Type

**boolean**

Returns "true" if the attachment was downloaded successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## See also