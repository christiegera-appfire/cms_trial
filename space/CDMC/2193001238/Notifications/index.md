# Notifications

## Overview

Workflow notifications in Comala Document Management keep you informed about changes in a page’s workflow state. These notifications trigger on specific workflow events, such as page approvals, rejections, or transitions between states.

Comala Document Management does not send a built-in email when a reviewer is assigned to an approval or when a document is approved. To be notified of these events by email, configure a custom `send-email` trigger action in your workflow (see [Custom notifications](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/2162163922/Notifications#Custom-notifications) below).

## Workflow notifications

Comala Document Management sends email notifications for the following events

- The expiry date has been reached for content with the [Content Expiry workflow](/cms_trial/space/CDMC/2192776431/Content+expiry+workflow/) applied

To notify reviewers when they are assigned, configure a `send-email` trigger action targeting `@assignee` on the `on-assign` event (see [Custom notifications](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/2162163922/Notifications#Custom-notifications)).

On-screen notification messages are created when reviewers have made an approval decision:

![Comala notification email preview](/cms_trial/assets/92641c37-9fe2-4efd-9283-a1f262056097.png)

For content with the **Content Expiry workflow** applied, when the expiry date is reached, the content state changes to **Expired** and email notifications are sent to users who are watching it.

The email notifications come from `no-reply@appfire.com`.

This is not from the address that normally sends emails related to built-in Confluence functionality.

## Custom notifications

You can add custom notifications using JSON triggers. You can set a trigger to fire for a specific event and create one or more notifications.

**Example Trigger**

```plaintext
[{"event":"on-expire","actions":
[{"action":"send-email","recipients":["@watchers"],
"notification":
{"subject":"${content.title} has expired",
"title":"${content.title} has expired",
"body":"Hello, ${content.link} in the ${content.space} space has expired and needs to be reviewed"}},
{"action":"set-message",
"type":"info",
"title":"Expired",
"body":"The page has expired",
"tags":"state",
"mode":"autoClose"}]}]
```

You can add a JSON trigger using a [JSON editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/) or a [visual builder](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/).