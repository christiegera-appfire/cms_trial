# JMCF for Jira Cloud 6.0

This version, released on February 10, 2025, includes the following changes:

## Custom Fields

### Scripted fields code snippets

![JMCFC-ScriptedFieldSnippets.png](/cms_trial/assets/06ef39d9-62e2-4627-9897-0568d4184f57.png)

A number of new code snippets have been added to the [Scripted Field](/cms_trial/space/JMCFC/731676729/Scripted+Field/) roster. These snippets address some of the most common data access scenarios. See [Scripted Field Snippets](/cms_trial/space/JMCFC/1741815975/Scripted+Field+Snippets/) for more information.

### Script editor updates

The JMCF script editor has seen several updates in addition to the snippets mentioned above. The script editor console has been improved to properly show null and undefined values and to display object contents. Additionally, in-editor hover help has been expanded for functions and APIs.

### Updated broken dependency prevention

JMCF custom fields [Last Field Change Time](/cms_trial/space/JMCFC/465405628/Last+Field+Change+Time/) and [Last FIeld Changed by User](/cms_trial/space/JMCFC/465272986/Last+Field+Changed+by+User/) will no longer include other JMCF custom fields as options in the **Fields to watch** customization. This change was made to prevent broken dependencies; JMCF custom fields cannot currently monitor other JMCF custom fields, resulting in neither field correctly updating or displaying.

## Bug Fixes

- **Disabled custom fields still display in Issue view** - Disabled custom fields were still displayed in the Issue view page. This has been resolved.
- **Duplicated custom fields do not copy all configurations** - Duplicated custom fields did not always copy all configuration options from the original field. This has been resolved.
- **Scheduled recalculations do not occur** - In some circumstances custom fields were being incorrectly identified as disabled, causing scheduled recalculations to not trigger. This has been resolved.
- **‘Parent Status' custom fields show errors** - When creating a [Parent Status](/cms_trial/space/JMCFC/465600657/Parent+Status/) custom field using the native Jira UI, the field incorrectly showed an error stating that the configuration is missing. This has been resolved.
- **‘Transition count’ custom field does not increment after 40** - In some circumstances, the Transition count custom field failed to increment once it had reached 40. This has been resolved.
- **Difficulty acknowledging multiple error logs** - When acknowledging multiple error logs simultaneously, the [Error Logs](/cms_trial/space/JMCFC/465436864/Error+Logs/) page required a hard refresh to see that the logs had been acknowledged. This has been resolved.
- **New custom fields listed twice on the Calculations page** - In some circumstances, a new custom field would be listed twice on the Calculations administration page immediately after the field was created. This has been resolved.
- **Re-enabled fields do not display on the Calculations page** - When quickly disabling and re-enabling a custom field, the re-enabled field did not correctly display on the [Calculations](/cms_trial/space/JMCFC/465633417/Calculations/) page. This has been resolved.
- **Error Logs page crashes when selecting an error count**. When clicking an error count badge from [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/), the [Error Logs](/cms_trial/space/JMCFC/465436864/Error+Logs/) page opened but did not load correctly. This has been resolved.
- **UI issues when creating a new context** - Several minor UI issue were occurring after a new context was created, including the **Save** button remaining enabled, incorrect issue and project counts, and incorrect Issue types listed in the tooltip. These have been resolved.
- **Changing a formatter's timezone causes the field value to not display** - Changing a custom date field’s formatter from any timezone to the **Browser default** option caused the field’s value to not display properly. This has been resolved.
- **Formatter for number fields allows incorrect values** - The Decimal option of the formatter for number fields allowed for invalid values, causing errors. This has been resolved.
- **Selected screens displaying incorrectly when editing a custom field** - When editing an existing custom field, the associated screens did not always display correctly in the Custom Field Wizard. This has been resolved.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!

|  |  |
| --- | --- |
| **Release date** | February 10, 2025 |
| **Highlights** | - Scripted field code snippets - Script editor updates - Bug fixes |
| **Tags** | ADMINIStration custom fields UI bug fixes |