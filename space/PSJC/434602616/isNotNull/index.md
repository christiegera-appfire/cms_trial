# isNotNull

## Description

Checks if the provided variable is not null or has a value associated and returns true. Otherwise returns false.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | currentSilScript() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| variable | Any | Yes | Value you want to test. Value argument can be a string or a variable of any type. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
if(isNotNull(reporter))
{
  assignee = reporter;
}
```

**isNotNull** returns "true" if the variable has a value attached (including **zero** for numeric variables or **blank** for character/string).

## See also