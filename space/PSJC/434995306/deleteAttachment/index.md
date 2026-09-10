# deleteAttachment

## Description

Deletes the attachment for a given id or for a specified issue and file name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteAttachment(issueKey, attachmentName) or deleteAttachment(attachmentId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Issue key. |
| attachmentName | String | Yes | Attachment name. |

### Or

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| attachmentId | Number | Yes | Attachment id. |

## Return Type

**Boolean (true/false)**

Returns "true" if the attachment was deleted successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

## Examples

### Example 1

```javascript
deleteAttachment(10104);
```

### Example 2

```javascript
deleteAttachment("TEST-1", "attachmentToDelete.txt");
```

If you have multiple attachments on an issue with the same file name, all of them will be deleted.

## See also