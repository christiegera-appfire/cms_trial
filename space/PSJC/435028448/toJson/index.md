# toJson

## Description

Converts any given struct, array or primitive parameter to a JSON string. By default, the JSON resulted from the conversion also contains the empty fields (in the case of structures for example) with null values.If you want these to be excepted from the conversion, you will have to set the **convertEmptyFields** flag to false.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toJson(<any struct, array or primitive type> [, convertEmptyFields, writeNull, datesFormat]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| <any struct, array or primitive type> | variable: primitive type, array or struct | Yes | The variable to be converted to JSON |
| convertEmptyFields | Boolean | No | Flag that indicates if empty fields should be converted (if missing or true) or excepted |
| writeNull | Boolean | No | If true: an empty field will have a null value, for example: "emptyField": nullIf false: an empty field will have empty string value, for example: "emptyField": ""Note: the behavior described above applies only for the **convertEmptyFields** flag set to true. |
| datesFormat | String | No | The format used for date formatting (e.g. use “yyyy-MM-dd” if you want your dates to be formatted like this, otherwise it will be defaulted to “yyyy-MM-dd’T’HH:mm:ssZ” |

## Return Type

**String**

## Example

### Colors JSON Example Code

You can look at this function as the preparatory one for the integration with other systems. You build your data structure first and then convert your struct to json to be sent to an external system. This script demonstrates the process of using structs and/or arrays to create JSON output.

```javascript
//Step 1 - define the structs/arrays
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
    color [] colors;
}
//Step 2 - add data to the structs
color red;
red.color = "red";
red.category = "hue";
red.type = "primary";
red.code.rgba = {255, 0, 0, 1};
red.code.hex = "#FF0";
color yellow;
yellow.color = "yellow";
yellow.category = "hue";
yellow.type = "primary";
yellow.code.rgba = {255, 255, 0, 1};
yellow.code.hex = "#FF0";
color blue;
blue.color = "blue";
blue.category = "hue";
blue.type = "primary";
blue.code.rgba = {0, 0, 255, 1};
blue.code.hex = "#00F";
color green;
green.color = "green";
green.category = "hue";
green.type = "primary";
green.code.rgba = {0, 255, 0, 1};
green.code.hex = "#0F0";
colors colors;
colors.colors += red;
colors.colors += yellow;
colors.colors += green;
colors.colors += blue;
//Step 3 - create the JSON
return toJson(colors);
```

Resulting JSON:

```javascript
{
   "colors":[
      {
         "color":"red",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[255,0,0,1],
            "hex":"#FF0"
         }
      },
      {
         "color":"yellow",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[255,255,0,1],
            "hex":"#FF0"
         }
      },
      {
         "color":"green",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[0,255,0,1],
            "hex":"#0F0"
         }
      },
      {
         "color":"blue",
         "category":"hue",
         "type":"primary",
         "code":{
            "rgba":[0,0,255,1],
            "hex":"#00F"
         }
      }
   ]
}
```

## See also