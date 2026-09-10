# BA_setBlitzAttribute

The use of this function requires the Power Actions add-on be installed and licensed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_setBlitzAttribute(name) | **Package** | poweraction |
| **Alias** |  | **Pkg Usage** | setBlitzAttribute(name) |

## Description

Stores the given attribute as a (name, value) pair in the HTTP session.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Attribute name. |
| value | String | Yes | Attribute value |

## Return Type

**None**

The returned value has no meaning.

## Examples

### Example 1

```javascript
return BA_setBlitzAttribute("userKey", "admin");
```

### Example 2

```javascript
return BA_setBlitzAttribute("city", "Bucharest");
```

## See also