# Date Expression Compare precondition

## Description

The Date Expression Compare precondition compares the value of a date field with a date expression. For example, the date field must be more recent than the actual date.

## Configuration

You must select the date field, the comparison condition, the date expression, and whether to include the time part for comparison.

![Example configuration for the Date Expression Compare precondition as described on this page.](/cms_trial/assets/c1c7a4f8-fbed-4287-8310-3e49711618a3.png)

## Example

A workflow is configured so that the Resolve transition has the Date Expression Compare check where `Due date > 1w 1d`. If the transition is executed, and the due date is more than a week and five days away, the time left at resolution will be set to `> 1w`.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.