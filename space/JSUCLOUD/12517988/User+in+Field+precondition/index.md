# User in Field precondition

## Description

The User in Field precondition checks that the current user is in the specified field, typically a multi-select/user picker custom field.

## Configuration

You must specify the field that is the prerequisite for this transition, and whether the user must be in the field or not, when configuring the check. For example:

![Example of User in Field precondition as described on this page.](/cms_trial/assets/2182a405-6d3e-465f-98bf-4a7600beac4e.png)

## Example

A workflow is configured so that the Approve transition has the User in Field check. If the current user is not the specified reviewer, the description will be modified to show who performed the review instead.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.