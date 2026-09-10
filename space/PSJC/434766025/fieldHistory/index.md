# fieldHistory

## Description

Returns all the pairs **date + value** for the selected field from the selected issue's history.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fieldHistory(key, history\_field\_name\_or\_id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |
| field name or id | String | Yes | Name or the id of the selected field. |

## Return Type

**String []**

The return value is an array of strings. The strings come in pairs. The first value is a date representing the time when the value was modified and the second value is the content of the requested field at that date.

## Examples

### Example 1

```javascript
//values for field Amount are 2000 at 12.02.2011, 3000 at 13.03.2011 and 4000 at 10.05.2011
string field_name;
string[] field_history;
field_name = "Amount";
field_history = fieldHistory(key, field_name);
```

Result: |12/02/2011|2000|13/03/2011|3000|10/05/2011|4000

### Example 2

```javascript
//values for field Amount are 2000 at 12.02.2011, 3000 at 13.03.2011 and 4000 at 10.05.2011
string field_name;
string[] field_history;
field_history = fieldHistory(key, customfield_10101);	//customfield_10101 = Amount
```

Result: |12/02/2011|2000|13/03/2011|3000|10/05/2011|4000

1. Besides the labels of the custom fields, the name of the standard Jira fields (summary, assignee, and so on) can be used as parameters.
2. If it returns an empty array, you must get the last value of the field from the issue.
3. The second parameter is the field name as it appears in history or the custom field id.

## See also