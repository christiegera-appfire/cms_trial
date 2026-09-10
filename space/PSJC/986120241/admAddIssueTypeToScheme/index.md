# admAddIssueTypeToScheme

## Description

Adds an issue type ids for a scheme scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddIssueTypeToScheme(schemeId, issueTypeId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | addIssueTypeToScheme(schemeId, issueTypeId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| schemeId | int | Yes | Id of the issue type scheme. |
| issueTypeId | int | Yes | Id of the issue type. |

## Return Type

**boolean**

Returns true if the issue type was added.

## Example

```javascript
admAddIssueTypeToScheme(10204, 10008);
```

## See also