# gadget_createTextArea

## Description

Creates a text area suitable for longer text values like comments.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createTextArea(label, defaultValue, isDisabled [, rows[, isRequired, fieldDescription]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Specifies a label for the field. |
| defaultValue | String | Yes | Specifies a default value for the text area. |
| rows | number | No | Initial height of the text area (defaults to 5). Some browsers will allow resizing. |
| isRequired | Boolean | No | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | No | Description of the field to be displayed immediately under the input box. |

## Return Type

**String []**

The returned value has no meaning.

## Example

```javascript
gadget_createTextArea("Default Textarea", "Text");
gadget_createTextArea("Textarea with 3 rows", "Three rows", 3);
gadget_createTextArea("Required Textarea", "Required text", 5, true, "Textarea description");
```

## See also