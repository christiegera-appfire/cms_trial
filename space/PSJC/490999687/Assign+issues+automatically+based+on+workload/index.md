# Assign issues automatically based on workload

This function returns the user in the group that has the least number of issues  
the function takes a group name as an input parameter.

To invoke, you'd script like this:

string user = getUserLeastIssues("auto-assign-users");

## Script

```text
string username;
int countIssues;
string [] groupUsers;
string [] groups = {argv[0]};
    
groupUsers = usersInGroups(groups);
    
for(string u in groupUsers) {
        
    string jql = "project = EX AND statusCategory in (\"To Do\", \"In Progress\") and assignee = " + u;
    int tempCount = countIssues(jql);
        
    if(isNull(username) || (countIssues > tempCount)) {
        username = u;
        countIssues = tempCount;
    }
}
    
return username;
```