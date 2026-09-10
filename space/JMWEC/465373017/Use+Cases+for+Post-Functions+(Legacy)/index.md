# Use Cases for Post-Functions (Legacy)

**Note**: the Use Cases detailed on this page are still mostly valid! However, they are in the process of being updated, both in format and in specific post-function configurations that have been changed in recent JMWE updates.

This section has use cases that help you in understanding the usage of post functions. A few post-functions of JMWE have been deprecated and will no longer be enhanced. However, they still continue to work and you can configure and use the post-functions. But it is recommended to use their replacements instead.

## [Assign to role member](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Assign%20to%20role%20member&linkCreation=true&fromPageId=465373017)

A workflow post-function that assigns the target issue to a member of a selected project role.

**Sample use cases:**

#### [light bulb on icon] On the creation of a Bug assign it to a user only if he is a Product Owner

Steps

- Create a **Product Owner** project role, with the product owner as the only member.
- Add the *Assign to role member* post-function to the **Create** transition of the Bug workflow.
- Select `Product Owner` as the project role.
- Select the Conditional execution check box `Run this post-function only if a condition is verified`.
- Input the following code template in `Condition`.

  ```text
  {{ issue.fields.issuetype.name == "Bug" }}
  ```

#### [light bulb on icon] Assign an issue to a member of the QA team when the issue is transitioned to **Ready for testing status**

Steps

- Create a **QA** project role, with the testers as its members.
- Add the *Assign to role member* post-function to the transition that leads to ***Ready for testing***.
- Select `QA` as the project role to look for.

#### [light bulb on icon] Assign an issue to a member of the Support - UTC project role only when the reporter time zone is UTC.

Steps

- Add the *Assign to role member* post-function to the **Create** transition of the issue workflow.
- Select `Support-UTC` as the project role.
- Select the Conditional execution check box `Run this post-function only if a condition is verified`.
- Input the following code in `Condition`.

  ```text
  {{ issue.fields.reporter | userProperty("TimeZone") == "UTC" }}
  ```

#### [light bulb on icon] On approving a Story assign the subtasks of the Story to a member of the Developer project role

Steps

- Add the *Assign to role member* post-function to the **Approve** transition of the issue workflow.
- Select the “Target Issue(s)” as “Sub-tasks of the current issue”
- Select `Developers` as the project role.

## [Assign to last role member](/cms_trial/space/JMWEC/466225934/Assign+to+last+role+member+(Deprecated)/)

A workflow post-function that assigns the target issue to the last assignee who belongs to the selected project role.

**Sample use cases:**

#### [light bulb on icon]**W**hen a tester reopens an issue assign the issue to a Developer who last worked on it.

Steps

- Create a **Developer** project role, with the developers as its members.
- Add the *Assign to last role member* post-function to the **Reopen** transition.
- Select `Developer` as the project role to look for.

#### [light bulb on icon] After testers have validated an issue, it should be assigned to the last product owner who worked on it for the functional validation. The product owner might either have been explicitly assigned to the issue before, to write the functional specification or have written the specification while creating the issue.

Steps

- Create a **Product Owner** project role, with the product owners as its members.
- Add the *Assign to last role member* post-function to the **Validate** transition of the User Story workflow.
- Select `Product Owner` as the project role to look for.
- Select `Include Reporter` option in case a product owner created the issue but was never assigned to it afterward

#### [light bulb on icon] Assign the Story to the tester who last worked on the Story when all the bugs blocking the Story are fixed

Steps

- Add the *Assign to last role member* post-function to the **Done** transition of the Bug workflow
- Select “Target issue(s)” as “Issues linked to the current issue through the following link type”
- Select “blocks”
- Select `Testers`as the project role to look for.
- Select the “Conditional execution” option
- Input the following script:

  ```text
  {% set linkedIssues = targetIssue | linkedIssues("blocks",["status"]) | filter(["key",issue.key],true) %}
  {{linkedIssues | filter(["fields.status.name","Done"],true) | length == 0 }}
  ```

## [Build-your-own (scripted) Post-function](/cms_trial/space/JMWEC/466289991/Build-your-own+(Nunjucks+scripted)+Post+function/)

A post-function that allows you to run an arbitrary Nunjucks template (script). This can be used to create your own post-functions.

#### [light bulb on icon] Add a worklog entry to the issue. You can do this using the callJira custom Nunjucks filter.

Steps

1. Add the “Build-your-own (scripted)” post-function to the transition
2. Input the following Nunjucks template

   ```text
   {{ "/rest/api/2/issue/:issue/worklog" | callJira(verb=("post"), params={"issue":issue.key}, 
   body={ 
     "timeSpent": "1w" 
   }
   ) | dump(2) }}
   ```
3. Save the post-function and publish the workflow

## [Clear fields](/cms_trial/space/JMWEC/466226128/Clear+fields/)

A workflow post-function that clears the value(s) of the selected field(s) of the target issue.

#### [light bulb on icon] Clear the Fix Version/s field on the reopening of a ticket.

Steps

- Add the *Clear field value*post-function to the **Reopen**transition of the workflow.
- Select the field Fix Version/s to from `Field`.

#### [light bulb on icon] Clear a set of fields on all the linked issues of the current issue when an Abort is triggered on the current issue

Steps

- Add the *Clear field value* post-function to the **Abort**transition of the workflow.
- Select the “Target Issue(s)” as “Issues linked to the current issue through any link type”
- Select all the fields to be emptied from `Field`

## [Clear fields of linked issues](/cms_trial/space/JMWEC/466289629/Clear+fields+of+linked+issues+(Deprecated)/) - Deprecated - Use [Clear Fields](/wiki/spaces/MWECS/pages/78481302/Use+cases+for+post-functions#Clear-fields) instead

A workflow post-function that clears the value of the selected field(s) of the issues linked to the current issue through a specific link type.

#### [light bulb on icon] Clear a set of fields on all the linked issues of the current issue when an Abort is triggered on the current issue

Steps

- Add the *Clear field value of linked issues*post-function to the **Abort**transition of the workflow.
- Select all the fields to be emptied from `Field`

## [Comment issue(s)](#)

A workflow post-function that creates a comment on the target issue(s). The text of the comment to be created can be any simple text or a text with Nunjucks annotations.

**Sample use cases:**

#### [light bulb on icon] A customer using Jira Service Desk should be notified via comment when someone has started working on their support request.

Steps

- Add the *Comment issue(s)* post-function to the **Start Progress** transition of the issue's workflow.
- Write the following content in the `Comment` section.

  ```text
  {{issue.fields.assignee.name}} has started working on your support request. 
  We will get back to you within 24 hours.
  ```

#### [light bulb on icon] On resolving or closing the issue, comment the issue with a summary of the worklog.

Steps

