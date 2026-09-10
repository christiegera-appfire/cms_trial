# 3.2.3 Release notes

![Release Notes.png](/cms_trial/assets/1df658a4-c83e-4a6d-9b73-6f4c5bd17508.png)

**Release date**: December 2, 2024

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud. This release introduces an exciting new feature, some enhancements, and bug fixes.

#### Live Fields for Jira Cloud is finally here!

**Live Fields for Jira Cloud** lets you dynamically control your Jira fields' behavior. You can show, hide, enable, disable, and auto-populate fields based on conditions in both Create Issue and Issue views, with Transition View support coming soon.

As a dedicated Forge app built to work seamlessly in Jira Cloud, **Live Fields is included at no extra cost** with your Power Scripts for Jira Cloud license. Just install the app to get started.  

[Unmapped macro: button-handy — no content to fall back on]

---

| **Contents** |
| --- |
| - [Live Fields for Jira Cloud is finally here!](#live-fields-for-jira-cloud-is-finally-here) - [New Feature](#new-feature) - [Live Fields for Jira Cloud](#live-fields-for-jira-cloud) - [Enhancements](#enhancements) - [Increased speed for JQL indexing](#increased-speed-for-jql-indexing) - [Update parent issue field using SIL script](#update-parent-issue-field-using-sil-script) - [Bug fixes](#bug-fixes) |

---

## New Feature

## Live Fields for Jira Cloud

**Live Fields for Jira Cloud** lets you customize your Jira interface with JavaScript or TypeScript scripts. These scripts run across Jira screens to control field visibility, behavior, calculations, and validation. This ensures data quality while streamlining processes and improving user experience.

Learn more about Live Fields for Jira Cloud:

- [Feature tour](https://appfire.atlassian.net/wiki/spaces/LF/pages/1497892138)
- [Key concepts](https://appfire.atlassian.net/wiki/spaces/LF/pages/1497793566)
- [Limitations](https://appfire.atlassian.net/wiki/spaces/LF/pages/1497957671)

For detailed information, see the [Live Fields documentation](https://appfire.atlassian.net/wiki/spaces/LF).

---

## Enhancements

## Increased speed for JQL indexing

- Added (auto)parallelization to the indexing.
- Added a new parameter to the reindex function `admReindex(jql [, async])`. If set to false, it will not run in the background.

## Update parent issue field using SIL script

Users are now able to update the parent field of the current issue to the specified issue key, using the following syntax:

`%key%.parent = "NewIssueKey";`  
Some key points:

- The `%key%` represents the current issue key.
- The parent field is set to the desired issue key enclosed in quotes.
- This can be used to link the current issue to a parent issue in the system.

Let's look at a simple example:

```text
// Current issue key is PROJ-123
%key%.parent = "TEST-23";
```

This would update the parent field of the current issue PROJ-123 to be the issue TEST-23.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed project key search in context configuration.  
  The automatically generated JQL query included unexpected project keys, causing incorrect query results until the additional project key condition was manually removed. This fix ensures the automatically generated query only references the relevant project(s) without including unrelated project keys.
- Fixed an issue where consecutive SIL post-function executions corrupted rich text field formatting.  
  When a transition with a SIL script updated a rich text field multiple times, the formatting would become corrupted, causing display issues in subsequent runs. The fix ensures proper preservation of both content and formatting, maintaining field integrity across all transition executions.
- Fixed time zone handling in Date fields.  
  The system incorrectly considered the timezone for Date fields when it should only have been applied to DateTime fields.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think here. [unmapped inline: placeholder]

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [unmapped inline: placeholder]!

|  |  |
| --- | --- |
| **Release date** | December 2, 2024 |
| **Highlights** | - Take control of your Jira fields with Live Fields for Jira Cloud - Increased speed for JQL indexing - Update parent issue title using SIL script - Fixed project key search in context configuration - Rich Text Field corruption when updated by multiple SIL post-functions - Fixed time zone handling in Date fields |