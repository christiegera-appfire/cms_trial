# excelSetCell

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelSetCell(workbookFID, value, [worksheet\_name], cell\_addr\_or\_x\_y) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | setCell(workbookFID, value, [worksheet\_name], cell\_addr\_or\_x\_y) |

## Description

Updates the value of the specified cell in the open workbook.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| value | String | No | The value that the cell should be set to. |
| worksheet\_name | String | No | The name of the worksheet the cell is on. |
| cell\_addr\_or\_x\_y | String | No | The cell address, like A1, or the cell coordinates like 2, 3. |

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

Result: A new row with data is added to the worksheet.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387003985) to download the workbook used in this example.

## See also