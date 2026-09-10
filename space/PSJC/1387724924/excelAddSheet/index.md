# excelAddSheet

## Description

Adds a new sheet to the open workbook.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelAddSheet(workbookFID, worksheet\_name [, make\_default]) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | addSheet(workbookFID, worksheet\_name [, make\_default]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | Yes | The name of the worksheet to be added. |
| make\_default | Boolean | No | If the newley added worksheet should be made the default worksheet, true/false. |

## Return Type

**Boolean**

Returns true if the operation was successful, false otherwise.

## Example

Add a new worksheet to an existing workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
addSheet(fid, "Venemous Snakes", true);
closeWorkbook(fid);
```

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387724924) to download the workbook used in this example.

## See also