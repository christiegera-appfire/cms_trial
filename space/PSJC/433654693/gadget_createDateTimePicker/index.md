# gadget_createDateTimePicker

## Description

Creates a date/time picker.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createDateTimePicker(label, defaultValue, isRequired, fieldDescription) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| defaultValue | Date | Yes | Default value or an empty string. |
| isRequired | Boolean | Yes | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | Yes | Description of the field to be displayed immediately under the input box. |

## Return Type

**String**

The returned value has no meaning

## Example

```javascript
gadget_createDateTimePicker("DateTimePicker", currentDate(), true, "Required DateTimePicker");
gadget_createDateTimePicker("Another DateTimePicker", (date)"2014-09-09", false, "Not required DateTimePicker");
```

## See also