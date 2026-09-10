# Custom filters

Filters are essentially functions that can be applied to variables. Filters are called with a pipe operator (|) and can take arguments.

This document details *custom* Nunjucks filters created for JMWE.

## ADFparse

This is a *custom* Nunjucks filter that parses a rich text field that uses the Atlassian Document Format (ADF) such as Description, Comments, or custom textarea fields. Returns Wiki markup representation of the field that matches the Jira Rest API v2 to provide compatibility for existing scripts with v3 ADF fields. Addresses the latest changes to the [Jira Cloud REST API v3](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/). For example:

```text
{% 
  set myObj = '{ 
    "version": 1, 
    "type": "doc", 
    "content": [
      {
        "type": "text",
        "text": "Hello "
      },
      {
        "type": "text",
        "text": "world",
        "marks": [
          {
            "type": "strong"
          }
        ]
      }
    ]
  }' | ADFparse 
%}
```

## allIn

**allIn** is a *custom* Nunjucks filter that returns true if every element of the input array is included in the parameters, otherwise it returns false. The parameters can be scalar values and/or arrays of scalar values to compare against the input. This applies to an array of scalar values (string, number, etc.). For example:

`{{ ["a","c"] | allIn( ["a","b"], "c" ) }}` outputs `true` because both `a` and `c` are in the parameters  
`{{ ["a","z"] | allIn( ["a","b"], "c" ) }}` outputs `false` because `z` is not in the parameters  
`{{ issue.fields.components | field("name") | allIn("Comp1","Comp2") }}` outputs `true` if the issue's Components are `Comp1` and/or `Comp2`.

## availableOptions

This is a *custom* Nunjucks filter that operates on a string representing the name or ID of a select-type custom field implemented by a third-party add-on, such as Tempo's Account and Team fields and returns the list of values available for a Select-type field.

**Note**: This filter can be slow. Use with caution.

For example:

`{{"Account" | availableOptions}}` returns the list of available Tempo accounts.

## commentProperty

This is a *custom* Nunjucks filter that returns the value of a comment property.

For example:

`{{ issue.fields.comment.comments | last | commentProperty("sd.public.comment") | field("internal") }}` returns `true` if the latest comment of the issue is a Jira Service Desk "internal" comment.

## componentInfo

**componentInfo** is a *custom* Nunjucks filter that operates on a component ID, a component object, an array of component IDs, or an array of component objects and takes **fieldName** as a parameter. Fieldname is the name of the field to return, or a path using dot notation. If not provided, the full component object is returned.

For example:

`{{ "11205" | componentInfo | dump(2) }}` returns the component information of the component whose id is `11205` and dumps it in a "pretty" JSON format, using 2 spaces as indentation.

`{{ ["11205","11204"] | componentInfo | field("lead.accountId") }}` returns the *accountId(s)* of the component leads of the specified array of components.

`{{ issue.fields.components | componentInfo | dump(2)}}`dumps the details of the components of the current issue in JSON.

## date

This is a *custom* Nunjucks filter that offers rich date manipulation and formatting features. For more information, see [Date filter](/cms_trial/space/JMWEC/466323491/date+filter/).

## dateadd

This is a *custom* Nunjucks filter that adds (or substracts) hours, days, weeks or months from a date. Its syntax is dateadd(<number>,<units>) where :

- <number> is the number of units to add to the date (can be negative)
- <units> is one of "days", "hours", "weeks" or "months" (or their equivalent: "d", "h", "w", "m")

For example:

`{% set duedate = issue.fields.created | dateadd(2,"w") %}` sets the `duedate` variable to two weeks after the creation date of the issue.

## emailAddress

This is a *custom* Nunjucks filter that operates on a user's accountId, a user object, an array of accountIds, or an array of user objects and returns the email address of one or more users. This Nunjucks filter is now the only way to return the email address of a user, since Jira removed the emailAddress property of user objects.

For example:

`{{ issue.fields.reporter | emailAddress}}` returns the email address of the Reporter.

`{{ issue.fields.Approvers | emailAddress}}` returns an array of the emails of the issue's Approvers.

## epic

**epic** is a *custom* Nunjucks filter that returns the Epic of an issue. If you don't specify which fields to return, you can access all the fields of the Epic, just like with any issue object.

