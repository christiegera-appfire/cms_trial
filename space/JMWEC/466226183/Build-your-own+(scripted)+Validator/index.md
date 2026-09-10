# Build-your-own (scripted) Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator that is based on the result of a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).

![Build-your-own Validator No Code Configuration Screen](/cms_trial/assets/cabc25e4-3b9b-449b-937c-5161bf6119a3.png)

If the Jira expression returns `false`, a validation error message will be displayed. This can be used to test or compare issue fields, to test for linked issues, to check for open Sprints, among many others.

When you add this validator to a transition and attempt to trigger the transition, the extension checks the result of a logical test, comparing a field value to either another field value or to a set value. The logical test can be a [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) entered manually, or you can build an expression using the *No Code* option (see below). If the expression returns `true` the transition will trigger; if it returns `false` or any non-boolean value, a validation error message is displayed.

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

![Build-your-own Validator Jira Expression Configuration Screen](/cms_trial/assets/bccd09e2-4b6c-4c68-b380-c1f5a6d80a93.png)

The following configurations are available:

- **Description** - Give the validator a description; this will be included in the list of validators for the transition and in the [Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) administration page.
- **No Code** (Figure 1, right) - These fields will only display when **Choose type** is set to *No Code*. Select this option to create the validator without the need to write a Jira expression. Set each of the following options:

  - **Field** - Select the field to be tested.
  - **Operator** - Select the logical operation to use in the test; for example, *Equals*, *Does not equal*, *is empty*, *Less than*, or *Greater than* (among others).
  - **Value to compare type** - Select against what value the test will be evaluated:

    - *Field* - Compare the condition field against the value(s) of another field.
    - *Text* - Compare the condition field against a set value.
  - **Value to compare** - Either select a field from the pulldown menu, or enter a set value.
- **Jira Expression** (Figure 2, right) - The Jira expression editor will only display when **Choose type** is set to *Jira Expression*. Enter the [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) for the logical test for the validator. If this test evaluates to `false`, the validator will fail and prevent the transition from executing.
- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this box to configure the validator to only run in specific circumstances.
  - **Condition** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.

### Computed Expressions

![Computed Expression field showing the JavaScript result of configurations](/cms_trial/assets/2b4c8b5e-ac4a-465a-949e-c6fa80cb42ee.png)

If you use the *No Code* option to create your condition, the **Computed Expression** box (Figure 3, right) will populate with the equivalent Jira expression for your configurations. You will not be able to alter the script, but it is possible to test the script and to copy the script so it can be pasted elsewhere.

Click **Test** ( ▢ ) to open a window where you can select an issue against which the script should be tested.

Click **Copy** ( ▢ ) to copy the script to your clipboard.