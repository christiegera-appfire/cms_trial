# Migrate data center variables to cloud

## Overview

When you migrate a Comala Document Management Data Center workflow to Cloud, CDM translates its value references to the equivalent Cloud variables. For example, `@creator@` becomes `@Content.CreatorId@`.

Use this page to find the Cloud equivalents of Data Center value references and identify any references that need attention after migration.

For information about using variables in Cloud workflows, see [Variables](/cms_trial/space/CDMC/3842114162/Variables/).

## Where variables are translated

During migration, **Comala Document Management** translates Data Center value references in workflow fields, including:

- Message text in `set-message` actions.
- The subject, title, and body of `send-email` actions.
- User fields, such as preassigned reviewers.
- Workflow, state, approval, and trigger fields that contain value references.

Translated variables also appear in migration warnings, so the warnings reflect the values used in the migrated workflow.

Data Center value references are not case-sensitive. For example, `@Creator@`, `@CREATOR@`, and `@creator@` are all translated to `@Content.CreatorId@`.

Text that resembles a variable, such as an email address (`john@example.com`), remains unchanged.

During migration, Data Center value references can have one of the following results:

- **Translated:** The value reference is replaced with its equivalent Cloud variable.
- **Unchanged:** The value reference remains unchanged and is not reported during migration. Cloud typically resolves it as a CDM metadata value at runtime.
- **Not supported:** The value reference remains unchanged and is reported as an unmapped value reference. Review the workflow and replace or remove the unsupported reference.

Some value references depend on the trigger event in which they are used. For example, `@comment@` is translated in an approval trigger but is not supported in a state message. See the [Event](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Event) section for details.

## Differences in returned values

In Cloud, user-related variables can return Atlassian account IDs, display names, or email addresses.

During migration, Data Center value references such as `@creator@` and `@approvers@` are translated to `@Content.CreatorId@` and `@Approval.ApproversId@`, respectively. These variables return account IDs, which can be used in reviewer assignments and other user fields.

If these variables are used in messages or emails, the account IDs appear instead of display names. To display the appropriate value, use the corresponding suffix:

| **Suffix** | **Value returned** | **Use it for** |
| --- | --- | --- |
| `Id` | Atlassian account ID | Reviewer assignments and other user fields |
| `Name` | Display name | Messages |
| `Email` | Email address | Email recipients |

For example, to display the creator's name in a message, replace `@Content.CreatorId@` with `@Content.CreatorName@`.

The following sections list Data Center value references and their corresponding Cloud variables, organized by category. Use these tables to identify the equivalent variables when reviewing your migrated workflows.

## Workflow parameters

During migration, Data Center value references that match workflow parameter names are translated to the corresponding Cloud parameter variables. The parameter name is preserved as defined in the workflow.

| **Data Center** | **Cloud** |
| --- | --- |
| `@Parameter Name@` | `@Parameter['Parameter Name']@` |

For example, if a workflow contains a parameter named **Owner**, `@Owner@` is translated to `@Parameter['Owner']@`.

Workflow parameters take precedence over other value references. If a parameter has the same name as a built-in value reference, CDM translates it as a parameter. For example, if a workflow contains a parameter named **creator**, `@creator@` is translated to `@Parameter['creator']@` instead of `@Content.CreatorId@`.

## Workflow and state

The following table lists the Data Center value references for workflow and state information and their Cloud equivalents.

| **Data Center** | **Cloud** |
| --- | --- |
| `@workflow@`, `@workflowname@`, `@pageworkflowname@` | `@Workflow.Name@` |
| `@workflowversion@` | `@Workflow.Version@` |
| `@state@`, `@awpstate@` | `@State.Name@` |
| `@expirydate@`, `@duedate@` | `@State.ExpiryDate@` |
| `@workflow:state > name@` | `@State.Name@` |
| `@workflow:state > duedate@` | `@State.ExpiryDate@` |

## Event

The following tables list Data Center event value references and their Cloud equivalents. Some value references are translated only when used with specific trigger events.

### Current user

| **Data Center** | **Cloud** |
| --- | --- |
| `@user@` | `@Event.UserId@` |
| `@userfullname@` | `@Event.UserName@` |
| `@useremail@` | `@Event.UserEmail@` |

For more information about Event variables in Cloud workflows, see the [Event section in Variables](/cms_trial/space/CDMC/3842114162/Variables/).

### Values that depend on the trigger event

The following value references are translated only when used in triggers that provide the corresponding values. In other contexts, these references are not supported because the Cloud variables would resolve to empty values.

| **Data Center** | **Cloud** | **Supported Data Center triggers** |
| --- | --- | --- |
| `@comment@` | `@Event.Comment@` | `pageapproved`, `pagerejected`, `pageapprovalassigned`, `approvalunassigned`, `statechanged`, `pagecreated` |
| `@approvaluser@` | `@Approval.FinalReviewersId@` | `pageapproved`, `pagerejected` |
| `@label@` | `@Event.Label@` | `labeladded`, `labelremoved` |
| `@addedlabel@` | `@Event.Label@` | `labeladded` |
| `@removedlabel@` | `@Event.Label@` | `labelremoved` |
| `@filename@`, `@name@`, `@attachment > filename@`, `@attachment > name@` | `@Event.FileName@` | Attachment-related triggers, such as `attachmentadded` |
| `@size@`, `@attachment > size@` | `@Event.FileSize@` | Attachment-related triggers, such as `attachmentadded` |

