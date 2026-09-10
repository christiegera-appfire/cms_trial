# Creating issues with createIssue() function: a step-by-step guide

## Problem

The `createIssue()` function takes the most arguments of any SIL function and is the most likely to cause syntax errors. The examples here are intended to make the process of creating a script using `createIssue()` as easy as possible.

## Solution - the easy way

When testing a script with `createIssue()`, start with the fewest number of arguments.

|  |
| --- |
| ```text string newIssueKey = createIssue(     "DEMO",      "",      "Task",      "Summary goes here" );   if (isNotNull(newIssueKey)){     runnerLog("Issue " + newIssueKey + " was created."); } else {     runnerLog("An issue was not created"); } ``` |

## Adding custom field information after issue creation

After you have created the issue, you can add values to custom fields as you would normally. See the [Variable Resolution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/)page for information on how to set custom fields.

|  |
| --- |
| ```text %newIssueKey%.#{custom field name here} = "string value goes here"; ``` |

## Custom field mapping

While the method above tends to be easier to implement, doing everything at once is easier to read.

One of the trickiest `createIssue()` arguments (and most prone to error) is the custom field mapping. The custom field mapping argument is intended to accept key/value pairs such as those shown in the following example.

Let's say I have a custom field named textField and another with the id of "1234". You can set those values using the following:

|  |
| --- |
| ```text string [] custom_fields_mapping = "textField|text value here|customfield_1234|jira-users"; ``` |

To pass an array value to a custom field, use the curly braces to denote an array.

|  |
| --- |
| ```text string [] custom_fields_mapping = {"checkbox", {"released", "accepted"}};     string newIssueKey = createIssue(         "DEMO",                 // project key         "",                     // parent key         "Task",                 // issuetype         "Summary goes here",    // summary          "",                     // priority         "",                     // description         "",                     // components         "",                     // due date         "",                     // estimate     "",                     // security level       custom_fields_mapping   // custom fields mapping         ); ``` |

Place each argument on a separate line with a comment for each one to help keep each argument straight.

## createIssue() in the cloud

The arguments for the createIssue() function are exactly the same, except there is no argument for the due date.

## Additional help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.