**For example:**

`{{ issue | epic }}` returns the Epic of the issue

`{{issue | epic("status") | field("fields.status.name")` returns the name of the status of the Epic.

`{{ issue` |  `epic("key") | field("fields.description")`returns the description of the Epic.

`{% set stories = issue | epic("key") | stories("status") %}` creates a variable 'stories' that holds all stories of the parent Epic of the current issue (i.e. the current issue and all its sibling stories), limiting the fields returned for each story.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## field

**field** is a *custom* Nunjucks filter that returns the value of a field of an object. It applies to an object or an array of objects and takes the field name as a parameter. In the case of an array of objects, it returns an array containing the values of the specified field for each object of the input array. The field name can also be a path (using dot notation). This is useful to access the field of the result of another filter, instead of having to use an intermediate variable.

For example:

`{{ issue.fields.versions | first | field("name") }}` returns the *name* of the first Affects Version/s.

`{{ issue | epic | field("fields.reporter.accountId") }}` returns the *accountId*of the reporter of the Epic of the issue.

`{{ issue | parentIssue | field("fields['Original Estimate']") }}` returns the original estimate of the issues' parent issue.

`{{issue.fields["Comment"].comments | field("body")}}` returns an array of strings, each string representing the body of a comment.

## fieldHistory

**fieldHistory** is a *custom* Nunjucks filter that returns the change history of the specified field of the issue. It applies to an issue object or an issue key and takes the field name or field id as a parameter. It returns an array of objects each object representing a change item.

**For example:**

`{{ "TEST-1" | fieldHistory( "assignee" ) | dump(2) }}` dumps an array of objects, each object representing a change to the Assignee field.

`{{ "TEST-1" | fieldHistory( "assignee" ) | first | field("to") }}` returns the accountId of the first assignee of the issue.

`{{ "TEST-1" | fieldHistory("Affects versions") | dump(2) }}` dumps an array of objects, each object representing a change to the Affects Versions field.

`{{ issue | fieldHistory( "Affects versions" ) | last | field("removed_string")}}` returns the Affects versions that were removed during the last change, if any.

`{{ linkedIssue | fieldHistory( "assignee" ) | field("to_string") | dump(2) }}` returns an array of display names of users the linked issue is assigned to.

## filter

This is a *custom* Nunjucks filter that filters an array, searching for either a *scalar* value (e.g. string) or an object whose fields must match with those of the array members, or an array of a path followed by a value to match. The filter returns an array of objects. When no value matches the criteria, an empty array is returned.

You can inverse the filter using its **exclude** parameter. Passing `true` in this parameter returns an array of objects that *do not* match the search.

For example:

`{{ issue.fields.fixVersions | filter({name:"3.0"}) | dump(2) }}` filters the **fixVersions**, for a version with *name* of ‘3.0’ and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ issue.fields['MWEC_Check'] | filter({value:"Option 1"}) }}` filters the options, for an option with *value* of**Option 1** and returns an array containing that option.

`{{ issue.fields['MWEC_Group picker'] | filter({}) }}` returns all the selected groups.

`{{ issue.fields.labels | filter("test") }}` filters the array of values, for label **test** and returns that label in an array.

`{{ issue.fields.versions | filter({name:"2.0"} , true) | dump(2) }}` filters the **fixVersions**, for versions that *do not* have the *name* ‘2.0’ and dumps them in a "pretty" JSON format, using 2 spaces as indentation.

`{{ issue.fields.watches | filter({accountId:issue.fields.reporter.accountId} , true) }}`  filters the **Watchers**, for users that are not the reporter of the issue.

`{{issue.fields.comment.comments | filter(["author.active",true]) | join("\n","body")}}` returns the body text of all comments made by active users, separated by newlines.

## find

This is a *custom* Nunjucks filter that finds the first element of an array matching the condition, searching for either a value (string) or an object based on the value of a field, and returns an object. When no match is found, null is returned.

For example:

`{{ issue.fields.fixVersions | find({name:"3.0"}) | dump(2) }}` finds for the first version with the **name** value of ‘3.0’and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ issue.fields['MWEC_Check'] | find({value:"Option 1"}) }}`finds for the first option with the **value**of ‘Option 1’ and returns the option.

`{{ issue.fields.components | find({}) }}` returns the first component.

