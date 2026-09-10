# gadget_createMultiSelectList

## Description

Creates a multi select list.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_createMultiSelectList(label, options, defaultValues[, isRequired, fieldDescription]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Label of the field. |
| options | String [] | Yes | List of selectable options. |
| defaultValue | String [] | Yes | Sub-list of the options provided or an empty array. |
| isRequired | Boolean | No | Specifies if the field is should be marked as required with a dark red asterisk. Note that marking the field as required does not add any validation. |
| fieldDescription | String | No | Description of the field to be displayed immediately under the input box. |

## Return Type

**String []**

The returned value has no meaning

## Example

```javascript
gadget_createMultiSelectList("Default Multiselect", {"A", "B", "C", "D", "E"}, {"C", "D"});
gadget_createMultiSelectList("Required Multiselect", {"a", "b", "c", "d", "e"}, {"a", "c", "e"}, true, "This field is required");
```

## See also