# Older Release Notes

[Unmapped macro: button-handy — no content to fall back on]

[Unmapped macro: button-handy — no content to fall back on]

## Version 3.0.19 / Released Feb 2024

#### Minor Improvements

A few routines added, linkIssue routine has been changed for performance reasons. We promised to deliver them ASAP, so we did it.

1. PS-723 | [internal, impr] New JSM routine getUserOrganizations
2. PSCL-629 | [support, impr] linkIssues did extra checks and was slow
3. | [internal, mgmt] Adjusted cache parameters to maximize standard usage
4. PS-517 | [internal, impr] Convenience routines to create boards createScrumBoardForProjects / createKanbanBoardForProjects

## Version 3.0.18 / Released Feb 2024

#### Improvements

More improvements

1. PSCL-586 | [internal, impr] Filter columns routines
2. PSCL-598 | [internal, impr] Set and get for jql custom keywords
3. PSCL-585 | [internal, impr] Added component routines: addComponent, updateComponent, deleteComponent
4. PSCL-587 | [internal, impr] Full dashboard support
5. PSCL-522 | [internal, impr] Added more JSM routines: getKBArticles, getFeedbackForRequest, addFeedbackForRequest, removeFeedbackFromRequest, getRequestsTypes, getCustomersFromServiceDesk, getServiceDeskKBArticles, createRequestTypeInServiceDesk, removeRequestTypeByIdFromServiceDesk, removeCustomersFromServiceDesk, getRequestTypePropertyKeys, getRequestTypePropertyValues, setRequestTypePropertyValue, deleteRequestTypeProperty
6. PSCL-439 | [internal, impr] Added version routines: addVersion, updateVersion, deleteVersion, archiveVersion, releaseVersion, setVersionRelease, setVersionStart

## Version 3.0.17 / Released: Jan 2024

#### Major improvements, minor bug fixes

More improvements on events and JSD support. Filter & Worklog support.

1. PSCL-139 [internal, impr] Worklog events and getWorklogFromEvent function [PSCL-139]
2. PSCL-573 [internal, impr] Attachment events and getAttachmentFromEvent [PSCL-573]
3. PSCL-560 [internal, impr] Added GET support for Objects custom field [PSCL-560]
4. PSCL-584 [internal, impr] Added getAllAccounts, createAccount and deleteAccount admin functions plus getAllUsers [PSCL-584]
5. SUPPORT-166192 [support, bug] Description / rich text contains a width in double [SUPPORT-166192]
6. PSCL-421 [internal, impr] Filter administrative functions [PSCL-421]
7. PSCL-575 [internal, impr] Filter events and getFilterFromEvent function [PSCL-575]
8. SUPPORT-166192 [support, bug] Description / rich text contains a width in double [SUPPORT-166192]
9. [internal, bug] Fixed dashboard gadget functions: createUserPicker and createMultiUserPicker
10. [internal, bug] Fixed a wrong inclusion of a older version of JS on the mail page

## Version 3.0.16 / Released: Jan 2024

#### Major improvements, minor bug fixes

We start 2024 with big improvements. JQL keywords got a lot more flexible, we added Atlassian Document Format support, and we provided a way for you to create scripts from snippets. Added support for more events. Many more functions are on the way, so stay tuned! Happy New Year!

1. PSCL-546 [internal, impr] JQL properties may be now set and calculated on current issue or other issues [PSCL-546]
2. PSCL-504 [internal, impr] Support for Atlassian Document Format [PSCL-504]
3. PSCL-561 [internal, impr] Added Agile function 'boardsForProject' [PSCL-561]
4. PSCL-425 [internal, impr] Added the ability to create new files from SIL snippets and to insert SIL snippets into current file [PSCL-425]
5. KATL-189 [internal, bug] Aliases are not immediately available [KATL-189]
6. PSCL-570 [internal, impr] Support for sprint and board events [PSCL-570]
7. PSCL-571 [internal, impr] Support for project soft deleted and version moved events [PSCL-571]
8. PSCL-555 [support, bug] Fixed downloading archives from SIL Manager [PSCL-555]
9. PSCL-512 [internal, impr] Added more JSM functions: getAllServiceDesks, getServiceDesk, getServiceDeskByProjectKey, addCustomersToServiceDesk, getAllServiceDeskQueues, getServiceDeskQueue, getIssuesInQueueFunction, getRequestTypesForServiceDesk, getRequestTypeByIdForServiceDesk, getRequestTypeFields, getRequestTypeGroupsForServiceDesk [PSCL-512]

