# gadget_createMultiUserPicker

## Description

Creates a multi user picker.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createMultiUserPicker(label, defaultValues, isRequired, fieldDescription) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field |
| defaultValues | String [] | Yes | Few default values or an empty array. If one the default values is not a valid username, it will be discarded and an empty default value will be provided. |
| isRequired | Boolean | Yes | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | Yes | Description of the field to be displayed immediately under the input box. |

## Return Type

**String []**

The returned value has no meaning

## Example

```javascript
gadget_createMultiUserPicker("MultiUserPicker", {"admin", "demouser"}, true, "Required Multi User Picker");
gadget_createMultiUserPicker("Another MultiUserPicker", {"admin", "demouser"}, false, "Not required");
```

## See also