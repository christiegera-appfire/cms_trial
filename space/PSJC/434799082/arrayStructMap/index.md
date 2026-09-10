# arrayStructMap

## Description

Returns an indexed array of structs mapped to a given field name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayStructMap(structArray, field) | **Package** | array |
| **Alias** |  | **Pkg Usage** | structMap(structArray, field) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Struct Array | Array of Structs | Yes | An array of structs to be indexed. |
| Field | String | Yes | Name of the field to use as the indexer. |

## Return Type

**String []**

Returns an array of indexed structs.

## Examples

### Example Part 1 - Data for structs

Assume we have a CSV file containing a list of toys. There is a column for the toy name and another for the toys color.

```javascript
name, color
Airplane, White
Bouncy Ball, Blue
Car, Red
Dog, Brown
Elephant, Gray
...
```

### Example Part 2 - Populating structs

With the given CSV data we can quickly populate an array of structs.

```javascript
//define struct
struct _toy {
    string name;
     string color;
}
//create struct array and populate from csv
_toy [] toys = readFromCSVFile("toysList.csv", true);
```

### Example Part 3 - Mapping the struct array

Now that we have a list of structs we can map them to one of the fields.

```javascript
string [] attachmentsCreatedToday;
for(string a in attachments) {
    string [] file = fileInfo(getAttachmentPath(key, a));
    date created = parseDate("yyyy-MM-dd hh:mm:ss", file["created"]);
    if(created > startOfDay(currentDate())) {
        attachmentsCreatedToday += a;
    }
}
return attachmentsCreatedToday;
```

Result: "Blue"

## See also