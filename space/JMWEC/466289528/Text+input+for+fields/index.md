# Text input for fields

This document lists the expected text input value that should be provided to set Jira Standard and Custom fields. You might also want to look at [Standard Jira fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/), [Predefined Custom fields](/cms_trial/space/JMWEC/465242312/Predefined+Custom+Fields/) and [User-created custom fields](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/) to know how to access the fields of an issue.

#### Standard Jira fields

| Field Name | Expected input value | Examples |
| --- | --- | --- |
| Affect Version/s | Version *name(s)*or *ID(s)*should be provided. You can add multiple versions by typing them separated by commas.  To obtain the ID of a version, use this REST API call that returns all version details in a project:  https://{[yourdomain.atlassian.net](http://yourdomain.atlassian.net)}/rest/api/2/project/{projectIdorprojectKey}/version  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10101. | - 2.0 - 2.0,3.0 - `id:10011` - `1.0, id:10111` |
| Assignee | *AccountId*should be provided, or empty string for *Unassigned* | `accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e` |
| Attachments | Attachment URLshould be provided. You can add multiple attachments typing the URL's separated by commas. | - <https://picsum.photos/200/300> |
| Components | Component *name(s)* or *ID(s)*should be provided. You can add multiple components by typing them separated by commas.  To obtain the ID of *Components*, navigate to the field configuration, edit the field and look at the end of the page URL in the navigation bar to find the ID.  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10101. | - C1 - C1,C2 - `id:20500` - `C3, id:20100` |
| Description | Any simple single/multi-line text should be provided | - This is a description |
| Due Date | Date in [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) format | - 2016-08-05 |
| Environment | Any simple single/multi-line text should be provided | - This is the QA Environment - QA |
| Fix Version/s | Version *name(s)*or *ID(s)*should be provided. You can add multiple versions by typing them separated by commas.  To obtain the ID of version, use this REST API call that returns all version details in a project:  https://{[yourdomain.atlassian.net](http://yourdomain.atlassian.net)}/rest/api/2/project/{projectIdorprojectKey}/version  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10101. | - 2.0 - 2.0,3.0 - ```text   id:10102   ``` - `1.0, id:10111` |
| Issue Type | Issue Type *name* or *ID*should be provided.  To obtain the ID of *Issue Type*, navigate to the field configuration, edit the field and look at the end of the page URL in the navigation bar to find the ID.  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10101. | - Bug - Task - `id:10010` |
| Labels | Any simple text should be provided. You can add multiple labels by typing them separated by spaces. | - NewLabel - Label1 Label2 Label3 - 1 2 3 |
| Linked Issues | You cannot set this field using a text value. See [JSON input for fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/) to set this. | NA |
| Original Estimate | A Number of seconds or a duration string. | - 25200 - 3w - 4w 2d 1h |
| Parent | The value should be a valid issue key.  Examples of Nunjucks expressions returning an issue key:   - {{ issue.key }} - {{ issue.fields.parent.key }} | For example:   - TEST-1 - SCRUM-222 |
| Priority | Priority *name* or *ID*should be provided.  To obtain the ID of *Priority*, navigate to the field configuration, edit the field and look at the end of the page URL in the navigation bar to find the ID.    When you set an input value using the ID(s) you need to prefix it with "id". For example: id:1. | - Highest - Low - `id:4` |
| Remaining Estimate | A Number of seconds or a duration string. | - 25200 - 3w - 4w 2d 1h |
| Reporter | *Username* should be provided. | - carter |
| Resolution | Resolution *name* or *ID*should be provided.  To obtain the ID of *Resolution*, navigate to the field configuration, edit the field and look at the end of the page URL in the navigation bar to find the ID.  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10000. | - Won't Do - Duplicate - `id:10000` |
| Security level | Security level *name* or *ID*should be provided.  When you set an input value using the ID(s) you need to prefix it with "id". For example: id:10001. | - QA Domain - Security Level for Dev - id:10001 |
| Summary | Any single-line text should be provided | - Credit Card issue module |
| Time Tracking | You cannot set this field using a text value. See [JSON input for fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/) to set this. | ```text NA ``` |
| Watchers | *AccountId*should be provided. You can add multiple users by typing them separated by commas. | - `accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e` - accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e,accountId:557356:3a41d4ee-3331-4363-8cdf-f90a2da925e8 |

