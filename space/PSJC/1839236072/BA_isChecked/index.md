# BA_isChecked

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_isChecked(argv, label) | **Package** | poweraction |
| **Alias** | form\_isChecked | **Pkg Usage** | isChecked(argv, label) |

## Description

A method for checking whether a checkbox is selected or not.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable (predefined variable). |
| label | String | Yes | The label of the checkbox. |

## Return Type

**Boolean**

Returns true if the box was checked, false otherwise.

## Example

Assume we have the following parameter script:

```javascript
BA_createSingleCheckbox("Single Checkbox", true, false, true, "Required checkbox");
```

The following call is used in the execution script to determine if the checkbox created above is checked:

```javascript
boolean res = BA_isChecked(argv, "Single Checkbox");
```

## See also