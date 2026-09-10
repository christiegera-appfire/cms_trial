# User Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator that can validate that either the *current user* or users in a specific field meet certain criteria, such as being the reporter or assignee, belonging to certain groups or project roles, satisfying a Jira expression, etc.

![JMWE for Jira Cloud user validator configuration with validation criteria](/cms_trial/assets/e77139db-2e5f-46dc-b3a0-1f0874ed5df0.png)

When you add this validator to a transition and trigger the transition, the validator checks whether the configured user(s) satisfy the configured criteria, and displays a validation error message if not.

To add a validator:

1. Log into your Jira Server instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Workflows**.
5. Click **Actions** (▢ ) for the workflow you want to edit and select **Edit**.
6. Edit the Transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Validators** link. Click **Add validator** at the top of the list of existing validators.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Validators** tab. Click **Add validator** at the top of the list of existing validators.

When using validators in **Jira Service Management**, you must be careful about exposing transitions to end users through the JSM portal. When a user transitions an issue through the portal, the transition will ignore all validators. Additionally, the customer will not see the `Error message` when the validator fails. This is due to a known limitation with JSM and Atlassian has no timeline for resolution. More information:

- [Show a workflow transition in the portal](https://support.atlassian.com/jira-service-management-cloud/docs/show-a-workflow-transition-in-the-portal/) including information about validators on portal transitions.
- [JSDCLOUD-4007](https://jira.atlassian.com/browse/JSDCLOUD-4007) - Bug covering custom validators failing on customer portals.
- [JSDCLOUD-5853](https://jira.atlassian.com/browse/JSDCLOUD-5853) - Bug on customer portals not displaying error messages.

**Note**: This validator does not work for the following fields when used on the Create transition:

- ***All JSM fields***

JSM-specific fields cannot be validated during the Create transition because these fields are applied to the issue after it is initially created. This is an Atlassian limitation; the native Field Required validator, however, does not have this issue.

## Configure the validator

1. Follow the steps above to add a validator to a transition.
2. From the list of validators, select *Build-your-own (scripted) Validator (JMWE app)*.
3. The *Build-your-own (scripted) Validator* page will open. Configure the validator as needed. See below for details on each of the configurations.
4. Click **Add**.

Note that you will need to publish the workflow for the new validator to take effect.

The following configurations are available:

- **User(s) to check** - You must first configure which user(s) need to be checked.

  - **Current user** - The current user will be checked.
  - **User(s) in field** - The user in the specified field, such as Assignee, Reporter, or any User Picker custom field, will be checked. If the selected field is a multi-valued field, such as Voters, Watchers, or a Multi-user Picker custom field, all users in that field will be checked, and they **all** need to satisfy the criteria.
- **Mode** - You need to specify whether the user(s) to be checked must satisfy *all* the configured criteria or *at least one*.

  - **all the criteria configured below** - Each user will need to satisfy every criterion.
  - **at least one of the criteria configured below** - Each user will need to satisfy at least one of the criteria.
  - **or the field can be empty** - *Only available if* ***User(s) in field*** *and* ***at least one of the criteria configured below*** *are both set.* Choose this option if an empty field satisfies the validator. For example, if you are checking the Assignee field and you select the “or the field can be empty” option, the validator will succeed even if the issue is unassigned.
- **Criteria** - Specify at least one criterion that the user(s) must satisfy for the validator to succeed.

  - **The user is**:

    - **the Reporter**
    - **the Assignee**
    - **a Watcher**
    - **a Voter**
  - **Project roles** - The user belongs to one of the specified Project Roles in the issue’s project.
  - **Groups** - The user belongs to one of the specified groups.
  - **Users** - The user is one of a list of specific users.
  - **User fields** - The user is selected in the specified user-type field, such as a user picker custom field.
  - **Condition for user(s)** - The user or users satisfy a Jira expression. For each user to check, the Jira expression will be evaluated and must return `true` for the validation to succeed. Note that the user being checked is available through the `selectedUser` variable.
  - **Reverse condition** - If this box is checked, the condition specified in **Condition for user(s)** must return `false` for the validation to succeed.

**Note**: The user being checked in your Jira expression is available through the `selectedUser` variable.

- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this box to configure the validator to only run in specific circumstances.
  - **Condition** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.