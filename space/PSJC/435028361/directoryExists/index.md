# directoryExists

## Description

Returns "true" if the directory exists and "false" otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | directoryExists(path\_to\_directory) | **Package** | file |
| **Alias** |  | **Pkg Usage** | dirExists(path\_to\_directory) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_directory | String | Yes | Specifies the name of the directory to locate. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
if(directoryExists("C:/myDirectory")){
    print("The directory exists!");
} else {
    print("The directory does not exist!");
}
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also