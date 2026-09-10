# Accessing the details of an issue or a transition in Jira expressions

This document briefs you on how to access the details of *issue* and *transition* objects in Jira expressions, such as those available through the [issue](/cms_trial/space/JMWEC/465241693/Variables+used+in+Jira+expressions/) and [transition](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) variables.

Structure of an `issue` object

An issue object consists of the issue key and a collection of fields. To know the structure of the issue object (such as those available through the `issue`and `linkedIssue` variables) returned in Jira expressions:

1. Go to the [Jira expressions editor](/cms_trial/space/JMWEC/466225418/Jira+Expressions+Editor/)
2. Test the following code against an issue

   ```javascript
   issue
   ```
3. The result shows the issue structure as a JSON.

Not all data types are supported in Jira expressions. See [here](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#issue) to find all the Data types supported in Jira expressions along with their properties and methods.

### Access the fields of an issue

To write a Jira expression that accesses the fields of an issue, the easiest way is to use the "Issue Fields" tab in the Jira expressions editor help. To see the properties and methods of the returned value use the "Data Types" tab in the editor. For example, to access the "Assignee" field of an issue using the Jira expressions:

1. Click on "Issue Fields" tab.
2. Select the "Assignee" field from `Select a field;`the help shows you how to access the field, its sub-fields and test the field value.
3. Click on one of the expressions to insert it into the editor; the help shows you the supported properties and methods of the returned Data Type.

Another way is to go to the "Data Types" tab of the Jira expressions editor and select "Issue" from "Select a Data Type" field. The help lists properties and methods of the *Issue* data type. Click on a button to insert it into the editor; hover over it to get the information.

## Structure of the `transition` variable

The `transition` variable describes the current workflow transition. It contains information about the transition that is currently happening and allows to inspect the source and target status. The transition of an issue consists of the following fields:

- `id`: The transition ID ([Number](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#number)).
- `name`: The transition name ([String](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#string)).
- `from`: The current status of the issue ([IssueStatus](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#issuestatus)).
- `to`: The target status of the transition ([IssueStatus](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#issuestatus))
- `hasScreen`: *true* if there is a screen configured for this transition, *false* otherwise ([Boolean](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference/#boolean))

Use the "Global Variables" tab of the Jira expressions editor to access the current transition information.