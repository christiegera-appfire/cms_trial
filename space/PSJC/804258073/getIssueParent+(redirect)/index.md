# getIssueParent (redirect)

Looking for a getIssueParent() function? You won’t find it because there isn’t any. Instead, the parent for an issue can be retrieved by using the ‘parent’ [standard variable](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/). Examples on how to use this variable can be found below.

**Example 1**

```text
string myIssue = "ABC-123";
return myIssue.parent;
```

**Example 2**

```text
//set issue assigne to be the same as the parent assignee
assignee = parent.assignee;
```