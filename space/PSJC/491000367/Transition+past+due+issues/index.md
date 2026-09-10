# Transition past due issues

Call this script on a set schedule. It will transition issues that are past due.

```text
string [] keys = selectIssues("project = EX AND duedate is not  EMPTY AND duedate < startOfDay()");
for(string k in keys) {
    autotransition(61, k, true, true, true);
}
```