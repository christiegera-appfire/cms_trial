# Use Cases for Validators

This section has use cases that help you in understanding the usage of Validators provided by JMWE.

### Build-your-own (scripted) Validator

This validator can be used to perform validation with a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/). Based on the result of the expression, the user is either allowed or blocked to transition to the destination status.

**Sample use cases:**

#### [light bulb on icon]**Prevent the employee from applying for a leave if the employee is in the 3 month probation period**

Click here for the steps to configure

- Add the `Build-your-own (scripted) validator` to the **Apply leave**transition.

  - Write the following script in Jira expression field

    ```text
    !! issue.customfield_12116 && new CalendarDate(issue.customfield_12116).plusMonths(3) > new Date().toCalendarDate()
    ```
  - Configure the error message: Cannot apply for a leave

#### [light bulb on icon] **Force users to select both the parent and child values for a cascading select field**

Click here for the steps to configure

- Add the `Build-your-own (scripted) validator` to the transition.

  - Write the following script in Jira expression field

    ```text
    !!issue.customfield_10400 && !!issue.customfield_10400.value && !!issue.customfield_10400.child
    ```
  - Note customfield\_xxxxx is the id of the Cascading select field
  - Configure the error message: `Input values for both the child and parent of the cascading field`

### Field required Validator

This validator can be used to conditionally perform a validation to ensure that the specified field has a value during a transition.

**Sample use cases:**

#### [light bulb on icon] **Force users to provide Fix Version/s only when the resolution is Fixed**

Click here for the steps to configure

- Add the `Field required validator` to the **Resolve**transition.
- Input the following script in `Validator scope` section

  ```text
  issue.resolution.name != "Fixed"
  ```

#### [light bulb on icon]**Prevent the user from progressing on the Bug it is not assigned**

Click here for the steps to configure

- Add the `Field required validator` to the **Start Progress** transition.
- Select the Assignee field
- Select the `Conditional validation` option
- Input the following script in `Validator scope` section

  ```text
  issue.issueType.name == "Bug"
  ```
- Configure the error message: `Assign the issue`

### Linked Issue(s) validator

This validator can be used to ensure that issues linked to the current issue have certain characteristics

**Sample use cases:**

#### [light bulb on icon] Prevent creation of more than 5 subtasks for a parent issue of "Story" issue type

Click here for the steps to configure

- Add the `Linked Issue validator`to the **Create** transition.
- Select the issue link type is Subtask of from the `Issue Link Type` field.
- Select the issue type `Story`from the `Issue Type` field.
- Select the option "Every linked issue must satisfy the condition below"
- Input the Jira expression:

  ```text
  !!issue.parent && issue.parent.subtasks.length < 5
  ```
- Add the error message, "`You cannot create more than 5 subtasks`"

### Linked Issues Status validator

This validator can be used to ensure that the current issue's linked issues are in one of the selected statuses.

**Sample use cases:**

#### [light bulb on icon]**Block the transition of the Epic to Closed status, if its stories aren't closed.**

Click here for the steps to configure

- Add the `Linked issues status validator` to the **Closed** transition.
- Select the issue link type `is Epic of` from the `Issue Link Type` field.
- Select the “Closed” status from `Statuses`
- Add the error message, "`The Stories of the Epic are not yet resolved`"

#### [light bulb on icon]**Prevent creation of new subtasks to the parent if the parent is in "Resolved" or "Closed" or "Rejected" status**

Click here for the steps to configure

- Add the `Linked issues status validator` to the **Create**transition.
- Select the issue link type `is subtask of` from the `Issue Link Type` field.
- Select the statuses "Resolved", "Closed",  "Rejected", from `Statuses`
- Add the error message, "`The parent should be in Resolved or Closed or Rejected`" status.