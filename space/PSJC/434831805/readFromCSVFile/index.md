# readFromCSVFile

## Description

Reads the values from the CSV file, returning them to an array, of N rows \* M columns values.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | readFromCSVFile(path, hasHeader [, charset]) | **Package** | file |
| **Alias** |  | **Pkg Usage** | readCSV(path, hasHeader [, charset]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path | String | Yes | Specifies the file name to read from. |
| hasHeader | Boolean | Yes | Specifies if the file has header. |
| charset | String | No | Specifies the charset used to read that file. |

## Return Type

**String []**

The values from the file, as a string array.

## Examples

The basic form will look like this:

```javascript
string [] fileContent = readFromCSVFile("C:/test.csv", true);
```

However it is hardly usable. A better form will look like this:

```javascript
//Suppose we have a CSV file with 3 columns, First Name, Last Name, Age
struct Emp {
  string fName;
  string 
  lName;
  number age;
}

Emp [] fileContent = readFromCSVFile("C:/test.csv", true);
for(Emp e in fileContent) {
  //we can address them now in a better way.... so process row after row
  string s = e.fName + " " + e.lName + " / " + e.age;
  //do smth with that 's'
}
```

Unless calendar dates are in formats SIL can understand, dates should be imported as strings and further parsed afterwards in your SIL program.

1. You can use absolute paths and relative paths to "sil.home".
2. If the header exist, it must not have duplicated columns, otherwise you need to skip it manually.
3. If the file is not found, an error will be raised.

## See also