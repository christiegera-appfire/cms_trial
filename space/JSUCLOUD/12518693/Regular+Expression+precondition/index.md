# Regular Expression precondition

## Description

The Regular Expression precondition compares the value of a text, number, or URL field against a regular expression. Use it to verify that the content matches a specified format.

## Configuration

You must select the field to be checked and enter the regular expression. For example:

![Example of the Regular Expression precondition as described on this page.](/cms_trial/assets/1e755638-9ffb-45fb-a4ef-db0b7f632eac.png)

- **[0-9]{4}-[0-9]{4}** allows numbers such as: 1245-7783
- **[0-9]+ EUR$** allows price tags such as: 34 EUR
- **[a-z]\*** allows an empty string, or any lowercase word such as: yellow
- **Option [A,B]** allows a selection of options: Option A, Option B or both.

Detailed documentation on regular expressions can be found in [Oracle's documentation](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) for a technical description, or at [regular-expressions.info](https://www.regular-expressions.info/) for a more general description. Another good resource for developing and testing regular expressions is [freeformatter.com](https://www.freeformatter.com/java-regex-tester.html).

## Example

A workflow is configured so that the Create transition has the Regular Expression precondition. If the summary contains the phrase `'Onboarding'`or `'onboarding'`, a sub-task will be created for creating the user account in the company's systems.

## Supported field types

JSU supports many different field types; system fields, as well as custom fields.

You should be aware, however, that not all field types or all combinations are supported. We have tried to cover the most important field types but we are continuously adding more and improving how different field types are supported. We recommend you test JSU with fields to see if it is compatible with your system. Our evaluation license provides you with a 30-day free trial.