Outside attachment-related triggers, `@filename@`, `@name@`, `@size@`, and `@type@` remain unchanged because Data Center treats them as page metadata in those contexts.

**Example: Approval comment in a message**

In Data Center, a `pageapproved` trigger contains the following message:

`Approved by @approvaluser@: @comment@`

After migration, the message becomes:

`Approved by @Approval.FinalReviewersId@: @Event.Comment@`

The Cloud variable `@Approval.FinalReviewersId@` returns the reviewer's Atlassian account ID. To display the reviewer's name instead, replace it with `@Approval.FinalReviewersName@`.

## Approval

### Approvals in the current state

The following Data Center value references are translated to Cloud variables that retrieve information from all approvals in the current workflow state.

| **Data Center** | **Cloud** |
| --- | --- |
| `@approval@`, `@approvalname@` | `@Approval.Name@` |
| `@approvalcomment@` | `@Approval.Comment@` |
| `@approvalassignees@`, `@assignees@`, `@selected@`, `@selectedapprover@`, `@selectedapprovers@` | `@Approval.AssignedReviewersId@` |
| `@pendingusers@` | `@Approval.PendingReviewersId@` |
| `@approver@`, `@approvers@` | `@Approval.ApproversId@` |
| `@rejector@`, `@rejectors@` | `@Approval.RejectorsId@` |

### Named approvals

In Data Center, you can use `@Approval Name > attribute@` to reference a specific approval. During migration, these references are translated to Cloud variables that include the approval name.

The approval name is preserved as written, and spaces around `>` are optional.

| **Data Center** | **Cloud** |
| --- | --- |
| `@QA Review > approvalassignees@`, `@QA Review > assignees@`, `@QA Review > selected@`, `@QA Review > selectedapprover@`, `@QA Review > selectedapprovers@` | `@Approval['QA Review'].AssignedReviewersId@` |
| `@QA Review > pendingusers@` | `@Approval['QA Review'].PendingReviewersId@` |
| `@QA Review > approver@`, `@QA Review > approvers@`, `@QA Review > approvaluser@`, `@QA Review > user@` | `@Approval['QA Review'].ApproversId@` |
| `@QA Review > rejector@`, `@QA Review > rejectors@` | `@Approval['QA Review'].RejectorsId@` |
| `@QA Review > approvalcomment@`, `@QA Review > comment@` | `@Approval['QA Review'].Comment@` |

### Name modifiers

In Data Center, you can add `> wiki-link` or `> fullname` to an approval reference to display a user's name. During migration, these references are translated to Cloud variables with the `Name` suffix.

Cloud variables return display names rather than user mentions.

| **Data Center** | **Cloud** |
| --- | --- |
| `@QA Review > approvers > wiki-link@` | `@Approval['QA Review'].ApproversName@` |
| `@QA Review > approver > fullname@` | `@Approval['QA Review'].ApproversName@` |
| `@QA Review > selected > fullname@` | `@Approval['QA Review'].AssignedReviewersName@` |
| `@QA Review > pendingusers > wiki-link@` | `@Approval['QA Review'].PendingReviewersName@` |
| `@QA Review > rejectors > wiki-link@` | `@Approval['QA Review'].RejectorsName@` |

Other modifiers are not supported. This also applies to modifiers used with non-user attributes, such as `@QA Review > comment > fullname@`.

## Metadata

During migration, Data Center value references that don't match a workflow parameter or a built-in value reference are treated as CDM metadata references.

These references remain unchanged, and Cloud resolves their values from the page metadata when the workflow runs.

| **Data Center** | **Cloud** |
| --- | --- |
| `@My metadata@` | `@My metadata@` (unchanged) |

Approval references with attributes that aren't recognized as approval attributes, such as `@Section > owner@`, also remain unchanged.

### Metadata from another page

The following table shows how Data Center metadata references to another page are translated to Cloud variables.

| **Data Center** | **Cloud** |
| --- | --- |
| `@Page title:key@` | `@ContentTitle['Page title']:Metadata['key']@` |
| `@SPACEKEY:Page title:key@` | `@SpaceKey['SPACEKEY']:ContentTitle['Page title']:Metadata['key']@` |

For example, `@DEMO:Target Page:region@` is translated to `@SpaceKey['DEMO']:ContentTitle['Target Page']:Metadata['region']@`.

References containing more than three parts or an empty part, such as `@DEMO::region@`, are not supported.

A two-part reference beginning with `workflow`, `content`, `space`, `user`, or `page` is treated as a Reporting supplier chain rather than a page reference. See [Reporting supplier chains](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Reporting-supplier-chains) for details.

