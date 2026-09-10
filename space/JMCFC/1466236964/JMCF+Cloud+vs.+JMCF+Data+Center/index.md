# JMCF Cloud vs. JMCF Data Center

Last updated October 31, 2025.

**JMCF for Jira Cloud** shares many features with the original JMCF for Jira Server/Data Center; however, **JMCF for Jira Cloud** does not yet have full parity with the features available on Data Center. The lists below detail the differences between the two platforms.

**Note**: Due to the difference in supported scripting languages between Jira Data Center and Jira Cloud, scripted custom fields will need to be manually recreated; ***scripts will need to be rewritten in JavaScript***.

## Custom Fields

| **Custom Field Type** | **Cloud** | **Data Center** |
| --- | --- | --- |
| Last Field Change Time | ✅ | ✅ |
| Last Field Changed by User | ✅ | ✅ |
| Parent Status | ✅ | ✅ |
| Status Entered by User | ✅ | ✅ |
| Status Entered Time | ✅ | ✅ |
| Time in Status | ✅ | ✅ |
| Transition Time | ✅ | ✅ |
| Transitioned by User | ✅ | ✅ |
| Transitioned by Users | ✅ | ✅ |
| Transition Count | ✅ | ✅ |
| Scripted Date | ✅ | ✅ |
| Scripted Date/Time | ✅ | ✅ |
| Scripted Duration | ❌ | ✅ |
| Scripted Group | ✅ | ❌ |
| Scripted Labels | ❌ | ✅ |
| Scripted Multi-select | ❌ | ✅ |
| Scripted Multi-user | ✅ | ✅ |
| Scripted Number | ✅ | ✅ |
| Scripted Single-select | ❌ | ✅ |
| Scripted Single-user | ✅ | ✅ |
| Scripted Text/HTML | ❌ | ✅ |
| Scripted Text (**No HTML**) | ✅ | N/A |
| Scripted Wiki Text | ❌ | ✅ |

## Jira Search Templates

**JMCF for Jira Data Center** includes custom search templates for its fields. **JMCF for Jira Cloud** does not currently include its own custom search templates, but it is possible to use the Forge custom field searcher (Figure 2, right). Future updates will include expanded options as the Jira Forge team releases additional functionality.

JMCF for Jira Cloud uses the Jira native data types, so fields are generally searchable using basic search. However, JMCF Cloud is not as flexible in terms of how to display fields or search using alternate units.

## Field Formatting

Some formatting options for custom fields are available in Jira Data Center, but any formatting options that have been applied will not transfer during migrations. JMCF for Jira Cloud includes [Formatters](/cms_trial/space/JMCFC/1559003309/Formatters/) for changing the appearance of custom fields, but these options are controlled and stored differently and therefor cannot be migrated automatically.

## JMCF Administration

The Administration pages for each product vary based on the capabilities of each of the platforms.

| **Administration Page** | **Cloud** | **Data Center / Server** |
| --- | --- | --- |
| [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) | ✅ | ❌ |
| [Calculations](/cms_trial/space/JMCFC/465633417/Calculations/) | ✅ | ❌ |
| [Error Logs](/cms_trial/space/JMCFC/465436864/Error+Logs/) | ✅ | ❌ |

![Jira Misc Custom Fields (JMCF) Cloud native UI custom field interface](/cms_trial/assets/242b3019-5ec3-4a95-87e1-caaaa541c436.png)