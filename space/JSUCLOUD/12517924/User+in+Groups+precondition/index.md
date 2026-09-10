# User in Groups precondition

## Description

The User in Groups precondition checks that the current user is a member of at least one of the specified groups.   
There is a '*User Is In Group'* condition in Jira that only allows you to verify the membership of a user against a *single* group.

## Configuration

You must specify the groups when configuring the check. For example:

![Example of User in Groups precondition as described on this page.](/cms_trial/assets/49b031b8-6419-4da3-b973-8d05cb32878b.png)

## Example

A workflow is configured so that the Resolve transition has the User in Groups check. If the user is a developer, and the issue is a Story, a sub-task will be created for the QA Analysis.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.