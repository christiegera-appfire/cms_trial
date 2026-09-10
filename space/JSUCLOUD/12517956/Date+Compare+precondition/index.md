# Date Compare precondition

## Description

The Date Compare precondition compares the values of two date fields on the issue. For example, one field must be greater than the other.

## Configuration

You must select the two date fields and the comparison function for the check when configuring the transition. For example:

![Date Compare precondition where the Resolved date is greater than the Due Date.](/cms_trial/assets/b3854595-f6c3-42f7-95c8-bdccb1715fd0.png)

## Example

A workflow is configured so that the Resolve transition has the Date Compare check where `Resolved date > Due date`. If a user attempts to resolve an issue on this workflow where the Resolved date is after the Due date, the check will succeed, and a comment will be created regarding the late resolution.

### Supported Field Types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.