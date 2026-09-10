# linkIssue

## Description

Links two issues by a specified link type name. First issue will have the outward description of the link type, the second issue will have the inward description of the link type.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | linkissue(inwardIssueKey, outwardIssueKey, issueLinkTypeName [, comment, securityLevel]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey1 | String | Yes | Key of the first issue to be linked. |
| issueKey2\_or\_url | String | Yes | Key of the second issue to be linked or the URL. |
| issueLinkTypeName | String | Yes | Issue link type name. |
| comment | String | No | Comment that will be posted on the selected issue. |
| securityLevel | String | No | Security level of comment. |

## Return Type

**None**

The returned value has no meaning.

## Examples

### Example 1

```javascript
linkIssue(key, "TEST-5", "Duplicate");
```

Result: current issue is linked to issue "TEST-5" by Duplicates link type, such that "TEST-5" duplicates the current issue and the current issue is duplicated by "TEST-5".

### Example 2

```javascript
linkIssue(key, "TEST-5", "Duplicate", "some text here")
```

The same as example 1 however a public comment will be added.

### Example 3

```javascript
linkIssue(key, "TEST-5", "Duplicate", "some text here", "Developers")
```

The same as example 1 however a comment will be added and only visable to users with the project role "Developers".

## See also