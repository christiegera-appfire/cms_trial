# Validation error (Field mapping)

## Problem

You receive the following validation error message when saving your general or custom [field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/) settings:

![Validation error that says Changes not saved. Field mapping must be unique - each field can be selected for mapping only once.](/cms_trial/assets/c3f1aace-a02c-47b1-8491-06a3e9145389.png)

## Solution

Each field in BigPicture must be mapped to a unique Jira field. For example, if you map the End date field in BigPicture to the End date in Jira, that Jira field cannot be mapped again to any other field in the same Jira project.

![The end date field in Jira is mapped twice in BigPicture.](/cms_trial/assets/290c5a23-93aa-4924-9322-52c47cef4f55.png)

To solve the issue, select another suitable field from the dropdown to replace the Jira field that appears twice in your field mapping setup.

## More information

- [Fields](/cms_trial/space/SPM/1918635376/Fields/)
- [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/)