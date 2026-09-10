# toJiraDateFormat

## Description

Displays the given date using Jira format.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toJiraDateFormat(date\_as\_string, [includeTime]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date\_as\_string | String | Yes | Date given as a string that will be converted to Jira format. |
| includeTime | Boolean | No | "True" if you want to include the time to the new format and "false" if not. |

## Return Type

**String**

The return value represents the converted date.

## Examples

### Example 1

Example 1Let's consider the following SIL code:

```javascript
return toJiraDateFormat("2017-04-19", true);
```

This will return: 19/Apr/17 12:00 AM

### Example 2

By running this code:

```javascript
return toJiraDateFormat("2017-04-19", false);
```

The result will be: 19/Apr/17

### Example 3

By running this code:

```javascript
return toJiraDateFormat("2017-04-19");
```

he result will be: 19/Apr/17

## See also