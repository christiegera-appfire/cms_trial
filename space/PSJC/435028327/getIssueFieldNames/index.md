# getIssueFieldNames

## Description

Returns a list with the names of all standard and custom fields of an issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueFieldNames(issueKey[, getNullFields]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Key of the selected issue. |
| getNullFields | Boolean | No | Flag for specifying whether the fields with null values should be retrieved too. If not specified, it defaults to "false". |

## Return Type

**String []**

The return value is a string array containing all fields values for the selected issue. Each value can be retrieved from the array by key (the field id).

## Example

```javascript
string[] fields = getIssueFieldNames("DEMO-1");
return fields;
```

## See also