`{{ issue.fields.labels | find("test") }}` finds label **test** and returns it. Can be useful to check whether the labels field contains a specific label.

## find(path, value)

This is a *custom* Nunjucks filter that finds the first element of an array of objects matching the condition, searching for the specified value at the specified path. When no match is found, **null** is returned.

For example:

`{{ issue.fields.fixVersions | find("name", "3.0"}) | dump(2) }}` finds for the first version with the **name**value of ‘3.0’and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{issue.fields.comment.comments | find("author.active", true) | field("body") }}` returns the body text of the first comment made by an activeuser.

## findUsers

This is a *custom* Nunjucks filter that returns the list of *active* users that match a specified string. The string will be searched for in the **accountId**, **emailAddress** and **displayName** fields. This filter returns an array of users. When no match is found, an empty array is returned. Note that the search string is*not* case-sensitive.

For example:

`{{ "Carter" | findUsers | dump(2) }}` returns an array of users and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ "john@acme.com" | findUsers | first | field("accountId") }}` returns the accountId of the Jira user whose email address is `john@acme.com` .

`{{ issue.fields['Custom text field'] | findUsers | first | field("emailAddress") }}` returns the email Address of the first user that matches the string in the custom text field.

## groupMembers

This is a *custom* Nunjucks filter that returns the members (users) of a group. The input to the filter can be either the *name* of the Group, the *ID* of the group, or a Group object. The maximum number of users that the filter can return is 1000. When no match is found, an empty array is returned.

By default, only active users are returned, but you can pass true as an optional parameter to return inactive users as well.

By default, only 50 members are returned, but you can pass a second parameter, maxUsers, and return at most that number of users.

For example:

`{{ ‘administrators' | groupMembers | join(',',"accountId") }}` returns the active users of the group with the name 'administrators’

`{{ issue.fields["MWEC_Group picker"] | first | groupMembers(true) | join(',',"accountId") }}` returns all (active and inactive) members of the first group of the MWEC\_Group picker field

`{{ "418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx" | groupMembers(true,60) | join(',',"accountId") }}` returns 60 (active and inactive) members of the group with an ID of “418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx"

To return the active members of all the groups that appear in the "MWEC\_group picker" multi-group picker custom field:

```javascript
{% set names = [] %}
{% for group in issue.fields["MWEC_Group picker"] %}
{% set ignored = names.push( group | groupMembers | join(",","accountId") )%}
{% endfor %}
{{names}}
```

## in

**in** is a *custom* Nunjucks filter that returns true if the input is contained in the parameters, otherwise it returns false. The parameters can be scalar values and/or arrays of scalar values to compare against the input. If the input is an array, then at least one element of the array must be included in the parameters for the filter to return true. This applies to any scalar value (string, number, etc.) or an array of scalar values. For example:

`{{ "a" | in("a","b") }}` outputs true.

`{{ "a" | in( ["a","b"], "c" ) }}` outputs true.

`{{ ["a","z"] | in( ["a","b"], "c" ) }}` outputs true because ‘a' is in the parameters.  
`{{ ["y","z"] | in( ["a","b"], "c" ) }}` outputs false because neither ‘y’ nor 'z’ is in the parameters.

`{{ issue.fields.project.key | in("TEST","KAN") }}` outputs true if the issue belongs to projects TEST or KAN.

`{{ issue.fields.assignee.accountId | in(issue.fields.watches | field("accountId"), issue.fields["Request Participants"] | field("accountId")) }}` outputs true if the **Assignee** of the issue is watching the issue or is a requesting participant.

## initiative

**initiative**is a *custom* Nunjucks filter that returns the Initiative of an issue, or more precisely the "parent" issue in the Jira Portfolio hierarchy of the issue visible through the "Parent Link" field. If you don't specify which fields to return, you can access all the fields of the Initiative, just like with any issue object.

**For example:**

`{{ issue | initiative("status") | field("fields.status.name") }}` returns the name of the status of the Initiative.

`{{ issue | initiative("key") | field("fields.description") }}`returns the description of the Initiative

`{% set epics = issue | initiative("key") | membersOfInitiative("status") %}`creates an epics variable that holds all epics of the parent Initiative of the current issue (i.e. the current issue and all its sibling epics), limiting the fields returned for each Initiative.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## insightFieldValue

