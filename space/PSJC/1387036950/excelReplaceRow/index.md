# excelReplaceRow

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelReplaceRow(workbookFID, [worksheet\_name,] rowIndex) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | replaceRow(workbookFID, [worksheet\_name,] rowIndex) |

## Description

Clears the specified row without impacting the index of any rows beneath of it.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | No | The name of the worksheet the row is on. |
| rowIndex | Integer | Yes | The row index of the row to be cleared (index starts at 0). |

## Return Type

**Boolean**

Returns true if the operation was successful, false otherwise.

## Example

Opens a workbook, clears a row and then saves and closes the workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
replaceRow(fid, "Venemous Snakes", 4);
closeWorkbook(fid);
```

Result: The row containing the Blue Krait snake (row 5) will be replaced with empty cells.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387036950) to download the workbook used in this example.

## See also