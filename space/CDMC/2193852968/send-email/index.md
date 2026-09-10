# send-email

## Overview

Using the **send-email action** in a workflow trigger lets you send customized emails. The trigger action sends a custom email when a chosen workflow event occurs, such as a change of workflow state or the expiration of a state due date.

![Comala visual editor sendemail trigger action with recipients configured](/cms_trial/assets/854cf86d-999e-4a16-92f7-adf6fb803778.png)

You must add at least one recipient to the custom email. This must be at least one value from any of the following:

- email address of a recipient
- Confluence user
- Confluence user group
- Confluence smart value, such as **watchers** of the page, the page **creator**, and the last user who edited the page
- a workflow user parameter or group parameter

When the workflow trigger event occurs, the trigger checks that all required conditions are met. If these conditions and met, the `"send-email"` action sends an email to the specified recipients.

## `"send-email"`

The trigger action `"send-email"` sends a custom email to one or more specified recipients.

- **action (*****send-email*****)**
- **recipients (array)** **❗️**Recipients to send the email to (***at least one recipient value must be added***). A comma-separated list of one or more recipients is added using a combination of:

  - one or more `email` addresses
  - one or more users using `{"user"="userID"}` specifying the Atlassian `userID`.**†**
  - one or more user groups `{"group":"groupID"}` specifying Atlassian `groupID`**‡** or the Atlassian `groupName`**‡**
  - one or more **user**-**type workflow parameters** using `@userTypeParameterName@`(see [workflow parameter references](/cms_trial/space/CDMC/2192837939/Parameters/))
  - one or more **group type workflow parameters** using `@groupTypeParameterName@`(see [workflow parameter references](/cms_trial/space/CDMC/2192837939/Parameters/))
  - One or more of the following Confluence `value references`

    - `@watchers` (set at document level only)
    - `@lastUpdatedBy`
    - `@creator`
    - `@assignee`(sends the email to the user assigned to the page.

For `@assignee` to work correctly, the assigner and assignee must be different users.

`@assignee` value is currently supported only for the [on-assign](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CDMC&title=on-assign%20event) and [on-unassign](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CDMC&title=on-unassign%20event) events, as the assignees are resolved from these events.

- **notification (object) ❗️** Notification holder. This includes the following parameters as a comma-separated list within curly brackets:

  - `"title"` (optional)
  - `"subject"` **❗️**
  - `"body"` **❗️**

---

### ❗️Mandatory parameters

**recipients**

At least one value for **recipients** must be included

**notification**

The **"notification"** holder is required. This must include both

- **"subject"**
- **"body"**

---

**†** Each **Confluence user** must be specified individually using `{"user":"userID"}`. Add multiple Confluence users in a comma-separated list `{"user":"userID_One"},{"user":"userID_Two"}, ...`

**‡** Each **Confluence group** must be specified individually using `{"group":"groupID"}` and/or `{"group":"groupName"}`. Add multiple Confluence groups in a comma-separated list `{"group":"groupID_One"},{"group":"groupID_Two"},{"group":"groupName_Users1"},{"group":"groupName_Users2"}, ...`

You can embed any of the following as part of the text value in the `"title"`, `"subject"`, and `"body"` parameters

- `${content.title}` - inserts the name of the page or blog post
- `${content.link}` - inserts the link of the page or blog post
- `${content.space}` - inserts the name of the space

### Example trigger code

```text
"triggers":
[
  {"event": "on-change-state",
    "conditions":
    [
      {"state": "Review"}
    ],
    "actions":
    [
      {"action": "send-email",
        "recipients":
        [
          "@creator",
          "@watchers",
          "@lastUpdatedBy",
          "@user_type_parameter_1@",
          "@user_type_parameter_2@",
          "@group_type_parameter_1@",
          "@group_type_parameter_2@",
          "email_1@email.com",
          "email_2@email.com",
          {"user": "user_ID_1"},
          {"user": "user_ID_2"},
          {"group": "group_ID_1"},
          {"group": "group_ID_2"},
          {"group": "group_Name_1"},
          {"group": "group_Name_2"}
        ],
        "notification":
        {"subject": "${content.title} is In Review State",
          "title": "${content.title} is In Review State",
          "body": "Hello, ${content.link} in the ${content.space} space is in review state."
        }
      }
    ]
  }
]
```

On-screen notification messages can be created using the `"set-message"` trigger action.

Workflow trigger-generated email '*failure to send'* errors are included in the Confluence log.