## Version 3.0.15 / Released: Dec 2023

#### Improvements

Small improvements, bug fixes

1. PSCL-557 [internal, impr] Microsoft Outlook requires graceful degradation on SMTP+STARTTLS (ofc!) [PSCL-557]
2. PSCL-544 [internal, impr] Hardening of the Self-Help service [PSCL-544]
3. PSCL-556 [internal, impr] Added getUserPropertiesKeys function [PSCL-556]
4. SUPPORT-163096 [support, bug] Unable to Create User Properties [SUPPORT-163096]

## Version 3.0.14 / Released: Dec 2023

#### Improvements

UI improvements, more functions, internals

1. PSCL-540 [internal, impr] More ways to deal with retries. Expose the notifications toggle in dark features. [PSCL-540]
2. PSCL-543 [support, impr] Ported: add and remove groups, add and remove users to / from groups [PSCL-543]
3. PSCL-324 [internal, impr] UI Improvements [PSCL-324]
4. PSCL-538 [internal, impr] Added more Service Management functions: getCustomerRequests, getCustomerRequest, getApprovals, getApproval, getAttachmentsForRequest, getCommentsForRequest, getCommentForRequest, getSubscriptionStatus [PSCL-538]
5. PSCL-539 [internal, impr] Added JSM function: createCustomerRequest [PSCL-539]
6. PSCL-545 [support, impr] Added STARTTLS support for mail [PSCL-545]
7. PSCL-548 [support, impr] Dealt with the unreliability of the Atlassian license service [PSCL-548]
8. PSCL-537 [internal, impr] Added more JSM functions: getRequestParticipants, getSlaInformation, getCustomerRequestStatus [PSCL-537]
9. SUPPORT-162834 [support, bug] When entering text containing double-quotes in the message box, the code containing the “Jira Expressions” will fail [SUPPORT-162834]

## Version 3.0.13 / Released: Nov 2023

#### Thanksgiving version

TLS / SSL configuration now possible. You will be able to better secure the comms with your own internet-exposed services and resources. Performance improvement on update issues.

1. SUPPORT-128343 [support, bug] Dashboard Gadget Params - Parameters are not carried over on run [SUPPORT-128343]
2. PSCL-475 [internal, impr] TLS/SSL certificates over connections [PSCL-475]
3. PSCL-519 [internal, impr] userTimezone() and userCurrentDate() functions [PSCL-519]
4. PSCL-477 [support, bug] Watchers should not be read-only and should impact performance as little as possible [PSCL-477]
5. PSCL-541 [support, bug] Mentioned in SUPPORT-128158, createIssue CF mapping problem [PSCL-541]
6. PSCL-514 [internal, bug] Documentation links were pointing to server doc sets [PSCL-514]

## Version 3.0.12 / Released: Nov 2023

#### Improvements & bug fixes

Dark feature: Atlassian retries control

1. SIL-72 [internal, impr] Language improvement : Null on struct members. [SIL-72]
2. SIL-73 [internal, bug] Interval calculation is wrong with dates prior to 1955 [SIL-73]
3. SUPPORT-127919 [support, bug] Power Scripts Validator breaks after update, when script contains line breaks [SUPPORT-127919]
4. PSCL-534 [support, fug] Dark feature: Atlassian retry policy [PSCL-534]

## Version 3.0.11 / Released: Nov 2023

#### Improvements & bug fixes

Asynchronous actions. Updated all libraries

1. PSCL-474 [internal, impr] Asynchronous actions [PSCL-474]
2. SUPPORT-127696 [support, bug] Numeric custom fields do not get treated right on createIssue [SUPPORT-127696]
3. PSCL-530 [internal, bug] Dashboard Gadget Params - Parameters are not displayed for non-admin users [PSCL-530]

## Version 3.0.10 / Released: Nov 2023

#### Bug fixes and improvements

