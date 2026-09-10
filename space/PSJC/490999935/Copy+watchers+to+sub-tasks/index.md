# Copy watchers to sub-tasks

Call this script on a set schedule. The script adds the watchers from the parent issue to all subtasks.

```text
string [] keys = selectIssues("key in silJQLList(\"silJql_IssuesWithSubtasks.sil\", \"Project = EX\") AND statusCategory not in (Done)");

for(string k in keys) {
    for(string s in subtasks(k)) {
        
        %s%.watchers += %k%.watchers;
    }
}
```

The JQL script can be replaced with the predefined [hasSubtasks](/cms_trial/space/PSJC/490997937/JQL+Support/) JQL function.

This script is used in silJQL to return a list of all issues with subtasks. It takes a JQL search as parameter.

It is recommended to use **silJQLList**, for example, the key in silJQLList("silJql\_IssuesWithSubtasks.sil", "Project = EX").

```text
string [] keys = selectIssues(argv[0]);
string [] ret;
for(string k in keys) {
    if(size(subtasks(k)) != 0) {
        ret += k;
    }
}

return ret;
```