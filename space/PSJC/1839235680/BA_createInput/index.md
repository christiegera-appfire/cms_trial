# BA_createInput

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createInput(label, defaultValue, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createInput | **Pkg Usage** | createInput(label, defaultValue, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a simple text input suitable for short values. For longer text values like comments, see BA\_createTextArea.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| defaultValue | String | Yes | A default value or an empty string. |
| isDisabled | Boolean | Yes | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createInput("input 1", "", false, false, "description of field 1");
BA_createInput("input 2", "default value for field 2", false, false, "description of field 2");
BA_createInput("input 3", "read-only default value for field 3", true, false, "description of field 3");
```

![Power Scripts for Jira Cloud input text form field](/cms_trial/assets/5f0c2a60-6909-4b8f-9cdd-88e4a610a7e3.PNG)

## See also