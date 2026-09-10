# gadget_getMultiUserPickerValue

## Description

Retrieves the value from a multi user picker.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_getMultiUserPickerValue(argv, label) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable |
| label | String | Yes | The label of the multi user picker |

## Return Type

**String []**

## Example

Assume we have the following script that creates a multi user picker:

```javascript
gadget_createMultiUserPicker("MultiUserPicker", {"admin", "demouser"}, true, "Required Multi User Picker");
```

in order to retrieve the values entered in the field above we need to use the **gadget\_getMultiUserPicker** function as follows:

```javascript
string[] res = gadget_getMultiUserPickerValue(argv, "MultiUserPicker");
//res[0] = admin
//res[1] = demouser
//The function has returned in this case an array of two strings, "admin" and "demouser".
```

## See also