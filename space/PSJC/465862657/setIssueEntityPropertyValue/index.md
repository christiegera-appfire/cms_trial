# setIssueEntityPropertyValue

## Description

Adds or updates an already existing property of an entity (see [jira entity properties](https://developer.atlassian.com/cloud/jira/platform/jira-entity-properties/))

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | setIssueEntityPropertyValue(issueKey, propertyKey, propertyValue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Key of the selected issue. |
| propertyKey | String | Yes | Property key |
| propertyValue | String | Yes | Value to set for the property. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
setIssueEntityPropertyValue("CD-1", "day1", "Monday");
```

## See also