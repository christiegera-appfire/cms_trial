# Slack integration

SIL scripts define the message content and specify when messages are sent. The connection supports Slack's formatting options, including text styling, attachments, and color-coding, to make your notifications more readable and organized.

---

## Prerequisites

Before setting up the integration, ensure you have:

- Administrator permissions in your Jira instance.
- Access to create and manage Slack apps in your workspace.

  - Contact your Slack administrator to request permissions.
- Basic understanding of Jira workflows and transitions.
- Familiarity with JSON structures.

  - This is helpful, but not required.

---

## Procedure

To configure your Slack integration, follow these steps:

|  |  |
| --- | --- |
| **Step 1: Obtain a Slack API token** | 1. Visit the [Slack API](https://api.slack.com/) website to create a new Slack app for your workspace, or access an existing Slack app. 2. Configure the app to have the necessary permissions:     1. `chat:write` - permission to post messages    2. `channels:read`  - permission to access channel information 3. Generate and copy the API token. 4. Save this token securely as you'll need it for the Power Scripts configuration.   For security reasons, in Cloud environments, the Slack access token is only visible at the time of creation and cannot be viewed again later. Make sure to store it securely elsewhere in case you need it again. |
| **Step 2: Create a Slack integration in Power Scripts** | 1. In your Jira Cloud instance, go to **Power Scripts** > **Configurations**. 2. Click the **Integrations** tab and select the **Slack** sub-tab. 3. Click **Add Slack integration** andfill in the necessary fields:     - **Name**: Create a unique name for this integration.    - **Access token**: Enter the Slack access token you obtained in Step 1 of this procedure. 4. Click **Save**. The integration displays as a new entry on the *Slack Configurations*page. You can modify or remove a configuration at any time by clicking the **Edit** or **Delete** icons.   You can read more about internal integrations in [Slack's API](https://api.slack.com/internal-integrations) documentation. |

---

## Prepare for implementation

Before creating SIL scripts that send messages to Slack, you need to:

1. Identify the target Slack channels for your notifications.
2. Learn the structure of Slack messages and attachments.
3. Understand how to reference Jira issue data in your messages.

### How to find your Slack channel ID

To send messages to a specific Slack channel, you need the channel's ID.

1. Open Slack in your browser and navigate to the channel you want to use.
2. Reference the URL in your browser's address bar, for example:  
   `https://app.slack.com/client/T12345678/C12345678`  
   The channel ID is specified after the team ID; it starts with `C` followed by alphanumeric characters.

### About message structure

SIL provides predefined structures for creating Slack messages:

| **Structure name** | **Field** | **Type** |  |
| --- | --- | --- | --- |
| JSlackMessage | channel | string | `JSlackMessage.channel`: The Slack channel ID where the message will be posted. |
| text | string | `JSlackMessage.text`: The main message text. |
| attachments | JSlackAttachment[] | `JSlackMessage.attachments`: An array of formatted attachments. |
| JSlackAttachment | pretext | string | `JSlackAttachment.pretext`: Text that appears above the attachment. |
| fallback | string | `JSlackAttachment.fallback`: Plain text for notifications when attachments aren't supported. |
| title | string | `JSlackAttachment.title`: Bold heading for the attachment. |
| title\_link | string | `JSlackAttachment.title_link`: URL that the title links to. |
| text | string | `JSlackAttachment.text`: Main content of the attachment (supports Slack markdown). |
| color | string | `JSlackAttachment.color`: Hex color code for the left border of the attachment |

---

## Implementation example

The following example demonstrates how to use the Slack integration with Jira through SIL scripts. It shows how to create a Slack message with multiple attachments, different colors, and various text formatting styles. The first attachment demonstrates pretext and bold/strikethrough formatting, while the second attachment showcases code formatting with a different color scheme. This approach is useful for creating visually distinct sections in your notifications or for highlighting different types of information within a single message.

```text
JSlackAttachment att1;
att1.pretext = "Optional text that appears above the attachment block";
att1.title = "This is an example of attachment ...";
att1.text = "*Bold* ~strike~ text";
att1.color = "#4286f4";
 
JSlackAttachment att2;
att2.title = "This is an example of attachment with code.";
att2.text = "`var i = 0; doSomethingWith(i);`";
att2.color = "#f45641";
 
JSlackMessage message;
message.channel = "C9S2LC24T";
message.text = "Test slack message with attachment...";
message.attachments = {att1, att2};
 
return sendIntegrationMessage("SLACK", message);
```

---

## More configuration guides