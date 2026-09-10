# Variables used in Jira expressions

Context variables (as mentioned in [Jira expressions official documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#syntax-and-semantics)) are available depending on the context in which the Jira expression is evaluated. JMWE makes the `issue, transition` and `user`variables available to Jira expressions.

### **customerRequest variable**

The customerRequest variable is used to insert data from the current customer request. Only applies when the current issue is a Jira Service Desk customer request. Returns `null`otherwise.

**For example:**

`customerRequest.issue.key == issue.key`

### **serviceDesk variable**

The serviceDesk variable provides information about the Service Desk to which the current customer request belongs. Only applies when the current issue is a Jira Service Desk customer request. Returns `null`otherwise.

**For example:**

`serviceDesk.id == 9`

### **issue variable**

The `issue`variable is used to insert data of the issue being transitioned. You can access the issue data (fields) either by

- looking up at its properties and methods that are displayed under the "Data Types" tab of the Jira expressions editor when you insert (click on the variable) the `issue` variable into the editor or
- selecting the field you wish to access from the "Issue Fields" tab of the Groovy expression editor

**For example:**

`issue.labels` returns an array of label values, e.g. `[ "Blue","Red" ]`

`issue.reporter.displayName`returns the `display Name`of the reporter, e.g. `Carter`

### **originalIssue variable**

The `originalIssue`variable is used to insert data from the current issue as it was *before the transition started*. This is useful to determine which fields were changed on the transition screen. You can access the issue data (fields) either by

- looking up at its properties and methods that are displayed under the "Data Types" tab of the Jira expressions editor when you insert (click on the variable) the `issue` variable into the editor or
- selecting the field you wish to access from the "Issue Fields" tab of the Jira expression editor

Note you cannot test this variable in the Jira expression tester.

**For example:**

`originalIssue.labels` returns an array of label values before the transition started, e.g. `[ "Blue","Red" ]`

`originalIssue.assignee.displayName` returns the display name of the Assignee before the transition started, e.g. `Carter`

### **transition variable**

The `transition`variable is used to insert information of the transition being executed. You can access the transition information under "Current Transition" section in the "Global Variables" tab of the Jira expressions editor. Click on a button to insert the expression into the editor. You can also find the properties and methods of the `transition` variable from the "Data Types" tab by selecting "Transition" under "Select a Data type".

**For example:**

`transition.name` returns the name of the current transition, e.g. `Start Progress`

`transition.hasScreen` indicates whether there is a screen configured for this transition

### **user variable**

The `user`variable is used to insert information about the current user, i.e. the user triggering the transition. You can access the current user information under "Current User" section in the "Global Variables" tab of the Jira expressions editor. Click on a button to insert the expression into the editor.

You can also find the properties and methods of the `user` variable from the "Data Types" tab by selecting "User" under "Select a Data type".

**For example:**

`user.accountId` returns the `accountId` of the user triggering the transition, e.g. `accountId:5ca5b1469a000c1180956957.`

`user.groups` returns the list of names for all the groups to which the current user belongs.

`user.groups.includes("jira-users")`returns `true` if the current user is a member of the "jira-users" group.

`user.groupIds.includes("418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx")`returns `true` if the current user is a member of the group with the ID "418a6fa4-d69e-4e0a-90ef-a25ef56xxxxx".

`user.getProjectRoles(issue.project) returns the list of project roles the current user belongs to in the issue's project`

`user.getProjectRoles(new Project("TEST"))` returns the list of project roles the current user belongs to in the project with key TEST

`user.getProjectRoles(issue.project).some(pr =>` [pr.name](http://pr.name) `== "Developers")`returns `true` if the current user is a member of the "Developers" project role in the issue's project.

The `groups` and `getProjectRoles(project)` methods are applicable to Jira Standard Single-User picker type fields (like Assignee, Reporter, etc) *only*. They are not applicable to custom fields of Single-User picker type. This is because Jira expressions don't return "real" user objects for custom fields.