# excelRemoveRow

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelRemoveRow(workbookFID, [worksheet\_name,] rowIndex) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | removeRow(workbookFID, [worksheet\_name,] rowIndex) |

## Description

Removes a row in the opened workbook.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | No | The name of the worksheet the row is on. |
| rowIndex | Integer | Yes | The row index of the row to be deleted (index starts at 0). |

## Return Type

**Boolean**

Returns true if the operation was successful, false otherwise.

## Example

Opens a workbook, deletes a row and then saves and closes the workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
removeRow(fid, "Venemous Snakes", 4);
closeWorkbook(fid);
```

Result: The row containg the Blue Krait snake (row 5) will be deleted.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1388118100) to download the workbook used in this example.

## See also