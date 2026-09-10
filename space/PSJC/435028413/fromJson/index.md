# fromJson

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fromJson(json) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Converts the given JSON string into a SIL type (can be a primitive, array or struct).

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| json | String | Yes | The JSON to be converted. |

## Return Type

**String**

Variable return type depends on the left hand side operator type.

## Examples

### Structs

Both examples show how JSON data can be parsed into an array or struct collections. Both examples use the following struct definitions:

```javascript
struct code {
    number [] rgba;
    string hex;
}
struct color {
    string color;
    string category;
    string type;
    code code;
}
struct colors {
    color [] colors;}
```

### Example 1 - Reading JSON from a file

```javascript
string json = readFromTextFile("C:\\colors.json");

colors [] cData;
cData = fromJson(json);
return cData.colors[0].color;
```

### Example 2 - Reading JSON from a variable

```javascript
string json = "{\"colors\":[{\"color\":\"red\",\"category\":\"hue\",\"type\":\"primary\",\"code\":{\"rgba\":[255,0,0,1],\"hex\":\"#FF0\"}}]}";
colors [] cData;
cData = fromJson(json);
return cData.colors[0].color;
```

## See also