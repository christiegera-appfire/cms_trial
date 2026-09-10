# saveURLToFile

## Description

Saves the content of some URL (HTTP GET) to the specified file.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | saveURLToFile(url, file) | **Package** | http |
| **Alias** |  | **Pkg Usage** | saveURLToFile(url, file) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url | String | Yes | Valid URL. No auth is performed. |
| file | String | Yes | Path to the (new) file that will keep the content of the URL. |

## Return Type

**Boolean**

The function returns a boolean indicating if the call succeeded or not.

## Example

```javascript
string testfile="c:/tests/mytempfile.html"; //assuming that folder 'tests' has been already created in c:\ path
if(saveURLToFile("https://kepler-rominfo.com/pages/solutions/jira-plugins", testfile)) {
  //do something with that html
}
```

## See also