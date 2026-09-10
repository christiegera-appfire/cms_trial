# Follow Up Transition post function

## Description

The Follow Up Transition post function evaluates the [workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/) of all subsequent transitions based on the target status of the current transition, including global transitions. If exactly one transition is possible, that transition will be triggered as a follow-up. If more than one transition is possible, JSU cannot determine which to use as the follow-up transition. To learn more about global transitions in Jira workflows, see Atlassian’s <https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/#Global-transitions>.

See [Workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) to learn how to add a JSU post function to a Jira workflow.

## Configuration

The Follow Up Transition post function has no additional parameters to configure; however, you must have at least one workflow condition configured.

## Use case

![An example Jira workflow that includes a junction status that leads to three different follow-up transitions depending on the condition that is met.](/cms_trial/assets/a8b752e2-380d-46e2-b93c-268f15a714ae.png)

- Our issue has a mandatory number custom field.
- At the end of the *Go* transition, we have configured a Follow Up Transition post function.
- Each transition leading away from the status junction has a workflow condition:

  - *Under Five* has the condition: Number field < 5?
  - *Exactly Five* has the condition: Number field == 5?
  - *Over Five* has the condition: Number field > 5?
- When a user performs the *Go* transition, this will always trigger a follow-up transition.

For example, if a user enters Number=3 during the Go transition, this leads to the in progress status. If they enter 42, this leads to closed.

We configured our workflow conditions so that only ever one condition can be true. This way, the user will never be stuck at the junction status.

## Conditions

Use conditions to ensure that only one transition is possible for the follow-up transition. Let's continue the example from above, where a number field is evaluated. We will configure three conditions: one for each outgoing transition from the junction status.

#### Under Five

![The Under Five condition.](/cms_trial/assets/8dcbaa10-c366-44f0-9332-f9f44d562fe9.png)

#### Exactly Five

![The Exactly Five condition.](/cms_trial/assets/df472d58-bdbe-42f1-8cd1-f5dc16a0a02f.png)

#### Over Five

![The Over Five condition.](/cms_trial/assets/9360b367-a49e-4be8-ad67-4207d5cd91eb.png)

#### Simple *Yes / No* example

A simpler use case occurs when there are only two transitions leading from a status, and you evaluate the same condition, with one condition being negated.

- a == b?

You can use Jira’s Value Field condition for this setup.

![Example Jira workflow with a junction status with only one condition that determines the follow up transition.](/cms_trial/assets/83e855ca-0957-4bb5-9669-d7d61c2009ea.png)

- Check it: Follow Up Transition post function.
- Yes: Condition a == b?
- No: Condition a != b?

#### Fast forward example

Some extra steps in your workflow might only be necessary if a specific condition is not met. Otherwise, that step could be skipped.

![Example Jira workflow that uses a condition to bypass a step.](/cms_trial/assets/c8e91a0f-1bf0-4c64-8a76-5701fd32f48f.png)

#### Management approval

See the [Streamline an approval process](/cms_trial/space/JSUCLOUD/12518631/Streamline+an+approval+process/) use case for another example.

You can learn more about workflow conditions in Atlassian’s [Configure Advanced Issue Workflows](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/#Validators) article.

## Troubleshooting

**Problem**: Workflow is blocked at the Junction status

**Cause**: Not exactly one condition

Usually, the problem can be tracked down by reviewing the expected outcome of the post function;  
if exactly one condition is valid, the corresponding transition will be triggered.

It's important to do your analysis with the same user who encountered the problem. There might be issues with permissions that could lead to a different result, depending on the user performing the transition.

Consider an issue blocked at the Junction status: How many transition buttons does it have? If you have none or more than one transition, review your workflow conditions on the transitions leading out from the JUNCTION status.

If there is only one button, there might be something wrong with that transition. For example, a validator could prevent the transition from being completed.

**Cause**: Triggered transition fails

Another reason might be that the triggered transition does not run. For example, if it has a validator that fails.

### Infinite Loop Detection

An infinite loop can occur when executing the Follow Up Transition post function. An infinite loop results in an endless cycle of issue creation and follow-up transitions following the triggering of the origin issue. When a loop is detected, JSU will stop the execution and log an execution failure.

When using post functions that create issues or follow-up transitions, consider the outcome of the rule and the user permissions of your project teams. You can also use [preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) to restrict when rules are run to reduce the likelihood of causing an infinite loop. Learn more about how JSU identifies an infinite loop in [Infinite loop detection](/cms_trial/space/JSUCLOUD/256770940/Infinite+loop+detection/) .

## Related pages

- [Streamline an approval process](/cms_trial/space/JSUCLOUD/12518631/Streamline+an+approval+process/)
- [Infinite loop detection](/cms_trial/space/JSUCLOUD/256770940/Infinite+loop+detection/)
- [Workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/)