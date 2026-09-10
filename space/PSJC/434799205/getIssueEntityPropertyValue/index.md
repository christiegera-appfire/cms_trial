# getIssueEntityPropertyValue

## Description

Returns the entity property value as a String.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIssueEntityPropertyValue(issueKey, propertyKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Key of the selected issue. |
| propertyKey | String | Yes | Property key |

## Return Type

**String**

The returned value represents the entity property of the issue.

## Example

```javascript
return getIssueProperty("JSD-2", "request.channel.type");
```

## See also