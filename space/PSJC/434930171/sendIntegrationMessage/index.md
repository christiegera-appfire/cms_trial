# sendIntegrationMessage

## Description

Sends a message to integration such as Slack.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sendIntegrationMessage(name, message or [SlackMessage]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the integration. Make sure that you have an integration configuration added for the specified name. |
| message | String | Yes | The message to be sent |
| SlackMessage | JSlackMessage | Yes | Slack message to be sent |

## Return Type

**None**

## Example

```javascript
JSlackAttachment att1;
att1.pretext = "Optional text that appears above the attachment block";
att1.title = "This is an example of attachment ...";
att1.text = "*Bold* ~strike~ text";
att1.color = "#4286f4";
JSlackAttachment att2;
att2.title = "This is an example of attachment with code.";
att2.text = "'var i = 0; doSomethingWith(i);'";
att2.color = "#f45641";
JSlackMessage message;
message.channel = "C94S1U658";
message.text = "Test slack message with attachment...";
message.attachments = {att1, att2};
return sendIntegrationMessage("SLACK", message);
```

## See also