**insightFieldValue** is a *custom* Nunjucks filter that returns the value of a Jira Insight Object custom field, including the details of the Insight Objects; Insight objects are a part of [Jira Assets](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-insight-in-jira-service-management-cloud/). The filter applies to the issue key or the issue object. The filter accepts parameters for the field name, and “detailed” which when set to `true` triggers the filter to return the original, detailed Insight Object field data.

**Jira Assets** is available in **Premium** and **Enterprise** versions only, and is only compatible with company-managed projects.

**For Example:**

`{{ "TEST-1" | insightFieldValue("customfield_12345", true) | dump(2) }}` returns the full JSON value of field customfield\_12345 for issue TEST-1.

`{{ "TEST-1" | insightFieldValue("customfield_12345") | first | field("label") }}` returns the label of the first Insight Object in field customfield\_12345.

## isActiveUser

The **isActiveUser** filter is a *custom* Nunjucks filter that returns true if the user exists and is active. The user, provided as input to the filter, can be either an **accountId** or a user object.

For example:

`{{issue.fields.reporter | isActiveUser}}` returns true if the Reporter of the issue is still active.

## isInGroup

The **isInGroup** filter is a *custom* Nunjucks filter that returns true if the user is in the specified group. A group may be identified by either name or ID (passed as a parameter to the filter). The user, provided as input to the filter, can be either an **accountId** or a user object.

For example:

`{{ currentUser | isInGroup("jira-administrators") }}` returns true if the current user is in the "jira-administrators" group.

`{{ issue.fields.assignee | isInGroup("418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx") }}` returns true if the assignee of the issue is in the group with the ID of "418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx".

## isInRole

The **isInRole** filter is a *custom* Nunjucks filter that returns true if the user is in the named role (passed as a parameter to the filter). The user, provided as input to the filter, can be either a **accountId** or a user object. Expected parameters are:

- **isInRole(roleName)** - Returns true if the user is in the named project role of the project of the current issue.
- **isInRole(roleName, projectKey)** - Returns true if the user is in the named project role of the project whose key is the specified projectKey.
- **isInRole(roleName, issueObject)** - Returns true if the user is in the named project role of the project of the given issue object

For example:

`{{ currentUser | isInRole("Developers") }}` returns true if the logged in user is in the "Developers" project role.

`{{ issue.fields.reporter | isInRole("Developers","ARM") }}` returns true if the reporter of the current issue is in the "Developers" project role of the project whose key is "ARM"

`{{ currentUser | isInRole("Developers",linkedIssue) }}` returns true if the logged in user is in the "Developers" project role of the project the first issue linked to the current issue with 'blocks' link type, belongs to.

## issueProperty

This is a *custom* Nunjucks filter that returns the value of an issue entity property.

For example:

`{{ issue | issueProperty("a.property") }}` returns the value of the "a.property" property of the current issue

## JSONparse

This is a *custom* Nunjucks filter that parses a JSON string and returns the resulting JavaScript Object.

For example:

`{% set myObj = '{"f1":"val"}' | JSONparse %}`  
`{{ myObj.f1 }}` outputs `val`

## linkedIssues

**linkedIssues** is a *custom* Nunjucks filter that returns an array of the issues linked to the current issue, optionally specifying one or more issue link type name(s) as they appear on the issue.

- If no link type name is specified the filter returns all linked issues except **initiative**, **memberOfInitiative**, **epic**, **parentIssue**, **stories**and **subtasks** of the issue.
- If a specified link type name is invalid, an error is logged.

If you don't specify which fields to return, you can access all the fields of these linked issues, just like with any issue object.

**For example:**

`{{ issue | linkedIssues }}` returns an array of issues linked to the current issue

`{{ issue | linkedIssues | last }}` returns the last linked issue of the current issue

`{{ issue | linkedIssues('blocks') }}` returns an array of issues linked to the current issue with 'blocks' link type.

`{{ issue | linkedIssues('blocks', 'is Initiative of') }}` returns an array of issues linked with the 'blocks' or 'is Initiative of' link types.

`{{ issue | linkedIssues('blocks', ['status','summary']) }}` returns an array of issues linked with the 'blocks' link type, with only the Summary and Status fields.

