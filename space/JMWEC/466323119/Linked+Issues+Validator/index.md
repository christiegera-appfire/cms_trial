# Linked Issues Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator that ensures the issues linked to the current issue (existing and ones added during the transition) have certain characteristics. The transition to which the validator is added will pass only when the linked issues respect these characteristics.

![JMWE for Jira Cloud linked issues validator setup with validation rules](/cms_trial/assets/ccefc130-0fde-4688-9258-d65e16eb6013.png)

When you add this validator to a transition and trigger the transition, the add-on checks the specified condition on linked issues (existing and ones added during the transition) that are of the specified issue link type and issue type; all the other linked issues will be considered as satisfying the condition and hence pass the validation. You can further customize the validation using the details mentioned in the next section.

- This validator does not work with **remote links** (links to Jira issues residing on another Jira instance/server).
- Beware of the default "relates to" link type, which can cause confusion. The problem stems from the fact that "relates to" is both the *inward* *direction* and the *outward direction* of the "Relates" link type. We recommend that you rename one of the directions to "is related to" to avoid confusion. This can be done on the Issue Linking Jira admin page.
- Jira portfolio links are not supported in Jira expressions and, hence, are not available in the validator.

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
2. From the list of validators, select *Linked Issues Validator (JMWE app)*.
3. The *Linked Issues Validator* page will open. Configure the validator as needed. See below for details on each of the configurations.
4. Click **Add**.

Note that you will need to publish the workflow for the new validator to take effect.

The following configurations are available:

- **What to validate** - Select one of the following validations to be run on the linked issues to allow or stop the transition from proceeding further:

  - **Require the creation of issue links on the transition screen** -At least one issue link must be added on the transition screen, and that link must be of the specified **Issue Link Type** and respect the constraints in the *What to enforce on linked issues*section.
  - **Validate issue links added on the transition screen, if any** -If issue links are added on the transition screen, validate that they are of the specified **Issue Link Type** and must respect the constraints in the *What to enforce on linked issues*section.
  - **Require certain linked issues** -The transition cannot proceed if linked issues respect the specified **Issue Link Type** and must respect the constraints in the *What to enforce on linked issues*section. These issue links can either already exist or be added on the transition screen.
  - **Check linked issues** -If the specified linked issue(s) exist, the transition cannot proceed unless these linked issues respect the specified **Issue Link Type** and must respect the constraints in the *What to enforce on linked issues*section. These issue links can either already exist or be added on the transition screen.
  - **Forbid certain linked issues** - If any linked issue with the defined **Issue Link Type** and the constraints mentioned in the *What to enforce on linked issues* section exists, the transition cannot proceed. These issue links can either already exist or be added on the transition screen.
- **Issue Link Type** - Select the issue link type that links the current issue to the linked issues to check the specified condition against.
- **What to enforce on linked issues**

  - **Issue Type** - Select the issue type of the linked issues to check the specified condition against. Leave "Any (default option)" for no restrictions.
  - **Additional condition** - Select one of the following:

    - **None** -Select this option for no additional condition.
    - **At least one linked issue must satisfy the condition below** - Select this option for at least one linked issue to satisfy the condition specified in **Jira expression**.
    - **Every linked issue must satisfy the condition below** - Select this option for every linked issue to satisfy the condition specified in **Jira expression**.
    - **Jira expression** - *Only visible when* ***Additional condition****, above, is set to either 'At least one linked issue must satisfy the condition below' or ‘Every linked issue must satisfy the condition below’.* Enter a Jira expression to be checked on all linked issues. If the Jira expression evaluates to true for all linked issues, only then the workflow validation will pass. If it evaluates to false for at least one linked issue the workflow condition will fail. See [Using Jira Expressions](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) for information on writing a Jira expression.

### Avoid errors in Jira expressions

When a Jira expression throws an error, Jira considers the result as false, and hence the workflow validator fails (for all linked issues irrespective of the option selected under "Additional condition"). The best way to avoid errors in your Jira expressions is to test your Jira expressions against an issue using the "Jira expression tester" before saving the validator. Here are typical problems you need to look out for:

- null **values:** if your Jira expression accesses properties of an object that is null, then your Jira expression and thereby your workflow validator fails with an error. For example, to check that the issue's parent is a Story if you provide the Jira expression:

  ```text
  issue.parent.issuetype.name == "Story"
  ```

  when tested against an issue without a parent, the Jira expression will return an error "Type null does not have any properties". To handle this you should include an expression to test that the issue has a parent.

  ```text
  !! issue.parent && issue.parent.issuetype.name == "Story"
  ```

- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this box to configure the validator to only run in specific circumstances.
  - **Condition** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.