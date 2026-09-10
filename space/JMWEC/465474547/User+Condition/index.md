# User Condition

A workflow condition that lets you hide/show a particular transition from the list of available workflow actions based on either the *current user* or users in a specific field meeting certain criteria, such as being the reporter or assignee, belonging to certain groups or project roles, satisfying a Jira expression, etc.

When you add this condition to a transition, the transition will be available only if the configured user(s) satisfy the configured criteria.

![JMWE for Jira Cloud user condition configuration with user selection criteria](/cms_trial/assets/a0b07715-0739-4511-b2db-2def695bdcd2.png)

**To add a 'User Condition' to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to configure the validator on.
2. In the Workflow Designer, select the transition.
3. Click on **Conditions**in the properties panel.
4. Click on `Add condition`.
5. Select `User Condition`from the list of validators.
6. Click on `Add` to add the condition.
7. Configure the user(s) to check and the criteria (see below).
8. Click on `Add` to add the condition to the transition.

## Configuration

### User(s) to check

You must first configure which user(s) need to be checked. You can check either the current user, or user(s) in an issue field such as Assignee, Reporter, or any user picker custom field.

- **Current user:** the current user will be checked
- **User(s) in field:** the user in the specified field, such as Assignee, Reporter, or any User Picker custom field, will be checked. If the selected field is a multi-valued field, such as Voters, Watchers, or a Multi-user Picker custom field, all users in that field will be checked, and they **all** need to satisfy the criteria.

### User(s) must meet

You need to specify whether the user(s) to be checked must satisfy *all* the configured criteria or *at least one*.

- **all the criteria configured below:** each user will need to satisfy every criterion
- **at least one of the criteria configured below:** each user will need to satisfy at least one of the criteria
- **or the field can be empty:** if you select the “at least one of the criteria configured below” option and the “User(s) to check” is “User(s) in field”, you can also decide whether an empty field satisfies the condition. For example, if you are checking the Assignee field and you select the “or the field can be empty” option, the condition will succeed and the transition will be available even if the issue is unassigned.

### Criteria

You need to specify at least one criterion that the user(s) must satisfy for the validator to succeed. You can check whether each user:

- **The user is**:

  - **the Reporter**
  - **the Assignee**
  - **a Watcher**
  - **a Voter**

## Advanced Options

### More criteria

- **Project roles**: The user belongs to one of the specified **Project Roles** in the issue’s project.
- **Groups**: The user belongs to one of the specified **groups**.
- **Users**: The user is one of a list of **specific users**.
- **User fields**: The user is selected in the specified user-type **field**, such as a user picker custom field.

### Scripted condition

- **Condition for user(s)**: The user satisfies a **Jira expression**. For each user to check, the Jira expression will be evaluated and must return `true` for the validation to succeed. Note that the user being checked is available through the `selectedUser` variable.

### Reverse Condition

- **Reverse condition**: If this box is checked, the condition specified in **Condition for user(s)** must return `false` for the validation to succeed.