- Add the *Comment issue(s)* post-function to the **Resolve** transition of the issue's workflow.
- Write the following content in the `Comment` section.

  ```text
  {% set worklogs = issue.fields.worklog.worklogs %}
  {% set count = 1%}
  {% for worklog in worklogs %}
  Worklog {{count}}:
  Started : {{ worklog.started }}
  Time Spent : {{ worklog.timeSpent }}
  Work Description : {{ worklog.comment }}

  {% set count = count + 1 %}
  {% else %}
  No work logged for this issue
  {% endfor %}
  ```

#### [light bulb on icon] An issue is blocking another and you want to ensure the Assignee of the blocked issue is notified when the impediment has been resolved.

Steps

- Add the *Comment issue(s)* post-function to the transition that resolves the current issue.
- Select the “Target issue(s)” as “Issues linked to the current issue through the following link type:”
- Select the issue link type `blocks` under “Issue Link”
- Write the following content in the `Comment` section.

  ```text
  The impediment {{targetIssue.key}} - "{{targetIssue.fields.summary}}" has been resolved.
  ```

#### [light bulb on icon] Add a comment on all the sub-tasks when the parent is canceled

Steps

- Add the *Comment issue(s)* post-function to all the transitions of the internal issue workflow.
- Select the “Target issue(s)” as “Sub-tasks of the current issue”
- Write the following content in the `Comment` section.

  ```text
  {{ issue.fields.comment.comments | last | field("body") }}
  ```

#### [light bulb on icon] On the Approval of an issue, copy the comment added if any to its sub-tasks.

Steps

- Add the *Comment issue(s)* post-function to all the transitions of the internal issue workflow.
- Select the “Target issue(s)” as “Sub-tasks of the current issue”
- Write the following content in the `Comment` section.

  ```text
  {% if issue.fields.comment.comments and now | date("clone") - issue.fields.comment.comments | last | field("created") | date("clone") < 6000 %}
  {{ issue.fields.comment.comments | last | field("body") }}
  {% endif %}
  ```

#### [light bulb on icon] Add a comment on the Epic when its user story is resolved.

Steps

- Add the *Comment issue(s)* post-function to the **Resolved** transition of the Story workflow.
- Select the “Target issue(s)” as “Epic of the current issue”
- Write the following content in the `Comment` section.

  ```text
  The user story {{issue.key}} - "{{issue.fields.summary}}" has been resolved.
  ```

#### [light bulb on icon] The Service Desk Agent responsible for a support request should be notified when the linked Bug is resolved.

Steps

- Add the *Comment issue(s)* post-function to the **Resolved** transition of the Bug workflow.
- Select the “Target issue(s)” as “Issues linked to the current issue through the following link type:”
- Select the issue link type `blocks` under “Issue Link”
- Write the following content in the `Comment` section.

  ```text
  {{issue.key}} has been resolved. You should get back to the customer.
  ```
- Check the `Restrict to internal (Jira Service Desk only)` option to make sure the customer doesn't see the comment.

## [Comment linked issues](/cms_trial/space/JMWEC/465373854/Comment+linked+issues+(Deprecated)/) - Deprecated - Use [Comment issue(s)](#) instead

A workflow post-function that creates a comment on all issues linked to the current issue through a selected link type. The text of the comment to be created can be any simple text or a text with Nunjucks annotations.

**Sample use cases:**

#### [light bulb on icon] An issue is blocking another and you want to ensure the Assignee of the blocked issue is notified when the impediment has been resolved.

Steps

- Add the *Comment linked issues* post-function to the transition that resolves the current issue.
- Choose the issue link type `blocks`
- Write the following content in the `Comment` section.

  ```text
  The impediment {{issue.key}} - "{{issue.fields.summary}}" has been resolved.
  ```

#### [light bulb on icon] Add a comment on all the sub-tasks when the parent is canceled

Steps

- Add the *Comment linked issues* post-function to all the transitions of the internal issue workflow.
- Choose the issue link type is Parent of
- Write the following content in the `Comment` section.

  ```text
  {{ issue.fields.comment.comments | last | field("body") }}
  ```

#### [light bulb on icon] On the Approval of an issue, copy the comment added if any to its sub-tasks.

Steps

- Add the *Comment linked issues* post-function to all the transitions of the internal issue workflow.
- Choose the issue link type `is Parent of`
- Write the following content in the `Comment` section.

  ```text
  {% if issue.fields.comment.comments and now | date("clone") - issue.fields.comment.comments | last | field("created") | date("clone") < 6000 %}
  {{ issue.fields.comment.comments | last | field("body") }}
  {% endif %}
  ```

#### [light bulb on icon] Add a comment on the Epic when its user stories are resolved.

Steps

- Add the *Comment linked issues* post-function to the **Resolved** transition of the Story workflow.
- Choose the issue link type `belongs to Epic`
- Write the following content in the `Comment` section.

  ```text
  The user story {{issue.key}} - "{{issue.fields.summary}}" has been resolved.
  ```

#### [light bulb on icon] The Service Desk Agent responsible for a support request should be notified when the linked Bug is resolved.

Steps

- Add the *Comment linked issues* post-function to the **Resolved** transition of the Bug workflow.
- Choose the issue link type `blocks`
- Write the following content in the `Comment` section.

  ```text
  {{issue.key}} has been resolved. You should get back to the customer.
  ```
- Check the `Restrict to internal (Jira Service Desk only)` option to make sure the customer doesn't see the comment.

## [Copy comments to related issues](/cms_trial/space/JMWEC/465474211/Copy+comments+to+related+issues/)

A workflow post-function that copies the comment(s) of the current issue to the specified related issues

**Sample use cases:**

#### [light bulb on icon] When a developer transitions an issue to "Customer Feedback" copy the developer's comment on the transition screen to the linked issue.

Steps

- Add the *Copy comments to related issues* post-function to the transition.
- Select the “Target issue(s)” as “Issues linked to the current issue through the following link type:”
- Select the issue link type under “Issue Link”
- Choose `The comment added on the transition screen, if any` under `Comments to copy`
- Click on `Add`

#### [light bulb on icon] Configure bi-directional sync of comments between the issues linked through the “causes” link type.

Steps

- Create a global transition “Sync Comments”

  - Add the *Copy comments to related issues* post-function to the transition
  - Select the “Target issue(s)” as “Issues linked to the current issue through the following link type:”
  - Select “causes” under “Issue Link”
  - Choose `All comments`
  - Add another *Copy comments to related issues* post-function to the transition
  - Select the “Target issue(s)” as “Issues linked to the current issue through the following link type:”
  - Select “is caused by” under “Issue Link”
  - Choose `All comments`
  - Add a few seconds delay
- Click on `Add`

Now when you trigger the transition on the issue(s), the newly added comments on the issue are added to the linked issue

