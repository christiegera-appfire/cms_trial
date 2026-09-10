# runSILInline

## Description

Executes the script with the given arguments.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runSILInline(script, args) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| script | String | Yes | Script to be executed. |
| args | string[] | Yes | Arguments for the script. |

## Return Type

**String[]**

## Example

```javascript
string [] result = runSILInline("return \"SIL is \" + argv[0];", "awesome"); // returns "SIL is awesome"
string script = "number sum = 0; for (string s in argv) { sum += (number)s; } return sum;"; 
string [] argsArr = "1|2|3";
string [] result = runSILInline(script, argsArr); // returns "6"
```

1. If you don't need/have any arguments, pass an empty string for the args parameter.
2. You need to perform all the necessary escapes.

## See also