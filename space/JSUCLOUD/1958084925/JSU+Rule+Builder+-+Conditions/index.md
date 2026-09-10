# JSU Rule Builder - Conditions

JSU Rule Builder - Conditions is a new way to configure conditions for your workflow transitions. You can now add one or more conditions from one place without navigating back to the workflow editor in Jira. The rule builder includes nine new conditions previously only available with our Data Center app to help you deliver better control and compliance to your project workflows. See [Workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/) for the complete list.

### Feature overview video

Watch the video below for a quick introduction to our conditions rule builder.

## When to use conditions

You can use conditions to determine if a workflow transition is available for a user transitioning a work item. For example, you can require that the user is in a specific group, that a field has a specific value or format, or that related work items are in a specific status. If the conditions aren’t met, the user won’t see the transition. See the list of [conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/) to explore more possibilities.

## How to open the rule builder

Jira offers two versions of the workflow editor in Jira Cloud: the old editor and the new workflow editor experience. Currently, you can choose between editors according to your preference. Follow the steps below for your version of the workflow editor in Jira.

| **Old workflow editor in Jira** | **New workflow editor in Jira** |
| --- | --- |
|  |  |
| Step-by-step:   1. Open a draft workflow. 2. Select the transition where you want to apply the check. 3. Select *Conditions*. 4. Click **Add condition**. 5. Select *JSU Rule Builder - Conditions* from the list of available conditions. 6. Click **Add** at the bottom of the page. The JSU Rule Builder opens. | Step-by-step:   1. Select the transition where you want to apply the check. 2. Click **Add Rule**. 3. Select *JSU Rule Builder - Conditions* from the list of available conditions. 4. Click **Select**. The JSU Rule Builder opens. |

## How to configure conditions with the JSU Rule Builder

The rule builder is the same whether you use the old workflow editor or the new workflow experience in Jira Cloud.

1. In the *General* section, provide a name for the rule.
2. Add an optional description or summary for the rule. This is helpful if you configure multiple rules for your workflows.
3. In the left panel, click **Add condition**.
4. In the right panel, select the condition you want to apply to the transition, for example, Field value. This condition checks that a selected field has a specific value.
5. Select the required parameters for the condition. In the example below, the first condition is set so that the transition can be performed only when the Budget field is >= 500.
6. Add another condition to check that the user is a member of a selected user group. In the example below, the User in group condition is set so only users in the Approvers group can transition the issue. The relation to the first condition is set to AND. Therefore, the Approve transition will be available only when the Budget field is >= 500 and the user is in the Approvers group.
7. To add an optional note to help with workflow management, click the **Add note** icon next to the branch header on the left side of the rule builder.
8. Click **Add** at the bottom of the page to save the rule.

   ![Screenshot of the JSU Rule Builder - Conditions as described on this page.](/cms_trial/assets/7c08bbf2-e3bc-4a93-b9bf-85e3f4d1f97c.png)

### Condition expressions

By default, a condition is set to `IS`, which means the statement must be true for the condition to pass. For example, if you set the **Fields required condition** to the *Assignee* field, then that field must have a value for the transition to be available. You can use the condition expression to change the check to IS NOT instead. For additional conditions, you can set their relation to the first using `AND`, `AND NOT`, `OR`, and `OR NOT`.

### Expensive operations

Atlassian considers some conditions expensive when they require large amounts of data to be checked. For example, User in group might involve checking against thousands of users and multiple groups. The additional resource needed for these checks can slow down the system. Atlassian limits expensive operations to 10 per rule. Expensive operations are indicated in the app with a brain icon.

![User in group condition showing the expensive operation icon.](/cms_trial/assets/f5b3df55-f54e-4c23-8a19-9ec86a0a49ff.png)

Refer to Atlassian’s [developer documentation](https://developer.atlassian.com/cloud/jira/software/jira-expressions/#restrictions) to learn more about how they identify expensive operations.

## How to add complex rules

You can use the rule builder to build complex rules to meet a variety of use cases in a single rule.

### Add multiple conditions

You can add multiple conditions under a single IF block using different expressions. For example, you can create a condition that checks if a user is in a selected group and then another to check that the parent work item is a particular status using the `AND` expression.  
JSU checks both conditions before moving to the next check. In the example below, the user must be in the Approvers group, and the Parent work item (issue) must be in the approved status for the check to pass.

![JSU-CV showing multiple conditions.](/cms_trial/assets/e21f70d7-5a2b-4eaa-b17a-1dfd4a94ea5f.png)

### Add duplicate conditions

If you want to add multiple conditions of the same type, you can duplicate a condition and then update the configuration. The duplicate is added under the original condition. To create a duplicate, click the **Duplicate** icon in the condition configuration panel.

### THEN IF and ELSE blocks

If the check doesn’t pass, the transition won’t be available to select. You can add additional or alternative checks using a nested THEN IF block or an ELSE branch.

- **THEN IF blocks**: Conditions added to a THEN IF block are checked only when the previous check passes. To add a THEN IF block, click the plus icon (**+**) next to the IF header, then select **Add nested IF block**.▢
- **ELSE branches**: Else branches are checked when the previous check fails. To add an ELSE branch, click the plus icon (**+**) next to the ELSE header, then select **Add nested IF block**.

## Related pages

- [Workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/)