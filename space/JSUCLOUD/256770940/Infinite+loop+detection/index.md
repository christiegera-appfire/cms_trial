# Infinite loop detection

## What is an infinite loop in JSU?

An infinite loop occurs when an automation rule results in an endless cycle of issue creation and follow-up transitions following the triggering of the origin issue.

An infinite loop can occur if you build your rules with any of the following JSU post functions:

- Create a Linked Issue
- Follow Up Transition
- Linked Transition

When using post functions that create issues or follow-up transitions, consider the outcome of the rule and the user permissions of your project teams. You can also use [preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) to restrict when rules are run to reduce the likelihood of causing an infinite loop.

## What is loop detection?

JSU is configured to detect when a triggered post function results in an infinite loop. When a loop is detected, JSU will stop the execution and log an execution failure. You can then identify and make any necessary adjustments to your workflow. JSU determines the following criteria to identify a loop:

- name of the post function (action)
- transition ID
- workflow ID
- issue ID

Where all of the criteria are the same and the execution is triggered by JSU, the execution is paused.

If your rule results in multiple but different *create* post functions in the same transition, or the post function is triggered on different issues, JSU will not block it.

### Override option for Jira administrators

When an infinite loop is detected and the execution is paused, you can override the detection mechanism and continue with the execution of the post function.

If more than one post function is configured for a transition and more than one is executed, selecting **Continue** will apply to all the triggered post functions. Similarly, selecting **Stop** will stop all the triggered post functions.

![contentId-256770940](/cms_trial/assets/45b902c1-8093-4085-a01e-ae113ce9e41b.png)

The override messages are displayed only to Jira administrators who have triggered the original post function.