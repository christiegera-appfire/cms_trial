# Comment Required Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator that forces users to enter a comment during a transition. If the user does not enter a comment, a custom error message will be displayed.

![Comment Required Validator configuration screen](/cms_trial/assets/be6694cc-75ce-4f7c-ba91-2aff7c847e66.png)

The comment should be entered on the transition screen (in the Comment section) of the transition.

When you add this validator to a transition and trigger the transition, the add-on checks for a value in the **Comment** field of the **Transition screen.** If it is blank, the configured validation error message will be displayed.

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
2. From the list of validators, select *Comment Required Validator (JMWE app)*.
3. The *Comment Required Validator* page will open. Configure the validator as needed. See below for details on each of the configurations.
4. Click **Add**.

Note that you will need to publish the workflow for the new validator to take effect.

The following configurations are available:

- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this option if you want validation to occur only in certain cases, such as if the issue is of a certain issue type, has certain field values, or more generally satisfies an arbitrary [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).
  - **Conditional validation expression** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.