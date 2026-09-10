# Linked Issues Status Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator which ensures that the current issue's linked issues have a status value matching the status values you’ve configured.

![JMWE for Jira Cloud linked issues status validator configuration with status checking](/cms_trial/assets/305db11c-f0a3-4bfc-84b0-ae9984d247b0.png)

When you add this validator to a transition and trigger the transition, the extension validates the specified condition against the **Status** of the linked issue(s) (existing and ones added during the transition). If the condition is not met, the transition fails, and an error message.

**Note**: The list of statuses displayed under the `Statuses` field has all the statuses across different workflows. This is because the workflow of an issue and that of its linked issues can be different.

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

- **Issue Link Type** - Select the issue link type that links the current issue to the linked issues to check the specified condition against. Leave "Any (default option)" for no restrictions.
- **Mode** - Select one of the following conditions to be run on the linked issue(s) for the transition to be enabled:

  - **All issues must be in the selected statuses below**
  - **At least one issue must be in one of the selected statuses below**
  - **No issue must be in one of the selected statuses below**
  - **At least one issue must not be in one of the selected statuses below**
- **Issue Type** - Select the issue type of the linked issue(s) to check the specified condition against. Leave "Any (default option)" for no restrictions.
- **Statuses** - Select one or more statuses from the available list against which to check the issues.
- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this box to configure the validator to only run in specific circumstances.
  - **Condition** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.