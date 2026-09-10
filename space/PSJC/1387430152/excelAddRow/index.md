# excelAddRow

## Description

Adds a new row to a sheet in a workbook.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelAddRow(workbookFID, [worksheet\_name,] rowIndex) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | addRow(workbookFID, [worksheet\_name,] rowIndex) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | No | The name of a worksheet in the worbook where the row should be added to. |
| rowIndex | Integer | No | The row index that the new row should be added to. |

## Return Type

**Boolean**

Returns true if the operation was successful, false otherwise.

## Example

Add a new row and data to an existing workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
setCurrentSheet(fid, "Venemous Snakes");
addRow(fid, 1);
setCell(fid, "Lawyer Snake", 1, 0);
setCell(fid, "Cheatum Maximus", 1, 1);
closeWorkbook(fid);
```

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387430152) to download the workbook used in this example.

## See also