1. SUPPORT-125145 [support, impr] autotransition function to accept transition name too [SUPPORT-125145]
2. SUPPORT-127337 [support, bug] aliases are not always getting resolved [SUPPORT-127337]
3. PSCL-525 [internal, bug] Fixed the Issue Type picker selection in the SIL Issue Panels add/edit screens [PSCL-525]

## Version 3.0.9 / Released: Nov 2023

#### Improvements

More improvements, some small bug fixes. Providing Agile functions ( [Jira Software Functions](/cms_trial/space/PSJC/523993366/Jira+Software+Functions/) ). lastFieldHistory returns now an array 2 elements wider to be castable to JFieldChange.

1. PSCL-506 [internal, impr] Jira Agile Board functions [PSCL-506]
2. PSCL-515 [internal, bug] Issues will NULL priority were yielding errors [PSCL-515]
3. PSCL-516 [internal, impr] aliases are now fully cached [PSCL-516]
4. PSCL-507 [internal, impr] Jira Agile Issues functions [PSCL-507]
5. SUPPORT-126891 [support, bug] Documentation on lastFieldHistory states that array should be castable to JFieldChange [SUPPORT-126891]
6. PSCL-509 [internal, impr] Added Service Management Organizations functions: getOrganizationNameById, getOrganizationIdByName, getOrganizationPropertyKeys, getOrganizationPropertyValues, setOrganizationPropertyValue, deleteOrganizationProperty, getUsersInOrganization, addCustomerToOrganization, removeCustomerFromOrganization, addOrganization, removeOrganization [PSCL-509]
7. SUPPORT-126892 [support, bug] Dashboard Gadget Rule - Roles are empty [SUPPORT-126892]
8. PSCL-472 [internal, impr] Added the ability to filter by project & issue type for listeners that react to Issue events [PSCL-472]

## Version 3.0.8 / Released: Oct 2023

#### Improvements

Lots of improvements on the engine itself, and on the supported features as well. Potential breaking changes: cloneIssue() receives now the project as a param, which may render prior usage unusable in some particular cases.

1. PSCL-476 [internal, impr] Performance improvements [PSCL-476]
2. PSCL-476 [internal, impr] Part of the above, added cloneIssue() param, addIssueToSprint(), addIssuesToSprint() functions [PSCL-476]
3. SUPPORT-124107 [support, impr] SIL Engine Operations: Reconfigure confirmation popup [SUPPORT-124107]
4. PSCL-501 [internal, impr] Ported CF aliases editing in cloud [PSCL-501]
5. SUPPORT-125651 [support, bug] Fixed the Editor Console's Copy and Download buttons [SUPPORT-125651]
6. PSCL-482 [internal, bug] Validators/Conditions/Post Functions views are loading very slow [PSCL-482]
7. SUPPORT-125259 [support, bug] getIssueLinkFromEvent() does not work [SUPPORT-125259]
8. PSCL-495 [internal, impr] Basic issue sprint functions ported, foundational improvements [PSCL-495]
9. PSCL-496 [internal, impr] Added support for the next custom fields: SLA, Request Type, Request Participants, Request Language, Request Feedback, Request Feedback Date, Approvers [PSCL-496]
10. PSCL-496 [internal, impr] Added Service Management Functions: addJSDComment, createCustomer, createOrganization, deleteOrganization [PSCL-496]

## Version 3.0.7 / Released: Oct 2023

#### Bug fixes and improvements

1. PSCL-482 [internal, bug] Validators are not updated on view screen until publish [PSCL-482]
2. PSCL-430 [internal, feature] Added system functions: admReindex, admReindexIssue, admReindexProjects, getJiraVersion, getJiraBuildNumber, getAllEvents [PSCL-430]
3. SUPPORT-125259 [support, bug] SIL Listener not triggered by "Issue link added" event in Cloud Jira [SUPPORT-125259]

## Version 3.0.6 / Released: Oct 2023

#### Bug fixes

1. SUPPORT-123833 [support, bug] Fixed a NPE in sendEmail with attachments [SUPPORT-123833]
2. SUPPORT-125642 [support, bug] sendEmail sends mail but creates errors [SUPPORT-125642]

## Version 3.0.5 / Released: Oct 2023

#### Improvements and a few bug fixes

