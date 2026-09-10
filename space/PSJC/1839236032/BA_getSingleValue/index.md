# BA_getSingleValue

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_getSingleValue(argv, label) | **Package** | poweraction |
| **Alias** | form\_getSingleValue | **Pkg Usage** | getSingleValue(argv, label) |

## Description

Gets the value entered or the selected option for the given field label.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable (predefined variable). |
| label | String | Yes | The label of the text/text area/select list/radio group field. |

## Return Type

**String**

For a checkbox it will return "checked" if the checkbox was selected or an empty string if not.

## Example

For any field that may contain only a single string type value we may use the BA\_getSingleValue routine. For the following script

```javascript
BA_createInput("Enter keyword", "demo", false);
```

We may obtain the field's value as in the next code sample:

```javascript
string res = BA_getSingleValue(argv, "Enter keyword");
//res = demo
```

## See also