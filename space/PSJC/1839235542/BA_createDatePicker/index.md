# BA_createDatePicker

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createDatePicker(label, defaultValue, isDisabled, isRequired, fieldDescription) | **Package** | poweraction |
| **Alias** | form\_createDatePicker | **Pkg Usage** | createDatePicker(label, defaultValue, isDisabled, isRequired, fieldDescription) |

## Description

Creates a date picker.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| defaultValue | Date | Yes | A default value or an empty string. |
| isDisabled | Boolean | Yes | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createDatePicker("date 1", currentDate(), true, false, "description for date 1");
BA_createDatePicker("date 2", (date), false, true, "description for date 2");
```

![Power Scripts for Jira Cloud date picker form field](/cms_trial/assets/7f4e9846-8a75-41b2-a9c8-98a8e9bfae18.PNG)

## See also