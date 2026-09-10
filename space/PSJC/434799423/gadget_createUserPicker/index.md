# gadget_createUserPicker

## Description

Creates a user picker.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createUserPicker(label, defaultValue, isDisabled, isRequired, fieldDescription) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| defaultValue | String | Yes | Default value or an empty string. If the default value is not a valid username, it will be discarded and an empty default value will be provided. |
| isRequired | Boolean | Yes | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | Yes | Description of the field to be displayed immediately under the input box. |

## Return Type

**String**

The returned value has no meaning

## Example

```javascript
gadget_createUserPicker("User Picker", "admin", true, "Required UserPicker");
gadget_createUserPicker("Another User Picker", "admin", false, "Not required UserPicker");
```

## See also