`{{ issue | linkedIssues('blocks', ['status']) | first | field("fields.status.name") }}`returns the name of the status of the first linked issue with the 'blocks' link type.

`{{ issue | linkedIssues('belongs to Initiative') | field("fields.status.name") }}`returns the name of the status of the issue's Initiative.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## membersOfInitiative

**membersOfInitiative**is a *custom* Nunjucks filter that returns the issues that belong to the Initiative. If you don't specify which fields to return, you can access all the fields of these epics, just like with any issue object.

**For example:**

`{{ issue | membersOfInitiative }}` returns an array of the epics associated with the Initiative.

`{{ issue | membersOfInitiative("assignee") | last | field("fields.assignee.accountId") }}` returns the **accountId** of the user the last epic belonging to the Initiative is assigned to.

{{ `issue | membersOfInitiative("key") | join(",","key") }}` returns the issuekey of all epics of the Initiative, separated by a comma.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## optionID

The **optionID**filter is a *custom* Nunjucks filter that returns the Option ID (numerical ID) of an Option value applicable to a select-type field implemented by third party add-ons, such as the Tempo' s Team and Account fields. The filter is applied to a string representing an Option value and takes the **fieldNameOrID** as a parameter.

For example:

`{{ "Account 1" | optionID("Account") }}` returns the numerical ID of the Account whose name is "Account 1"

`{{ "Shared Team" | optionID("customfield_14589") }}` returns the numerical ID of the Tempo team whose name is "Shared Team"

Note that this filter can be slow. When setting the field to a constant value, it is, therefore, preferable to directly input the numerical ID in the post-function configuration, which you will get by running the Nunjucks expression above in the Nunjucks Tester.

## organizationID

The **organizationID** filter is a *custom* Nunjucks filter that returns the Jira Service Desk Organization numerical ID of one or more Organization(s). The filter is applied to a string representing an Organization name, or to an array of Organization names.

For example:

`{{ "Innovalog" | organizationID }}` returns the organization ID of the Organization "Innovalog".

`{{ ["Innovalog","Tempo"] }}` returns the organization IDs of the Organizations "Innovalog" and "Tempo".

## organizations

The **organizations** Nunjucks filter returns the Organizations a user belongs to. It applies to a user object or an **accountId** string, and takes an optional **projectKeyOrIssue** parameter that is either the project key of the service desk in which to look for the organizations, or an issue object in whose service desk to look for the organizations. If not specified, the filter returns organizations from the service desk to which the target issue belongs. If null is specified, the filter will return all organizations to which the user belongs, in any Service Desk.

For example:

`{{ issue.fields.reporter | organizations | join(",", "name") }}` returns a comma-separated list of organization names the Reporter of the current issue belongs to, in the service desk of the current issue  
`{{ currentUser | organizations("SD") | join(",", "id") }}` returns a comma-separated list of the IDs of the organizations the current user belongs to in the SD service desk.  
`{{ currentUser | organizations(null) | join(",", "id") }}` returns a comma-separated list of the IDs of the organizations the current user belongs to in any service desk.

## parentIssue

**parentIssue** is a *custom* Nunjucks filter that returns the Parent of the issue. If you don't specify which fields to return, you can access all the fields of the parent, just like with any issue object.

**For example:**

`{{ issue | parentIssue }}` returns the parent of the issue

`{{ issue` | `parentIssue("status") | field("fields.status.name") }}` returns the status of the parent issue.

`{{ issue | parentIssue | field("fields['Epic Link']") }}`returns the Epic link of the current issue's parent.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## previousStatus

This is a *custom* Nunjucks filter that operates on an issue key or issue object and returns an object representing the previous status of the issue, before the status it was in when the transition was triggered.

```text
{
  "name": "To Do",
  "id": "10000"
}
```

For example, if the issue was transitioned from status **Open** to **To Do**, and the current transition is from status **To Do** to **In Progress**, then the previousStatus filter will return the **Open** status.

This filter only returns an accurate value when run as part of a transition and not when tested in the Nunjucks tester.

**For example:**

`{{ "TEST-1" | previousStatus | field("name") }}` returns the name of the previous status

`{{ issue.key | previousStatus | field("id") }}` returns the ID of the previous status

## projectInfo

**projectInfo** is a *custom* Nunjucks filter that operates on an issue (that has the "fields.project.key" field) or a string representing a project key and returns the full details of the project, including versions and components.

**For example:**

`{{ issue | projectInfo | dump(2) }}` returns the project information of the current issue and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ "TEST" | projectInfo }}` returns the project information of a project whose key is "TEST".

`{{ parentIssue | projectInfo | field("roles") | dump(2) }}` returns the project roles of the project the parent issue and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ "TEST" | projectInfo | field("components") | find({name:"A"}) | field("lead.accountId") }}` returns the accountId of the component lead of component "A" of project "TEST".

