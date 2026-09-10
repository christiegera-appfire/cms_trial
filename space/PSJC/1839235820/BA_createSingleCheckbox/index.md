# BA_createSingleCheckbox

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createSingleCheckbox(label, isChecked, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createSingleCheckbox | **Pkg Usage** | createSingleCheckbox(label, isChecked, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a single checkbox.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| isChecked | Boolean | Yes | Is the check box checked by default, true or false. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createSingleCheckbox("cbx 1", false, false, false, "description for checkbox 1");
BA_createSingleCheckbox("cbx 2", true, false, false, "description for checkbox 2");
BA_createSingleCheckbox("cbx 3", true, true, false, "description for checkbox 3");
```

![Power Scripts for Jira Cloud checkbox form component](/cms_trial/assets/87abacbe-bc9c-470d-b77d-114c8f0c4488.PNG)

## See also