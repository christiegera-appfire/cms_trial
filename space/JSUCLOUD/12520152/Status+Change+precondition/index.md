# Status Change precondition

## Description

The Status Change precondition checks if status of the issue will be changed when executing the current transition. This condition is useful to prevent Any status transitions from being displayed when the transition does not change the current issue status (i.e. a transition Start Progress when the status is currently In Progress ).

## Configuration

This precondition does not have any configurable options.

For information on how to configure a check for a workflow transition in Jira, see the [Jira documentation](http://confluence.atlassian.com/display/JIRA/Configuring+Workflow#ConfiguringWorkflow-Addingacondition).

![Example of the Status Change precondition as described on this page.](/cms_trial/assets/0b93f11e-b0d8-4307-ac02-aee5f0aca7dd.png)

### Example

A From Any Status workflow transition is configured so that the Start Progress transition will change the status from any issue status to in progress . The From Any Status transition will be available in all statuses, however, you may want to prevent the 'Start Progress' transition from being displayed when the issue is already in the status 'In Progress'. When adding the 'Status Changed Condition' the 'Start Progress' transition will not be available when the issue is in the status 'In Progress'.

### Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.