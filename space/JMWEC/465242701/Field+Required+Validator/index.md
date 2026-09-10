# Field Required Validator

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

A workflow validator that ensures the specified field or fields have a value during a transition.

![Field Required configuration screen](/cms_trial/assets/cd86dab3-e0a6-4c33-b93a-2a318ce43a64.png)

When this validator is added to a transition and that transition is triggered, the extension checks for a value in the selected field or fields. If no values are found, an error message is displayed; this error message will display a default value, or it can be customized.

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

**Note**: This validator does not work for the following fields:

- ***Security Level***
- ***Watchers***
- ***Epic Color***
- ***Epic Name***
- ***Epic Status***
- ***Raised during***

And it does not work for the following fields when used on the Create transition:

- ***Parent***
- ***All JSM fields***

Please see the additional notes below for more information.

Additionally, some custom fields from other apps, like ***Team*** of Jira Portfolio, though available in the list are not supported because of certain limitations (of the apps).

### JSM fields

JSM-specific fields cannot be validated during the Create transition because these fields are applied to the issue after it is initially created. This is an Atlassian limitation; the native Field Required validator, however, does not have this issue.

### Parent field

It is not currently possible to verify the **Parent** field during a Create transition, or if the Parent field is selected during a transition screen. This is due to a limitation in Atlassian’s implementation of the new **Parent** field (refer to <https://support.atlassian.com/jira-software-cloud/docs/upcoming-changes-epic-link-replaced-with-parent/> for more information). *The workaround for validating the* ***Parent*** *field is to create the Field Required validator using the* ***epic-link*** *(for Epic-Story relationships) or* ***parent-link*** *(for other relationships).* This will still validate the Parent field, as currently some of the updates in Jira are cosmetic only.

## Configure the validator

1. Follow the steps above to add a validator to a transition.
2. From the list of validators, select *Field Required Validator (JMWE app)*.
3. The *Field Required Validator* page will open. Configure the validator as needed. See below for details on each of the configurations.
4. Click **Add**.

**Please note**: only 10 (ten) ***custom*** fields can be added to the selected fields for the **Field Required** validator; more than ten system fields can be added. If more than ten custom fields are added, it will not be possible to add the validator to the transition. This is a known issue with Jira expressions, as documented in [ACJIRA-2312](https://ecosystem.atlassian.net/browse/ACJIRA-2312).

The following configurations are available:

- **Field(s)** - Select the field or fields that are required for the issue to transition. Click the **X** beside a field to remove it from the list.
- **Error message** - The error message that will display if the validator fails.
- **Validator scope**

  - **Conditional validation** - Check this box to configure the validator to only run in specific circumstances.
  - **Condition** - *Only visible when* ***Conditional validation****, above, is checked.* Enter a Jira expression; if the expression evaluates to `true`, the validator will run.
  - **Skip validation when cloning an issue** - Check this option to skip the validator when an issue is being cloned.