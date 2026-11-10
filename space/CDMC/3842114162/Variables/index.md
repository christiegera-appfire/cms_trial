# Variables

## Overview

Use variables in Comala Document Management Cloud workflows to insert values that change when the workflow runs. A variable is a dynamic placeholder: write it in the workflow, and CDM replaces it with the current value at runtime. Variable syntax keywords are not case-sensitive. For example, `@State.Name@` and `@STATE.NAME@` refer to the same value. Names inside brackets, such as parameter, metadata, and approval names, must match the name as entered. Property names are checked first for an exact match, then without regard to case. Space keys are case-sensitive.

## Where you can use variables

Variables are resolved at runtime in workflow configurations and trigger actions.

You can use variables in:

- Message text in `set-message` actions.
- The subject, title, and body of `send-email` actions.
- User fields that accept an account ID or a list of account IDs.
- Other text and user fields that the workflow evaluates when entering a state or running a trigger action.

Variables can be nested one level deep. For example, if a metadata value contains `@Parameter['Color']@`, CDM resolves the parameter value. A second level of nesting is not supported.

If a valid variable has no value, CDM replaces it with an empty value and the workflow continues. For example, this happens when the current state has no expiry date or a referenced parameter, metadata field, or page property doesn't exist.

If CDM doesn't recognize a variable, it may leave the text unchanged. For example, `@Content.Tittle@` remains unchanged, while `@State.Nme@` resolves to an empty value. Check messages and emails for unresolved variables when testing a workflow.

Choose the suffix that matches the type of value required by the destination field:

| Suffix | Value returned | Use it for |
| --- | --- | --- |
| `Id` | Atlassian account ID | Reviewer assignments and other user fields |
| `Name` | Display name | Messages |
| `Email` | Email address | Email recipients |

When a variable returns a list as text, CDM separates the values with commas and no spaces.

## Variable types

| **Type** | **When to use it** |
| --- | --- |
| CDM Value References | Workflow, event, state, and approval information. Without a prefix, these refer to the current page; a cross-reference prefix can target another page. |
| CDM Parameters | Named parameters defined on the workflow. For the current page, CDM checks the page value, then the workflow value, then the parameter default. A cross-reference prefix reads the parameter from another page. |
| CDM Metadata | Fields stored by CDM metadata macros. Without a prefix, this reads the current page; a cross-reference prefix reads another page. |
| Confluence Smart Values | Confluence page and space information, the site, the current user, and the current date and time. Content and Space values can target another page or space; Date, DateTime, User, and Site values describe the current run or site. |
| Confluence Page Properties | The native Confluence Page Properties macro supports text and user-mention values in its vertical two-column layout. User mentions return account IDs. Other cell types, such as groups, teams, dates, status lozenges, and links, aren’t supported. |

## CDM Value References

### Workflow

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Workflow.Name@` | `@Workflow@`, `@WorkflowName@` | Name of the workflow applied to the page. |
| `@Workflow.Version@` | `@WorkflowVersion@` | Version of that workflow. |

### State

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@State.Name@` | `@State@`, `@Content.State@`, `@Workflow.State@` | Name of the current state. |
| `@State.ExpiryDate@` | `@ExpiryDate@`, `@Content.ExpiryDate@`, `@Workflow.ExpiryDate@` | Expiry date of the current state as a UTC timestamp in ISO 8601 format, if set. |

**Example: Include workflow and state information in an email**

You can use `@Workflow.Name@` and `@State.Name@` in an email notification to identify the workflow and its current state.

For example, add the following text to the email body:

**Workflow:** `@Workflow.Name@`  
**Current state:** `@State.Name@`

When the workflow runs, CDM replaces the variables with the corresponding workflow and state names.

### Event

Event variables return information about the current workflow event. Variables specific to an event return an empty value outside that event.

