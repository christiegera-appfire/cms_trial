# Release notes

Power Scripts for Jira Cloud uses two distinct version numbers:

| Version type | Description | Location | Example | Update Trigger |
| --- | --- | --- | --- | --- |
| Atlassian Marketplace version | Automatically generated descriptor with 'AC' (Atlassian Cloud) identifier | Atlassian Marketplace listing | 3.0.2-AC | Updates with each marketplace deployment. |
| App version | The internal version number in the application. | On this page. Also available in Jira Administration console:  **Power Apps Config** > **General** > **Release Notes** | 3.0.2 | Updates independently based on feature releases. |

The app version is the primary reference for features and updates.

Cloud deployments of Power Scripts automatically update to the latest version, ensuring immediate access to new features and fixes. In exceptional cases, custom version control can be implemented for specific instances.

|  |  |  |
| --- | --- | --- |
| **Title** | **Release date** | **Highlights** |
| [7.1.0 Release notes](https://support.appfire.com/space/PSJC/3553690702/7.1.0+Release+notes) | August 11, 2026 | - Bug fix:    - Fixed unavailable workflow validations after an update. |
| [7.0.0 Release notes](https://support.appfire.com/space/PSJC/3530293356/7.0.0+Release+notes) | August 10, 2026 | - Bug fix:    - Removed an incorrect license warning. |
| [5.0.0 Release notes](https://support.appfire.com/space/PSJC/3513254170/5.0.0+Release+notes) | August 8, 2026 | - Enhancements:    - Power Scripts for Jira Cloud now runs on Atlassian’s Forge platform. |
| [3.2.24 Release notes](https://support.appfire.com/space/PSJC/3501424641/3.2.24+Release+notes) | July 31, 2026 | - Enhancements:    - Added support for the `addWebhookResponseHeader()`SIL function.   - Improved Jira Cloud Migration Assistant (JCMA) migration handling. |
| [3.2.21 Release notes](https://support.appfire.com/space/PSJC/3400859655/3.2.21+Release+notes) | June 29, 2026 | - Enhancements:    - Added the addSILWorkflowAction post function.   - Added the getSILWorkflowActionPath post function. |
| [3.2.20 Release notes](/cms_trial/space/PSJC/3237937187/3.2.20+Release+notes/) | May 15, 2026 | - Enhancements:    - Improved several custom field-related functions to accept a context name or context ID as an alternative to the project and issue type mappings. |
| [3.2.19 Release notes](https://support.appfire.com/space/PSJC/3194388494/3.2.19+Release+notes) | May 1, 2026 | - Enhancements:    - Improved several functions for retrieving email addresses - Bug fixes |
| [3.2.16 Release notes](/cms_trial/space/PSJC/2413101057/3.2.16+Release+notes/) | October 6, 2025 | - Enhancements:    - Added the getCustomerObject routine   - Added the admGetWorkflowsFromScheme routine   - Reorganized the Admin configuration menu - JCMA migration bug fix |
| [3.2.15 Release notes](/cms_trial/space/PSJC/2229469185/3.2.15+Release+notes/) | July 28, 2025 | - Enhancements:    - Improved SIL Manager performance when running scripts in Default Script Context   - Improved the usersInGroups function performance - JCMA migration bug fix |
| [3.2.14 Release notes](/cms_trial/space/PSJC/2192506903/3.2.14+Release+notes/) | July 14, 2025 | - Enhancements:    - Enhanced Product Discovery field support   - Performance enhancement - Bug fixes |
| [3.2.13 Release notes](/cms_trial/space/PSJC/2098200588/3.2.13+Release+notes/) | June 9, 2025 | - Hotfix |
| [3.2.12 Release notes](/cms_trial/space/PSJC/2085060613/3.2.12+Release+notes/) | June 9, 2025 | - Enhancements:    - Implemented configurable buttons for Forms and Wizards - Bug fixes |
| [3.2.11 Release notes](/cms_trial/space/PSJC/2009006135/3.2.11+Release+notes/) | May 7, 2025 | - Bug fixes    - Fixed IMAP email body retrieval   - Fixed global JQL synchronization |
| [3.2.10 Release notes](/cms_trial/space/PSJC/1992130877/3.2.10+Release+notes/) | April 30, 2025 | - Enhancements:    - Moved to Atlassian's new JQL search REST endpoints   - Implemented a new function: getStatusCategory() |
| [3.2.9 Release notes](/cms_trial/space/PSJC/1931477524/3.2.9+Release+notes/) | April 8, 2025 | - New feature: Forms and Wizards - Enhancement: Traces recording time limit |
| [3.2.8 Release notes](/cms_trial/space/PSJC/1847558255/3.2.8+Release+notes/) | March 22, 2025 | - Enhanced migration support - Other enhancements:    - SIL Runner Gadget optimization   - Workflow Editor compatibility   - Customer Detail fields   - Increased archive size limit - Bug fixes |
| [3.2.7 Release notes](/cms_trial/space/PSJC/1632240817/3.2.7+Release+notes/) | January 17, 2025 | - New custom field functions to simplify Jira Cloud migrations. - Fixed issue impacting Power Scripts migrations to Jira Cloud. |
| [3.2.6 Release notes](/cms_trial/space/PSJC/1563722139/3.2.6+Release+notes/) | December 19, 2024 | - Enhanced post-function workflow migration support - Newly added SIL functions - Fixed Group picker search functionality issue - Fixed Power Scripts Validator wizard loading wizard |
| [3.2.3 Release notes](/cms_trial/space/PSJC/1524269228/3.2.3+Release+notes/) | December 2, 2024 | - Take control of your Jira fields with Live Fields for Jira Cloud - Increased speed for JQL indexing - Update parent issue title using SIL script - Fixed project key search in context configuration - Rich Text Field corruption when updated by multiple SIL post-functions - Fixed time zone handling in Date fields |
| [3.2.2 Release Notes](/cms_trial/space/PSJC/1434386557/3.2.2+Release+Notes/) | October 31, 2024 | - Minor release - Bug fixes & small improvements |
| [3.2.1 Release Notes](/cms_trial/space/PSJC/1416658945/3.2.1+Release+Notes/) | October 29, 2024 | - **Rushed release** - Internal library correctly included in build - Date parsing fixed - JQL Config page was not saving correctly the projects to synchronize |
| [3.2.0 Release Notes](/cms_trial/space/PSJC/1411874818/3.2.0+Release+Notes/) | October 26, 2024 | - **Major release**, runtime updated - Traces of executions - SIL Excel Connector in Cloud - Time-Zone is obeyed everywhere - Security was greatly improved |
| [3.1.3 Release Notes](/cms_trial/space/PSJC/1302102019/3.1.3+Release+Notes/) | September 18, 2024 | - Minor enhancements - A couple of bug fixes |
| [3.1.2 Release Notes](/cms_trial/space/PSJC/1234239504/3.1.2+Release+Notes/) | August 23, 2024 | - More automated project administration routines - A couple of bug fixes |
| [3.1.0 Release Notes](/cms_trial/space/PSJC/1199013900/3.1.0+Release+Notes/) | August 10, 2024 | - Basic support for CMJ and JCMA. - Script templates (BETA) - 'Team' field support - Tens of administrative routines added |
| [3.0.26 Release Notes](/cms_trial/space/PSJC/1033797796/3.0.26+Release+Notes/) | June 8, 2024 | - Two relatively minor security flaws are fixed in this release. - Better container management & statuses - Panels improvements |
| [3.0.25 Release Notes](/cms_trial/space/PSJC/1009648681/3.0.25+Release+Notes/) | May 29, 2024 | - **Rushed release** - an initialization bug in our latest addition, the incoming mail feature, was preventing the container to start up. |
| [3.0.24 Release Notes](/cms_trial/space/PSJC/1003683844/3.0.24+Release+Notes/) | May 25, 2024 | - Major features added: incoming email processing - Scripted Custom Fields can now be synced over - WebLinks functions - Issue Type Scheme functions |
| [3.0.23 Release Notes](/cms_trial/space/PSJC/933822467/3.0.23+Release+Notes/) | April 26, 2024 | - Minor bug fixes and performance improvements |
| [3.0.22 Release Notes](/cms_trial/space/PSJC/923172868/3.0.22+Release+Notes/) | April 23, 2024 | - Minor bug fixes and performance improvements |
| [3.0.21 Release Notes](/cms_trial/space/PSJC/913899545/3.0.21+Release+Notes/) | April 17, 2024 | - Implemented new performance improvements - Introduced **Scripted Custom Fields** - Updated support for the execution of large updates and refreshing issues for dealing with asynchronous updates from other add-ons |
| [3.0.20 Release Notes](/cms_trial/space/PSJC/874512390/3.0.20+Release+Notes/) | March 11, 2024 | - The JQL page was completely redesigned - Added a token expiry mechanism - Added more than 50 new routines - Improved support, available options, and screens for custom fields - Added more than 50 new routines |

Previous release notes are here: [Older Release Notes](/cms_trial/space/PSJC/573997127/Older+Release+Notes/)