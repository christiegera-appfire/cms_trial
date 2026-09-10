# BA_createUserPicker

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createUserPicker(label, defaultValue, isDisabled, isRequired, fieldDescription) | **Package** | poweraction |
| **Alias** | form\_createUserPicker | **Pkg Usage** | createUserPicker(label, defaultValue, isDisabled, isRequired, fieldDescription) |

## Description

Creates a user picker.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| defaultValue | String | Yes | A default value or an empty string. If the default value is not a valid username, it will be discarded and an empty default value will be provided. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createUserPicker("up 1", "admin", true, false, "description for up 1");
BA_createUserPicker("up 2", "", false, true, "description for up 2");
```

![Power Scripts for Jira Cloud user picker form element](/cms_trial/assets/6dee439f-a74c-4a50-aa08-abc81a2edfbf.PNG)

## See also