# excelRemoveSheet

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelRemoveSheet(workbookFID, worksheet\_name) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | removeSheet(workbookFID, worksheet\_name) |

## Description

Removes the selected sheet from an open workbook.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| workbookFID | Integer | Yes | The file id of the open workbook. The file id is returned from running the excelOpenWorkbook() routine. |
| worksheet\_name | String | Yes | The name of the worksheet to be deleted |

## Return Type

**Boolean**

Returns true if the operation was successful, false otherwise.

## Example

Opens a workbook, deletes a sheet and then saves and closes the workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
removeSheet(fid, "Venemous Snakes", 4);
closeWorkbook(fid);
```

Result: The 'Venemous Snakes' sheet will be removed.

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387430165) to download the workbook used in this example.

## See also