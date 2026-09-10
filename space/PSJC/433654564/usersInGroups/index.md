# usersInGroups

## Description

Returns a list of users common to all the specified groups.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | usersInGroups(groups) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| groups | String [] | Yes | Array containing the groups names to retrieve the common users from. |

## Return Type

**String []**

Returns a list with the usernames of the common users for all the specified groups. The result of the function is the intersection of the sets of users for each specified group, not the union.

## Examples

### Example 1

```javascript
//The following users belong to both groups jira-developers and jira-administrators: user1, user2
string[] groups = {"jira-developers", "jira-administrators"};
string[] usersByGroups;
usersByGroups = usersInGroups(groups);
print("The following users belong to both groups jira-administrators and jira-developers: ");
print(usersByGroups);
```

Result: The following users belong to both groups jira-administrators and jira-developers: user1|user2

### Example 2: Union of groups

```javascript
function getUsers(string [] groups){ 
  string [] users; 
  for(string group in groups){ 
    string [] currentGrp; 
    currentGrp = addElement(currentGrp, group); 
    for(string user in usersInGroups(currentGrp)){ 
      users = addElementIfNotExist(users, user); 
    } 
  } 
  return users;
} 

string [] groups = {"jira-developers", "jira-administrators"}; 
description = getUsers(groups);
```

This example uses the usersInGroups function to get all users in each group individually and then adding them into a predefined array. So the usersInGroups function will be called twice: once for jira-administrators and once for jira-developers. Since each time it will be called with a single group, it will return all users from the specified group.

### Example 3: Union of groups

The code above (example 2) can be rewritten with the following code:

```javascript
string [] developers = usersInGroups({"jira -developers"});
string [] administrators = usersInGroups ({"jira-administrators"});
return arrayUnion (developers, administrators );
```

## See also