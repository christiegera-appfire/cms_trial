# Add an internal comment to Jira Service Desk request

```text
string commentMsg = "This is an internal JSD comment: \\\\Summary - " + summary + "\\\\Description - " + description ;
addJSDComment(key, currentUser(), commentMsg, false);
```