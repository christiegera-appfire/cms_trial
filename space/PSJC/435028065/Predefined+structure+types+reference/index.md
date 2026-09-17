# Predefined structure types reference

This reference lists the predefined structure types used in Simple Issue Language (SIL) for Power Scripts for Jira Cloud. Use it to identify the fields, data types, and return structures returned by SIL functions across Jira products.

SIL provides two categories of structure types:

- Predefined structures are built-in structure types that come with SIL and are designed to interface with specific Jira functionalities. Each predefined structure maps to a corresponding Jira object model and is used by specific SIL functions for operations like HTTP requests, workflow management, and issue tracking.
- Custom structures are structure types you can create to model custom data relationships and organize complex data. Custom structures follow the same syntax rules as predefined structures and can be created using the structure definition syntax detailed in the [Structures](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487006/Syntax+and+types+introduction#Structures) section on the [Syntax and types introduction](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487006) page.

All structures in SIL operate in a detached state, meaning that modifying structure fields only exists within your script. The changes don't get saved to Jira. For example, if you modify fields in a project version structure, the actual project version in Jira remains unchanged. This makes it safe to manipulate structure data in your scripts without affecting the real Jira data.

---

## How to use the reference tables

This page provides a full list of the predefined structures used in SIL. Here’s a breakdown of the information you can find in the tables:

| **Table column** | **Description** |
| --- | --- |
| Name | This is the unique identifier for the structure type. |
| Fields | These are named properties that hold data within the structure. |
| Field types | The data type for each field. Can be one of the following:   - Basic types (`string`, `number`, `integer`, `boolean`, `date`) - Arrays (marked with `[]`)    - Other structure types (like a field of type HttpHeader in HttpRequest) |
| Returned by function | Predefined structures serve as return types for specific SIL functions. When you call these functions, they return data organized in the corresponding structure format. |

#### Example

This is example shows the `JComment` structure, which has seven fields of `string` and `date` type.

```text
struct JComment {
    string id;            // Field name: id, Type: string
    string text;          // Field name: text, Type: string 
    string author;        // Field name: author, Type: string
    date created;         // Field name: created, Type: date
    string updatedBy;     // Field name: updatedBy, Type: string
    date updated;         // Field name: updated, Type: date
    string securityLevel; // Field name: securityLevel, Type: string
}This page provides a reference of the predefined structure types used in SIL.
```

The `JComment` structure is returned when you use functions like:

- `editComment()`
- `getCommentById()`
- `getLastComment()`

This means when you write:

```text
JComment comment = getCommentById("12345");
```

The function returns the comment data organized in the `JComment` structure, allowing you to access fields like `comment.text` or `comment.author`.

---

## Standard types

Standard structure types are core structures that handle fundamental Jira operations and integrations. These include HTTP communication, email handling, user management, comments, custom fields, project components, and other basic Jira entities. These structures are available in all Jira installations and form the foundation of SIL scripting.

| **Name** | **Fields** | **Field types** | **Returned by function** |
| --- | --- | --- | --- |
| HttpRequest | headers | HttpHeader [] | - [httpDelete](/cms_trial/space/PSJC/434733492/httpDelete/) - [httpGet](/cms_trial/space/PSJC/434472661/httpGet/) - [httpOptions](/cms_trial/space/PSJC/434995455/httpOptions/) | - [httpPatch](/cms_trial/space/PSJC/434930150/httpPatch/) - [httpPost](/cms_trial/space/PSJC/434766152/httpPost/) - [httpPut](/cms_trial/space/PSJC/434995476/httpPut/) |
| cookies | HttpCookie [] |
| parameters | HttpQueryParam [] |
| HttpHeader | key | string | - [httpCreateHeader](/cms_trial/space/PSJC/434766083/httpCreateHeader/) - [httpBasicAuthHeader](/cms_trial/space/PSJC/434602768/httpBasicAuthHeader/) |
| value | string |
| HttpCookie | name | string | - [httpCreateCookie](/cms_trial/space/PSJC/433654478/httpCreateCookie/) |
| value | string |
| HttpQueryParam | name | string | - [httpCreateParameter](/cms_trial/space/PSJC/434766101/httpCreateParameter/) |
| value | string |
| HttpResponseInfo | class | string | - [httpGetResponseInfo](/cms_trial/space/PSJC/434374319/httpGetResponseInfo/) |
| statusCode | integer |
| errorMessage | string |
| reasonPhrase | string |
| HttpProxy | host | string | - [httpDelete](/cms_trial/space/PSJC/434733492/httpDelete/) - [httpGet](/cms_trial/space/PSJC/434472661/httpGet/) - [httpOptions](/cms_trial/space/PSJC/434995455/httpOptions/) | - [httpPatch](/cms_trial/space/PSJC/434930150/httpPatch/) - [httpPost](/cms_trial/space/PSJC/434766152/httpPost/) - [httpPut](/cms_trial/space/PSJC/434995476/httpPut/) |
| port | number |
| JAttachment | id | integer | - [getAttachmentFromEvent](/cms_trial/space/PSJC/705003561/getAttachmentFromEvent/) |
| author | string |
| created | date |
| content | string |
| filename | string |
| mimeType | string |
| thumbnail | string |
| size | integer |
| JComment | id | string | - [editComment](/cms_trial/space/PSJC/434507059/editComment/) - [getCommentById](/cms_trial/space/PSJC/434930021/getCommentById/) - [getLastComment](/cms_trial/space/PSJC/434995323/getLastComment/) |
| text | string |
| author | string |
| created | date |
| updatedBy | string |
| updated | date |
| securityLevel | string |
| JComponent | id | number | - [admGetProjectComponent](/cms_trial/space/PSJC/434733545/getComponent/) |
| name | string |
| description | string |
| lead | string |
| defaultAssignee | number |
| JCustomField | id | string | - [getCustomField](/cms_trial/space/PSJC/1626374145/getCustomField/) - [getAllCustomFields](/cms_trial/space/PSJC/1626898458/getAllCustomFields/) |
| name | string |
| type | string |
| dataType | string |
| orderable | boolean |
| searchable | boolean |
| JCustomFieldOption | id | string | - [admAddCustomFieldOptions](/cms_trial/space/PSJC/791282009/admAddCustomFieldOptions/) - [admDeleteCustomFieldOptions](/cms_trial/space/PSJC/790627240/admDeleteCustomFieldOptions/) - [admGetCustomFieldOptions](/cms_trial/space/PSJC/791511311/admGetCustomFieldOptions/) - [admUpdateCustomFieldOptions](/cms_trial/space/PSJC/790528847/admUpdateCustomFieldOptions/) |
| optionId | string |
| value | string |
| disabled | boolean |
| JDashboard | id | string | - [admCopyDashboard](/cms_trial/space/PSJC/748162099/admCopyDashboard/) - [admCreateDashboard](/cms_trial/space/PSJC/747965192/admCreateDashboard/) - [admGetAllDashboards](/cms_trial/space/PSJC/748552437/admGetAllDashboards/) - [admGetDashboardById](/cms_trial/space/PSJC/748683420/admGetDashboardById/) - [admGetDashboardsByName](/cms_trial/space/PSJC/748683364/admGetDashboardsByName/) | - [admGetDashboardsByOwner](/cms_trial/space/PSJC/748618158/admGetDashboardsByOwner/) - [admGetDashboardsForUser](/cms_trial/space/PSJC/748618168/admGetDashboardsForUser/) - [admGetFavouriteDashboards](/cms_trial/space/PSJC/747801635/admGetFavouriteDashboards/) - [admUpdateDashboard](/cms_trial/space/PSJC/748718317/admUpdateDashboard/) |
| name | string |
| description | string |
| viewUrl | string |
| system | boolean |
| owner | string |
| refreshintegererval | integer |
| popularity | integer |
| rank | integer |
| editPermissions | JSharePermission [] |
| sharePermissions | JSharePermission [] |
| JEmailAttachment | file | string | - [sendEmail](/cms_trial/space/PSJC/433654656/sendEmail/) |
| name | string |
| mimeType | string |
| JEmailMessage | to | string [] | - [sendEmail](/cms_trial/space/PSJC/433654656/sendEmail/) - [sendHtmlEmail](/cms_trial/space/PSJC/435028575/sendHtmlEmail/) |
| cc | string [] |
| bcc | string [] |
| subject | string |
| message | string |
| from | string |
| attachments | JEmailAttachment [] |
| JFieldChange | user | string | - [getFieldChanges](/cms_trial/space/PSJC/434930045/getFieldChanges/) - [lastIssueChanges](/cms_trial/space/PSJC/434799219/lastIssueChanges/) |
| changeDate | date |
| field | string |
| oldVal | string |
| newVal | string |
| oldValString | string |
| newValString | string |
| JFieldConfigurationScheme | id | integer | - [admGetAllFieldConfigSchemes](/cms_trial/space/PSJC/514818850/admGetAllFieldConfigSchemes/) - [admGetFieldConfigScheme](/cms_trial/space/PSJC/515146283/admGetFieldConfigScheme/) |
| name | string |
| description | string |
| JFieldConfiguration | id | integer | - [admGetFieldConfigById](/cms_trial/space/PSJC/860717838/admGetFieldConfigById/) - [admCreateFieldConfig](/cms_trial/space/PSJC/861667573/admCreateFieldConfig/) | - [admUpdateFieldConfig](/cms_trial/space/PSJC/861733003/admUpdateFieldConfig/) |
| name | string |
| description | string |
| isDefault | boolean |
| JFieldConfigITMapping | fieldConfigurationId | integer | - [admGetFieldConfigITMappings](/cms_trial/space/PSJC/860357745/admGetFieldConfigITMappings/) |
| issueTypeId | integer |
| JFieldConfigurationItem | field | string | - [admGetAllFieldConfigItems](/cms_trial/space/PSJC/862224438/admGetAllFieldConfigItems/) |  |
| description | string |
| renderer | string |
| hidden | boolean |
| required | boolean |
| JFieldValue | fieldName | string | - [createIssue](/cms_trial/space/PSJC/434507110/createIssue/) |
| values | string [] |
| JFilter | id | integer | - [admCreateFilter](/cms_trial/space/PSJC/720902428/admCreateFilter/) - [admGetAllFilters](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489492) - [admGetAllOwnedFilters](/cms_trial/space/PSJC/722174348/admGetAllOwnedFilters/) - [admGetFavouriteFilters](/cms_trial/space/PSJC/722076017/admGetFavouriteFilters/) - [admGetFilterById](/cms_trial/space/PSJC/720473851/admGetFilterById/) | - [admGetFiltersByName](/cms_trial/space/PSJC/720473817/admGetFiltersByName/) - [admGetFiltersForProject](/cms_trial/space/PSJC/720605278/admGetFiltersForProject/) - [admUpdateFilter](/cms_trial/space/PSJC/722141349/admUpdateFilter/) - [getFilterFromEvent](/cms_trial/space/PSJC/720473609/getFilterFromEvent/) |
| jql | string |
| name | string |
| description | string |
| owner | string |
| editPermissions | JSharePermission [] |
| sharePermissions | JSharePermission [] |
| JGadget | id | integer | - [admAddGadgetToDashboard](/cms_trial/space/PSJC/747801902/admAddGadgetToDashboard/) - [admGetAvailableGadgets](/cms_trial/space/PSJC/748618518/admGetAvailableGadgets/) - [admGetDashboardGadgetById](/cms_trial/space/PSJC/748718574/admGetDashboardGadgetById/) | - [admGetDashboardGadgets](/cms_trial/space/PSJC/748063606/admGetDashboardGadgets/) - [admUpdateGadgetInDashboard](/cms_trial/space/PSJC/748162444/admUpdateGadgetInDashboard/) |
| moduleKey | string |
| titlen | string |
| uri | string |
| color | string |
| row | integer |
| column | integer |
| JIssueLink | id | number | - [getIssueLinksDetail](/cms_trial/space/PSJC/434602750/getIssueLinksDetail/) |
| name | string |
| direction | number |
| description | string |
| issue | string |
| JIssueNotificationScheme | id | integer | - [admGetAllNotificationSchemes](/cms_trial/space/PSJC/513441877/admGetAllNotificationSchemes/) - [admGetNotificationScheme](/cms_trial/space/PSJC/512852100/admGetNotificationScheme/) |
| name | string |
| description | string |
| JIssueNotificationSchemeEvent | event | string | - [admGetAllNotificationSchemes](/cms_trial/space/PSJC/513441877/admGetAllNotificationSchemes/) | - [admGetNotificationScheme](/cms_trial/space/PSJC/512852100/admGetNotificationScheme/) |
| notifications | JIssueNotificationSchemeNotificationDetail [] |
| JIssueNotificationSchemeNotificationDetail | notificationType | string | - [admGetAllNotificationSchemes](/cms_trial/space/PSJC/513441877/admGetAllNotificationSchemes/) | - [admGetNotificationScheme](/cms_trial/space/PSJC/512852100/admGetNotificationScheme/) |
| parameter | string |
| JIssueNotificationSchemeProjectMapping | notificationSchemeId | integer | - [admGetNotificationProjectMappings](/cms_trial/space/PSJC/1213858059/admGetNotificationProjectMappings/) |
| projectId | integer |
| JIssueSecurityScheme | id | integer | - [admGetAllIssueSecuritySchemes](/cms_trial/space/PSJC/514818823/admGetAllIssueSecuritySchemes/) - [admGetIssueSecurityScheme](/cms_trial/space/PSJC/514720797/admGetIssueSecurityScheme/) |
| defaultSecurityLevelId | integer |
| name | string |
| description | string |
| JIssueTypeScheme | id | integer | - [admGetAllIssueTypeSchemes](/cms_trial/space/PSJC/514786551/admGetAllIssueTypeSchemes/) - [admGetIssueTypeScheme](/cms_trial/space/PSJC/515211665/admGetIssueTypeScheme/) |
| name | string |
| description | string |
| defaultIssueTypeId | integer |
| JIssueTypeScreenScheme | id | integer | - [admGetAllIssueTypeScreenSchemes](/cms_trial/space/PSJC/518324501/admGetAllIssueTypeScreenSchemes/) - [admGetIssueTypeScreenScheme](/cms_trial/space/PSJC/518291809/admGetIssueTypeScreenScheme/) |
| name | string |
| description | string |
| JIssueTypeScreenMapping | id | integer | - [admGetITSSMappings](/cms_trial/space/PSJC/805961911/admGetITSSMappings/) |
| screenSchemeId | integer |
| JLastActiveDates | productLastActiveDates | JProductLastActiveDate [] | - [admGetLastActiveDates](/cms_trial/space/PSJC/1159823773/admGetLastActiveDates/) |
| addedToOrganization | date |
| JPermissionGrant | holder | JPermissionHolder | - [admGetAllPermissionSchemes](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) | - [admGetPermissionScheme](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) |
| id | integer |
| permission | string |
| JPermissionHolder | parameter | string | - [admGetAllPermissionSchemes](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) | - [admGetPermissionScheme](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) |
| type | string |
| value | string |
| JPermissionScheme | id | integer | - [admGetAllPermissionSchemes](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) | - [admGetPermissionScheme](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) |
| name | string |
| description | string |
| permissions | JPermissionGrant [] |
| JLdapUserAttribute | name | string | - [ldapUserStruct](/cms_trial/space/PSJC/434635671/ldapUserStruct/) |
| value | string [] |
| JLdapUserStruct | DN | string | - [ldapUserStruct](/cms_trial/space/PSJC/434635671/ldapUserStruct/) |
| attributes | JLdapUserAttribute [] |
| JPermissionScheme | id | integer | - [admGetAllPermissionSchemes](/cms_trial/space/PSJC/512852111/admGetAllPermissionSchemes/) - [admGetPermissionScheme](/cms_trial/space/PSJC/513114265/admGetPermissionScheme/) |
| name | string |
| description | string |
| JPriority | id | integer | - [admGetAllPriorityObjectsFromScheme](/cms_trial/space/PSJC/1183383653/admGetAllPriorityObjectsFromScheme/) - [admGetAvailablePriorityObjectsForScheme](/cms_trial/space/PSJC/1182433849/admGetAvailablePriorityObjectsForScheme/) |
| name | string |
| description | string |
| iconUrl | string |
| statusColor | string |
| isDefault | boolean |
| JPriorityScheme | id | integer | - [admGetAllPrioritySchemesObjects](/cms_trial/space/PSJC/1183056204/admGetAllPrioritySchemesObjects/) - [admGetPrioritySchemeObject](/cms_trial/space/PSJC/1183252905/admGetPrioritySchemeObject/) |
| name | string |
| description | string |
| priorities | string [] |
| projects | string [] |
| JProductLastActiveDate | product | string | - [admGetLastActiveDates](/cms_trial/space/PSJC/1159823773/admGetLastActiveDates/) |
| lastActive | date |
| JProject | id | number | - [admProjectProperties](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=PSJC&title=admProjectProperties&linkCreation=true&fromPageId=435028065) |
| key | string |
| name | string |
| description | string |
| lead | string |
| url | string |
| unassignedByDefault | boolean |
| category | string |
| projecttype | string |
| JProjectIssueTypes | projectKey | string | - [admAddCustomFieldOptions](/cms_trial/space/PSJC/791282009/admAddCustomFieldOptions/) - [admDeleteCustomFieldOptions](/cms_trial/space/PSJC/790627240/admDeleteCustomFieldOptions/) - [admGetCustomFieldOptions](/cms_trial/space/PSJC/791511311/admGetCustomFieldOptions/) - [admUpdateCustomFieldOptions](/cms_trial/space/PSJC/790528847/admUpdateCustomFieldOptions/) |
| issueTypesNames | string [] |
| JRemoteIssueLink | id | integer | - [getWebLink](/cms_trial/space/PSJC/957940055/getWebLink/) - [getWebLinksForIssue](/cms_trial/space/PSJC/958955774/getWebLinksForIssue/) - [updateWebLink](/cms_trial/space/PSJC/958333364/updateWebLink/) |
| globalId | string |
| appName | string |
| relationship | string |
| iconTitle | string |
| iconUrl | string |
| summary | string |
| title | string |
| url | string |
| statusResolved | string |
| statusIconTitle | string |
| statusIconUrl | string |
| statusIconLink | string |
| JScreen | id | integer | - [admCreateScreen](/cms_trial/space/PSJC/790758340/admCreateScreenScheme/) - [admGetAllScreens](/cms_trial/space/PSJC/790758380/admGetAllScreens/) | - [admGetScreensByName](/cms_trial/space/PSJC/790987285/admGetScreensByName/) - [admUpdateScreen](/cms_trial/space/PSJC/791478898/admUpdateScreen/) |
| name | string |
| description | string |
| scope | string |
| projectKey | string |
| JScreenScheme | id | integer | - [admCreateScreenScheme](/cms_trial/space/PSJC/790758340/admCreateScreenScheme/) - [admGetAllScreenSchemes](/cms_trial/space/PSJC/790986895/admGetAllScreenSchemes/) - [admUpdateScreenScheme](/cms_trial/space/PSJC/791740479/admUpdateScreenScheme/) |
| name | string |
| description | string |
| defaultScreenId | integer |
| createScreenId | integer |
| editScreenId | integer |
| viewScreenId | integer |
| JSharePermission | id | integer | - [admShareFilter](/cms_trial/space/PSJC/722174268/admShareFilter/) - [admCopyDashboard](/cms_trial/space/PSJC/748162099/admCopyDashboard/) - [admCreateDashboard](/cms_trial/space/PSJC/747965192/admCreateDashboard/) - [admGetAllDashboards](/cms_trial/space/PSJC/748552437/admGetAllDashboards/) - [admGetDashboardById](/cms_trial/space/PSJC/748683420/admGetDashboardById/) | - [admGetDashboardsByName](/cms_trial/space/PSJC/748683364/admGetDashboardsByName/) - [admGetDashboardsByOwner](/cms_trial/space/PSJC/748618158/admGetDashboardsByOwner/) - [admGetDashboardsForUser](/cms_trial/space/PSJC/748618168/admGetDashboardsForUser/) - [admGetFavouriteDashboards](/cms_trial/space/PSJC/747801635/admGetFavouriteDashboards/) - [admUpdateDashboard](/cms_trial/space/PSJC/748718317/admUpdateDashboard/) |
| type | string |
| object | string |
| JTeam | id | string |  |
| name | string |
| isVisible | boolean |
| title | string |
| isShared | boolean |
| JUser | key | string | - [getUserByEmail](/cms_trial/space/PSJC/434831877/getUserByEmail/) - [getUserByFullName](/cms_trial/space/PSJC/434864483/getUserByFullName/) - [getUser](/cms_trial/space/PSJC/434507251/getUser/) |
| username | string |
| displayname | string |
| email | string |
| active | boolean |
| timezone | string |
| JVersion | id | number | - [admGetProjectVersion](/cms_trial/space/PSJC/434733561/getVersion/) - [getVersionFromEvent](/cms_trial/space/PSJC/491002320/getVersionFromEvent/) |
| name | string |
| description | string |
| projectId | number |
| startDate | date |
| releaseDate | date |
| archived | boolean |
| released | boolean |
| JWorkflow | id | string | - [admGetWorkflowsFromScheme](/cms_trial/space/PSJC/2255552747/admGetWorkflowsFromScheme/) |
| name | string |
| assocIssueType | string |
| statuses | string [] |
| transitions | string [] |
| JWorkflowScheme | id | integer | - [admGetAllWorkflowSchemes](/cms_trial/space/PSJC/517865958/admGetAllWorkflowSchemes/) - [admGetWorkflowScheme](/cms_trial/space/PSJC/517800504/admGetWorkflowScheme/) |
| name | string |
| description | string |
| defaultWorkflow | string |
| JWorklog | id | number | - [getWorklogsForIssues](/cms_trial/space/PSJC/434439996/getWorklogsForIssues/) |
| author | string |
| startDate | date |
| timeSpent | integererval |
| comment | string |
| issue | string |
| WebhookParam | name | string | - [getWebhookPayload](/cms_trial/space/PSJC/434733710/getWebhookPayload/) |
| values | string [] |
| WebhookPayload | queryParams | WebhookParam [] | - [getWebhookPayload](/cms_trial/space/PSJC/434733710/getWebhookPayload/) |
| httpMethod | string |
| payload | string |

---

## Jira Software types

These are structures specific to agile project management features in Jira Software. They handle boards, sprints, and other agile artifacts. These structures are only available when Jira Software is installed and are used for managing agile development processes.

| **Name** | **Fields** | **Field types** | **Returned by function** |
| --- | --- | --- | --- |
| JBoard | id | integer | - [getAllBoards](/cms_trial/space/PSJC/567574550/getAllBoards/) - [getAllKanbanBoards](/cms_trial/space/PSJC/567148594/getAllKanbanBoards/) - [getAllScrumBoards](/cms_trial/space/PSJC/567476263/getAllScrumBoards/) |
| name | string |
| type | string |
| JEpic | id | integer | - [activeEpics](/cms_trial/space/PSJC/570589652/activeEpics/) - [epics](/cms_trial/space/PSJC/570458590/epics/) - [getEpic](/cms_trial/space/PSJC/570785880/getEpic/) |
| name | string |
| summary | string |
| done | boolean |
| JSprint | id | integer | - [getAllOpenSprintegers](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480979) - [getClosedSprintegers](/cms_trial/space/PSJC/561283337/getClosedSprints/) - [getNotStartedSprintegers](/cms_trial/space/PSJC/560858284/getNotStartedSprints/) - [getStartedSprintegers](/cms_trial/space/PSJC/560400319/getStartedSprints/) |
| name | string |
| startDate | date |
| endDate | date |
| completeDate | date |
| goal | string |
| state | string |
| boardId | integer |

---

## Jira Service Management types

These are structures focused on IT service management functionality. They handle service requests, approvals, SLAs, customer portals, and other service desk specific features. These structures are only available when Jira Service Management is installed.

For actual examples using the structures see the main [Jira Service Management functions page](/cms_trial/space/PSJC/523731239/Jira+Service+Management+Functions/) or see the individual routine pages.

| **Name** | **Fields** | **Field types** | **Returned by function** |
| --- | --- | --- | --- |
| JSlaCompletedCycle | startTime | date | - [getSlaInformation](/cms_trial/space/PSJC/644940133/getSlaInformation/) |
| stopTime | date |
| breached | boolean |
| goalDuration | number |
| elepsedTime | number |
| remainingTime | number |
| JSlaInformation | name | string | - [getSlaInformation](/cms_trial/space/PSJC/644940133/getSlaInformation/) |
| completedCycles | JSlaCompletedCycle |
| ongoingCycle | JSlaOngoingCycle |
| JSlaOngoingCycle | startTime | date | - [getSlaInformation](/cms_trial/space/PSJC/644940133/getSlaInformation/) |
| breachedTime | date |
| breached | boolean |
| paused | boolean |
| withinCalendarHours | boolean |
| goalDuration | number |
| elepsedTime | number |
| remainingTime | number |
| JSMApproval | approvers | JSMApprover [] | - [answerApproval](/cms_trial/space/PSJC/654050404/answerApproval/) - [getApproval](/cms_trial/space/PSJC/621906541/getApproval/) - [getApprovals](/cms_trial/space/PSJC/622298390/getApprovals/) |
| canAnswerApproval | boolean |
| completedDate | date |
| createdDate | date |
| finalDecision | string |
| id | integer |
| name | string |
| JSMApprover | approver | JUser | - [answerApproval](/cms_trial/space/PSJC/654050404/answerApproval/) - [getApproval](/cms_trial/space/PSJC/621906541/getApproval/) | - [getApprovals](/cms_trial/space/PSJC/622298390/getApprovals/) |
| approverDecision | string |
| JSMAssetsObject | workspaceId | string | (used with asset custom fields) |
| globalId | string |
| id | string |
| JSMAttachment | created | string | - [getAttachmentsForRequest](/cms_trial/space/PSJC/622298412/getAttachmentsForRequest/) |
| filename | string |
| mimeType | string |
| size | string |
| JSMComment | attachments | JSMAttachment [] | - [getCommentForRequest](/cms_trial/space/PSJC/621906575/getCommentForRequest/) - [getCommentsForRequest](/cms_trial/space/PSJC/622134858/getCommentsForRequest/) |
| author | JUser |
| body | string |
| created | string |
| id | integer |
| isPublic | boolean |
| renderedBody | string |
| JSMCustomerRequest | actions | JSMCustomerRequestActions | - [createCustomerRequest](/cms_trial/space/PSJC/637665389/createCustomerRequest/) - [getCustomerRequest](/cms_trial/space/PSJC/621939095/getCustomerRequest/) |
| attachments | string [] |
| comments | number [] |
| createdDate | date |
| currentStatus | JSMCustomerRequestStatus |
| issueId | integer |
| issueKey | string |
| participants | JUser [] |
| reporter | JUser |
| requestTypeId | integer |
| serviceDeskId | integer |
| slaIds | number [] |
| status | JSMCustomerRequestStatus [] |
| JSMCustomerRequestActions | addAttachment | boolean | - [createCustomerRequest](/cms_trial/space/PSJC/637665389/createCustomerRequest/) - [getCustomerRequest](/cms_trial/space/PSJC/621939095/getCustomerRequest/) |
| addComment | boolean |
| addParticipant | boolean |
| removeParticipant | boolean |
| JSMCustomerRequestStatus | status | string | - [getCustomerRequestStatus](/cms_trial/space/PSJC/644678772/getCustomerRequestStatus/) |
| statusCategory | string |
| statusDate | date |
| JSMFeedback | rating | number | - [addFeedbackForRequest](/cms_trial/space/PSJC/741539984/addFeedbackForRequest/) - [getFeedbackForRequest](/cms_trial/space/PSJC/740624371/getFeedbackForRequest/) |
| comment | string |
| type | string |
| JSMKBArticle | content | string | - [getKBArticles](/cms_trial/space/PSJC/741212243/getKBArticles/) - [getServiceDeskKBArticles](/cms_trial/space/PSJC/742162499/getServiceDeskKBArticles/) |
| excerpt | string |
| source | string |
| title | string |
| JSMQueue | fields | string [] | - [getServiceDeskQueue](/cms_trial/space/PSJC/694093332/getServiceDeskQueue/) - [getAllServiceDeskQueues](/cms_trial/space/PSJC/694125994/getAllServiceDeskQueues/) |
| id | integer |
| issueCount | integer |
| jql | string |
| name | string |
| JSMRequestType | description | string | - [getRequestTypesForServiceDesk](/cms_trial/space/PSJC/693994346/getRequestTypesForServiceDesk/) - [getRequestTypeByIdForServiceDesk](/cms_trial/space/PSJC/694321675/getRequestTypeByIdForServiceDesk/) |
| helpText | string |
| iconId | integer |
| id | integer |
| issueTypeId | integer |
| portalId | integer |
| name | string |
| JSMServiceDesk | id | integer | - [getServiceDesk](/cms_trial/space/PSJC/693994370/getServiceDesk/) |
| projectId | integer |
| projectKey | string |
| projectName | string |

## Jira Product Discovery types

These are structures specific to product discovery and idea management features in Jira Product Discovery. They handle date intervals and other specialized date types for product planning. These structures are only available when Jira Product Discovery is installed and are used for managing product discovery processes.

| **Name** | **Fields** | **Field types** |
| --- | --- | --- |
| JPDInterval | start | date |
| end | date |