## [Create issue](/cms_trial/space/JMWEC/466256916/Create+issue(s)/)

A workflow post-function that creates one or more new issue(s). The specifications of the issue(s) to be created can be customized using the options provided.

**Sample use cases:**

#### [light bulb on icon] Create a documentation ticket only if "Needed" is selected in the "Documentation ticket" checkboxes field

Steps

- Add the *Create issue* post-function to the transition on whose trigger you want to create a documentation ticket
- Select `Documentation` from the `Project` field.
- Select `Document` from the `Issue type` field.
- Select `caused by` in the `Link to new issue` section.
- Add an appropriate Summary (such as `Release documentation`)
- Select the conditional execution and write the following template

  ```text
  {{ issue.fields["Documentation ticket"] | find({"value":"Needed"}) != null }}
  ```

#### [light bulb on icon] On the approval of a Story, create two sub-tasks: one for Development and another for QA.

Steps

- Add the *Create issue* post-function to the transition Approve of the Story workflow to create a `QA` ticket.
- Select `Same as current issue` from the `Project` field.
- Select `Subtask` from the `Issue type` field.
- Select `Current issue` from the `Parent issue` field.
- Add an appropriate Summary (such as `Validation`)
- Repeat the above steps for the `Development` ticket.

#### [light bulb on icon] We use Jira Service Desk for support and Jira Software for development. When the support agent's problem analysis identifies a bug, a Bug should be created in the development project.

Steps

- Add the *Create issue* post-function to the **Create** transition of the Service desk project workflow.
- Select the `Development` project from the `Project` field.
- Select `Bug` from the `Issue type` field.
- Set Summary field to `{{issue.fields.summary}}`
- Select `caused by` in the `Link to new issue` section.

#### [light bulb on icon] To onboard a new employee in the HR database, create tasks for the New Employee ticket for Configuring a new computer system, Set up an employee phone and Configure a new employee work space.

Steps

- Add the *Create issue* post-function to the transition **Create** of the New Employee ticket workflow.
- Select `Same as current issue` from the `Project` field.
- Select `Sub-task` from the `Issue type` field.
- Select `Current issue` from the `Parent issue` field.
- Edit the `Summary` field value to : `Configuring a new computer system`
- Repeat the above steps for the remaining tickets.

#### [light bulb on icon] An Epic has a Story and the Story has a sub-task. When the sub-task is reopened we want to create a bug in another project linking it to the sub-task. On creation of the Bug, set its Epic link to the Story's Epic link

Steps

- Add the *Create issue*post-function to the **Reopen**transition of the sub-task workflow.
- Select the project from `Project`
- Select the `Bug` in Issue type
- Select `is caused by` in Link to new issue
- Select the Epic Link field in Set fields of new issue.
- Write the following in the `Value` section

  ```text
  {% if issue | linkedIssues("is caused by") %}
    {{ issue | linkedIssues("is caused by") | first | parentIssue | field("Epic Link") }}
  {% endif %}
  ```

#### [light bulb on icon] When a user raises a bug report, post-verification, automatically add it to the backlog in the development project and copy the issue links of the Bug to the newly created issue.

Steps

- Add the *Create issue* post-function to the transition the **Verify** of the Bug workflow.
- Select Development from the `Project` field.
- Select Task from the `Issue type` field.
- Select `duplicates` in the `Link to new issue` section.
- Add an appropriate Summary (such as `Duplicates - {{ issue.key}}`)
- Select the field `Linked Issues` from the `Set fields of new issue` section.
- Select `Copy value from current issue` from the drop-down.
- Add the post-function.

## [Copy field value from linked issues](/cms_trial/space/JMWEC/466322381/Copy+field+value+from+linked+issues+(Deprecated)/)

A workflow post-function that sets the value(s) of a selected field to the value(s) from the same/different field of an issue linked to the current issue through a selected link type.

**Sample use cases:**

#### [light bulb on icon] Copy the Fix Version/s field from the Epic to a Story, while creating a Story.

Steps

|  |
| --- |
| - Add the *Copy field value from linked issues* post-function to the **Create** transition of the Story workflow. - Choose the `has Epic` link type. - Select `Fix Version/s` in `Source Field`. - Select `Same as source field` in the `Destination field`. |

#### [light bulb on icon] Automatically add the Reporter of an Epic to the watchers of its User Stories while creating a Story.

Steps

|  |
| --- |
| - Add the *Copy field value from linked issues* post-function to the **Create** transition of the Story workflow. - Select `Reporter` in the `Field`. - Select `Watchers` in the `Destination field`. - Choose the `belongs to Epic` link type. - Select `Add value(s) to the issue` option. |

## [Copy field value to linked issues](/cms_trial/space/JMWEC/466257072/Copy+field+value+to+linked+issues+(Deprecated)/)

A workflow post-function that copies the value(s) of a selected field into the same/different field of all issues linked to the current issue through a selected link type.

**Sample use cases:**

#### [light bulb on icon] Copy the Fix Version/s field from the Stories to Epic, after resolving a user story.

Steps

|  |
| --- |
| - Add the *Copy field value to linked issues* post-function to the **Resolve** transition of the Story workflow. - Choose the `has Epic` link type. - Select `Fix Version/s` in `Source Field`. - Select `Same as source field` in the `Destination field`. - Check `Add value(s) to the linked issue` option. |

#### [light bulb on icon] On resolving an issue, copy the Fix Versions to all the linked issues regardless of the link type.

Steps

|  |
| --- |
| - Add the *Copy field value to linked issues* post-function to the transition **Resolve.** - Select `Fix Versions` in `Source Field.` - Select `Same as source field` in the `Destination field`. - Select `Any(except Issue/Subtask and Epic/Story)` in the `Issue Link Type` field. - Select `Add value(s) to the linked issue` option. |

## [Copy field value from parent issue](/cms_trial/space/JMWEC/466257573/Copy+field+value+from+parent+issue+(Deprecated)/)

A workflow post-function that sets the value(s) of a selected field with value(s) from the same/different field of an issue's parent issue.

**Sample use cases:**

#### [light bulb on icon] When creating a child bug of another bug (i.e. the parent bug), copy the fields Assignee, Component and Affect versions if they are left empty.

Steps

|  |
| --- |
| - Add the *Copy field value from parent issue* post-function to the **Create** transition of the sub-task workflow. - Select `Assignee` in `Source Field`. - Select `Same as source field` in the `Destination field`. - Select `Copy only if not set` option. - Repeat the above steps for the `Component/s` and `Affects` `Versions` fields. |

## [Copy field value to parent issue](/cms_trial/space/JMWEC/466257136/Copy+field+value+to+parent+issue+(Deprecated)/)

A workflow post-function that copies the value(s) of a selected field to the same/different field of the issue's parent issue.

**Sample use cases :**

