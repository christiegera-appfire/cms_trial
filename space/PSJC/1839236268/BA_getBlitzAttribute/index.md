# BA_getBlitzAttribute

The use of this function requires the Power Actions add-on be installed and licensed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_getBlitzAttribute(name) | **Package** | poweraction |
| **Alias** |  | **Pkg Usage** | getBlitzAttribute(name) |

## Description

Returns the value stored for the given attribute name or an empty string, if no value is stored for that name. The values are retrieved from the HTTP session, where they have been previously set using the BA\_setBlitzAttribute function.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Attribute name. |

## Return Type

**String**

## Examples

### Example 1

```text
return BA_getBlitzAttribute("userKey");
```

### Example 2

```text
return BA_getBlitzAttribute("city");
```

## See also