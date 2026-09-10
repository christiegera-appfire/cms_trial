# BA_createMultiSelectList

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createMultiSelectList(label, options, defaultValues, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createMultiSelectList | **Pkg Usage** | createMultiSelectList(label, options, defaultValues, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a multi select list.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| options | String [] | Yes | A sub-list of the provided options or an empty array. |
| defaultValue | String [] | Yes | A sub-list of the provided options or an empty array. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createMultiSelectList("msel 1", {"option 1", "option 2", "option 3"}, {"option 1", "option 3"}, true, false, "select some options");
BA_createMultiSelectList("msel 2", {"option 1", "option 2", "option 3"}, "", false, true, "select some options");
```

![Power Scripts for Jira Cloud multiselect list form element](/cms_trial/assets/ce93c577-5676-43a0-a9b7-535c0a40b651.PNG)

## See also