# linkedIssues

## Description

Returns an array with the Issue keys linked with the specified one.  
This function searches for all the **linked issues**  with the one given as argument (parameter) and builds an array that contains them. The second parameter **[linkTypeName]** is optional and represents a searching filter that selects only those issues that have a certain relation (link type) with the argument issue.  
The **Issue types**  that can be given as arguments are:

1. Blocks
2. Relates
3. Clones

But also other **Issue links** can be defined. To add new link type follow the tutorial from <https://confluence.atlassian.com/display/JIRA/Configuring+Issue+Linking>. It can be used to find connections between different issues.  
The third parameter [**direction**] is optional and it is used to specify whether to retrieve inward links or outward links.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | linkedIssues(issueKey, [[linkTypeName], [direction]]) | **Package** |  |
| **Alias** | getLinkedIssues (issueKey, [[linkTypeName], [direction]]) | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Specifies a string representing the key of the issue. |
| linkTypeName | String | No | Specifies the link type. |
| direction | number | No | -1, 0, 1 :Negative means inward links. Positive means outward links. Use zero to get both outward and inward links. |

## Return Type

**String[]**

## Example

A good way to understand the idea of this function is by using an example, so:

```javascript
return linkedIssues("TUT-1","Blocks");
```

## See also