# admSetIssueTypeScheme

## Description

Sets an issue type scheme for an project.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admSetIssueTypeScheme(pKey, schemeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | setIssueTypeScheme(pkey, schemeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | string | Yes | Id of the issue type. |
| schemeId | int | Yes | Id of the issue type scheme. |

## Return Type

**boolean**

Returns true if the issue type scheme was set.

## Example

```javascript
admSetIssueTypeScheme("TT", 10204);
```

## See also