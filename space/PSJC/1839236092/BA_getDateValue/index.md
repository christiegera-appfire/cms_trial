# BA_getDateValue

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_getDateValue(argv, label) | **Package** | poweraction |
| **Alias** | form\_getDateValue | **Pkg Usage** | getDateValue(argv, label) |

## Description

This will retrieve a date value from the argv array. Note that for the date time picker, the value in the argv variable uses the user's time zone. BA\_getDateValue will convert this value from the user's time zone to the server time zone.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable (predefined variable). |
| label | String | Yes | The label of the date/date time field. |

## Return Type

**Date**

## Example

For the Date type fields let's assume we have the following script:

```javascript
BA_createDatePicker("Start Date", currentDate(), false, true, "Required DatePicker");
```

The date selected in the DatePicker field created above can be obtained in the execution script using the following code:

```javascript
date res = BA_getDateValue(argv, "Start Date");
```

## See also