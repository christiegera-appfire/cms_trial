# User Is In Any Users condition

---

From June 6, 2025, the User Is In Any Users condition has been replaced by **Only selected users**. The Only selected users condition is included in the JSU Rule Builder for conditions. This does not affect any rules that you created before this date. If you need to edit the rule, the new dedicated version of the rule builder is available. You can recreate the rule using the **Only selected users** condition in the new rule builder if you prefer.

## Description

The *User Is In Any Users* condition verifies that the current user acting on the issue is one of the selected users.

## Configuration

You must specify one or more allowed users to set up the condition. If you add this condition without specifying a user, no one will be able to perform the transition. See [Workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/) to learn how to add a condition to a workflow transition.

![User Is In Any Users condition Allowed Users selection dropdown with a sample name selected](/cms_trial/assets/61baee4f-8af0-4c0b-aaef-dd4a88f72cdb.png)

## Use cases

### Enforce automations

A workflow is configured so the transition has the User Is In Any User condition set to `jsu-technical-user` only. This is a user account that is not assigned to a person but is used for all sorts of automations. It has more permissions than normal users, so automations can be used to perform actions that would be restricted for normal users. A normal user viewing an issue in that workflow will not see the transition.

You can use this to hide a transition that will be triggered by a Perform As User (impersonate) post function. You would also configure `JSU-add-on-user` as the Perform As User in the post function.

### Supervisors or managers

You can restrict some transitions in your workflow to supervisors or managers. You can also consider other conditions like Jira’s User Is In Any Groups or User Is In Any Roles conditions.