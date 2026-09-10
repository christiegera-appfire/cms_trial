# Add a group as participants in Jira Service Desk

Call this script from a workflow transition action. The script adds a group to the Service Desk participants.

```text
string [] groups = {"auto-assign-users"};
customfield_10301 = usersInGroups(groups);
```