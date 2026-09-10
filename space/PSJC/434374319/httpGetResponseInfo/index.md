# httpGetResponseInfo

## Description

Retrieves the complete response information (if existing) from the latest HTTP function call.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGetResponseInfo() | **Package** | http |
| **Alias** |  | **Pkg Usage** | responseInfo() |

## Return Type

[**HttpResponseInfo**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
...
// do some http function call
...
HttpResponseInfo respInfo = httpGetResponseInfo();
runnerLog("Http call ended with status: " + respInfo.statusCode);
runnerLog("Http response error message: " + respInfo.errorMessage);
runnerLog("Http response reason phrase: " + respInfo.reasonPhrase);
runnerLog("Class of last http response: " + respInfo.class);
...
```

## See also