#### Predefined Custom fields

| Field Name | Expected input value | Examples |
| --- | --- | --- |
| Account | Account *ID* or *name* should be provided. To obtain the Account ID navigate to the Account and look at the end of the page URL in the navigation bar to find the ID, as shown below.  Eg: [https://test.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-accounts#!/account/](https://jmwe-test-2.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-accounts#!/account/2/)[2](https://jmwe-test-2.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-accounts#!/account/2/)[/](https://jmwe-test-2.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-accounts#!/account/2/) | - `1` - `NewYork Account` |
| Approvers | *AccountId*should be provided. You can add multiple users by typing them separated by commas. | - `accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e` - accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e,accountId:557145:3a41d4ee-3331-4363-8cdf-f90a2da926h9 |
| All Capture for Jira fields | Any simple single/multi-line text should be provided | All the Capture for Jira fields expect a text value. |
| Customer Request Type | The Customer Request Type ID or name should be provided. To obtain the Customer Request Type ID   - Manually set the Customer Request Type for an issue - In the Nunjucks tester, test for the id of the Customer Request Type for the issue: {{ issue.fields['Customer Request Type'].[requestType.id](http://requestType.id) }}   Note that when setting the Customer Request Type in the [Create issue](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function, you must provide a value for *every* field that is declared as mandatory for that request type. | - `41` - `Travel Request` |
| Epic Color | Any simple single/multi-line text should be provided | - ghx-label-6 |
| Epic Link | Issue *KEY* of an Epic should be provided. | - TEST-300 - TP-33 |
| Epic Name | Any simple single/multi-line text should be provided | - `Creation of a new issue` |
| Epic Status | Status *value* should be provided | - `To Do` - `Done` |
| Flagged | Option *value* should be provided. | - Impediment |
| Organizations | The value should be a comma-separated list of Organization names or IDs. To obtain an Organization ID, navigate to the Organization and look at the end of the page URL in the navigation bar to find the ID, as shown below:  Eg: [https://test.atlassian.net/projects/PSDF/organization/](https://jmwe-test-2.atlassian.net/projects/PSDF/organization/1)[1](https://jmwe-test-2.atlassian.net/projects/PSDF/organization/1) | - 1 - 1,33 - Org 1, Org 2 - Org 1, 4 |
| Raised during | Session *ID* should be provided. The session ID can be obtained from the URL when you view the session. To obtain the Session ID navigate to the Session and look at the end of the page URL in the navigation bar to find the ID. | - 10011 |
| Request Participants | *AccountId*should be provided. You can add multiple users by typing them separated by commas. | - `accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e` - accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e,accountId:557145:3a41d4ee-3331-4363-8cdf-f90a2da926h9 |
| Satisfaction Date | Date in [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) format | - 2016-08-05 |
| Sprint | Sprint ID should be provided.  ℹ️ To identify the Sprint ID, add the Sprint to an issue and use the Nunjucks Script tester with the following template: {{issue.fields["Sprint"] }} and look at the id field in the result. | - `3` - `12` |
| Story points | Any number | - 3.1 - 10 |
| Team | Team *ID* should be provided. To obtain the Team ID navigate to the Team and look at the end of the page URL in the navigation bar to find the ID, as shown below.  Eg: [https://test.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-teams#!/team/](https://jmwe-test-2.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-teams#!/team/2)[2](https://jmwe-test-2.atlassian.net/plugins/servlet/ac/io.tempo.jira/tempo-teams#!/team/2) | - 3 - 1 (for the default team) |
| Team (Portfolio) | Team *ID* should be provided.  ℹ️ To identify the team ID, add the Team to an issue and use the Nunjucks Script tester with the following template: {{ issue.fields.Team }}  Limitations when setting this field You cannot clear this field, nor set it if it already has a value. This is due to JIRA Portfolio bugs. | - `3` - `1` |
| Test Sessions | Session *ID* should be provided. You can add multiple sessions by typing them separated by commas. To obtain the Session ID navigate to the Session and look at the end of the page URL in the navigation bar to find the ID. | - 10011 - 10012, 10013 |

#### User-created custom fields

The value expected by custom fields depends on the Custom Field Type:

| Custom field type | Expected input value | Examples |
| --- | --- | --- |
| Check boxes / Multi select list | Option *value(s)* or *id(s)*should be provided. You can add multiple options by typing the *value(s) or id(s)* separated by commas.  When you provide the id(s) you need to prefix it with "id". For example: `id:10209`  To obtain an option ID, you can go to the custom field configuration, navigate to the Option, edit it and look at the end of the page URL in the navigation bar to find the ID. | - choice1 - choice2,choice3 - id:10209,id:10206 |
| Radio buttons / Single select list | Option *value* or *id*should be provided  When you provide the id you need to prefix it with "id". For example: `id:10209`  To obtain an option ID, you can go to the custom field configuration, navigate to the Option, edit it and look at the end of the page URL in the navigation bar to find the ID. | - Option1 - Option2,Option3 - id:10204 |
| Select list (cascading) | *Parent* *value or id* - *Child* *value or id*should be provided to set both the parent and child levels. To set just the parent, you should provide only the parent *value* or *id*.  When you provide the id you need to prefix it with "id". For example: `id:10209`  To obtain the parent or child ID, you can go to the custom field configuration, navigate to the parent or child, edit it and look at the end of the page URL in the navigation bar to find the ID. | - Parent and child values:    - 2 - 2.1   - OS - Z/OS   - id:10200 - id:10202 - Parent value only:    - 2   - OS   - id:10200 |
| Single Group Picker | Group *name* should be provided | - Group1 |
| Multi Group Picker | Group *name* should be provided. You can add multiple groups by typing them separated by commas. | - Group1 - Group1,Group2 |
| Project Picker (single project) | Project *key* should be provided | - TEST |
| User Picker (single user) | *AccountId*should be provided. | accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e |
| User Picker (multiple users) | *AccountId*should be provided. You can add multiple users by typing them separated by commas. | - accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e - accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e,accountId:557145:3a41d4ee-3331-4363-8cdf-f90a2da926h9 |
| Version Picker (single version) | Version *name* should be provided. | - 2.0 |
| Version Picker (multiple versions) | Version *name* should be provided. You can add multiple versions by typing them separated by commas. | - `2.0,3.0` |
| Text Field (single line) | Any simple single text should be provided | - `Testing in progress` |
| Text Field (multi line) | Any simple single/multi-line text should be provided | - `Description:` `Development in progress` |
| Text Field (read only) | Any simple single/multi-line text should be provided | - `This is a regression test` |
| URL Field | Text representing a URL should be provided | - <https://www.google.co.in/> |
| Number Field | Number should be provided | - `30` |
| Labels | Any simple text should be provided. You can add multiple labels by typing them separated by *spaces*. | - NewLabel - Label1 Label2 Label3 - 1 2 3 |
| Date picker | Text representing a date should be provided | - ```text   2017-02-21   ``` |
| Date Time Picker | Text representing a date/time should be provided | - ```text   2017-02-21T10:20:00.000+0100   ``` |
| Insight Objects | The value should be a comma-separated list of Insight Object IDs. To obtain an Insight Object ID, you need to evaluate the following expression in the Nunjucks tester against an issue that has that Insight Object in the Insight Objects field: `{{ issue.fields["Insight Objects"][0].id }}` | - `88004398-99ef-464c-831f-498469698f29:1` - `88004398-99ef-464c-831f-498469698f29:1`,`88004398-99ef-464c-831f-498469698f29:2,88004398-99ef-464c-831f-498469698f29:3` - To clear the field, use an empty value. |