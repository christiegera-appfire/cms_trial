# gadget_createInput

## Description

Creates a simple text input suitable for short values.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createInput(label, defaultValue[, isRequired, fieldDescription]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| defaultValue | String | Yes | Default value or an empty string. |
| isRequired | Boolean | No | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | No | Description of the field to be displayed immediately under the input box. |

## Return Type

**String**

The returned value has no meaning

## Example

```javascript
gadget_createInput("Default Input", "value");
gadget_createInput("Another Input", "1900", true, "Required Input");
```

## See also