# print

## Description

Returns the printable string in the application log. This function is similar to printing a string on the console in any programming language.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | print(variable) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| variable | Any | Yes | Value you want to be printed. The value argument can be any printable characters: strings, chars, numbers, dates, intervals, and so on. |

## Return Type

**None**

## Example

```javascript
if(isNotNull(dueDate))
{
  print("You should complete this task before " + dueDate);
}
else
  print("This task has no deadline!");
```

## See also