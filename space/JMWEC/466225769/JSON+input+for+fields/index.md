# JSON input for fields

This document lists the expected JSON input value that should be provided to set Jira Standard and Custom fields. You might also want to look at [Standard Jira fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/), [Predefined Custom fields](/cms_trial/space/JMWEC/465242312/Predefined+Custom+Fields/) and [User-created custom fields](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/) to know how to access the fields of an issue.

#### Standard Jira fields

| Field Name | Expected input type | Expected input value | Example |
| --- | --- | --- | --- |
| Affects Version/s | An array of objects | Version object | - `[{"name":"2.0"}]` - `[{"name":"2.0"},{"name":"1.0"}]` - `{{issue.fields.fixVersions | dump}} -` Using [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations to copy the Fix Versions |
| Assignee | Object | User object, or `null` for *Unassigned* | - `{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}` - `{{issue.fields.reporter | dump}} -` Using [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) annotations to copy the Reporter - `null` |
| Attachments | An array of objects | Attachment object | - `[{"content":"`<https://picsum.photos/200/300>`"}]` |
| Component/s | An array of objects | Component object | - `[{"name":"C1"}]` - `[{"name":"C1"},{"name":"C2"}]` |
| Description | String | Any simple single/multi-line text within quotes should be provided. | - `"This is a description"` |
| Due date | String | String containing an [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) date within quotes should be provided. | - `"2016-08-09"` |
| Environment | String | Any simple single/multi-line text within quotes should be provided. | - `"This is the QA Environment"` |
| Fix Version/s | An array of objects | Version object | - `[{"name":"2.0"}]` - `[{"name":"2.0"},{"name":"1.0"}]` |
| Issue Type | Object | Issue Type object | - `{"name":"Bug"}` |
| Labels | Array of values | Value within quotes should be provided. | - `["Label"]` - `["a","b"]` |
| Linked Issues | An array of objects | IssueLink object | - `{{issue | epic | field("fields.issuelinks") | dump}} -` Using [Nunjucks](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)annotations to copy the Linked issues of the current issue's Epic. - [{   "type": {"name":"Blocks"},   "outwardIssue": {"key":"TEST-1"}   },   {   "type": {"name":"Blocks"},   "inwardIssue": {"key":"TEST-2"}   }] |
| Original Estimate | String | A Number of seconds or a duration string within quotes should be provided. | - `"3w"` - `"2w 1d 6h"` - `"25200"` |
| Parent | Object | The value should be a valid issue object, containing at least a key or id field.  Examples of Nunjucks expressions returning an issue object:   - {{ issue | dump }} - {{ issue.fields.parent | dump }} | - {"key":"TEST-1"} - {"id":"12345"} |
| Priority | Object | Priority object | - `{"name":"High"}` |
| Remaining Estimate | String | A Number of seconds or a duration string within quotes should be provided. | - `"3w"` - `"2w 1d 6h"` - `"25200"` |
| Reporter | Object | User object | - `{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}` |
| Resolution | Object | Resolution Object | - `{"name":"Duplicate"}` |
| Security level | Object | Security level object | - `{"name":"QA Domain"}` |
| Summary | String | Any simple single-line text within quotes should be provided. | - `"This is the Summary"` |
| Time Tracking | Object | Object with original and remaining estimates should be provided. Note: This requires checking the "Treat value as JSON" option. | - {   "originalEstimate": "5w",   "remainingEstimate": "4w 1d"   } - {   "originalEstimate": "5w 2h 6h",   "remainingEstimate": "25200"   } |
| Watchers | An array of objects | User object | - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}]` - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"},{"accountId":"accountId:557045:3a41d4ee-3331-4363-8cdf-f90a2da94fr3"}]` |

#### Predefined Custom fields

