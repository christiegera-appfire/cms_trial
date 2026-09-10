# Workflow elements translated from data center

## Overview

Comala Document Management Cloud workflows have different features and functionality. When using the Atlassian Confluence Cloud Migration Assistant to migrate to Confluence Cloud or using the **Workflow Translator for Cloud,** some hosted workflow elements are not translated to a cloud-compatible workflow:

## Workflow elements translated to cloud-compatible JSON

Workflow Translator for Cloud translates the following elements and their parameters of the hosted app workflow into cloud-compatible code.

- Workflow

  - name
  - description (if present)
  - **workflow parameters** 6.18.0+
  - **state**

    - name
    - description (if present)
    - final
    - color
    - due date 6.18.0+
  - **state transitions**

    - select\*
    - approved
    - rejected
    - updated
    - expired
  - **approval**

    - name
    - description ((if present)
    - approve button label (if present)
    - reject button label (if present)
    - credentials 6.18.0+
    - minimum 6.18.0+
    - assignable 6.18.0+
    - user 6.18.0+
    - group 6.18.0+
    - selectedapprover and selectedapprovers 6.18.0+
  - **trigger** v7.6.3+

    - Workflow triggers are translated based on their designated events, even if some conditions or actions in the trigger are unsupported in the Cloud
    - A trigger is translated regardless of unsupported conditions or actions, which will be omitted from the translation
    - Triggers translated by the tool need to be reviewed in the Cloud environment. They can be adjusted using the Cloud visual editor or code editor to meet specific requirements

The **submit** transition is not translated directly. When present in the hosted app workflow, it is created in the cloud-compatible JSON code template as a `"select"` transition with a single destination state.

## What is not translated to cloud-compatible code?

Unsupported workflow elements are excluded from the cloud-compatible JSON code translation.

In the cloud, **unsupported workflow parameters** include

For the workflow

- `header` parameter
- `footer` parameter

For a workflow **state**

- `hideselection` parameter

  - Hiding a user state selection in the workflow state dialog box is not available in the cloud.
- `hidefrompath` parameter

  - A state cannot be hidden from the progress bar in the workflow state dialog box in the cloud.
- `taskable` parameter

  - Workflow tasks, including manual addition by a user, are not supported in the cloud.
- `changeduedate` parameter

  - By default, the user can edit a state's due date in the cloud.

Other elements not translated include:

- **Read Confirmations** are not translated. In Confluence Cloud, read confirmations must be added by installing and using the [Comala Read Confirmations Cloud app](https://marketplace.atlassian.com/apps/1222969/comala-read-confirmations?hosting=cloud&tab=overview)

The following are translated but have different functionalities in the cloud:

- **Workflow parameters**

  - [Workflow parameters](/cms_trial/space/CDMC/2192837939/Parameters/) can be created and used in the cloud workflow, but have different functionality from those in the server app workflow.
- **Approvals**

  - [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/) are available in the cloud, but there are different options for managing reviewers.
- **Workflow triggers**

  - [Workflow triggers](/cms_trial/space/CDMC/2192967825/Triggers/) are translated into corresponding workflow events in the cloud, but function differently compared to the hosted app.
  - Some trigger events are not supported as there are no corresponding events in the cloud, and they are omitted from the JSON code.
  - Triggers can also include conditions and actions not supported in the cloud. In such cases, while the trigger is translated, the unsupported conditions and actions are omitted.
- **Workflow final state**

  - The [workflow final state](/cms_trial/space/CDMC/2193066115/States/) has a different functionality from the **final** state in the cloud workflow. The **final** state does not add or change restrictions on who can view the **workflow draft version** content or the **workflow approved version** content.
- **Metadata macros used in triggers**

  - Only the **set-metadata macro** is translated into a cloud-compatible JSON workflow. The get-metadata macro is not translated when included in a workflow trigger, but it is available in the cloud as a page macro to display page metadata values on the document.

## Translation of workflow triggers

v7.6.3+

[Workflow triggers](/cms_trial/space/CDMC/2192967825/Triggers/) are available in a cloud workflow, but have different functionality from the hosted app workflow trigger. The **Workflow Translator for Cloud** translates data center workflow triggers based on their events to their corresponding Cloud trigger event.

However, some data center workflow trigger conditions and actions are unsupported in the Cloud. This does not prevent trigger translation, but the translated workflow excludes unsupported conditions and actions. These are omitted from the cloud workflow template. In these cases, you need to review the use of the workflow trigger in the Cloud and the conditions and actions that support your process needs.

This approach simplifies migration while allowing flexibility for future customization and functionality expansion:

In addition, the workflow visual editor in the Confluence Cloud app now includes an option to add and edit a workflow trigger:

![contentId-2232485018](/cms_trial/assets/ef04e5e1-e706-465e-a0bd-955ea1bb2dcc.png)

#### Translation of workflow trigger events

The following workflow trigger events are translated into their equivalent Cloud events to align with the Cloud interface and future functionality:

| **Data Center workflow trigger event** | **Cloud workflow trigger event** | **Data Center release** |
| --- | --- | --- |
| `pageapprovalassigned` | `"on-assign"` | v7.6.3+ |
| `statechanged` | `"on-change-state"` | v7.6.3+ |
| `approvalunassigned` | `"on-unassign"` | v7.6.3+ |
| `pageapproved` | `"on-approve"` | v7.6.3+ |
| `stateexpired` | `"on-expire"` | v7.6.3+ |
| `pagerejected` | `"on-reject"` | v7.6.3+ |

Workflow trigger events without a corresponding cloud event are not translated, even if they include a trigger action that has a cloud equivalent.

#### **Translation of workflow trigger conditions**

Three workflow trigger conditions are available in the cloud.

| **Data Center workflow trigger condition** | **Cloud workflow trigger condition** | **Notes** | **Data Center release** |
| --- | --- | --- | --- |
| `state` | `state` | Triggers in the cloud only support three conditions for workflow trigger events:   - `state` - `final` - `initial`   The `initial` condition in the cloud is related to the initial state in the workflow. This is not compatible with the data center condition of the same name, as it sets the condition for the initial occurrence of a named state in the workflow. | v7.6.3+ |
| `final` | `final` |

All other trigger conditions are ignored when translating the workflow to cloud-compatible JSON.

#### **Translation of workflow trigger actions**

The following workflow trigger actions are translated into their equivalent Cloud actions to align with the Cloud interface and future functionality:

| **Data Center workflow trigger action** | **Cloud workflow trigger action** | **Notes** | **Data Center release** |
| --- | --- | --- | --- |
| `set-state` | `"change-state"` | Supported parameters:   - `state` parameter is `"state"`   Unsupported parameters:   - `page` | v7.6.3+ |
| `publish-page` | `"publish-page"` | No parameters.  Only used with Comala Publishing app integration. | v7.6.3+ |
| `approve-page` | `"approve"` | Supported parameters:   - `approval` - name of the approval   Unsupported parameters:   - `comment` - `credentials` | v7.6.3+ |
| `reject-page` | `"reject"` | Same as `approve-page`. | v7.6.3+ |
| `set-state-expiry` | `"set-expiration"` | Map `duedate`. | v7.6.3+ |
| `set-message` | `"set-message"` and `"clean-messages"` | Supported parameters:   - `body` - `type`   When the `body` is empty, the cloud action is `"clean-messages"`. | v7.6.3+ |
| `send-email` | `"send-email"` | Map `body` and `subject`; `user` becomes `recipients`. | v7.6.3+ |
| `add-restriction` | `"add-restrictions"` | Limited support; ignore unsupported parameters  The restrictions parameter value is translated with   - user - group - workflow user type parameter - workflow group type parameter   The cloud app restrictions parameter accepts Confluence smart values @watchers, @creator, and @lastUpdatedBy |  |
| `remove-restriction` | `"remove-restrictions"` | Limited support; ignore unsupported parameters  The restrictions parameter value is translated with   - user - group - workflow user type parameter - workflow group type parameter   The cloud app restrictions parameter accepts Confluence smart values @watchers, @creator, and @lastUpdatedBy | v7.6.3+ |
| `set-restrictions` | `"set-restrictions"` | The restrictions parameter value is translated with   - user - group - Confluence smart values - workflow user type parameter - workflow group type parameter   The cloud app restrictions parameter accepts Confluence smart values @watchers, @creator, and @lastUpdatedBy. | 7.6.3+ |
| `set-metadata` | `"set-metadata"` | Supports creating or updating metadata or page parameter values. | v7.9.1+ |
| `set-label` | `"add-labels"` | The boolean `children` parameter is translated and has the same functionality as the hosted app:   - If its value is `true`, the action adds the specified label(s) only to the immediate direct child pages. | v7.7.0+ |
| `remove-label` | `"remove-labels"` | The boolean `children` parameter is translated and has the same functionality as the hosted app:   - If its value is `true`, the action removes the specified label(s) only from the immediate direct child pages.   The cloud app also includes the `clean-labels` trigger action to remove all the labels on a page or blog post. | v7.7.0+ |

Not all of the trigger action parameters are supported in the cloud. The translated workflow template omits these unsupported parameters.

## New workflow trigger actions in the cloud

The following workflow trigger actions are new in the Cloud app and have no equivalent data center workflow trigger action:

- `"assign"` - assign a Confluence user or Confluence user group as a reviewer for an approval
- `"unassign"`- unassign a reviewer from an approval
- `"clear-expiration"` - removes the due date for a state
- `"clean-messages"` - removes any on-screen message notifications (this action is added to a translated workflow when the body of the data center messages action is empty)
- `"clean-labels"` - removes all the labels from a page or from the immediate child pages
- `"copy-page"` - copies the current page as one of a child of the current page, child of a named page, or child of a homepage of a specified space.

As the cloud app has no draft-view restriction (see the [Product comparison](https://appfire.atlassian.net/wiki/spaces/AWPD/pages/617493913) page), after a document has transitioned to the final workflow state, the `"copy-page"` trigger action is useful as a workaround when you want to provide users with view-only access to a copy of the latest approved final state version.

## Related pages

- [Workflow elements and concepts in Comala Document Management Cloud](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/)
- [Product comparison](https://appfire.atlassian.net/wiki/spaces/AWPD/pages/617493913)