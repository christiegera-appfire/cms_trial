# attachFileFromEmail

## Description

Saves an attachment from an incoming email, attaching it to an issue

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | attachFileFromEmail(attachmentName, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attachmentName | string | Yes | An attachment from the incoming mail |
| issueKey | string | Yes | Where to save that attachment, on what issue |

## Return Type

**boolean**

True if the attachment is saved on that issue

## See also