`{{ "TEST" | projectInfo | field("versions") | last | field("name") }}` returns the name of the topmost version on the project's "Releases" tab.

## projectProperty

This is a *custom* Nunjucks filter that returns the value of a project entity property.

**For example:**

`{{ issue.fields.project | projectProperty("a.property") }}` returns the value of the "a.property" property of the current issue's project.

## remoteLinks

**remoteLinks** is a custom Nunjucks filter that returns an array of all remote links (for example a Confluence page or an issue in another Jira instance) from the issue. It applies to an issue object or an issue key.

**For example:**

`{{ issue | remoteLinks | dump(2) }}` outputs all the remote links of the issue in a "pretty" JSON format, using 2 spaces as indentation.   
`{{ issue.key | remoteLinks | find("application.type","com.atlassian.confluence") | field("object.url") }}` returns the URL of the first link to a Confluence page.

## roleMembers

This is a *custom* Nunjucks filter that returns a comma-separated list of the **accountIds** or **displayNames** of the members (users) of a project role. The filter can return either only **active** Jira members or all members including **inactive** Jira members. The input to the filter is the role name. The filter takes three optional parameters:

- **projectKeyOrIssue** - Either the key of the project having the specified project role, or an issue object whose project has the specified project role. If not specified, the current issue’s project will be used.
- **displayNames** - If true, returns display names instead of **accountIds**.
- **includeInactiveUsers** - If true, returns inactive users. **This can only be passed via a named parameter**.

Note that a maximum of 50 users per group role member will be returned.

**Note**: If you want to return all users - active and inactive - of the specified project role, you **must** used named parameters for all optional parameters. *Do not mix* positional parameters and named parameters!

**For example:**

`{{ 'Administrators' | roleMembers | join(",") }}` returns the **accountIds** of all active users of the Administrators project role

`{{ 'Administrators' | roleMembers(true) | join(",") }}`returns the **displayNames** of all active users of the Administrators project role

`{{ ‘Administrators' | roleMembers("TEST") | join(",") }}` returns the **accountIds** of all members of the Administrators project role of the project whose key is 'TEST’.

`{{ 'Administrators' | roleMembers(linkedIssue) }}` returns the **accountIds** of all members of the Administrators project role of the project to which the linked issue belongs.

`{{ ‘Administrators' | roleMembers("TEST", true) }}` returns the **displayNames** of all active members of the Administrators project role of the project 'TEST’.

`{{ ‘Administrators' | roleMembers(projectKeyOrIssue="TEST", displayNames=true, includeInactiveUsers=true) }}` returns the **displayNames** of ***all users*** of the Administrators project role of the project 'TEST’.

## searchIssues

This is a *custom* Nunjucks filter that runs a JQL query and returns matching issues. The filter operates on a string (the JQL query) and takes the following optional, *named* parameters:

- **maxResults** - Maximum number of issues to return (default 10, maximum 1000 and minimum 1)
- **fields** - (Default: "summary") Either a comma-separated string or an array of strings listing fields to return for each issue. Examples:

  - `"*all"` - include all fields - **use only if you are limiting the number of results to 10 or less**
  - `"*navigable`" - include just navigable fields (fields that can be added as a column in list view) - **use only if you are limiting the number of results to 10 or less**
  - `"summary,comment"` or `["summary","comment"`] - include just the summary and comments
  - `"-description"` - include navigable fields except for the description (the default is \*navigable for search)
  - `"*all,-comment"` - include everything except comments - **use only if you are limiting the number of results to 10 or less**

Fields should be specified as field Keys, not field names (see [Standard Jira fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/) and [User created custom fields](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/))

