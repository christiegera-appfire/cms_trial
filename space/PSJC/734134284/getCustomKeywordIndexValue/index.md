# getCustomKeywordIndexValue

## Description

Gets the stored value for a given custom jql keyword, registered via Power Scripts.
NOTE: The keyword must be already in the system!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomKeywordIndexValue(issueKey, jqlKeyword) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | string | Yes | The issue key |
| jqlKeyword | string | Yes | The JQL keyword, registered in PS |

## Return Type

**string**

The value of the field, as a string

## Example

```javascript
return getCustomKeywordIndexValue("TEST-123", "customKeyword");
```

Returns the value of the keyword index for "customKeyword" for issue TEST-123.

## See also