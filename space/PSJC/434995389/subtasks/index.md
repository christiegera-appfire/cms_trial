# subtasks

## Description

Get the list of sub tasks linked to the parent issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | subtasks(issuekey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issuekey | String | Yes | Key of the issue. |

## Return Type

**String []**

Returns a list of **issue keys** that are subtasks of the specified issue.

## Examples

```javascript
//Subtasks of the issue "PRJ-32" are : PRJ-192,PRJ-193,PRJ-203.
subtasks("PRJ-32");
```

Returns: The list of the sub tasks linked to PRJ-32: |PRJ-192|PRJ-193|PRJ-203|

```javascript
subtasks(key);
```

Returns: The list of the sub tasks linked to the current issue in the form similar with the example above.

## See also