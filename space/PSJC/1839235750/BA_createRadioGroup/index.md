# BA_createRadioGroup

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createRadioGroup(label, options, defaultValue, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createRadioGroup | **Pkg Usage** | createRadioGroup(label, options, defaultValue, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a radio group.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| options | String [] | Yes | A sub-list of the provided options or an empty array. |
| defaultValue | String | Yes | A default value (one of the provided options) or an empty string. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createRadioGroup("radio 1", {"option 1", "option 2"}, "option 2", true, false, "select some options");
BA_createRadioGroup("radio 2", {"option 1", "option 2"}, "", false, true, "select some options");
```

![Power Scripts for Jira Cloud radio button group form component](/cms_trial/assets/7a53605a-ad2d-4293-9f6b-c8f1e81780fc.PNG)

## See also