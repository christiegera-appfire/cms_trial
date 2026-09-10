# excelCloseWorkbook

## Description

Saves and closes the workbook that was opened at the beginning of the process.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelCloseWorkbook(workbookFID) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | closeWorkbook(workbookFID) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the workbook that should be closed. The file id is returned from running the excelOpenWorkbook() routine. |

## Return Type

**None**

The return value has no meaning.

## Example

Add a new worksheet to an existing workbook and then saves and closes the workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
addSheet(fid, "Venemous Snakes", true);
closeWorkbook(fid);
```

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387561047) to download the workbook used in this example.

## See also