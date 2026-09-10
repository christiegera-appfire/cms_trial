# excelOpenWorkbook

## Description

Opens a workbook so that it may be used in the script.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | excelOpenWorkbook(path\_to\_excel\_file) | **Package** | excel |
| **Alias** |  | **Pkg Usage** | openWorkbook(path\_to\_excel\_file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path\_to\_excel\_file | String | Yes | File path of the workbook to open. |

## Return Type

**Integer**

## Example

Opens a workbook, adds a new worksheet and then saves and closes the workbook.

```javascript
use "excel";
int fid = openWorkbook("snakes.xlsx");
addSheet(fid, "Venemous Snakes", true);
closeWorkbook(fid);
```

Click [here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=SIL%20Excel%20Routines&linkCreation=true&fromPageId=1387266508) to download the workbook used in this example.

## See also