You can find more information about searching for Jira issues using JQL here: [Advanced searching](https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-764478330.html) and [Search Jira like a boss with JQL](https://confluence.atlassian.com/jiracore/blog/2015/07/search-jira-like-a-boss-with-jql).

**For example:**

`{{ "project=TEST order by created desc" | searchIssues | dump(2) }}`runs the specified JQL, returns 10 matching issues and dumps them in a "pretty" JSON format, using 2 spaces as indentation.

`{{ ("project=" + issue.fields.project.key + " order by created desc") | searchIssues(maxResults = 30, fields="summary,description,versions") }}`searches for issues in the project of the current issue and returns the first 30 matching issues, ordered by creation date (newer first), returning the **summary**, **description** and **Affects Version/s** fields.

`{{ "project = Test and assignee is empty" | searchIssues(fields="*navigable") }}` returns issues that are unassigned in project TEST.

`("assignee=" + issue.fields.assignee._accountId) | searchIssues(maxResults = 30)`returns the first 30 issues that have the same assignee as the current issue.

## serverInfo

This is a *custom* Nunjucks filter that displays the current server information. This allows post functions to perform actions based on the server (environment, e.g. Prod, Dev, QA) they are running on.

**For example:**

`{{ null | serverInfo | dump(2) }}` returns the server info and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ "serverTitle" | serverInfo }}` returns the server title

`{{ "deploymentType" | serverInfo == "Cloud"}}` returns `true` if the deployment type is `Cloud` (which will obviously always be true)

## sprints

**sprints** is a *custom* Nunjucks filter that returns the sprints of an issue or a board. It applies to an issue object or a board ID. For an issue, it uses the first scrum board to which the issue's project belongs. It takes an optional *state* or a list of comma-separated states as a parameter.

While applying the sprints filter to a board make sure the add-on user has the right to the board's JQL filter.

Click here to see the structure of the sprints of an Issue

```text
[
	{
    	"id": 37,
        "self": "http://www.example.com/jira/rest/agile/1.0/sprint/23",
        "state": "closed",
        "name": "sprint 1",
        "startDate": "2015-04-11T15:22:00.000+10:00",
        "endDate": "2015-04-20T01:22:00.000+10:00",
        "completeDate": "2015-04-20T11:04:00.000+10:00",
        "originBoardId": 5
    },
    {
        "id": 72,
        "self": "http://www.example.com/jira/rest/agile/1.0/sprint/73",
        "state": "future",
        "name": "sprint 2"
    }
]
```

Click here to see the structure of the sprints of a Board

```text
{
  "maxResults": 50,
  "startAt": 0,
  "isLast": true,
  "values": [
    {
      "id": 14,
      "self": "https://jmwe-test-2.atlassian.net/rest/agile/1.0/sprint/14",
      "state": "active",
      "name": "IT Sprint 1",
      "startDate": "2017-05-25T08:17:07.024+02:00",
      "endDate": "2017-06-08T08:17:00.000+02:00",
      "originBoardId": 11,
      "goal": ""
    },
    {
      "id": 15,
      "self": "https://jmwe-test-2.atlassian.net/rest/agile/1.0/sprint/15",
      "state": "future",
      "name": "IT Sprint 2",
      "originBoardId": 11
    }
  ]
}
```

**For example:**

`{{ issue | sprints }}` returns a list of sprints. You can add the `dump(2)` filter to see the actual contents.

`{{ issue | sprints | join("," , "name") }}` returns the *names* of the Sprints, separated by commas.

`{{ issue | sprints("active") | first | field("id") }}` returns the currently active first sprint *ID.*

`{{ 5 | sprints }}` returns the list of sprints for Agile board 5. You can find the board ID in its URL, after "rapidView="

`{{ 11 | sprints("active") | field("values") | first | dump(2) }}` returns first active sprint of the board. You can find the board ID in its URL, after "rapidView="

## stories

**stories** is a *custom* Nunjucks filter that returns an array of stories associated with the issue (which should be an Epic). If you don't specify which fields to return, you can access all the fields of the story, just like with any issue object.

**For example:**

`{{ issue | stories }}` returns an array of the stories associated with the Epic.

{{ `issue | stories("assignee") | last | field("fields.assignee.accountId") }}`returns the accountId of the user the last story belonging to the Epic is assigned to.

{{ `issue | stories("key") | join(",","key") }}` returns the issuekey of all stories of the Epic, separated by a comma.

**Note**: For better performance, it is recommended to specify the fields to return, whenever possible.

## subtasks

**subtasks** is a *custom* Nunjucks filter that returns an array of subtasks associated with the current issue. If you don't specify which fields to return, you can access all the fields of the subtask, just like with any issue object.

**For example:**

`{{ issue | subtasks("duedate") | first | field("fields.duedate")` returns the Due date of the first sub-task of the issue.

`{{ issue | subtasks("key") | length }}` returns the number of subtasks for an issue.

**Note**: When you need minimal information for better performance, it is recommended to use either the subtasks field of the issue or the subtasks filter specifying the fields to return, whenever possible. For example to get the status of the subtasks of the current issue.

- Using the subtasks field

  ```text
  {{ issue.fields.subtasks | field("fields.status.name") }}
  ```
- Using the subtasks filter

  ```text
  {{ issue | subtasks("status") | field("fields.status.name") }}
  ```

## text2html

This is a *custom* Nunjucks filter that converts a multi-line text value to html, as expected in the html body in the [Email Issue](/wiki/spaces/MWECS/pages/281717686) post-function. The newlines are converted to paragraphs and html tags are escaped. The input for the filter is either a multi-line text or a multi-line text field.

**For example:**

| Text or Multi-line text value | Template | Returns |
| --- | --- | --- |
| Hi  <i>This is a test Email<i>  Regards Radhika | `{{ issue.fields.description | text2html }}` | `<p>Hi</p><p>&lt;i&gt;This is a test Email&lt;/i&gt;</p><p>Regards<br>Radhika</p>` |
| Your issue has been resolved.\nPlease provide your feedback.\nThanks. | `{{ "Your issue has been resolved.\nPlease provide your feedback.\nThanks." | text2html }}` | `<p>Your issue has been resolved.<br>Please provide your feedback.<br>Thanks.</p>` |

## userInfo

This is a *custom* Nunjucks filter, which when provided with a **accountId**, or a user object containing a accountId field, returns the corresponding user object. You can [dump](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) the object, view its fields (in the template test result panel) and then either use the [field](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) filter to get a field value or pass the field as a parameter to the filter.

**For example:**

`{{currentUser | userInfo | dump(2) }}` dumps the current user object in a "pretty" JSON format, using 2 spaces as indentation.

`{{currentUser | userInfo("displayName") }}` returns the **displayName** of the current user

`{{ currentUser | userInfo | field("emailAddress") }}` returns the **emailAddress** of the current user.

`{{ issue.fields.assignee | userInfo | field("groups.size") }}` returns the number of groups to which the current assignee belongs.

## userProperty(<property key>)

The **userProperty** filter is a *custom* Nunjucks filter that returns the value of the user property key (passed as a parameter to the filter) from the user entity properties that are set on the [User Properties Editor page](/cms_trial/space/JMWEC/466256416/User+Properties+Editor/). The user, provided as input to the filter, can be either an accountId or a user object. If the requested user property cannot be found, the filter returns `undefined` (which is equivalent to an empty string).

**For example:**

`{{ currentUser | userProperty("Location") }}` returns the value of the key `Location`

`{{ issue.fields.assignee | userProperty("State") }}` returns the value of the key `State`

## usersInOrganization

The **usersInOrganization** filter is a *custom* Nunjucks filter that returns the users that belong to a Jira Service Desk Organization. The filter is applied to a number or string representing an Organization ID. If the organization is not found, returns `undefined` (which is displayed as an empty string).

**For example:**

`{{ 1 | usersInOrganization }}` returns the users in the organization whose ID is 1.

{{ `"Innovalog"` |  `organizationID | usersInOrganization`}} returns the users of the Organization "Innovalog".

## worklog

**worklog** is a *custom* Nunjucks filter that operates on an issue object or an issue key and returns an array of worklog entries.

**For example:**

`{{ issue | worklog | dump(2) }}` returns the worklog entries done for the issue and dumps it in "pretty" JSON format, using 2 spaces as indentation.

`{{ issue.key | worklog | last | field("timeSpent") }}` returns the time spent entered in the last worklog entry.