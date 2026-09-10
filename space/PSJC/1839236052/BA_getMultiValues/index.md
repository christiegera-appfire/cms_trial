# BA_getMultiValues

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_getMultiValues(argv, label) | **Package** | poweraction |
| **Alias** | form\_getMultiValues | **Pkg Usage** | getMultiValues(argv, label) |

## Description

Gets the value entered or the selected option for the given field label.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| argv | String [] | Yes | The argv variable (predefined variable). |
| label | String | Yes | The label of the multi select list/checkbox group/file upload field. |

## Return Type

**String []**

String array representing the selected options.

## Examples

### Example 1

For a script that creates a multi select list like the following:

```javascript
BA_createMultiSelectList("Multiselect", {"a", "b", "c", "d", "e"}, {"a", "c", "e"}, false, true, "This field is required");
```

The selected values may be obtained with the BA\_getMultiValues routine:

```javascript
string [] res = BA_getMultiValues(argv, "Multiselect");
//res[0] = a
//res[1] = c
//res[2] = e
//The routine has returned in this case an array of three strings, "a", "c" and "e".
```

### Example 2

Using a file upload field.

```javascript
BA_createFileUpload("File 1", false, true, "Description for file 1");
```

We may obtain the uploads field's value as in the next code sample:

```javascript
string [] res = BA_getSingleValue(argv, "File 1");
//res = "Demo_File.txt|C:\Program Files\Atlassian\Application Data\Jira\kepler\blitz-upload\Demo_File.txt"
```

With a file upload field the routine will return a string array containing pairs of original filename and uploaded path. Even indices will contain original filenames, while odd indices will contain an uploaded path.

## See also