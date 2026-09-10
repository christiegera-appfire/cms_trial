# User in Roles precondition

## Description

The User in Roles precondition verifies that the current user is in at least one of the specified project roles.  
There is a User Is In Role condition in Jira, that only lets you verify the membership of the user against a single project role.

## Configuration

You must specify the roles that are the prerequisite for this transition when configuring the check. For example:

![Example of User In Roles precondition as described on this page.](/cms_trial/assets/c8cc80da-eead-4f77-9f01-9945851fd9ba.png)

## Example

A workflow is configured so that the Resolve transition has the User in Roles check. If the executing user is an administrator, all subtasks will be closed as well.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.