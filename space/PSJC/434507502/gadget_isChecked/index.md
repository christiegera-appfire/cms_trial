# gadget_isChecked

## Description

Verifies if a checkbox is selected or not.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_isChecked(argv, label) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable |
| label | String | Yes | The label of the checkbox |

## Return Type

**Boolean**

## Example

Assume we have the following parameter script:

```javascript
gadget_createSingleCheckbox("Single Checkbox", true, false, "Required checkbox");
```

The following call is used in the execution script to determine if the checkbox created above is checked:

```javascript
boolean res = gadget_isChecked(argv, "Single Checkbox");
```

## See also