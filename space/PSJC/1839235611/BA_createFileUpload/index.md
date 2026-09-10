# BA_createFileUpload

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_createFileUpload(label, isDisabled[, isRequired, fieldDescription]) | **Package** | poweraction |
| **Alias** | form\_createFileUpload | **Pkg Usage** | createFileUpload(label, isDisabled[, isRequired, fieldDescription]) |

## Description

Creates a file upload field. Creates an upload control that enables the users to upload multiple files to a temporary folder. For more details about the temporary file directory, see the Administration Page.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| label | String | Yes | Field label. |
| isDisabled | Boolean | Yes | Specifies whether the field is read-only or no. |
| isRequired | Boolean | No | Specifies whether the field should be marked as required with a dark red asterisk. |
| fieldDescription | String | No | A description of the field to be displayed immediately under the input box. |

## Return Type

**None**

The returned value has no meaning

## Example

```javascript
BA_createFileUpload("file 1", false, true, "description for file 1");
BA_createFileUpload("file 2", true, false, "description for file 2");
```

![Power Scripts for Jira Cloud file upload form component](/cms_trial/assets/d4075fac-5143-4a69-b1e2-aaebda7e4a33.PNG)

## See also