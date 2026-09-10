# createDirectory

## Description

Returns "true" if the directory was created successfully and "false" otherwise. If returned "false" check the log for a detailed reason on why it failed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createDirectory(path\_to\_directory) | **Package** | file |
| **Alias** |  | **Pkg Usage** | createDir(path\_to\_directory) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_directory | String | Yes | Specifies a directory or a path. |

## Return Type

**Boolean (true/false)**

## Example

```javascript
string dir = "C:/myDirectory";
if(directoryExists(dir)){
    print("The directory exists!");
} else {
    if(!createDirectory(dir)){
        print("Failed to create directory " + dir);
    }
}
```

It is recommended that you use forward slashes ( / ) for file paths.

## See also