## Confluence Page Properties

The following table shows how Data Center Page Properties value references are translated to Cloud variables.

| **Data Center** | **Cloud** |
| --- | --- |
| `@property Name@` | `@Property['Name']@` |
| `@property('Name')@` | `@Property['Name']@` |

For example, `@property DocId@` is translated to `@Property['DocId']@`.

In Cloud, Page Properties variables support text and user mentions in the vertical two-column layout of the Page Properties macro. User mentions return Atlassian account IDs.

After migration, check that the referenced Page Properties use a supported layout and contain supported values.

## Confluence page and space

The following tables show how Data Center value references for dates, pages, and spaces are translated to Cloud variables.

### Date

| **Data Center** | **Cloud** |
| --- | --- |
| `@date@` | `@Date@` |
| `@datetime@` | `@DateTime@` |

### Current page

| **Data Center** | **Cloud** |
| --- | --- |
| `@pageid@`, `@id@` | `@Content.Id@` |
| `@pagetitle@`, `@title@` | `@Content.Title@` |
| `@page@`, `@url@` | `@Content.Link@` |
| `@version@` | `@Content.Version@` |
| `@labels@` | `@Content.Labels@` |
| `@parent@` | `@Content.ParentLink@` |
| `@creator@`, `@author@`, `@poster@` | `@Content.CreatorId@` |
| `@modifier@`, `@updater@`, `@updateuser@` | `@Content.LastEditorId@` |
| `@content:modifier > full name@` | `@Content.LastEditorName@` |
| `@watchers@` | `@Content.WatchersId@` |

### Space of the current page

| **Data Center** | **Cloud** |
| --- | --- |
| `@space@` | `@Space.Name@` |
| `@spacekey@` | `@Space.Key@` |

**Example: Page information in an email**

In Data Center, the body of a `send-email` action contains:

`@pagetitle@ (@page@) was created by @creator@ in @space@.`

After migration, the email body contains:

`@Content.Title@ (@Content.Link@) was created by @Content.CreatorId@ in @Space.Name@.`

The `@Content.CreatorId@` variable returns the creator's Atlassian account ID. To display the creator's name instead, replace it with `@Content.CreatorName@`.

## Reporting supplier chains

The following Data Center Reporting supplier chains have equivalent Cloud variables.

| **Data Center** | **Cloud** |
| --- | --- |
| `@workflow:state > name@` | `@State.Name@` |
| `@workflow:state > duedate@` | `@State.ExpiryDate@` |
| `@content:modifier > full name@` | `@Content.LastEditorName@` |

Other Reporting supplier chains, such as `@content:creator > email@`, are not supported in Cloud.

## Value references that are not supported

The following Data Center value references do not have Cloud equivalents. During migration, these references remain unchanged and are reported as unmapped value references.

Review these references in your migrated workflow and replace or remove them as needed.

| **Data Center** | **Description** |
| --- | --- |
| `@assignee@` | The user who was just assigned. There is no direct Cloud equivalent. To reference all assigned reviewers, use `@Approval.AssignedReviewersId@`. |
| `@approvaldate@`, `@Approval Name > approvaldate@` | No Cloud equivalent. |
| `@signature@` | No Cloud equivalent. |
| `@pagelatest@`, `@pageactivity@`, `@modification@` | No Cloud equivalent. |
| `@attachmenturl@` | No Cloud equivalent. |
| `@type@`, `@attachment > type@` in attachment triggers | No equivalent attachment type variable. `@Content.Type@` returns the page content type, not the attachment type. |
| `@task@`, `@taskname@`, `@taskassignee@`, `@taskassigner@`, `@taskcompleter@`, `@taskcreator@`, `@taskcomment@` | No Cloud equivalent. |
| `@errormessage@` | No Cloud equivalent. |
| `@comment@`, `@approvaluser@`, `@label@`, `@addedlabel@`, `@removedlabel@` outside the supported trigger contexts | These references are supported only in the trigger contexts listed in the [Event](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Event) section. |
| Approval chains with modifiers other than `wiki-link` or `fullname` | See [Name modifiers](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Name-modifiers) under Approval. |
| Reporting supplier chains not listed in [Reporting supplier chains](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Reporting-supplier-chains) | No Cloud equivalent. |
| Cross-page references containing more than three parts or an empty part | See [Metadata from another page](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/3842048384/Migrate+data+center+variables+to+cloud#Metadata-from-another-page) for supported formats. |

## Check your workflow after migration

After migrating your workflow to Cloud, check that the value references work as expected.

1. Review the migration report for unmapped value references. Replace or remove any unsupported references.
2. Check messages and emails for variables with the `Id` suffix, such as `@Content.CreatorId@`. Replace them with the corresponding `Name` variables if you want to display names instead of account IDs.
3. Verify that referenced metadata, Page Properties, and pages exist in Cloud with the expected names.
4. Test the workflow on a page and check messages and emails for unresolved variables.