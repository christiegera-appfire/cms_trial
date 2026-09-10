# excelGetCell

## Description

Gets the string value from the specified cell.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelGetCell(workbookFID, [worksheet\_name], cell\_addr\_or\_x\_y) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | getCell(workbookFID, [worksheet\_name], cell\_addr\_or\_x\_y) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | No | The name of the worksheet the cell is on. |
| cell\_addr\_or\_x\_y | String | No | The cell address, like A1, or the cell coordinates like 2, 3. |

## Return Type

**String**

## Example

Get the values from cells in a workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
string name = getCell(fid, "Venemous Snakes", "A2");
string species = getCell(fid, "Venemous Snakes", 1, 1);
runnerLog(name + " - " + species);
closeWorkbook(fid);
```

Result: Mainland Tigersnake - Notechis Scutatus. Note that the row index used to get the species name is 1 even though the cell address would be B2. This is because the cell index starts at 0.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1388118090) to download the workbook used in this example.

## See also