#### [light bulb on icon] Copy the labels from each sub-task to its parent when the sub-task is closed.

Steps

|  |
| --- |
| - Add the *Copy field value to linked issues* post-function to the **Create** transition of the Sub-task workflow. - Select `Labels` in `Source Field`. - Select `Same as source field` in the `Destination field`. - Check the `Add subtask's value(s) to parent issue` option. |

## [Copy value from field to field](/cms_trial/space/JMWEC/466225614/Copy+value+from+field+to+field+(Deprecated)/)

A workflow post-function that copies the value(s) of a selected field to another field of the same issue.

**Sample use cases :**

#### [light bulb on icon] Set the component of an issue with a value selected from a cascading field that carries the Main and Sub-components in parent and child.

Steps

|  |
| --- |
| - Add the *Copy value from field to field* post-function to the **Create** transition of the issue workflow. - Select the `Cascading` field as the `From field`. - Select the `Components` field as the `To field.` - Select `Return "parent - child" for cascading custom fields` option.   Note: The Component name should be in `Component - Subcomponent` format. |

#### [light bulb on icon] Issues in our project are fixed in the version they are found . So I want to copy the Affect versions of the issue to the Fix Versions, on resolving the issue.

Steps

|  |
| --- |
| - Add the *Copy value from field to field* post-function to the **Resolve** transition of the issue's workflow. - Select `Affect Version/s` as the `From field.` - Select `Fix Version/s` as the `To field`. |

#### [light bulb on icon] I want 'Capture for JIRA Environment' field to be copied to the 'Environment' field when a bug is created using Capture for JIRA.

Steps

|  |
| --- |
| - Add the *Copy value from field to field* post-function to the **Create** transition of the Bug workflow. - Select `Capture for JIRA Environment` as the `From field.` - Select `Environment` as the `To field.` |

#### [light bulb on icon] Copy value from a Single Version Picker select list to the Fix Version(s) field if the resolution provided while closing the issue is "Fixed".

Steps

|  |
| --- |
| - Add the *Copy value from field to field*post-functionto the **Close** transition of the issue's workflow. - Select the Single version picker in the `From field`. - Select the Fix Version/s in the `To field`. - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Write the following content in `Condition.`  ```text   {{ issue.fields.resolution.name == "Fixed" }}   ``` |

## [Delete issue](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Delete%20issue%20%28Archived%29&linkCreation=true&fromPageId=465373017)

A workflow post-function that deletes one or more issues.

**Sample use cases:**

#### [light bulb on icon] Automatically move the issue to a project when it is approved.

Steps

Since there is no REST API to move issues between projects the workaround is to clone the issue into the desired project and delete the current issue.

|  |
| --- |
| **Clone issue**   - Add the *Create issue*post-functionto the **Approve**transition of the issue's workflow. - Fill in mandate/all fields of the new issue in "Set fields of new issue" section - Save the post-function.   **Delete issue**   - Add the *Delete issue* post-function to the **Approve**transition of the issue's workflow. - Add a delay of a few seconds to the post-function - Save the post-function and publish the workflow |

#### [light bulb on icon] On rejecting a Story delete its subtasks

Steps

***Not suggested***

|  |
| --- |
| - Add the *Delete issue* post-function to the **Reject**transition of the Story workflow. - Select the “Target issue(s)” as “Sub-tasks of the current issue” - Save the post-function and publish the workflow |

## [Display Message to user](/cms_trial/space/JMWEC/465242070/Display+Message+to+User/)

A workflow post-function that displays a message on the issue view page to the user triggering the transition.

#### [light bulb on icon] On triggering a transition display a notification message on the issue view if a new issue has been created by the Create Issue(s) post-function with a link to the newly created issue.

Steps

- Add the *Display Message to User post-function*to a transition.
- Input the "Message title" as `New issue created`
- Input the "Message body" as:

  ```text
  A new ticket has been created.
  ```
- Select the "Message type" as `Warning`
- Select the "Action link" option
- Input the "Action title" as `Go to the created issue`
- Select the "Navigate to URL" option
- Input the URL as

  ```text
  https://myjira.atlassian.net/browse/{{ issue | issueProperty("jmwe.last.issue.created") }}
  ```

The message will be displayed as shown below in the issue view.

![JMWE for Jira Cloud project analysis interface showing workflow and issue management](/cms_trial/assets/65f552a0-dd5b-4b04-a0e9-c507e1904fdd.png)

## [Email issue](/cms_trial/space/JMWEC/466322658/Email+issue/)

A post-function that will send an email to certain recipients of the target issues specified in the post-function configuration.

**Sample use cases:**

#### [light bulb on icon] Send an Email to the voters of the issue when a new feature is approved.

Steps

|  |
| --- |
| - Add the *Email issue*post-functionto the **Approve** transition of the issue's workflow. - Input the subject of the Email in `Subject` - Select the `Voters` in `Issue members` under `Recipients.` |

#### [light bulb on icon] Send an Email notification when an issue is created but avoid Email notification when the issue is cloned

Steps

|  |
| --- |
| - Add the *Email issue*post-functionto the **Create**transition of the issue's workflow. - Input the subject of the Email in `Subject` - Select the `Recipients` you wish to send the Email to`.` - Select Conditional execution and write the following script:  ```text   {{ issue | linkedIssues('clones') | length == 0 }}   ``` |

#### [light bulb on icon] Send an Email notification to the reporter of the Service Desk ticket when a linked bug is created

Steps

|  |
| --- |
| - Add the *Email issue*post-functionto the **Create**transition of the issue's workflow. - Select the “Target issue(s)” as “Issues linked to the current issue through the following link type” - Select “blocks” as the “Issue Link” - Input the subject of the Email in `Subject` - Select “Reporter” under “Issue members” |

## [Increase value of field](/cms_trial/space/JMWEC/466289696/Increase+value+of+field/)

A workflow post-function that increases the value of a selected numerical field by one.

**Sample use cases:**

#### [light bulb on icon] Track the number of times a bug fix was rejected by the QA team.

Steps

|  |
| --- |
| - Create a **Rejection counter** numerical custom field. - Add the *Increase value of field* post-function to the **Reject** transition of the Bug workflow. - Select the `Rejection counter` field. |

## [Link issues to the current issue](/cms_trial/space/JMWEC/465242225/Link+issues+to+the+current+issue/)

A post-function that will link the current issue to all issues that satisfy a parameterized JQL query.

**Sample use cases:**

#### [light bulb on icon] Link all the Faults in Service desk project to the current issue with "blocks" link type

Steps

|  |
| --- |
| - Add the *Link issues to current issue*post-function to the transition - Input the following JQL expression  ```text   project = "Service Desk project" and issuetype =  Fault   ``` - Select `50` in Max. issues - Select the `blocks` link type in `Issue link` |

