# JMCF for Jira Cloud 3.0

This version, released on September 26, 2024, includes the following changes:

## Administration

### Enhanced context settings

![changelog-CustomFieldContext.png](/cms_trial/assets/b583bb9e-ee46-4de3-8a9a-f235b3bc357b.png)

When creating and editing custom fields, context settings can now be explicitly set within the JMCF [Create Custom Field wizard](/cms_trial/space/JMCFC/465405703/Create+Custom+Field/). This includes designating specific projects and issue types for the custom field when you create them!

### Improved ‘My Custom Fields’

The [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) administration page has been enhanced with additional information about your custom fields, including context information and better visibility of enabled and disabled fields.

## Custom Fields

### Expanded API access to related issue data

API access to issue data has been greatly expanded! In addition to accessing field values of the current issue within scripted fields, it’s now possible to access field values from related issues - including Parent, Child, and Linked issue fields! See the [APIs section](/cms_trial/space/JMCFC/1325596783/APIs/) for more information.

### Automatic Dependency Detection

Scripted fields have been further updated to include automatic dependency detection for issue fields and properties! **JMCF for Jira Cloud** will now scan your script and detect any dependencies it includes; for field dependencies, it will trigger an automatic recalculation of the dependent field. You will no longer need to set dependencies manually, and any existing fields will be updated to utilize the new feature!

---

## Bug fixes

The following bugs are fixed in this release:

- **Scripted fields do not display correctly on new issues** - In some instances, scripted field values are not displayed or show incorrect values when viewing a newly created issue. New issues should now display custom field values correctly.
- **Recalculating custom fields incorrectly shows a warning** - The ‘My Custom Fields’ administration page incorrectly displays a warning for recalculating fields, even when the field results are displayed correctly within issues. This has been resolved.
- **Deleted issues prevent recalculations from completing** - In some instances, deleting an issue after a recalculation begins but before the deleted issue’s value is recalculated causes the recalculation to hang and not complete. This has been resolved.

---

|  |  |
| --- | --- |
| **Release date** | September 26, 2024 |
| **Highlights** | - Enhanced context settings - Expanded API access to linked issue data - Automatic dependency detection for scripted fields - Updated ‘My Custom Fields’ administration - Various Bug Fixes |
| **Tags** | CUSTOM FIELDS ADMINISTRATION UI BUG FIXES |