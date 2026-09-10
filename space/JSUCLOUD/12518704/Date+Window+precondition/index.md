# Date Window precondition

## Description

The Date Window precondition checks whether the value of one date field falls within the range/window of another date field. Date checking is only one-way; it only looks forward, not backward.

## Configuration

You must select the two date fields and the window period when configuring the transition. For example:

![Example of the Date Window precondition as described on this page.](/cms_trial/assets/3e3c1c84-8c16-42fd-b4e2-deae13b480b6.png)

## Example

A workflow is configured so that the Close transition has the Date Window check. The Resolved date is checked using a window of 5 days with respect to the Created date. If the issue is resolved within five days of being created, a comment with the text `Quick Win!` will be added.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.