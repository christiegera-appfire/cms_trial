# admCreateFilter

## Description

Creates a filter. Returns the JFilter structure. Name should be unique in your Jira

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateFilter(name, jql, owner[,description]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; createFilter(name, jql, owner[,description]);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The name, must be unique within your Jira. |
| jql | string | Yes | The jql you want to set up for this filter. |
| owner | string | Yes | The owner of the filter. If empty it is assumed to be the current user. |
| owner | string | No | A description. |

## Return Type

[**JFilter**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFilter f = admCreateFilter("pcfilter", "project = TEST and issueType = Bug", currentUser(), "This is programatically created");
```

Returns the JFilter object, if correctly created.

## See also