`@Event.UserId@`, `@Event.UserName@`, and `@Event.UserEmail@` return the same user as `@User.Id@`, `@User.Name@`, and `@User.Email@`.

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Event.UserId@` | - | Account ID of the user who triggered the current workflow event. |
| `@Event.UserName@` | - | Display name of that user. |
| `@Event.UserEmail@` | - | Email address of that user. |
| `@Event.Comment@` | `@Comment@` | Latest comment entered in the workflow state dialog. This is not a Confluence page comment or inline comment. |
| `@Event.Label@` | `@Label@` | Label associated with a *label-added* or *label-removed* event; empty for other events. |
| `@Event.FileName@` | `@FileName@`, `@File@` | Attachment filename for an *attachment added, updated, removed,* or *changed* event. |
| `@Event.FileSize@` | `@FileSize@` | Attachment size, in bytes, for an *attachment added, updated, removed*, or *changed* event. |
| `@Event.PageComment@` | `@PageComment@` | Comment added to the page that triggered the *page-comment-added* event. |
| `@Event.InlineComment@` | `@InlineComment@` | Inline comment that triggered the *inline-comment-added* event. |

**Example: Include a workflow comment in an email**

You can use Event variables to include the name of the user who triggered a workflow event and the comment entered in the workflow state dialog.

For example, add the following text to the email body:

**User:** `@Event.UserName@`

**Comment:** `@Event.Comment@`

When the workflow runs, CDM replaces these variables with the user's display name and the latest comment entered in the workflow state dialog. If no comment is available, the comment value is empty.

### Approval

Use approval variables to retrieve information from all approvals in the current state or from a specific approval. For example, `@Approval.ApproversId@` returns approvers across the current state's approvals, while `@Approval['QA Review'].ApproversId@` refers only to the approval named **QA Review**.

`Reviewers` and `FinalReviewers` can also return decision data from the most recent state change. This can let you show reviewers or final reviewers in a later state, such as Published. `AssignedReviewers`, `PendingReviewers`, `Approvers`, and `Rejectors` refer to approvals in the current state.

Each reviewer field includes the `Id`, `Name`, and `Email` suffixes. Use the same pattern with a named approval by adding `['Approval Name']` after `Approval`.

| **Reviewer field** | **Alias** | **Description** |
| --- | --- | --- |
| `AssignedReviewersId`, `AssignedReviewersName`, `AssignedReviewersEmail` | `@AssignedReviewersId@`, `@approvalassignees@`, `@assignees@`, `@AssignedReviewersName@`, `@AssignedReviewersEmail@` | Everyone assigned to the approval, whether or not they have decided. |
| `PendingReviewersId`, `PendingReviewersName`, `PendingReviewersEmail` | `@PendingReviewersId@`, `@PendingReviewersName@`, `@PendingReviewersEmail@` | Assigned reviewers who have not approved or rejected yet. |
| `ReviewersId`, `ReviewersName`, `ReviewersEmail` | `@ReviewersId@`, `@reviewer@`, `@ReviewersName@`, `@ReviewersEmail@` | Assigned reviewers who have approved or rejected. Approval does not need to be complete. |
| `ApproversId`, `ApproversName`, `ApproversEmail` | `@ApproversId@`, `@ApproversName@`, `@ApproversEmail@` | Reviewers who approved. |
| `RejectorsId`, `RejectorsName`, `RejectorsEmail` | `@RejectorsId@`, `@RejectorsName@`, `@RejectorsEmail@` | Reviewers who rejected. |
| `FinalReviewersId`, `FinalReviewersName`, `FinalReviewersEmail` | `@FinalReviewersId@`, `@FinalReviewersName@`, `@FinalReviewersEmail@` | Account IDs, display names, or email addresses of reviewers whose decisions contributed to the final approved or rejected outcome. These variables return an empty value while the approval is pending. |

For example, `@Approval.PendingReviewersId@` returns account IDs. Use `@Approval['QA Review'].PendingReviewersEmail@` to return email addresses for pending reviewers on the named approval.

| Variable | Alias | Description |
| --- | --- | --- |
| `@Approval.Comment@` | `@ApprovalComment@` | Latest comment entered in the workflow state dialog by the user who approved or rejected. |
| `@Approval['Approval Name'].Comment@` | — | Latest comment entered in the workflow state dialog for the named approval by the user who approved or rejected. |

For example, after a document is approved, you can use `@Approval.FinalReviewersName@` in a workflow message to display the names of reviewers whose decisions contributed to the final approval outcome. This variable can also retrieve the final reviewers after the workflow transitions to another state, such as **Published**.

## CDM Parameters

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Parameter['Parameter Name']@` | - | Value of the named workflow parameter, resolved using the order described above. |

