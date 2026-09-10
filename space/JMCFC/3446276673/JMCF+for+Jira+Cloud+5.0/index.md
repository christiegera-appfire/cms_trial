# JMCF for Jira Cloud 5.0

This version, released on December 17, 2024, includes the following changes:

## Custom Fields

### Formatters for custom fields

![JMCFC-Formatters.png](/cms_trial/assets/9624ce3a-bb16-47fe-adb3-e509b28b28d2.png)

It is now possible to control the display format of your custom fields! With Formatters, you can set various properties of your custom field values, including background and font colors, font size, and capitalization. Additionally, you can add prefixes and suffixes, and control display formats for date and datetime fields! See [Formatters](/cms_trial/space/JMCFC/1559003309/Formatters/) for more information.

### New scripted field type - date field

The custom field type [Scripted Field](/cms_trial/space/JMCFC/731676729/Scripted+Field/) has been expanded to include a new output type - date. Similar to the scripted datetime type, this calculates only a date.

### New API access to change history

The JMCF APIs have been expanded to include access to changelog data through the [Scripted Field](/cms_trial/space/JMCFC/731676729/Scripted+Field/) custom field. Two new endpoints are available - getFieldHistory and getIssueHistory. See their respective pages for more information:

- [getFieldHistory](/cms_trial/space/JMCFC/1562447291/getFieldHistory/)
- [getIssueHistory](/cms_trial/space/JMCFC/1563854403/getIssueHistory/)

## Administration

### Script editor updates

The script editors used throughout JMCF configuration pages have been updated to better use the available screen space. Editing longer scripts should now be more accessible.

## Bug Fixes

- **Performance fixes for large instances**

  - JMCF Cloud instances with a large number of custom fields are experiencing performance issues when enabling or disabling custom fields. This release makes significant improvements to performance.
- **Numeric custom fields don’t display decimals**

  - In some circumstances, custom number fields are not displaying their decimal values in Jira. This has been resolved.
- **Scripted String Collection fields do not display values in Jira**

  - In some configurations, Scripted fields that return a collection of strings are not displaying values in Jira. This has been fixed.
- **Disabling a custom field during recalculation**

  - Disabling a custom field while the field is recalculating causes the **Calculations** value to get stuck at ‘0%’ even though the recalculation has stopped. This has been fixed.
- **Search results on the Administration page incorrectly sorting by Calculation**

  - When sorting the My custom fields list by the **Calculation** column, using the Search feature causes the sorting to break. This has been resolved.
- **Updated names for custom fields are not reflected on the ‘Calculations’ page**

  - After updating the name of a custom field, the Calculations page would sometimes fail to update the name. This has been resolved.
- **‘Post migration’ page date filters not working correctly**

  - The TO date filter on the Post migration page was not filtering migrations correctly. This has been resolved.
- **The ‘My custom fields’ page is blank when using the Safari browser**

  - This has been resolved.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!

|  |  |
| --- | --- |
| **Release date** | December 17, 2024 |
| **Highlights** | - Custom field formatters! - New scripted field type - date fields - getFieldHistory and getIssueHistory APIs - Bug fixes |
| **Tags** | ADMINIStration custom fields UI bug fixes |