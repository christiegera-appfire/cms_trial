# currentSilScript

## Description

Returns the current running SIL script name.

When you run the script directly from the editor, the content (code) of the script is ran and not the file, so you won't be able to retrieve the file name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | currentSilScript() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**string**

## Example

```javascript
string scriptName = currentSilScript();
```

Returns the name of the current running script.

## See also