# JSU Rule Builder - Validators

JSU Rule Builder - Validators is a new way to configure validators for workflow transitions. You can build, preview, and edit one or more validators from one place without navigating back to the workflow editor in Jira. The rule builder includes 11 JSU validators to help you deliver better control and compliance to your project workflows. See [Workflow validators](/cms_trial/space/JSUCLOUD/12518578/Workflow+validators/) for the complete list.

### Feature overview video

Watch the video below for a quick introduction to our validation rule builder.

## When to use validators

You can use validators in your workflows to determine if a workflow transition can be completed by checking field values, selections, and statuses. For example, they could require that an input follow a specific format, that an attachment be added, or that the Resolution field not be empty. If a validation check fails, JSU blocks the transition.

## How to open the rule builder

Jira offers two versions of the workflow editor in Jira Cloud: the old editor and the new workflow editor experience. Currently, you can choose between editors according to your preference. Follow the steps below for your version of the Jira workflow editor.

| **Old workflow editor in Jira** | **New workflow editor in Jira** |
| --- | --- |
|  |  |
| Step-by-step:   1. Open a draft workflow. 2. Select the transition where you want to apply the check. 3. Select *Validators*. 4. Click **Add validator**. 5. Select *JSU Rule Builder - Validators* from the list of available validators. 6. Click **Add** at the bottom of the page. The JSU Rule Builder opens. | Step-by-step:   1. Select the transition where you want to apply the check. 2. Click **Add Rule**. 3. Select JSU Rule Builder - Validators from the list of available validators. 4. Click **Select**. The JSU Rule Builder opens. |

## How to add a validator with the rule builder

The rule builder is the same whether you use the old workflow editor or the new workflow experience in Jira Cloud.

1. In the *General* section of the rule, provide a name for the validation rule.
2. Add an optional description or summary for the rule. This is helpful if you configure multiple rules for your workflows.
3. Add an optional error message to show the user if the transition is blocked, for example, `The Assignee field can’t be empty.` If you don’t add a custom error message, JSU displays a default error message instead. See [How to add dynamic custom error messages](/cms_trial/space/JSUCLOUD/2199978970/How+to+add+dynamic+custom+error+messages/) to learn more.
4. In the left panel, click **Add validator**.
5. In the right panel, select the validator you want to apply to the transition, for example, **Fields required**.
6. Select the required parameters for the validator. In the example below, the Fields required validator is set so the Assignee field can’t be empty.
7. To add an optional note to help with workflow rule management, click the **Add note** icon next to the branch header on the left side of the rule builder.
8. Click **Add** at the bottom of the page to save the rule. With this validator, the user must assign the work item to complete the transition.

   ![Screenshot of a validator setup in the JSU rule builder.](/cms_trial/assets/56d6d3eb-9545-41e3-b1e2-e107e1658466.png)

### Validator expressions

By default, validators and conditions are set to `IS`. For a single validator, you can change the expression to `IS NOT` so that the validator result must be false to pass. For additional validators, you can set their relation to the first using `AND`, `AND NOT`, `OR,` and `OR NOT`.

### Expensive operations

Atlassian considers some validators expensive when they require large amounts of data to be checked. For example, User in group might involve checking against thousands of users and multiple groups. The additional resource needed for these checks can slow down the system. Atlassian limits expensive operations to 10 per rule. Expensive operations are indicated in the app with a brain icon.

![User in group validator with the Expensive operation icon shown.](/cms_trial/assets/85b6bd65-a911-4100-af0b-de8f4861fff5.png)

Refer to Atlassian’s [developer documentation](https://developer.atlassian.com/cloud/jira/software/jira-expressions/#restrictions) to learn more about how they identify expensive operations.

## How to add complex rules

You can use the rule builder to build complex rules to meet a variety of use cases in a single rule.

Watch the overview video for a quick example, or read the sections below to learn more about adding multiple validators.

### Add multiple validators

You can add multiple validators under a single IF block using different expressions. For example, you can create a validator that checks if a user is in a selected group and then another to check that the parent work item is a particular status using the `AND` expression.  
JSU checks both validators before moving to the next check. In the example below, the user must be in the Approvers group, and the Parent work item (issue) must be in the approved status for the check to pass.

![JSU rule using multiple validators.](/cms_trial/assets/3ca5f58d-2635-4bd1-9685-1410c4e52e0f.png)

### Add duplicate validators

If you want to add multiple validators of the same type, you can duplicate a validator and then update the configuration. The duplicate is added under the original validator. To create a duplicate, click the **Duplicate** icon in the validator configuration panel.

![Screenshot of the highlighted duplicate icon in validators rule builder.](/cms_trial/assets/d6b6c74c-983c-40ab-8cad-e3c383a97794.png)

### THEN IF and ELSE blocks

If the check doesn’t pass, JSU blocks the transition and displays an error message to the user. You can add additional or alternative checks using a nested THEN IF block or an ELSE branch.

- **THEN IF blocks**: Validators added to a THEN IF block are checked only when the previous check passes. To add a THEN IF block, click the plus icon (**+**) next to the IF header, then select **Add nested IF block**.

  ![JSU-CV-nested-IF.png](/cms_trial/assets/b3964744-f1bc-4072-8c7a-69ae9c74b59d.png)
- **ELSE** **branches**: Else branches are checked when the previous check fails. To add an ELSE branch, click the plus icon (**+**) next to the ELSE header, then select **Add nested IF block**.