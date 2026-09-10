# gadget_getMultiValues

## Description

Retrieves the value from a multi select list or a checkbox group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_getMultiValues(argv, label) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable |
| label | String | Yes | The label of the multi select list/checkbox group |

## Return Type

**String []**

## Example

For a script that creates a multi select list like the following

```javascript
gadget_createMultiSelectList("Multiselect", {"a", "b", "c", "d", "e"}, {"a", "c", "e"}, true, "This field is required");
```

The selected values may be obtained with the **gadget\_getMultiValues** function:

```javascript
string[] res = gadget_getMultiValues(argv, "Multiselect");
//res[0] = a
//res[1] = c
//res[2] = e
//The function has returned in this case an array of three strings, "a", "c" and "e".
```

## See also