For example, if a workflow has a parameter named **Color** with the value **Red**, you can use `@Parameter['Color']@` in a workflow message. When the workflow runs, CDM replaces the variable with **Red**.

## CDM Metadata

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Metadata['Metadata Name']@` | `@Metadata Name@` | Value of the named metadata field. If no page-scoped value exists, CDM checks the page-scoped default, then the workflow-scoped parameter value, and finally its default. |

For example, if a page has a metadata field named **My team** containing two users, you can use `@Metadata['My team']@` to retrieve their values when the workflow runs. You can also use this variable in a reviewer assignment field that accepts user account IDs.

## Confluence Smart Values

### Date and site

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Date@` | - | Current date in the site time zone, in `YYYY-MM-DD` format. |
| `@DateTime@` | - | Current date and time in `YYYY-MM-DD HH:mm:ss` format (24-hour clock). |
| `@DateTimeISO@` | - | Current date and time in ISO 8601 format, including the time zone offset. Depending on the time zone, the value ends in an offset such as `+02:00` or `Z`. |
| `@Site.Name@` | `@Site@` | Site base URL. |

If CDM can’t determine the site time zone, it uses UTC.

### Current user

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@User.Id@` | - | Account ID of the user in the workflow context. |
| `@User.Name@` | - | Display name of the user in the workflow context. |
| `@User.Email@` | - | Email address of the user in the workflow context. |

### Space of the current page

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Space.Id@` | - | ID of the space. |
| `@Space.Key@` | - | Key of the space. |
| `@Space.Name@` | - | Name of the space. |
| `@Space.Link@` | - | Link to the space. |

### Current page

| **Variable** | **Alias** | **Description** |
| --- | --- | --- |
| `@Content.Id@` | `@Content@` | ID of the page or other content. |
| `@Content.Title@` | `@Title@` | Title of the page or content. |
| `@Content.Link@` | `@Link@` | Link to the page or content. |
| `@Content.Type@` | `@Type@` | Content type, such as a page or blog post. |
| `@Content.Version@` | `@Version@` | Current content version. |
| `@Content.Labels@` | - | Labels on the content, sorted alphabetically and separated by commas. |
| `@Content.Status@` | `@Content.ConfluenceStatus@`, `@ConfluenceStatus@` | Confluence content status, such as *In progress*. This is not the CDM workflow state. |
| `@Content.Space@` | `@Space@` | Name of the space containing the content. |
| `@Content.ParentId@` | `@Parent.Id@` | ID of the parent content. |
| `@Content.ParentTitle@` | `@Parent.Title@` | Title of the parent content. |
| `@Content.ParentLink@` | `@Parent.Link@` | Link to the parent content. |
| `@Content.CreatorId@`, `@Content.CreatorName@`, `@Content.CreatorEmail@` | `@Creator.Id@`, `@Creator.Name@`, `@Creator.Email@` | Creator's account ID, display name, and email address. |
| `@Content.OwnerId@`, `@Content.OwnerName@`, `@Content.OwnerEmail@` | `@Owner.Id@`, `@Owner.Name@`, `@Owner.Email@` | Owner's account ID, display name, and email address. |
| `@Content.LastEditorId@`, `@Content.LastEditorName@`, `@Content.LastEditorEmail@` | `@LastEditor.Id@`, `@lastUpdatedBy@`, `@LastEditor.Name@`, `@LastEditor.Email@` | Last editor's account ID, display name, and email address. |
| `@Content.WatchersId@`, `@Content.WatchersName@`, `@Content.WatchersEmail@` | `@Watchers.Id@`, `@Watchers.Name@`, `@Watchers.Email@` | Watcher account IDs, display names, and email addresses. |

