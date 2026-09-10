# getIssueFields

## Description

Returns a map with all standard and custom fields of an issue. The map contains pairs of field name and field values.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueFields(issueKey[, getNullFields]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Key of the selected issue. |
| getNullFields | Boolean | No | Flag for specifying whether the fields with null values should be retrieved too. If not specified, it defaults to "false". |

## Return Type

**String []**

The return value is a string array containing all fields values for the selected issue. Each value can be retrieved from the array by key (the field id).

## Examples

### Example 1

```javascript
string[] fields = getIssueFields("DEMO-1");
return fields["summary"];
```

### Example 2

We can use the function to partially clone an issue by copying only some of the fields from the original issue:

```javascript
string[] fields = getIssueFields("TP-1", true);
string issue = createIssue(fields["project"], fields["parent"], fields["issueType"], fields["summary"] + " - part 2");
%issue%.customfield_10000 = fields["customfield_10000"];
%issue%.description = "Partial clone of issue TP-1";
return issue;
```

## See also