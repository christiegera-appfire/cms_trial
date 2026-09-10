# Use Cases for Conditions (Legacy)

**Note**: the Use Cases detailed on this page are still mostly valid! However, they are in the process of being updated, both in format and in specific Condition configurations that have been changed in recent JMWE updates.

This section has use cases that help you understand the usage of the Conditions provided by JMWE.

### Build-your-own (scripted) Condition

This condition can be used to hide/show a transition based on a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).

**Sample use cases:**

#### [light bulb on icon]**Only the Reporter of the issue should be able to close the service ticket.**

- Add the `Build-your-own (scripted) condition`to the **Close issue** transition.
- Write this content in the `Jira expression`

  ```text
  user == issue.reporter
  ```

#### [light bulb on icon] **Hide the transition from the current user if he is not in the Approvers field**

- Add the `Build-your-own (scripted) condition`to the transition you wish to hide
- Write this content in the `Jira expression.`

  ```text
  !! issue.customfield_10002 && issue.customfield_10002.some(it => it == user)
  ```

  Replace the custom field id with the id of the Approvers field in your instance

#### [light bulb on icon]**Block a specific transition when the Time to resolution is breached.**

- Add the `Build-your-own (scripted) condition`to the transition you wish to hide
- Write this content in the `Jira expression.`

  ```text
  !! issue.customfield_10102 && (!issue.customfield_10102.ongoingCycle || !issue.customfield_10102.ongoingCycle.breached)
  ```

  where `customfield_10101`is the id of the Time to resolution field.

#### [light bulb on icon]**Prevent the users from "Return/Exchange" on the purchase order after 15 days from the item delivery date**

- Add the `Build-your-own (scripted) condition`to the transition "Return/Exchange"
- Write this content in the `Jira expression.`
- ```text
  new Date().minusDays(15) < issue.created
  ```

#### [light bulb on icon]**Enable the "Start Progress" only on issues in the current sprint**

- Add the `Build-your-own (scripted) validator`to the **Start Progress**transition.
- Name the validator as “Check Sprint”
- Write the following script in Jira expression field

  ```text
  !!issue.sprint && issue.sprint.state == "active"
  ```

#### [light bulb on icon]**Ensure at least one pdf file is attached before the issue can be transitioned**

- Add the `Build-your-own (scripted) validator`to the **Start Progress**transition.
- Name the validator as “Check attachments”
- Write the following script in Jira expression field

  ```text
  issue.attachments.filter(attachment => attachment.mimeType == 'application/pdf').length > 0
  ```

#### [light bulb on icon]**Show transition “Reject” only for users of the “Management” project role and “jira-administrators” group**

- Add the `Build-your-own (scripted) validator`to the **Reject**transition.
- Name the validator as “Current user Project Role and Group”
- Write the following script in Jira expression field

  ```text
  user.getProjectRoles(issue.project).some(pr => pr.name == "Management") || user.groups.includes("jira-administrators")
  ```

### Current Status Condition

This condition can be used to hide/show a particular transition from the list of available workflow actions, based on the current status of the issue.

**Sample use cases:**

#### [light bulb on icon] **Disable a global transition from certain statuses**

- Add the `Current status condition` to the transition.
- Select the statuses from which the Global transition should be enabled from the `Current Status` field.

#### [light bulb on icon]**Block issue transition from current status to itself**

- Add the `Current status condition` to all the transitions of the workflow, the issue follows.
- On each condition select all the status(es) from the `Current Status` field except the destination status of the current transition

#### [light bulb on icon] **Block transition to 'On Hold' status when the issue is in 'Closed' status**

- Add the `Current status condition` to the transition "On Hold".
- Select all the status(es) applicable to the current issue, except the 'On Hold' status.

### Linked Issues Condition

This condition can be used to hide/show a particular transition from the list of available transitions, based on the issue's linked issues.

**Sample use cases:**

#### [light bulb on icon]**Hide the transition "Triage" until at least one assigned subtask is available for the issue**

- Add the `Linked Issue condition`to the "Triage" transition.
- Select the issue link type `is Parent Of` from the `Issue Link Type` field.
- Select the issue type as `Sub-task`
- Select the option "At least one linked issue must satisfy the condition below"
- Input the Jira expression:

  ```text
  linkedIssue.assignee !=null
  ```

#### [light bulb on icon]**Hide the "Start Progress" transition on a ticket when there is an issue linked to it through the “is blocked by” link type**

- Add the `Linked Issue condition`to the "Start Progress" transition.
- Select the issue link type `is blocked by` from the `Issue Link Type` field.
- Select the option "Every linked issue must satisfy the condition below"
- Input the Jira expression:

  ```text
  false
  ```

#### [light bulb on icon]**For a parent of issue type “Story” hide the In Progress transition until all its subtasks are in “In Progress”**

- Add the `Linked Issue condition`to the "Start Progress" transition of the workflow.
- Select the issue link type `is Parent Of` from the `Issue Link Type` field.
- Select the option "Every linked issue must satisfy the condition below"
- Input the Jira expression:

  ```text
  issue.issueType.name != "Story" || linkedIssue.status.name == "In Progress"
  ```

### Linked Issues Status Condition

This condition can be used to hide/show a particular transition from the list of available transitions, based on the status of the issue's linked issues.

**Sample use cases:**

#### [light bulb on icon]**Hide the "Close" transition of the Epic until all its Stories are closed.**

- Add the `Linked Issue Status condition`to the `Close` transition.
- Select `is Epic of` as the `Issue Link`
- Select the "Closed" status from `Statuses`

#### [light bulb on icon]**Prevent the user from resolving the ticket, if there are any unresolved bugs associated to it.**

- Add the `Linked Issue Status condition`to the `Resolve`transition.
- Select `is blocked by` as the `Issue Link Type`
- Select `Bug` as the `Issue Type`
- Select the "Resolved" status from `Statuses`