| Field Name | Expected input type | Expected input value | Examples |
| --- | --- | --- | --- |
| Account | String | Account *ID* or *name* | - `2` - `"NewYork Account"` |
| Approvers | An array of objects | User object | - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}]` - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"},{"accountId":"accountId:557124:3a41d4ee-3331-4363-8cdf-f90a2da92r46"}]` |
| All Capture for JIRA fields | String | Any simple single-line text within quotes should be provided. | - `"1064X780"` to set the JIRA Capture for screen resolution field |
| Epic Color | String | Any simple single-line text within quotes should be provided. | - "`ghx-label-6"` |
| Epic link | String | Issue *KEY* of an Epic should be provided within quotes. | - `"TEST-300"` - `"TP-33"` |
| Epic Name | String | Any simple single/multi-line text within quotes should be provided. | - `"Creation of a new issue"` |
| Epic Status | String | Status *value* should be provided | - `{"value":"Done"}` |
| Flagged | An array of objects | Options object | - `[{"value":"Impediment"}]` |
| Organizations | An array of values | An array of organization IDs or Organization names.  To obtain an Organization ID, navigate to the Organization and look at the end of the page URL in the navigation bar to find the ID, as shown below:  Eg: [https://test.atlassian.net/projects/PSDF/organization/](https://jmwe-test-2.atlassian.net/projects/PSDF/organization/1)[1](https://jmwe-test-2.atlassian.net/projects/PSDF/organization/1) | - `[1]` - `[1,33]` - `[Org 1, Org 2]` - `[Org 1, 4]` |
| Raised during | String | Session *ID* should be provided within quotes. The session ID can be obtained from the URL when you view the session. | - `"10011"` |
| Request Participants | An array of objects | User object | - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}]` - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"},{"accountId":"accountId:557345:3a41d4ee-3331-4363-8edf-f90a2da92f7e"}]` |
| Satisfaction Date | String | String containing an [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) date within quotes should be provided. | - `"2016-08-05"` |
| Sprint | String | Sprint *ID* should be provided within quotes.  ℹ️ To identify the Sprint ID, add the Sprint to an issue and use the Nunjucks Script tester with the following template: `{{issue.fields["Sprint"] }}`and look at the id field in the result. | - `"3"` |
| Story points | Number | Number should be provided. | - `3` |
| Team | String | Team *ID* should be provided within quotes. The team ID can be obtained from the URL when you view the tempo team. | - `"3"` - `"1"` (for the default team) |
| Team (Portfolio) | String | Team *ID* should be provided within quotes.  ℹ️ To identify the team ID, add the Team to an issue and use the Nunjucks Script tester with the following template: `{{ issue.fields.Team }}`  Limitations when setting this field You cannot clear this field, nor set it if it already has a value. This is due to JIRA Portfolio bugs. | - `"3"` - `"1"` |

#### User-created custom fields

The value expected by custom fields depend on the Custom Field Type:

| Custom field type | Expected input type | Expected input value | Examples |
| --- | --- | --- | --- |
| Check boxes/Select list (multiple) | An array of objects | Options object, each containing at least a `value or id` field.  To obtain an option ID, you can go to the custom field configuration, navigate to the Option, edit it and look at the end of the page URL in the navigation bar to find the ID. | - `[{"value":"Option A"}]` - `[{"value":"Option 1"},{"value":"Option 2"}]` - `[{"id":"10101"},{"id":"20102"}]` |
| Radio buttons/Select list(single) | Object | Option object, with the `value or id` field.  To obtain an option ID, you can go to the custom field configuration, navigate to the Option, edit it and look at the end of the page URL in the navigation bar to find the ID. | - `{"value":"A"}` - {   "value": "A",   "id": "10500"   } |
| Select list(cascading) | Object | Parent Object with the `value or id` field.  Parent Object - Child Object, with the `value or id` field.  To obtain the parent or child ID, you can go to the custom field configuration, navigate to the parent or child, edit it and look at the end of the page URL in the navigation bar to find the ID. | - `{"value":"parent", "child":{"value":"child"}}` - `{"id":"11111", "child":{"id":"22222"}}` - `{"value":"parent"}` |
| Single Group Picker | Object | Group object | - `{"name":"Group1"}` |
| Multi Group Picker | An array of objects | Groups object | - `[{"name":"Group1"}]` - `[{"name":"Group1"},{"name":"Group2"}]` |
| Project Picker (single project) | Object | Project object | - `{"key":"TEST"}` |
| User picker (Single user) | Object | User object | - `{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}` |
| User picker (Multi-users) | An array of objects | User object | - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}]` - `[{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"},{"accountId":"accountId:557124:3a41d4ee-3331-4363-8cdf-f90a2da92t4e"}]` |
| Version Picker (single version) | Object | Version object | - `{"name":"2.0"}` |
| Version Picker (multiple versions) | An array of objects | Version object | - `[{"name":"2.0"}]` - `[{"name":"2.0"},{"name":"1.0"}]` |
| Text Field (multi line) | String | Any simple single/multi-line text within quotes should be provided. | - `"This is a regression test\nResults are saved"` |
| Text Field (single line) | String | Any simple single line text within quotes should be provided. | - `"This is a regression test"` |
| Text Field (read only) | String | Any simple single/multi-line text within quotes should be provided. | - `"This is a regression test"` |
| URL Field | String | Any simple single text within quotes representing a URL should be provided. | - `"`<https://www.google.co.in/>`"` |
| Number Field | Number | Number should be provided | - `30` |
| Labels | An array of values | Value within quotes should be provided. | - `["Label"]` - `["a","b"]` |
| Date picker | String | String containing an [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) date within quotes should be provided. | - `"2017-02-15"` |
| Date Time Picker | String | String containing an [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) date/time within quotes should be provided. | - "`2017-02-21T10:20:00.000+0100"` |
| Insight Objects | An array of Insight Objects | The value should be an array of Insight Objects. To obtain an Insight Object, you need to evaluate the following expression in the Nunjucks tester against an issue that has that Asset in the Insight Objects field:  `{{ issue.fields["Insight Objects"][0] | dump(2) }}` | For a single object:  [{ "id": "88004398-99ef-464c-831f-498469698f29:1" }]  For multiple objects:  [ { "id": "88004398-99ef-464c-831f-498469698f29:1" }, { "id": "88004398-99ef-464c-831f-498469698f29:2" } ]  To clear the field, use an empty array: [] |