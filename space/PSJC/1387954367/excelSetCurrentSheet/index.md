# excelSetCurrentSheet

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelSetCurrentSheet(workbookFID, worksheet\_name\_or\_index) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | setCurrentSheet(workbookFID, worksheet\_name\_or\_index) |

## Description

Specifies the current sheet by name or index that subsequent processes should use.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name\_or\_index | String | Yes | The name or index of the worksheet that should be set as current (index starts at 0). |

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
setCurrentSheet(fid, "Non-Venemous Snakes");
addRow(fid, 1);
closeWorkbook(fid);
```

Result: A new row is first added to the Venemous Snake sheet then a new row is added to the Non-Venemous Snake sheet.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387954367) to download the workbook used in this example.

## See also