## [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+Post-functions/)

A post-function that runs a sequence of JMWE post-functions on the target issues. This is the easiest way of making sure that a series of post-functions run *in a predictable order* during a transition - it is easier and more reliable than using [Delayed execution](/cms_trial/space/JMWEC/466322009/Delayed+execution/) as was previously recommended.

#### [light bulb on icon] Create a new issue (using the Create Issue(s) post-function) and *then* send a notification email mentioning the new issue.

Steps

|  |
| --- |
| - Add the Sequence of post-functions post-function    - Add the [Create issue](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function to create a subtask   - Add the [Email issue](/cms_trial/space/JMWEC/466322658/Email+issue/) post-function to send an email. Refer to the issue created by the previous post-function using this:  ```text     {{ issue | issueProperty("jmwe.last.issue.created") }}     ``` - Save the post-function |

#### [light bulb on icon] To clone an issue and its subtasks to another project

Steps

|  |
| --- |
| 1. Add the "Sequence of post-functions" post-function to the transition 2. In the sequence add the "Create issue" post-function.     1. Select the destination project in "Project"    2. Select the "Issue type" as "Calculated" and input  ```text       {{ issue.fields.issuetype.name }}       ```    3. Select the "Link to new issue" as "clones"    4. Configure the fields    5. Click on Save 3. Add another "Create issue" post-function to clone the sub-tasks     1. Select the destination project in "Project"    2. Select the "Issue type" as "Subtask"    3. Under the "Parent issue" input the following template:  ```javascript       {{ transition.context.newIssueKey }}       ```    4. Select "Multiple issue creation" option and input the following template:  ```javascript       {{ issue | subtasks | length }}       ```    5. Save the post-function. 4. Click on "Save" 5. Publish the workflow. |

#### [light bulb on icon] Assign the subtasks of the current issue to the Developers project role and send an email to the assignee of the subtask

Steps

|  |
| --- |
| 1. Add the "Sequence of post-functions" post-function to the transition     1. In the sequence add the Assign to role member post-function    2. Select the project role “Developers”    3. Save the post-function    4. Add “Email issue” post-function    5. Input the “Subject” and “Body” of the Email    6. Select “Assignee” under “Issue members”    7. Save the post-function 2. Click on "Save" 3. Publish the workflow. |

## [Set field value](/cms_trial/space/JMWEC/465504849/Set+issue+fields/)

A workflow post-function that sets the value of a selected field of the target issues to the specified value

**Sample use cases:**

#### [light bulb on icon] Assign a reopened issue to the last person who last commented it.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the **Reopen** transition of the issue's workflow. - Select the `Assignee` field. - Write the following content in the `Value` section  ```text   {{ issue.fields.comment.comments | last | field("author.accountId") }}   ``` |

#### [light bulb on icon] Automatically add the Reporter of an Epic to the watchers of its User Stories while creating a Story.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the **Create**transition of the issue's workflow. - Select the Watchers field. - Write the following content in the `Value` section  ```text   {{ issue | epic | field("reporter") }}   ``` |

#### [light bulb on icon] Set the due date to today's date

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition. - Select the `Due date` field. - Write the following content in the `Value` section.  ```text   {{ now }}   ``` |

#### [light bulb on icon] Capture the developer who resolved an issue in a custom single-user picker field

Steps

|  |
| --- |
| - Create a `Resolved By` single-user picker custom field. - Add the *Set field value* post-function to the "Resolve Issue" transition. - Select the `Resolved By` field. - Write the following content in the `Value` section.  ```text   {{ currentUser.accountId }}   ``` |

#### [light bulb on icon] Assign the issue to the current user when the issue is being self-reviewed.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition that leads to the **Self-reviewed** status. - Select `Assignee` field. - Write the following content in the `Value` section  ```text   {{ currentUser.accountId }}   ``` |

#### [light bulb on icon] On the reopen of an issue, if a user is selected in the transition screen, verify that the user belongs to the Approvers. If not, assign the issue to the first user of the Approvers field.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition that leads to the **Reopen** status. - Select `Assignee` field. - Write the following content in the `Value` section  ```text   {% if issue.fields.Approvers | find({"accountId":issue.fields.assignee.accountId}) !=null %}   	{{issue.fields.assignee.accountId }}   {% else %}   	{{ issue.fields.Approvers | first | field("accountId") }}   {% endif %}   ``` |

#### [light bulb on icon] On the approval of an issue, append the current user to a multi-user picker custom field only when the current user is listed in "Approvers" field list.

Steps

|  |
| --- |
| - Add the *Set field value*post-function to the **Approve** transition of the issue workflow. - Select the **Approved By** field. - Write the following content in the `Value` section.  ```text   {% if issue.fields.Approvers | find({name:currentUser.accountId}) !=null %}   	{{ currentUser.accountId }}   {%endif%}   ``` - Select the `Add value(s) to the field` option. |

#### [light bulb on icon] On creating an issue, add it to the first active Sprint of the board the issue belongs to.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition **Create.** - Select `Sprint` field. - Write the following content in the `Value` section  ```text   {{ issue | sprints("active") | first | field("id") }}   ``` |

#### [light bulb on icon] Set the due date to issue created plus five days

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition **Create.** - Select Due date field. - Write the following content in the `Value` section  ```text   {{ issue.fields.created | dateadd(5,"d") }}   ``` |

#### [light bulb on icon] On the creation of an issue assign the issue to the current user only if the user belongs to the Administrators group.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the Create transition - Select the `Assignee` field. - Write the following content in the `Value` section  ```text   {{ currentUser.accountId }}   ``` - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`.  ```text   {{ currentUser | isInGroup("jira-administrators") }}   ``` |

#### [light bulb on icon] Copy Jira service desk customers in a multi-user picker field to Request Participants ignoring the reporter of the issue

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Request Participants` field. - Write the following content in the `Value` section  ```text   {{ issue.fields["Multi-user picker field"] | filter({accountId:issue.fields.reporter.accountId} , true) | join(',',"accountId") }}   ``` |

#### [light bulb on icon] On creating an issue, pick the component of the issue from a cascading field that carries the Main and Sub-components

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Component/s` field. - Write the following content in the `Value` section  ```text   {{ issue.fields['Cascading field'].value }},{{ issue.fields['Cascading field'] | field("child.value") }}   ``` |

#### [light bulb on icon] Set the Original estimate of the issue to the difference of its creation date and Due date

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Original Estimate` field. - Write the following content in the `Value` section  ```text   {% if issue.fields.duedate >= issue.fields.created %}   	{{ issue.fields.duedate | date('diff',issue.fields.created, 'days') }}d   {% else %}   	{{ issue.fields.created | date('diff',issue.fields.duedate, 'days') }}d   {% endif %}   ``` |

#### [light bulb on icon] Set the priority of the issue to Highest if the issue belongs to the "Customer Portal" component

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Priority` field. - Write `Highest` in the `Value` section - Write the following in `Conditional execution`  ```text   {{ issue.fields.components | find({name: "Customer Portal"}) }}   ``` |

#### [light bulb on icon] Assign the issue to the Project lead, if the issue is unassigned on creation

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Assignee` field. - Write the following in the `Value` section  ```text   {{ issue | projectInfo | field("lead.accountId")}}   ``` - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`  ```text   {{ issue.fields.assignee == null }}   ``` |

#### [light bulb on icon] Set the Affects Version/s of the issue to Affects Version/s of all its linked issues

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Affects Version/s` field. - Write the following in the `Value` section  ```text   {%set versions = [] %}   {% set links = issue | linkedIssues %}   {%for link in links %}   	{% set ignored = versions.push(link.fields.versions) %}   {% endfor %}   {{ versions | dump(2)}}   ``` - Select "Treat value as JSON" option |

#### [light bulb on icon] Set the Component/s of the issue to components whose lead is the current user

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Component/s` field. - Write the following in the `Value` section  ```text   {% set newComponents = [] %}   {% set components = issue | projectInfo | field("components") %}   {%for component in components %}   	{% if component.lead.accountId == currentUser.accountId %}   		{% set ignored = newComponents.push(component) %}       {% endif %}   {% endfor %}   {{ newComponents | dump }}   ``` - Select "Treat value as JSON" option |

#### [light bulb on icon] On the creation of a Story, change its priority to that of the Epic if the Epic's priority is lower than the current priority of the Story

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Priority` field. - Write the following in the `Value` section  ```text   {% if issue | epic | field("fields.priority") <= issue.fields.priority %}     {{ issue | epic | field("fields.priority.name") }}   {% endif %}   ``` - Select "Ignore empty values" option - Select "Treat value as JSON" option |

#### [light bulb on icon] On the creation of a Story add the reporter of its Epic to the Watchers

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Watchers` field. - Write the following in the `Value` section  ```text   {{ issue | epic | field("fields.reporter.accountId") }}   ``` - Select "Add value(s) to issue" option |

#### [light bulb on icon] On creating an issue, Copy the component leads of the selected components to a Multi-user picker field

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the `Multi-user picker` field. - Select the `Add value(s) to issue` option - Write the following in the `Value` section  ```text   {% set components = issue | projectInfo | field("components") %}   {% set comma = joiner() %}   {% for component in issue.fields.components -%}   {%- set lead = components | find({name:component.name}) | field("lead.accountId") -%}   {%- if lead -%}{{comma()}}{{lead}}{%- endif -%}   {%- endfor %}   ``` - Select "Add value(s) to issue" option. |

#### [light bulb on icon] Add the members of the group selected in a custom Single-Group picker to the Watchers of the issue

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition of the issue's workflow. - Select the Watchers field. - Write the following content in the `Value` section.  ```text   {{ issue.fields["Single Group picker"] | groupMembers | join(',','accountId') }}   ``` - Select `Add source value(s) to the destination` `field` option. |

#### [light bulb on icon] Identify all comments made between transitions A and B and add them to a custom text field

Steps

|  |
| --- |
| - Create Date-Time picker fields `Date of Transition A` and `Date of Transition B` - Create a Mulit-line text field `Comments between transitions A and B` - Add the *Set field value* post-function to the transition A - Select the `Date of Transition A` field. - Write the following in the `Value` section  ```text   {{ now }}   ``` - Add the *Set field value* post-function to the transition B - Select the `Date of Transition B` field. - Write the following in the `Value` section  ```text   {{ now }}   ``` - Add the *Set field value* post-function to the transition on whose trigger you want to identify the comments - Select the `Comments between transitions A and B` field - Write the following in the `Value` section  ```text   Comments between Transition A and Transition B are:   {% for comment in issue.fields.comment.comments %}   {% if comment.created > issue.fields["Date of Transition A"] and comment.created < issue.fields["Date of Transition B"] or comment.updated > issue.fields["Date of Transition A"] and comment.updated < issue.fields["Date of Transition B"] %}   Comment updated/added by {{comment.author.displayName}} at {{ comment.updated | date('dddd, MMMM Do YYYY, h:mm:ss a')}}:   "{{ comment.body }}"    {% endif %}   {% endfor %}   ``` |

#### [light bulb on icon] Select the Installation tasks in the Checkboxes/Multi-select type field when all the Installations are done

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the Checkboxes field. - Write the following in the `Value` section  ```text   {% set regExp = r/^Installation.*/i %}   {% set newValues = [] %}   {% for option in issue.fields["Tasks list"] -%}   {% if regExp.test(option.value) %}   {% set ignore = newValues.push(option) %}   {%endif%}   {%- endfor %}   {{newValues | join(',',"value")}}   ``` |

#### [light bulb on icon] Add the time spent during the rework on an issue in the Rework Hours custom field, every time a rework is performed on the ticket

Steps

|  |
| --- |
| - Add the *Set field value*post-function to the transition that leads to testing after Rework - Select the `Rework Hours` field. - Write the following in the `Value` section  ```text   {% set worklog = issue | worklog %}   {% set recententry = 0 %}   {% for entry in worklog %}     {% if now | date('diff', entry.updated) < 10000 %}       {% set recententry = entry.timeSpentSeconds %}     {% endif %}   {% endfor %}   {{ (recententry + issue.fields["Rework Hours"] * 60 * 60) / 3600 }}   ``` |

#### [light bulb on icon] Set the Assignee of the issue based on the selected office

Steps

|  |
| --- |
| - Add the *Set field value*post-function to the “Create” transition - Select the `Assignee` field. - Write the following in the `Value` section  ```text   {%set map = {       "Paris": "accountId:111",       "London": "accountId:222"     }   %}   {{map[issue.fields.Office.value]}}   ``` - Save the post-function and publish the workflow   If you have a lot of combinations, it is recommended to create a Shared Nunjucks template (because of [this](/cms_trial/space/JMWEC/465241739/Handle+post-function+configurations+that+are+too+long/)) and then use it in the post-function configuration. |

#### [light bulb on icon] Display the Man hours (a custom Numeric field) of an Epic as the sum of Man hours of all the user stories linked to the Epic.

Steps

|  |
| --- |
| - Add the post-function *Set field value* to the **Create** transition of the Story workflow. - Select the “Target Issues” as “Epic of the current issue” - Select the *Man hours* field. - Write the following content in the Value section.  ```text   {{ issue.fields["Man hours"] + targetIssue.fields["Man hours"] }}   ``` |

#### [light bulb on icon] On the creation of a sub-task add its summary to the description of its parent

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the Description field. - Select the “Target Issues” as “Parent issue of the subtask” - Write the following content in the `Value` section  ```text   {{targetIssue.fields.description}}   {{issue.fields.summary}}   ``` |

#### [light bulb on icon] Set the issue's due date to the maximum due date set in its sub-tasks.

Steps

|  |
| --- |
| - Add the *Set field value* to the **Create** transition of the subtask's workflow. - Select the `Due date` field. - Select the “Target Issues” as “Parent issue of the subtask” - Write the following content in the Value section.  ```text   {{ issue.fields.duedate }}   ``` - Write the following content in the Conditional execution section.  ```text   {{ targetIssue.fields.duedate <= issue.fields.duedate }}   ``` |

#### [light bulb on icon] On the Approval of an issue copy its components to issues linked to it with duplicates link type, only if the linked issue belongs to the same project as the current issue.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition of the issue's workflow. - Select the “Target issues” as “Issues linked to the current issue through the following link type” - Select “duplicates” as the “Issue Link” - Select the `Components` field. - Write the following content in the Value section.  ```text   {{ issue.fields.components | join ("," , "name") }}   ``` - Write the following content in the Conditional execution section.  ```text   {{ issue.fields.project.key == targetIssue.fields.project.key }}   ``` |

#### [light bulb on icon] Set the assignee of the linked issues with the current user only if the user is the Developer of the linked issue.

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition you wish to. - Select the “Target issues” as “Issues linked to the current issue through any link” - Select the `Assignee` field. - Write the following content in the `Value` section  ```text   {{ currentUser.accountId}}   ``` - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`.  ```text   {{ currentUser | isInRole("Developers",linkedIssue) }}   ``` |

## [Set field value from user entity property value](/cms_trial/space/JMWEC/466257282/Set+field+value+from+User+Entity+Property+value/)

A workflow post-function that sets the value of a selected field of the current issue to the value of a User Property of the current user.

**Sample use cases:**

#### [light bulb on icon] Store the Country, Department, Location, and Pin information of the Reporter of an issue into the issue itself while creating it.

Steps

|  |
| --- |
| - Create a user entity property to store the Country information. - Add the *Set field value from user property value* post-function to the **Create** transition of the issue's workflow. - Select the field to which the Country information is supposed to be copied. - Repeat the above steps for all the other fields. |

## [Set field value of linked issues post-function](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/) - Deprecated - Use [Set field value](/wiki/spaces/MWECS/pages/78481302/Use+cases+for+post-functions#Set-field-value) instead

#### [light bulb on icon] Display the Man hours (a custom Numeric field) of an Epic as the sum of Man hours of all the user stories linked to the Epic.

Steps

|  |
| --- |
| - Add the post-function *Set field value of linked issues* to the **Create** transition of the Story workflow. - Select the *Man hours* field. - Choose the issue link type `has Epic` and write the following content in the Value section.  ```text   {{ issue.fields["Man hours"] + targetIssue.fields["Man hours"] }}   ``` |

#### [light bulb on icon] On the creation of a sub-task add its summary to the description of its parent

Steps

|  |
| --- |
| - Add the *Set field value* post-function to the transition - Select the Description field. - Select `is Subtask of` in the Issue link type - Write the following content in the `Value` section  ```text   {{linkedIssue.fields.description}}   {{issue.fields.summary}}   ``` |

#### [light bulb on icon] Set the issue's due date to the maximum due date set in its sub-tasks.

Steps

|  |
| --- |
| - Add the *Set field value of linked issues* to the **Create** transition of the subtask's workflow. - Select the `Due date` field. - Choose the issue link type `is Subtask of` - Write the following content in the Value section.  ```text   {{ issue.fields.duedate }}   ``` - Write the following content in the Conditional execution section.  ```text   {{ linkedIssue.fields.duedate <= issue.fields.duedate }}   ``` |

#### [light bulb on icon] On the Approval of an issue copy its components to issues linked to it with duplicates link type, only if the linked issue belongs to the same project as the current issue.

Steps

|  |
| --- |
| - Add the *Set field value of linked issues* post-function to the transition of the issue's workflow. - Select the `Components` field. - Choose the issue link type as `duplicates` - Write the following content in the Value section.  ```text   {{ issue.fields.components | join ("," , "name") }}   ``` - Write the following content in the Conditional execution section.  ```text   {{ issue.fields.project.key == targetIssue.fields.project.key }}   ``` |

#### [light bulb on icon] Set the assignee of the linked issues with the current user only if the user is the Developer of the linked issue.

Steps

|  |
| --- |
| - Add the *Set field value of linked issues* post-function to the transition you wish to. - Select the `Assignee` field. - Write the following content in the `Value` section  ```text   {{ currentUser.accountId}}   ``` - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`.  ```text   {{ currentUser | isInRole("Developers",linkedIssue) }}   ``` |

## [Shared Action post-function](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/)

A post-function that runs an Action (a sequence of one or more JMWE post-functions), created in the [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) page, on the target issues.

**Sample use cases:**

#### [light bulb on icon] Setting multiple field values on the Create transition of every workflow of the instance

Steps

|  |
| --- |
| 1. Go to Manage apps → Jira Misc Workflow Extensions - >Shared Actions 2. Click on "New Shared Action" 3. Name it - "Set fields" 4. Click on "Add post-function"     - Add the Set field value post-function and configure it to set a field value    - Click on "Save"    - Repeat step 4 and add all other post-functions 5. Click on "Save" 6. Go to the "Create" transition of a workflow 7. Add the "Shared Action" post-function 8. Select "Set fields" shared action 9. Click on "Save" 10. Publish the workflow 11. Repeat the same with the "Create" transitions of all other workflows. |

## [Transition issue](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/)(s)

A workflow post-function that triggers a transition on the target issues. This can be used to an issue one step further in the workflow.

**Sample use cases:**

#### [light bulb on icon] Start the progress on an issue immediately after its creation.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function* to the **Create** transition of the issue's workflow. - Input the transition name or ID. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Automatically escalate an issue if it is being raised with a "Blocker" priority.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function*to the **Create**transition of the issue's workflow. - Input the transition name or ID of the transition that escalates the issue. - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Write the following content in the `Condition` section.  ```text   {{ issue.fields.priority == "Blocker" }}   ``` - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Start the progress on an issue immediately after its creation if the reporter of the issue is a Project Manager.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function*to the **Create**transition of the issue's workflow. - Input the transition name or ID. - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`.  ```text   {{ issue.fields.reporter.accountId | isInRole("Project Managers") }}   ``` - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Transition an issue only when all the Business Approvers approve the request through a comment "Approved"

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function*to the transition of the issue's workflow. - Input the transition name or ID. - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Type the following code in `Condition`  ```text   {% set regExp = r/^Approved.*/i %}   {% set users = [] %}   {% for comment in issue.fields.comment.comments %}   {% if regExp.test(comment.body) and issue.fields['Multi user picker'] | find({"accountId":comment.author.accountId}) !=null and users | find({"accountId":comment.author.accountId})==null %}       	{% set ignore = users.push(comment.author) %}       {% endif %}   {% endfor %}   {{users | length == issue.fields['Multi user picker'] | length }}   ``` - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] All the cloned issues of an issue should transition through the workflow in parallel with the current issue.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function* to all the transitions of the workflow**,** except the **Create** transition. - Select “Target issues” as “Issues linked to the current issue through the following link type” - Select “clones” as the “Issue Link” - Input the transition name or ID. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] We use Jira as our internal and external issue tracking system. Every client has his project to log issues into. If the issue is valid, the product owner creates a bug in the internal project and links it to the external issue. I want to automate the closing of external issues when its linked bug in the internal system is closed.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function* to the **Close** transition of the workflow. - Select “Target issues” as “Issues linked to the current issue through the following link type” - Select “clones” as the “Issue Link” - Input the respective transition name/ID. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Automatically transition the Epic when all Stories are resolved.

Steps

|  |
| --- |
| - Add the *Transition issue(s)* post-functionto the **Resolve** transition of the Story workflow. - Select “Target issues” as “Epic of the current issue” - Input the transition name or ID of the **Resolve** transition. - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Write the following content in the `Condition` section.  ```text   {% set stories = issue | epic("key") | stories("status") %}   {% set trigger = true %}   {% for story in stories %}   	{% if story.fields.status.name != "Resolved" %}   		{% set trigger = false %}   	{% endif %}   {% endfor %}   {{ trigger }}   ``` - Place this post-function at the end in the list of post-functions.   Note that you might need to adjust the Status name in the script above to the status in which all Stories should be to transition the Epic. |

#### [light bulb on icon] Resolve a support request when the bug blocking it is Resolved.

Steps

|  |
| --- |
| - Add the *Transition issue(s)* post-function to the transition **Resolve** of the Bug workflow. - Select “Target issues” as “Issues linked to the current issue through the following link type” - Select “blocks” as the “Issue Link” - Input the transition name or ID of the **Resolve** transition of the support workflow. - Select `Resolution` from the field list under the `Transition screen` section. - Select `Copy value from current issue.` - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Start progress on the parent issue when someone started working on its sub-task.

Steps

|  |
| --- |
| - Add the *Transition issue(s) post-function* to the **Start Progress** transition of the workflow. - Select “Target issues” as “Parent issue of the subtask” - Input the respective transition name/ID. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Block the parent from being transitioned until all its subtasks are resolved and automatically transition the Parent when all Subtasks are resolved.

Steps

|  |
| --- |
| - Add the *Transition issue(s)*post-functionto the **Resolve** transition of the Sub-task workflow. - Select “Target issues” as “Parent issue of the subtask” - Input the transition name or ID of the **Resolve** transition. - Place this post-function at the end in the list of post-functions. - Add the Sub-task blocking condition to the "Resolve" transition of the Parent workflow. |

## [Transition linked issue](/cms_trial/space/JMWEC/466257658/Transition+linked+issues+(Deprecated)/) - Deprecated - Use [Transition issues(s)](#) instead

A workflow post-function that triggers a transition on all issues linked to the current issue through a selected link type.

**Sample use cases:**

#### [light bulb on icon] All the cloned issues of an issue should transition through the workflow in parallel with the current issue.

Steps

|  |
| --- |
| - Add the *Transition linked issues post-function* to all the transitions of the workflow**,** except the **Create** transition. - Input the transition name or ID. - Choose the link type as `clones`. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] We use Jira as our internal and external issue tracking system. Every client has his project to log issues into. If the issue is valid, the product owner creates a bug in the internal project and links it to the external issue. I want to automate the closing of external issues when its linked bug in the internal system is closed.