We added a feature to get in touch with you on technical subjects and we clarified the Workflow wizards UI. A huge list of project functions has been added. You can now create projects, update projects, archive and delete them set their properties, etc. The following functions have been deprecated: admProjectProperties() in favor of projectObject(), admGetProjectVersions() for getVersions(), admGetProjectVersion() for getVersion(), admGetProjectComponents() in favor of getComponents(), admGetProjectComponent() for getComponent()

1. SUPPORT-96851 [support, impr] sendEmail function does not attach file when the filename is provided instead of regex and it have special regex chars in the name [SUPPORT-96851]
2. SUPPORT-96851 [support, bug] sendEmail function is not working when transitioned via autotransition [SUPPORT-96851]
3. PSCL-449 [internal, feature] Added a new Messages section under Self Help page [PSCL-449]
4. PSCL-407 [internal, feature] Workflow wizards improvements (Conditions, Validators, Postfunctions) [PSCL-407]
5. PSCL-427 [internal, feature] Project administration functions [PSCL-427]
6. [internal, deprecation] Deprecation notice for: projectProps/admProjectProperties, admGetProjectVersions, admGetProjectVersion,admGetProjectComponents,admGetProjectComponent
7. PSCL-457 [internal, feature] Added two issue functions: admArchiveIssues and admUnarchiveIssues [PSCL-457]

## Version 3.0.4 / Released: Sep 2023

#### Bug fixes and improvements

Slimmed the product, little bug fixes and improvements you requested.

1. PSCL-405 [internal, bug] Removed unnecessary logs [PSCL-405]
2. PS-679 [internal, feature] Added some messages on SIL Manager and Power Apps Config when the container is stopped [PS-679]
3. PSCL-408 [internal, bug] Fixed an issue with the instant trigger of one-time scheduled jobs (not following schedule) [PSCL-408]
4. PSCL-410 [support, bug] Fixed editor not opening files having '&' in the name [PSCL-410]
5. SIL-64 [internal, impr] Added sysLock, sysUnlock and sysSleep functions [SIL-64]
6. SUPPORT-99069 [support, impr] SIL Manager cannot be maximized [SUPPORT-99069]
7. PSCL-446 [internal, feature] Better container management [PSCL-446]
8. PSCL-451 [internal, bug] Fixed issue with Self Help automatic restore [PSCL-451]
9. PSCL-395 [internal, bug] Fixed attachment functions that didn't work: copyAttachment, attachFileFromURL and copyAttachmentById [PSCL-395]

## Version 3.0.3 / Released: Aug 2023

#### Performance - Parameters changed, Bug fixes

In order to achieve optimal performance, we adapted several parameters to match the observed usage patterns. Listened to the early feedback from you. Very small bug fixes

1. SUPPORT-99301 [support, feature] Re-enable notifications at update [SUPPORT-99301]
2. SUPPORT-99413 [support, bug] Fixed SIL Scheduled jobs incorrect display of Schedule interval in some particular cases [SUPPORT-99413]
3. PSCL-401 [internal, bug] Fixed an attachment problem [PSCL-401]
4. PSCL-404 [internal, bug] Set/Get Issue properties must wrap value under a Json [PSCL-404]
5. [internal, perf] Changed timeouts, connectivity params, better logs

## Version 3.0.2 / Released: Aug 2023

#### Hotpatch - Bug fixes

A promise is a promise

1. PSCL-398 [support, bug] Apache CSV library added into the image [PSCL-398]
2. PSCL-397 [internal, bug] Edit meta returns null when updating issue and you have no rights to do so [PSCL-397]
3. [internal, feature] Integrating Appfire G.T. latest requests (2023-08-15)

## Version 3.0.1 / Released: Aug 2023

#### Hotpatch - Bug fixes

You reported them, we cleaned them up

1. PSCL-392 [internal, bug] Scary warning "Could not get custom field by name" is logged everytime. Harmless. [PSCL-392]
2. PSCL-391 [internal, bug] NPE getting security level on non-authenticated requests [PSCL-391]
3. SUPPORT-99183 [support, bug] SIL scripts actions fail to run when a task transition is triggered by Jira project automation [SUPPORT-99183]

## Version 3.0.0 / Released: Aug 2023

#### Major release

Many improvements, better stability. There are countless changes, and we'll try to summarize here this release. Thanks for staying with us, and we hope you will enjoy this as you enjoy the server/DC version.

