# 3.2.6 Release notes

![Release Notes.png](/cms_trial/assets/26a06d5f-c311-4809-b56e-f34136080170.png)

**Release date**: December 19, 2024

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud. This release introduces some enhancements and bug fixes.

---

| **Contents** |
| --- |
| - [Enhancements](#enhancements) - [Enhanced post-function workflow migration support](#enhanced-post-function-workflow-migration-support) - [Newly added SIL functions](#newly-added-sil-functions) - [Bug fixes](#bug-fixes) |

---

## Enhancements

### Enhanced post-function workflow migration support

SIL post-functions are now automatically connected to their corresponding workflow transitions when migrating from Jira Server/Data Center to Jira Cloud using the Jira Cloud Migration Assistant (JCMA). This enhancement eliminates the need for manual reconnection of post-functions after migration, providing the following benefits:

- Seamless migration of workflow-related data.
- Automatic attachment of post-function SIL files to correct transitions.
- Reduced risk of configuration errors.
- Significant time savings during the migration process.

**Previous Behavior:** Post-function SIL scripts were copied to a *Migrated\_Post\_Functions* folder under `silprograms` and required manual reconnection to workflow transitions.

This improvement streamlines the migration process and helps ensure data integrity when moving to Jira Cloud.

### Newly added SIL functions

- `getAllAttachments`: gets attachment information.
- `getAttachmentMediaId`: retrieves an Atlassian Document Format (ADF) compatible media identifier when given an issue and its corresponding attachment ID.
- `allMatches`: enhances regular expression functionality by returning all capturing groups defined in the RegEx pattern.
- `allGroups()`: lets you bulk update group permissions.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed Group picker search functionality issue  
  Fixed an issue where the Group picker search was not properly processing user input. Previously, when searching for a specific group, the search results might not include the desired group even if it existed, as the search query was not included in the API call to Atlassian. The fix ensures that search terms are properly considered when retrieving group results.
- Fixed Power Scripts Validator wizard loading  
  Resolved an intermittent issue where the Power Scripts validator wizard would not load properly when configuring new validation rules in the workflow editor.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace. [unmapped inline: placeholder]
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think here. [unmapped inline: placeholder]

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in [unmapped inline: placeholder]!

|  |  |
| --- | --- |
| **Release date** | December 19, 2024 |
| **Highlights** | - Enhanced post-function workflow migration support - Newly added SIL functions - Fixed Group picker search functionality issue - Fixed Power Scripts Validator wizard loading wizard |