# Perform searches with LDAP

The following solution was kindly provided by Stefano Gevinti.

## Problem

When creating an issue, you want to first assign it to the manager of the current user, to enable them to review it. However, the manager role is not natively defined in Jira (for example, as a project admin). This makes it necessary to access the Lightweight Directory Access Protocol (LDAP).

## Solution

Enter the below script.

This workflow action (post function) should be the last in the call chain when creating an issue.

#### **create\_postfunction.sil**

```java
string mgr = ldapUserRecord("manager", "(sAMAccountName=" + currentUser() + ")"); //get the current user's manager DN
string cnUser = substring(mgr, 0, indexOf(mgr,",")); //establish the cn, this is the manager user (that may depend on your setup)
string mgrUserName = ldapUserRecord("sAMAccountName", cnUser); //again, a lookup in the Active Directory to get the manager

//Note: these LDAP calls are automatically cached, so performance gets better if it is found in cache

if(userExists(mgrUserName)) { //make sure this is defined in JIRA
 assignee = mgrUserName;
} else {
 //fallback to project admin
 assignee = projectPM(project);
}
```

Now [configure the LDAP](#).

This solution assumes that the Windows account name is the same one used to access Jira. This depends on the AD setup.