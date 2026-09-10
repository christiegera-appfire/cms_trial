# lastFieldHistory

## Description

Returns the last change details (user, date, field, oldValue, newValue) from the selected issue's history.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | lastFieldHistory(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |

## Return Type

[**JFieldChange**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Examples

### Example 1

```javascript
string[] lastChange = lastFieldHistory(key);
string ret = "Issue " + key + " was last changed on " + lastChange[1] + " by " + userFullName(lastChange[0]);
ret += ": Field " + lastChange[2] + " from>>" + lastChange[3] + "<<to>>" + lastChange[4] + "<<";
return ret;
```

Result: Issue DEMO-5 was last changed on 2013-08-20 16:47:57 by Admin User: Field assignee from >>Admin User<< to >>Test User<<

### Example 2

```javascript
JFieldChange last = lastFieldHistory("TEST -10");
runnerLog ("LFH:" + last.user + "Field:" + last.field + "Val:" + last.oldVal + " -> " + last.newVal);
```

Result: Issue DEMO-5 was last changed on 2013-08-20 16:47:57 by Admin User: Field assignee from >>Admin User<< to >>Test User<<

## See also