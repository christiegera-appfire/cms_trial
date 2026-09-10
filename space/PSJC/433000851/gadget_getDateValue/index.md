# gadget_getDateValue

## Description

Retrieves the date from a datePicker or dateTimePicker.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_getDateValue(argv, label) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable |
| label | String | Yes | The label of the datePicker |

## Return Type

**Date**

## Example

For the Date type fields let's assume we have the following script:

```javascript
gadget_createDatePicker("Start Date", currentDate(), true, "Required DatePicker");
```

The date selected in the DatePicker field created above can be obtained in the execution script using the following code:

```javascript
date res = gadget_getDateValue(argv, "Start Date");
```

## See also