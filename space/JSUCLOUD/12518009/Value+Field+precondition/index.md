# Value Field precondition

## Description

The Value Field precondition checks whether a field on the issue matches a value.

For more complex scenarios or to combine several Value Field preconditions, you could use a [JQL precondition](/cms_trial/space/JSUCLOUD/12518033/JQL+precondition/).

## Configuration

You must specify the field you want to check, the operation you want to perform, and the value you want to check against – although you can also check against an empty value.

If a field can have multiple values, for example, components, the precondition matches if one of the values is contained – or if it is not contained.

The following matching rules apply:

- Text fields with operators `=`  or `!=` will match with any text string.
- Text fields with operators `>=, >, <,` and `<=` will match with any number.
- Number fields will match with other numbers.
- Date fields will match with other date fields.
- Date time fields will match with other date time fields.
- Estimate fields (original, remaining estimate) will match with duration formatted strings like `1w 2d 3h 4m 5s`. If no unit is given, minutes are assumed.
- User fields can be matched against the user name or the account ID.
- Sprints, select options, components, versions, issue types, priorities, resolutions, security levels, and statuses are matched against their name or ID.
- Projects are matched against their name, key, or ID.

## Example

An Update Any Issue Field post function is added to the Create transition. A new comment should be created when the number of story points is exceeded, telling the user to break up the story.

![Summary of the Update Any Issue Field post function as described on this page.](/cms_trial/assets/c698a0e4-380d-46c0-9b23-780d4758fe89.png)![Example of the Value Field preconditions set up for Original Estimate, Story Points, and Issue Type.](/cms_trial/assets/68c4d281-53a3-4a43-96e6-df1b08e3b12c.png)

## Supported fields types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.