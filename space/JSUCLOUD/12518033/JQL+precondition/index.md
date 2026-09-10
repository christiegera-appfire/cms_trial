# JQL precondition

## Description

The JQL precondition compares the number of issues returned from the JQL query against predefined conditions like:

- Find at least one issue
- Must not find any issue
- Compare with a particular number

Some of the simple things you would do with the JQL Precondition, you might also achieve with the [Value Field Precondition](/cms_trial/space/JSUCLOUD/12518009/Value+Field+precondition/). Choose the approach that is the simplest for you and your Jira admin colleagues.

## Configuration

You must write the JQL query and choose one option for the number of issues found. In the example below,the post function will only be executed for bugs. You don’t need a separate workflow (and special workflow scheme configuration) when you only want one post function to perform differently for a particular issue type.

For tips on using JQL with JSU, see [JQL Reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/).

![Example of the JQL precondition as described on this page.](/cms_trial/assets/4bbfe4d5-d83d-43d6-8daf-2307fb722c89.png)

## Examples

See the [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for several examples.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.