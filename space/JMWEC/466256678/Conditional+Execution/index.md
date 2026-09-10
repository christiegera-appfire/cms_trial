# Conditional Execution

![JMWE for Jira Cloud conditional execution configuration panel with rule settings](/cms_trial/assets/3da6856e-2564-4a91-9a76-3d5e3d413bc4.png)

Most post-functions include an option for **Conditional execution**. Aside from the transition in which you include a post-function, this enables you greater control over the specific circumstances for when a post-function will (or will not) trigger. To configure Conditional Execution, you use the **Condition** field (Figure 1, right) with Nunjucks templates; create a Nunjucks template that evaluates to `true` (or a truthy value) and the post-function will be executed (or skipped, if you choose the Reverse option).

To add Conditional Execution to a post-function :

1. Select the check box **Run this post-function only if a condition is verified**.
2. Enter a Nunjucks template that returns either `true` or `false`, as needed by your post-function logic.

## Expected value in the Nunjucks template

The value returned by your Nunjucks template should be either a boolean value (`true` or `false`), or more generally any text that will be interpreted as either "truthy" or "falsy".

**Text:** Any text will be interpreted as "truthy" (the equivalent of `true`) *except* for:

- A string with a literal value of ‘false’
- An empty string
- Or a string consisting only of whitespaces

For example, the following text values are considered "truthy":

- `true`
- `1`
- `A string`
- `[Object object]`
- `[]`

**Boolean logic operators:** You can use traditional boolean logic operators, such as `or`, `and` and `not`, to combine conditions. You can also use parentheses to group expressions. For example:

- `{{ 1 == 1 or 1==2 }}`
- `{{ issue.key == 'TEST-1' and issue.fields.subject == 'Do it' }}`
- `{{ true and (false or true) }}`
- `{{ not 1==1 }}`
- `{{ issue.fields.description is null }}` returns `true` if the issue has no description
- `{{ issue.fields.assignee is not null }}` returns `true` if the issue has an Assignee

**Examples of Nunjucks expressions returning a "truthy" value:**

- `{{issue.fields.assignee}}` if the issue is assigned
- `{{issue.fields.assignee.accountId == "accountId:557058"}}` if the issue is assigned to the user whose accountId is "557058"
- `{{issue.fields.description is not null}}` if the issue's description is not empty
- `{{issue.fields.assignee and issue.fields.status.name == "In Progress"}}` if the issue is assigned and in the “In Progress” status

## Sample use cases for Conditional execution

For examples on how to use Conditional execution within post-functions, please see [Conditional Execution Samples](/cms_trial/space/JMWEC/998440999/Conditional+Execution+Samples/).