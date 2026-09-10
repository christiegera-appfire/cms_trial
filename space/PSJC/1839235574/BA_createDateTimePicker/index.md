# BA_createDateTimePicker

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createDateTimePicker(label, defaultValue, isDisabled, isRequired, fieldDescription) | **Package** | poweraction |
| **Alias** | form\_createDateTimePicker | **Pkg Usage** | createDateTimePicker(label, defaultValue, isDisabled, isRequired, fieldDescription) |

## Description

Creates a date time picker. Note that the default value of the date time picker uses the server's timezone, while the value shown to the user uses the user's time zone.

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
BA_createDateTimePicker("date 1", currentDate(), true, false, "description for date 1");
BA_createDateTimePicker("date 2", (date), false, true, "description for date 2");
```

![Power Scripts for Jira Cloud datetime picker form element](/cms_trial/assets/5fb34995-0053-44d8-8221-1c6c61bca530.PNG)

## See also