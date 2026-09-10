# deleteIssue

## Description

Deletes the selected issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteIssue(issuekey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issuekey | String | Yes | Key of the issue that has to be deleted. |

## Return Type

**None**

The returned value has no meaning.

## Examples

### Example 1

```javascript
deleteIssue("PRJ-323");
```

Result: If the current issue **is not** "PRJ-323" or **a child of** "PRJ-323", then the issue "PRJ-323" will be deleted.

### Example 2

```javascript
deleteIssue(key);
```

Result: Since "key" variable returns the key of the current issue, the delete operation will fail.

Cannot delete the current issue or the parent of the current issue.

## See also