Steps

|  |
| --- |
| - Add the *Transition linked issues post-function* to the **Close** transition of the workflow. - Input the respective transition name/ID. - Choose the link type as `clones.` - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Automatically transition the Epic when all Stories are resolved.

Steps

|  |
| --- |
| - Add the *Transition linked issues*post-functionto the **Resolve** transition of the Story workflow. - Input the transition name or ID of the **Resolve** transition. - Select the **belongs to Epic** link type - Select the Conditional execution check box `Run this post-function only if a condition is verified`. - Write the following content in the `Condition` section.  ```text   {% set stories = issue | epic | stories %}   {% set trigger = true %}   {% for story in stories %}   	{% if story.fields.status.name != "Resolved" %}   		{% set trigger = false %}   	{% endif %}   {% endfor %}   {{ trigger }}   ``` - Place this post-function at the end in the list of post-functions.   Note that you might need to adjust the Status name in the script above to the status in which all Stories should be to transition the Epic. |

#### [light bulb on icon] Resolve a support request when the bug blocking it is Resolved.

Steps

|  |
| --- |
| - Add the *Transition linked issues* post-function to the transition **Resolve** of the Bug workflow. - Input the transition name or ID of the **Resolve** transition of the support workflow. - Select `Resolution` from the field list under the `Transition screen` section. - Select `Copy value from current issue.` - Place this post-function at the end in the list of post-functions. |

