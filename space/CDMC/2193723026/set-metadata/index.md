# set-metadata

## Overview

You can use the `set-metadata` action to create or update metadata of page parameter values when a workflow trigger occurs.

![Comala setmetadata trigger action configuration dialog](/cms_trial/assets/44d658a3-9969-4c94-9463-3d676b86408b.png)

Click [here](/cms_trial/space/CDMC/2192967825/Triggers/) for more details on how to add a trigger to your workflow.

## set-metadata

### Attributes

The following are the supported attributes:

- **action** (`string`) - must be set to `"set-metadata"` to identify the action.
- **name** (`string`) - The name of the metadata field or page parameter.

  - If the name matches an existing **Page Parameter**, then its value will be updated.
  - If the name matches an existing **metadata** field, then the metadata value will be updated.
  - If the name does not exist, a new metadata field will be created.
- **value** (`string`) - The value to be assigned to the specified metadata or page parameter.

## Trigger example

```json
"triggers": [
    {
      "event": "on-assign",
      "actions": [
        {
          "action": "set-metadata",
          "parameters": [
            {
              "name": "Approvers Business",
              "value": "***"
            }
          ]
        },
        {
          "action": "set-metadata",
          "parameters": [
            {
              "name": "Approvers IT-Tech",
              "value": "***"
            }
          ]
        },
        {
          "action": "set-metadata",
          "parameters": [
            {
              "name": "Approvers QA",
              "value": "***"
            }
          ]
        }
      ]
    }
  ]
```

## Syntax

Metadata values can be used in your workflow markup, just like parameters, by referencing them with the format `@metadata_name@`. This lets you dynamically insert values in various parts of the workflow definition.

```json
  "actions": [
    {
      "action": "send-email",
      "recipients": [
        "@Approvers Business@",
        "user1"
      ],
      "notification": {
        "subject": "${content.title} is In Approval State",
        "title": "${content.title} is In Approval State",
        "body": "Hello @Approvers QA@, this document in approval state and needs to be reviewed"
      }
```