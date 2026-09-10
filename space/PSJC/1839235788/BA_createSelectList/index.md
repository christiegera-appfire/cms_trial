# BA_createSelectList

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createSelectList(label, options, defaultValue, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createSelectList | **Pkg Usage** | createSelectList(label, options, defaultValue, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a single select list.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| options | String [] | Yes | A sub-list of the provided options or an empty array. |
| defaultValue | String | Yes | A default value (one of the provided options) or an empty string. |
| isDisabled | Boolean | No | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createSelectList("sel 1", {"option 1", "option 2"}, "option 2", true, false, "select some options");
BA_createSelectList("sel 2", {"option 1", "option 2"}, "", false, true, "select some other options");
```

![Power Scripts for Jira Cloud single select list form element](/cms_trial/assets/c7705839-ba07-4bd9-b788-0d82b18e512a.PNG)

## See also