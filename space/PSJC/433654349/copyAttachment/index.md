# copyAttachment

## Description

Copies an attachment from one issue to another.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | copyAttachment(issueKey1, attachmentName, issueKey2) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey1 | String | Yes | Issue key. |
| attachmentName | String | Yes | Attachment name. |
| issueKey2 | String | Yes | Issue key where you want to copy the attachment. |

## Return Type

**Boolean**

Returns "true" if the attachment was copied successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## Examples

### Example 1

```javascript
copyAttachment("TEST-1", "attachmentToCopy.txt", "TEST-2");
```

### Example 2

Copy all the attachments from one issue to another.

```javascript
string issueKey = "TEST-1";
for(string s in issueKey.attachments) {
    copyAttachment(issueKey, s, "TEST-2");
}
```

If you have multiple attachments on an issue with the same file name, all of them will be copied.

## See also