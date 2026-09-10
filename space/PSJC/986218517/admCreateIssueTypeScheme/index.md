# admCreateIssueTypeScheme

## Description

Creates an issue type scheme. You must specify ids for the issue types

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateIssueTypeScheme(name, description, defaultIssueTypeId, array\_of\_issuetype\_ids) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createIssueTypeScheme(name, description, defaultIssueTypeId, array\_of\_issuetype\_ids) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | Name of the issue type scheme. |
| description | string | Yes | Description of the issue type scheme. May be null |
| defaultIssueTypeId | int | Yes | Default issue type id. |
| array\_of\_issuetype\_ids | int [] | Yes | Issue type ids. Must contain the default issue type id |

## Return Type

[**JIssueTypeScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the issue type scheme.

## Example

```javascript
int [] itsds = {10006,10007,10008,10009,10010,10000};
JIssueTypeScheme sch = createIssueTypeScheme("TT new scheme", "A copy of", 10000, itsds);
```

## See also