1. The architecture has been completely changed and it is completely aligned with our libraries; as a consequence, SIL language is now at the latest version and we will be able to evolve the product at a better pace.
2. We hope you will notice the changes in performance, as it was improved dramatically in some areas
3. Monitoring of the solution has been addressed, both in terms of auditing and CPU + memory graphs.
4. The overall solution was greatly improved
5. The user interface is fully aligned with the server line of the product. However, the changes are more profound, as you see, we didn't just painted the fence
6. JQL: you may now declare your own keywords, attach a script to them and use that as it was native in your Jira
7. Listeners: major improvements in terms of performance and stability, as we tried simplify things for our users. You can now examine which field(s) generated the update event
8. Workflow: major improvements, conditions and validators have been simplified
9. Management: We added a 'Self-Help' page so you may upload archives, restart the engine and request more resources
10. SIL: more functions for cloud in support for listeners, components, project, ...
11. SIL: we added a script DEBUGGER. Currently in BETA but we believe it is a huge asset for the script developers. Let us know your thoughts on this!

Links to release notes:

- [Version 3.0.19 / Released Feb 2024](#version-3-0-19-released-feb-2024)
- [Minor Improvements](#minor-improvements)
- [Version 3.0.18 / Released Feb 2024](#version-3-0-18-released-feb-2024)
- [Improvements](#improvements)
- [Version 3.0.17 / Released: Jan 2024](#version-3-0-17-released-jan-2024)
- [Major improvements, minor bug fixes](#major-improvements-minor-bug-fixes)
- [Version 3.0.16 / Released: Jan 2024](#version-3-0-16-released-jan-2024)
- [Major improvements, minor bug fixes](#major-improvements-minor-bug-fixes-2)
- [Version 3.0.15 / Released: Dec 2023](#version-3-0-15-released-dec-2023)
- [Improvements](#improvements-2)
- [Version 3.0.14 / Released: Dec 2023](#version-3-0-14-released-dec-2023)
- [Improvements](#improvements-3)
- [Version 3.0.13 / Released: Nov 2023](#version-3-0-13-released-nov-2023)
- [Thanksgiving version](#thanksgiving-version)
- [Version 3.0.12 / Released: Nov 2023](#version-3-0-12-released-nov-2023)
- [Improvements & bug fixes](#improvements-bug-fixes)
- [Version 3.0.11 / Released: Nov 2023](#version-3-0-11-released-nov-2023)
- [Improvements & bug fixes](#improvements-bug-fixes-2)
- [Version 3.0.10 / Released: Nov 2023](#version-3-0-10-released-nov-2023)
- [Bug fixes and improvements](#bug-fixes-and-improvements)
- [Version 3.0.9 / Released: Nov 2023](#version-3-0-9-released-nov-2023)
- [Improvements](#improvements-4)
- [Version 3.0.8 / Released: Oct 2023](#version-3-0-8-released-oct-2023)
- [Improvements](#improvements-5)
- [Version 3.0.7 / Released: Oct 2023](#version-3-0-7-released-oct-2023)
- [Bug fixes and improvements](#bug-fixes-and-improvements-2)
- [Version 3.0.6 / Released: Oct 2023](#version-3-0-6-released-oct-2023)
- [Bug fixes](#bug-fixes)
- [Version 3.0.5 / Released: Oct 2023](#version-3-0-5-released-oct-2023)
- [Improvements and a few bug fixes](#improvements-and-a-few-bug-fixes)
- [Version 3.0.4 / Released: Sep 2023](#version-3-0-4-released-sep-2023)
- [Bug fixes and improvements](#bug-fixes-and-improvements-3)
- [Version 3.0.3 / Released: Aug 2023](#version-3-0-3-released-aug-2023)
- [Performance - Parameters changed, Bug fixes](#performance-parameters-changed-bug-fixes)
- [Version 3.0.2 / Released: Aug 2023](#version-3-0-2-released-aug-2023)
- [Hotpatch - Bug fixes](#hotpatch-bug-fixes)
- [Version 3.0.1 / Released: Aug 2023](#version-3-0-1-released-aug-2023)
- [Hotpatch - Bug fixes](#hotpatch-bug-fixes-2)
- [Version 3.0.0 / Released: Aug 2023](#version-3-0-0-released-aug-2023)
- [Major release](#major-release)

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]