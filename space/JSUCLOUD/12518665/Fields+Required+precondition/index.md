# Fields Required precondition

## Description

The Fields Required precondition checks whether values for specified fields are set for a given transition.

## Configuration

You must select mandatory fields when configuring the transition. For example:

![Example of a Fields Required precondition as described on this page.](/cms_trial/assets/2b2191fb-3fab-43f1-9c29-67b6895d0347.png)

## Example

A workflow is configured so that the 'Ready for Review' transition has the 'Fields Required' check where the 'Reviewer' is mandatory. It will then copy the Reviewer to the Assignee, assigning the issue to the reviewer.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.