## [Transition parent issue](/cms_trial/space/JMWEC/465242394/Transition+parent+issue+(Deprecated)/) - Deprecated - Use [Transition issues(s)](#) instead

A workflow post-function that triggers a transition on the *parent issue* of the current issue.

**Sample use cases:**

#### [light bulb on icon] Start progress on the parent issue when someone started working on its sub-task.

Steps

|  |
| --- |
| - Add the *Transition parent issue post-function* to the **Start Progress** transition of the workflow. - Input the respective transition name/ID. - Place this post-function at the end in the list of post-functions. |

#### [light bulb on icon] Block the parent from being transitioned until all its subtasks are resolved and automatically transition the Parent when all Subtasks are resolved.

Steps

|  |
| --- |
| - Add the *Transition parent issue*post-functionto the **Resolve** transition of the Sub-task workflow. - Input the transition name or ID of the **Resolve** transition. - Select the **is Subtask of** link type - Place this post-function at the end in the list of post-functions. - Add the Sub-task blocking condition to the "Resolve" transition of the Parent workflow. |

## [Unlink issues from the current issue](/cms_trial/space/JMWEC/465504784/Unlink+issues+from+the+current+issue/)

This post-function is used to unlink issues from the current issue based on the result of a Groovy condition.

**Sample use cases:**

[light bulb on icon]**On rejection of an issue, unlink all its linked issues**

Steps

|  |
| --- |
| - Add the *Unlink issues from the current issue*post-functionto the **Reject**transition of the workflow. - Write `true` in Condition |