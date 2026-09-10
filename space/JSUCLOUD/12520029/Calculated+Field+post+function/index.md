# Calculated Field post function

Looking for the *Global Calculated Fields* post function? See the [deprecation](/cms_trial/space/JSUCLOUD/12519627/Deprecation+-+Global+Calculated+Fields/) information page.

## Description

The Calculated Field post function calculates field value based on the formula configured for all related issues.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

## Configuration

![Example configuration of the Calculated Fields post function.](/cms_trial/assets/ab17b2de-ca3f-4697-90f8-ddfc7852018c.png)

### Precondition

If you are using preconditions with a JSU post function, they can be evaluated in the following ways:

- **True** (Precondition must be true to execute the post function)
- **False** (Precondition must be false to execute the post function)

Learn more about JSU preconditions in [Workflow preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) or see our [use cases](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for examples.

### Issue relation

Related issues for the Calculated Field post function can be identified by one of the following Jira concepts:

- **Issue link:**You can define the link type to define which issues will be modified by the operation. If the post function includes the link type is ANY option, the operation will be performed on any linked issues.
- **Parent / Sub-Task:** The related issue is either a parent or a subtask of the issue.
- **Epic / Issue in** **Epic:**The other issue is either an epic related by an epic link or it is part of an epic. This is only applicable if you have Jira Software installed.
- **JQL:**A JQL query will be executed to retrieve the issues that the post function will modify. You can use some placeholders in the JQL query, which will be replaced with the current field values of the issue in transition. For tips on writing the JQL query, see [JQL reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) or our [JQL use cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for some examples.

### Formula

To define your formula, select the field on which the calculated value will be set, then enter your desired formula. You can select other fields, numbers, and mathematical expressions to calculate the formula. For example, you can select **Total story points** to display the sum of story points for all the issues in an epic. See [Calculated Field formulas](/cms_trial/space/JSUCLOUD/12519260/Calculated+Field+formulas/) for more information.

![Example formula used in the procedure described on this page.](/cms_trial/assets/143a1bed-7ec0-4c0c-9812-5c5f7aff5d4d.png)

## Related pages

- [Key concepts](/cms_trial/space/JSUCLOUD/12518573/Key+concepts/)
- [Workflow preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/)
- [Calculate total story points for an epic](/cms_trial/space/JSUCLOUD/12519508/Calculate+total+story+points+for+an+epic/)