# unlinkIssue

## Description

Removes the specified link between two issues.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | unlinkIssue(issueKey1, issueKey2, issueLinkTypeName[, keepReverseLink)] | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey1 | String | Yes | Key of the first issue to be unlinked. |
| issueKey2 | String | Yes | Key of the second issue to be unlinked. |
| issueLinkTypeName | String | Yes | Issue link type name. |
| keepReverseLink | Boolean | No | Consider the direction of the link. |

## Return Type

**None**

The returned value has no meaning.

## Examples

### Example 1

```javascript
unlinkIssue(key, "TST-123", "Relates");
//key represents the key of current issue, "TST-123" the key of the issue it will be linked to.
```

Result: The Relates link between current issue and issue "TST-123" will be removed.

### Example 2

```javascript
linkIssue("TST-123", "TST-234", "Blocks");
```

Result: The Blocks link between issue "TST-123" and issue "TST-234" will be removed.

### Example 3

```javascript
linkIssue("TST-123", "TST-234", "Blocks", "true");
```

Result: The Blocks link between issue "TST-234" and issue "TST-123" will not be removed because the link specified by the parameters of this call does not exist, but the reverse does.

## See also