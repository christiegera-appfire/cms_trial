# Group Administration Functions

This section contains functions that enable users to handle group administration.

Some of the functions below require an API token set up in PowerScripts.

## Functions Summary

- [admAddGroupToProjectRole](/cms_trial/space/PSJC/514720901/admAddGroupToProjectRole/)
- [admAddUserToGroup](/cms_trial/space/PSJC/622756311/admAddUserToGroup/)
- [admCreateGroup](/cms_trial/space/PSJC/621972420/admCreateGroup/)
- [admRemoveGroup](/cms_trial/space/PSJC/622169683/admRemoveGroup/)
- [admRemoveGroupFromProjectRole](/cms_trial/space/PSJC/515113550/admRemoveGroupFromProjectRole/)
- [admRemoveUserFromGroup](/cms_trial/space/PSJC/622657794/admRemoveUserFromGroup/)

**Example (requires API Token set up):**

```text
const string groupName = "mygang";
string user = currentUser();

if(groupExists(groupName)) {
    runnerLog("Must remove group :" + groupName);
    removeGroup(groupName);
} else {
    runnerLog("Group will be created :" + groupName);
}

if(createGroup(groupName)) {
    addUserToGroup(user, groupName);
    if(!userInGroup(groupName, user)) {
        return "nok-1";
    }
    removeUserFromGroup(user, groupName);
    if(userInGroup(groupName, user)) {
        return "nok-2";
    }
    removeGroup(groupName);
    return "ok";
}
return "nok-3";
```