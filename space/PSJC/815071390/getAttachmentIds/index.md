# getAttachmentIds

## Description

Sometimes you may wish to refer to the exact id of the attachment. This is how you get them

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAttachmentIds(key) or getAttachmentIds(key, partialName) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |
| partialName | string | Yes | Partial name to filter with. |

## Return Type

**int []**

Returns an array of attachment ids

## Example

```javascript
integer [] attach = getAttachmentIds("TP-222", "jpg");
for(int a in attach) {
    runnerLog(a);
}
```

## See also