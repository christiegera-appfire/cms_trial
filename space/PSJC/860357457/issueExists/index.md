# issueExists

## Description

Returns true if the key is indeed an issue key and the issue is valid. Does not throw if the issue is not there.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueExists(key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |

## Return Type

**boolean**

Returns true if the issue exists

## Example

```javascript
return issueExists("THEPRJ-666");
```

## See also