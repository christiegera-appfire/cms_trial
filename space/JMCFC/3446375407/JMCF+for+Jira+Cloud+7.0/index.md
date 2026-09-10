# JMCF for Jira Cloud 7.0

 This version, released on June 23, 2025, includes the following changes:

![runsOnAtlassian.png](/cms_trial/assets/67568995-23e7-4faf-9f50-904c70daf4a2.png)

JMCF for Jira Cloud now [**Runs on Atlassian**](https://www.atlassian.com/trust/marketplace?source=app-listing-badge)! Forge apps that are certified as **Runs on Atlassian** meet advanced standards for security and data management, including data residency compliance and hosting of the app within Atlassian systems.

## Custom Fields

### Time in Status Table custom field

A brand new custom field type has been added to **JMCF for Jira Cloud** - the Time in Status Table field! This field can be used to monitor total time spent in two or more statuses, and creates a table of values displaying cumulative times for each status as well as total time for all statuses. See [Time in Status Table](/cms_trial/space/JMCFC/2132509529/Time+in+Status+Table/) for more information!

### Scripted duration custom field

Scripted custom fields have been expanded to include a duration type. This scripted field type returns a duration value in seconds and can be formatted to display its values in various formats. See [Scripted Fields](/cms_trial/space/JMCFC/731676729/Scripted+Field/) for more information.

### Duration field formatters

Duration fields - [Time in Status](/cms_trial/space/JMCFC/465633373/Time+in+Status/), [Time in Status Table](/cms_trial/space/JMCFC/2132509529/Time+in+Status+Table/), and [Scripted Duration](/cms_trial/space/JMCFC/731676729/Scripted+Field/) - now include **Formatter** options. Display options include how to format the duration value, rounding, and precision settings. See [Formatters](/cms_trial/space/JMCFC/1559003309/Formatters/) for more information.

## Platform

### Data residency support

JMCF for Jira Cloud now supports Atlassian Data Residency. Long-term data in JMCF can now be limited to specific geographical regions. See [Data Residency and JMCF](/cms_trial/space/JMCFC/2132771038/Data+Residency+and+JMCF/) for more information.

## Bug Fixes

- **'Test with issue' error messages are unclear** - The **Test with issue** feature does not always return useful error messages when testing a new custom field configuration. Error messages have been improved across all custom field types.
- **Custom fields cannot be enabled when created through Jira native UI** - When a JMCF custom field is created through the native Jira custom field process, that custom field cannot be enabled through the My Custom Fields administration page. This has been resolved.
- **‘Test with issue’ not visible when editing scripted fields** - When editing a JMCF scripted field through the native UI (**Configure custom field** → **Custom field config**) the results are not visible when using the **Test with issue** feature. This has been resolved.
- **Associating screens with new custom fields is inconsistent when using the ‘All Screens’ option** - When creating a new custom field and using the **All Screens** option, the resulting custom field will occasionally miss association with some screens. This is due to rate limiting from Atlassian, but has been resolved in the method JMCF uses for fetching screens and associating new custom fields.
- **Sorting broken for some columns in administration pages** - The ‘Description’ column on the **My Custom Fields** administration page and the ‘Context’ column on the **Calculations** administration page are not sorting correctly. This has been resolved.
- **Formatters preview for date and datetime fields do not match configuration** - The preview displayed in the Formatters configuration screen for the Time Zone setting does not match the configuration selected (e.g. when selecting UTC, the preview displays GMT). This has been resolved.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!

|  |  |
| --- | --- |
| **Release date** | June 30, 2025 |
| **Highlights** | - Time in Status Table custom field - Scripted duration custom field - Data residency support added - Bug fixes |
| **Tags** | custom fields platform bug fixes |