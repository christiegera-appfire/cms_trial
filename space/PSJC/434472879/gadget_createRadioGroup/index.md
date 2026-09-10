# gadget_createRadioGroup

## Description

Creates a radio group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createRadioGroup(label, options, defaultValue[, isRequired, fieldDescription]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| options | String [] | Yes | List of selectable options. |
| defaultValue | String | Yes | Default value (one of the options provided) or an empty string. |
| isRequired | Boolean | No | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | No | Description of the field to be displayed immediately under the input box. |

## Return Type

**String []**

The returned value has no meaning

## Example

```javascript
gadget_createRadioGroup("Simple Radiogroup", {"A", "B", "C"}, "Not required");
gadget_createRadioGroup("Radiogroup 2", {"12", "13", "14", "15","16"}, {"13"}, true, "Required Radio Group");
```

## See also