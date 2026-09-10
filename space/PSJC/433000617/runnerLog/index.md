# runnerLog

## Description

Puts the 'message' on the console of a runner gadget or sil manager. The use of it has no effect in other places besides for the dashboard item or sil manager.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runnerLog(message [, treatAsHtml], percent]) or runnerLog(message [, percent, action]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| message | String | Yes | Specifies the message to be put on the runner console. |
| treatAsHtml | Boolean | No | Specifies either to show the message as a string, or treat it and render it in the browser as HTML code. |
| percent | Integer | No | Specifies the percent to be updated on the progress bar. |
| action | String | No | Specifies the action to be executed (so far, the only action considered is init\_progressBar - to initialize the progress bar; everything else will be ignored) |

## Return Type

**None**

The returned value has no meaning.

## Examples

Returns: Hello John Smith. How are you today?

```javascript
runnerLog("Hello " + userFullName(currentUsername()) + ". How are you today?");
```

Using HTML as output. Returns: This is a red text! (text will be red)

```javascript
runnerLog("<font color='red'>This is a red text!</font>", true);
```

## See also