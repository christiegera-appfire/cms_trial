# Text matches

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Text JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### exactTextMatch()

Matches issues that contain the text in the summary, description, or environment fields. Takes a case-sensitive text as an argument.

**Example**  
`issue in exactTextMatch("text")`

### exactTextMatchCaseInsensitive()

This function is similar to exactTextMatch() but is case-insensitive.

**Example**  
`issue in exactTextMatchCaseInsensitive("tExT")` matches issues with TEXT, Text, tEXT, etc.

### wildcardMatch()

Matches issues with a field containing a specified text (case-sensitive). You can use the asterisk (**\***) to match any text.

**Examples**  
`issue in wildcardMatch("summary", "Hello*")`  
`issue in wildcardMatch("fixVersion", "12.0*")`  
`issue in wildcardMatch("labels", "*Marketing*")`  
`issue in wildcardMatch("component", "Business*")`  
`issue in wildcardMatch("category", "MyOrg*")`

You can place the asterisk anywhere in the text, and use more than one.

### regex()

Use the full power of regular expressions to match field values. Regular expressions are strict and case-sensitive, following JavaScript syntax for regular expressions.

You can use backslashes to escape special characters.

**Examples**

`issue in regex("summary", "^Hello.*")` matches issues with summaries starting with  
`issue in regex("fixVersion", "12.[0-5]")` matches issues with versions from 12.0 to 12.5  
`issue in regex("labels", "Marketing$")`matches issues with labels that end with *Marketing*  
`issue in regex("component", "Business.*")`  
`issue in regex("category", "MyOrg.*")`  
`issue in regex("Acceptance checklist", "can proceed")` matches issues that have any checkbox with *can proceed* checked  
`issue in regex("Custom cascading select list", "- Georgia")` matches issues with a cascading select field with Georgia as a child value