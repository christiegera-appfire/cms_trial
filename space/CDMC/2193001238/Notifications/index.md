# Notifications

## Overview

Workflow notifications in Comala Document Management keep you informed about changes in a page’s workflow state. These notifications are triggered by specific workflow events such as page approvals, rejections, or transitions between states.

By default, Comala Document Management sends system-generated notifications based on the active workflow for existing workflows. For example, you will receive an email when assigned as a reviewer or when a document is approved in a [basic approval workflow](/cms_trial/space/CDMC/2193195328/Basic+approval+workflow/).

In addition to the default notifications, you can set up custom email notifications in your workflows. These can be sent during specific state transitions or conditions. You can also customize the message, decide who receives the notifications, and set what they say based on your needs.

## Workflow notifications

Comala Document Management sends email notifications for the following events

- Assignees receive a notification when they are assigned to review a page/blog
- The expiry date has been reached for content with the [Content Expiry workflow](/cms_trial/space/CDMC/2192776431/Content+expiry+workflow/) applied

On-screen notifications are displayed to a user viewing a page on which they have been assigned an approval.

![Comala notification message for approvalassigned user](/cms_trial/assets/fb9c6702-af19-46b7-b1c4-a4097b0c41b8.png)

The message includes details of the approval name and the user who manually assigned the reviewer.

On-screen notification messages are also created, for example, when reviewers have undertaken an approval decision:

![Comala notification email preview](/cms_trial/assets/704bf5a3-9dff-4401-9143-4407282b0f60.png)

For content with the **Content Expiry workflow** applied, when the expiry date is reached, the content state changes to **Expired** and email notifications are sent to users who are watching it.

The email notifications come from `no-reply@appfire.com`.

This is not from the address that normally sends emails related to built-in Confluence functionality.

## Custom notifications

Custom notifications can be added using JSON triggers. A trigger can be set to fire for a specific event and create one or more notifications.

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

A JSON trigger can be added using a [JSON editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/) or a [visual builder](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/).