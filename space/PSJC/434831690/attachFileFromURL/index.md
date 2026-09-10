# attachFileFromURL

## Description

Adds an attachment located on an URL path to a selected issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | attachFileFromURL(url\_to\_file, issue) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url to file | String | Yes | URL path to the file. |
| issue key | String | Yes | Key of the issue the file will be attached to. |

## Return Type

**Boolean (true/false)**

The return value represents the success of the attachment process. If the function returns "true" the file was attached successfully.

## Example

```javascript
string url_to_file;
string issueKey;
url_to_file = "http://otherServer/generateForm.aspx?PackageName=customField_10192";
issueKey = "PRJ-239";
attachFileFromURL(url_to_file, issueKey);
```

Result: Returns **True** if the file is at the selected location and the issue exists, meaning the file was attached. Returns **False** if any of the conditions stated before are not met.

If an error occurs, the function will return "false" and the error message will be visible in the log.

## See also