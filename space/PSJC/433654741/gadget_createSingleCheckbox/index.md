# gadget_createSingleCheckbox

## Description

Creates a single checkbox.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createSingleCheckbox(label, isChecked [, isRequired, fieldDescription])]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| isChecked | Boolean | Yes | Default value. |
| isRequired | Boolean | No | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | No | Description of the field to be displayed immediately under the input box. |

## Return Type

**String []**

The returned value has no meaning

## Example

```javascript
gadget_createSingleCheckbox("No description Checkbox", true);
gadget_createSingleCheckbox("Single Checkbox", true, false, "Required checkbox");
gadget_createSingleCheckbox("Another Checkbox", false, true, "Not required checkbox");
```

## See also