# gadget_getSingleValue

## Description

Retrieves the value from a text, text area, select list or radio group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | gadget\_getSingleValue(argv, label) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable |
| label | String | Yes | The label of the text/text area/select list/radio group |

## Return Type

**String**

## Example

For any field that may contain only a single string type value we may use the **gadget\_getSingleValue** function. For the following script

```javascript
gadget_createInput("Enter keyword", "demo");
```

We may obtain the field's value as in the next code sample:

```javascript
string res = gadget_getSingleValue(argv, "Enter keyword");
//res = demo
```

## See also