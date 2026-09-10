# setCustomKeywordIndexValue

## Description

Sets the value for a given custom jql keyword, registered via Power Scripts.
NOTE: The keyword must be already in the system!

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setCustomKeywordIndexValue(issueKey, jqlKeyword, val) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | string | Yes | The issue key |
| jqlKeyword | string | Yes | The JQL keyword, registered in PS |
| val | string | Yes | The value, as a string |

## Return Type

**boolean**

true if the property was set

## Example

```javascript
setCustomKeywordIndexValue("TEST-123", "customKeyword", "some value");
```

Sets the keyword index value for issue TEST-123.

## See also