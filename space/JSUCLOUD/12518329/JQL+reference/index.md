# JQL reference

## Use placeholders for JQL in JSU

Atlassian's [Jira Query Language](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-939938733.html) (JQL) allows you to perform [advanced searching](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-939938733.html) in Jira's search dialog. JSU extends JQL with additional placeholders, which are replaced with the values of the current issue in transition.

For example, if you use the following JQL query in a JSU post function:

`parent = {issue.Parent} AND component != {issue.Component/s} OR component is EMPTY`

it will be converted by JSU before the search is executed similar to the following:

`parent = 'ABC-123' AND component != 'Documentation' OR component is EMPTY`

*This will search all sibling issues (same parent) which do not have the same component as the current issue (in this example Documentation).*

Any text in curly brackets, which follows the pattern **{issue.FIELD NAME}** is replaced with the value of that field on the current issue (the issue in transition). See below for further details on which names you can use for the different field types. Depending on your use case, you might not use any {issue.FIELD NAME} placeholder at all.

Logical operators, functions, and operators are the same as the JQL in Jira. It is important to use the correct JQL syntax. The easiest way to write a JQL query for JSU is to prepare it first in Jira's standard search interface (use 'advanced search') with some sample value, then copy it to JSU configuration and replace some of your sample values with {issue.FIELD NAME} as required.

See [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for more examples.

### How to use JQL Search Extensions keywords with JSU

## Tips for using JQL with JSU

### Fields on the current issue

Add the following to your JQL query:

`... AND key = {issue.key}`

### Fields on the parent issue

Add the following to your JQL query:

`... AND key = {issue.parent}`

### Fields on all sibling issues (other sub-tasks of the same parent issue)

Add the following to your JQL query:

`... AND parent = {issue.parent} AND key != {issue.key}`

- sub-tasks with the same parent: parent = {issue.parent}
- excluding the current issue: key != {issue.key}

See [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for more examples.

## Query results

Think carefully about what values might be used as replacements for the {issue.FIELD NAME} placeholders. Or, what happens if an issue has no value in a specified field? There could be some variation in the data of your issues.

If you are not careful, the result of a JQL query might unexpectedly contain hundreds of issues. Or, the JQL query might fail because the syntax has become invalid after the placeholders have been replaced.

## Maximum issues allowed

You can set a limit for the maximum number of issues you expect from your JQL query. If the result of the JQL query returns more issues, JSU will not process anything. JSU essentially stops the process before things get out of control.

This way, you can prevent JSU from accidentally processing hundreds of issues. By default, this limit is 50 issues, and the maximum limit is 1,000.

## JQL injection

Be aware of potential JQL injection. JSU does not check any value that it retrieves from the current issue. A malicious user might craft the value of a field (for example the value of a text field) so that after the replacement it adds additional criteria to your JQL query.

We recommend that you do not use text fields as placeholders or any other field where a user can freely change the text. Only use fields that can contain one/several clearly defined values.

## Syntax for field names

Field names in your JQL should be the same as in the [Advanced Search](https://confluence.atlassian.com/jirasoftwareserver/advanced-searching-939938733.html). We suggest using the issue navigator's auto-complete feature to get the correct field names. In Jira, go to **Issues** > **Search for issues**, and switch to *Advanced search*.

## System fields

System field names should match those used in JQL. For example:

- reporter
- assignee
- issuetype
- priority

## Custom fields

Custom field names should match those used in JQL. For example:

- Approver or  cf[10010]
- Hosting Server or cf[12910]
- Date to Join or cf[11000]

If you have several custom fields with the same name, you can only use the cf[12345] notation to refer to one of them.

## Syntax for values of the current issue

The replaceable value from the issue must be between curly brackets:

`{issue.FIELD NAME}`

### System fields

Use the place holders from the following list:

- {issue.Affects Version/s}
- {issue.Assignee}
- {issue.Affects Version/s}
- {issue.Assignee}
- {issue.Component/s}
- {issue.Created}
- {issue.Creator}
- {issue.Customer Request Type}
- {issue.Description}
- {issue.Due Date}
- {issue.Environment}
- {issue.Epic Color}
- {issue.Epic Name}
- {issue.Epic Status}
- {issue.Epic Link}
- {issue.Fix Version/s}
- {issue.Issue Key}
- {issue.Issue Type}
- {issue.Labels}
- {issue.Original story points}
- {issue.Parent}
- {issue.Priority}
- {issue.Project}
- {issue.Rank}
- {issue.Reporter}
- {issue.Request participants}
- {issue.Resolution}
- {issue.Resolved}
- {issue.Security Level}
- {issue.Sprint}
- {issue.Status}
- {issue.Summary}
- {issue.Time to resolution}
- {issue.Updated}
- {issue.Voters}
- {issue.Watchers}
- {issue.Work Ratio}

Alternatively, you might use the technical field ID of a system field, or how JQL refers to it. For example, all three variants below refer to the same field:

- {issue.Affects Version/s}  
  Label in the English Jira user interface.
- {issue.versions}  
  Technical field ID. See also the constant values [reference from Atlassian](https://docs.atlassian.com/software/jira/docs/api/8.1.2/constant-values.html#com.atlassian.jira.issue.IssueFieldConstants.AFFECTED_VERSIONS).
- {issue.affectedVersion}  
  JQL's method to refer to that field.

### Custom fields

You can use either the name of a custom field or its ID. For example:

- {[issue.My](http://issue.My) Text Field}
- {issue.customfield\_12345}

However, the cf[12345] notation is not supported between curly brackets.

If you have several custom fields with the same name, you must use the custom field ID.