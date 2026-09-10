# BA_createTextArea

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createTextArea(label, defaultValue, isDisabled [, rows[, isRequired, fieldDescription]]) | **Package** | poweraction |
| **Alias** | form\_createTextArea | **Pkg Usage** | createTextArea(label, defaultValue, isDisabled [, rows[, isRequired, fieldDescription]]) |

## Description

Creates a text area suitable for longer text values like comments.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| defaultValue | String | Yes | Specifies a default value for the text area. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| rows | Number | No | The initial height of the text area (defaults to 5). Certain browsers allow resizing. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createTextArea("text 1", "", false , 5, false, "description 1");
BA_createTextArea("text 2", "mini textarea", false , 2, false, "description 2");
BA_createTextArea("text 3", "maxi textarea", true , 10, false, "description 3");
```

![Power Scripts for Jira Cloud textarea form field](/cms_trial/assets/dfc90342-3197-46c3-83e8-acdade5267af.PNG)

## See also