# BA_createCheckboxGroup

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createCheckboxGroup(label, options, defaultValues, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createCheckboxGroup | **Pkg Usage** | createCheckboxGroup(label, options, defaultValues, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a checkbox group.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| options | String [] | Yes | The list of selectable options. |
| defaultValue | String [] | Yes | A sub-list of the options provided or an empty array. |
| isDisabled | Boolean | Yes | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createCheckboxGroup("cbx 1", {"option 1", "option 2", "option 3"}, {"option 1", "option 3"}, true, false, "select some options");
BA_createCheckboxGroup("cbx 2", {"option 1", "option 2", "option 3"}, "option 1", false, true, "select some options");
```

![Power Scripts for Jira Cloud checkbox group form element](/cms_trial/assets/c4b955ec-95db-46a4-ae4f-2e0a269677e9.PNG)

## See also