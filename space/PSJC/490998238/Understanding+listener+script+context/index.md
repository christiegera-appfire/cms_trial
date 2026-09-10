# Understanding listener script context

This reference helps you understand what data your listener scripts can access and which functions to use based on whether your script runs in Issue context or Global context.

When your listener script executes, it receives specific parameters and has access to different functions and data depending on the event type. In other words, it operates within different contexts that determine what data and functions are available. The available context varies between issue-related events and global events.

- **Issue context**: Your script can directly access issue fields like summary, assignee, and custom fields. This is available for issue-related event types (Issue, Issue comments, Issue links, and Attachments).
- **Global context**: Your script cannot directly access issue fields and must use special event functions instead. Available for non-issue events (Project, Version, User, Sprint, Board, Filter).

For details about contexts and scope, see [Contexts and scope in SIL](/cms_trial/space/PSJC/491001721/Contexts+and+scope+in+SIL/).

## Script parameters

Every listener script automatically receives these parameters when it executes:

| **Position** | **Parameter** | **Description** |
| --- | --- | --- |
| 0 | `user` | The user who triggered the event. |
| 1 | `eventId` | Internal event identifier. |
| 2 | `eventName` | Name of the triggered event. |

These parameters provide essential information about the event that triggered your listener, including who caused it and what type of event occurred. This information is often needed for logging, conditional logic, or determining how your script should respond.

You can retrieve this information in your script with:

```text
string callingUser = argv[0];
string eventId = argv[1];
string eventName = argv[2];
```

## Available functions by event type

The data and functions available in your script depend on the event type and whether it provides Issue context. This determines not only what information you can access, but also how you access it: through direct field references or through specific event functions.

When your listener operates in **Issue context**, you can directly access all [standard issue variables](/cms_trial/space/PSJC/1938391090/Standard+variables+reference/) (summary, assignee, description, etc.) in your script. However, when operating in **Global context**, using issue variables will cause errors, and you must use event-specific functions instead.

| **Event type** | **Events** | **Context** | **Supported functions** |
| --- | --- | --- | --- |
| **Attachment** | - Attachment Added - Attachment Removed | Issue | - `getEventName` - `getAttachmentFromEvent` |
| **Issue** | - Issue Created - Issue Deleted | Issue | - `getEventName` |
| - Issue Updated | Issue | - `getEventName` - `g``etEventIssueChanges` - `getEventIssueFieldChange` - `isIssueFieldChanged` |
| **Issue comments** | - Issue Commented - Issue Comment Added - Issue Comment Deleted | Issue | - `getEventName` |
| **Issue links** | - Issue Link Added - Issue Link Deleted | Issue | - `getEventName` - `getIssueLinkFromEvent` |
| **Project** | - Project Created - Project Updated - Project Deleted | Global | - `getEventName` - `getProjectFromEvent` |
| **Version** | - Version Created - Version Updated - Version Deleted - Version Released - Version Unreleased - Version Moved | Global | - `getEventName` - `getVersionFromEvent` |
| **User** | - User Created - User Updated - User Deleted | Global | - `getEventName` - `getUserFromEvent` |
| **Boards** | - Board Created - Board Updated - Board Deleted - Board Config Updated | Global | - `getEventName` - `getBoardFromEvent` |
| **Filters** | - Filters Created - Filters Updated - Filters Deleted | Global | - `getEventName` - `getFilterFromEvent` |
| **Sprint** | - Sprint Created - Sprint Updated - Sprint Deleted - Sprint Started - Sprint Closed | Global | - `getEventName` - `getSprintFromEvent` |

See the [Listener functions](/cms_trial/space/PSJC/491002302/Listener+Functions/) page for details and examples.