**Example: Include page information in an email**

You can use Content variables to include information about a Confluence page in an email notification.

For example, add the following text to the email body:

**Page:** `@Content.Title@`

**Link:** `@Content.Link@`

**Created by:** `@Content.CreatorName@`

When the workflow runs, CDM replaces these variables with the page title, link, and creator's display name.

## Confluence Page Properties

| **Variable** | **Description** |
| --- | --- |
| `@Property['Page Property Name']@` | Value in the named row of the native Page Properties macro on the current page. |

For example, if a page has a Page Properties field named **Reviewer** containing a user mention, you can use `@Property['Reviewer']@` in the workflow's preassigned reviewers field. When the workflow runs, CDM retrieves the user's account ID and assigns that user as a reviewer.

If a Page Properties cell contains only user mentions, `@Property['...']@` returns account IDs. It does not return display names. If multiple Page Properties macros contain the same property, CDM uses the value from the first macro.

## Reference another page or space

Without a prefix, a variable reads from the current page or space. Add a prefix before the variable to read from another location:

| **Prefix** | **What it selects** |
| --- | --- |
| `@ContentTitle['Page title']:...@` | A page with that title in the current page’s space. If no page matches, CDM checks for a blog post with that title in the same space. Use `SpaceKey` to search another space. |
| `@ContentID['Content ID']:...@` | Content with that ID. It can be in another space. |
| `@SpaceKey['SPACEKEY']:...@` | The space with that key. Space keys are case-sensitive. |

**Examples:**

| **Reference** | **What it returns** |
| --- | --- |
| `@ContentTitle['My Page']:State.Name@` | State name from another page. |
| `@ContentID['1234']:Property['Size']@` | The **Size** page property from content with ID `1234`. |
| `@SpaceKey['DM']:Space.Name@` | Name of the space with key `DM`. |
| `@SpaceKey['DM']:ContentTitle['Reviewers']:Property['Reviewer']@` | The Reviewer Page Property from the **Reviewers** page in the **DM** space. |
| `@SpaceKey['DM']:ContentID['1234']:Property['Size']@` | A page property from content with ID `1234` in the **DM** space. The content must belong to that space. |

For example, you can store reviewer information on a Confluence page and reference it from workflows on other pages. If the **Reviewers** page in the **DM** space contains a Page Property named **Reviewer**, use `@SpaceKey['DM']:ContentTitle['Reviewers']:Property['Reviewer']@` to retrieve its value. When the Page Property is updated, workflows that reference it use the updated value without requiring changes to their configurations.

A `SpaceKey` prefix followed directly by a Content field, such as `@SpaceKey['DM']:Content.Title@`, is not a valid way to select a page. Use `SpaceKey` with `ContentTitle` or `ContentID` to select a page, or with a Space value to read information about that space.

Prefixes work with Workflow, State, Approval, Parameter, Metadata, Property, Content, and Space values. They do not apply to Event, Date, DateTime, User, or Site values; those describe the current event, current user, or site, and prefixed forms of them are empty.

CDM reads referenced pages and spaces as the app, so the value does not depend on who triggers the workflow. A message or email may include information that its recipient cannot open. Workflow editors can add cross-references directly. Users who can edit a page may also introduce them indirectly through Page Properties or metadata values, and CDM resolves those references with the app’s permissions.

If the target page does not exist, the content is not in the specified space, or the app cannot read the target, the variable resolves to an empty value and the workflow continues. If the page title matches more than one page, CDM uses the first match. Draft, archived, or trashed content resolves to an empty value. State, Approval, and Workflow variables also resolve to empty when the target page has no workflow.