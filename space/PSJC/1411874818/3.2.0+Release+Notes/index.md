# 3.2.0 Release Notes

![Release Notes.png](/cms_trial/assets/bf283073-1797-4b64-8dee-cf8488abcfa0.png)

**Release date**: October 26, 2024

Our team is thrilled to announce the 3.2.0 release of Power Scripts for Jira Cloud. In addition to runtime upgrades, this major release brings the first add-on functionality from the Data Center to the Cloud: SIL Excel Connector functions. You can now automatically populate and update Excel files directly from Jira.

---

| **Contents** |
| --- |
| - [New features](#new-features) - [Enhancements](#enhancements) - [Bug fixes](#bug-fixes) |

---

## New features

- **Traces of the executions**:

  - Monitor all Jira API calls and view their results.
  - Gain complete visibility into your script execution flow.
  - For details, check the [Traces](/cms_trial/space/PSJC/1413677135/Request+Traces/) topic.
- **SIL Excel Connector**:

  - Allows you to create and update Microsoft Excel files.
- **Custom Field Management**:

  - Added routines to get information about the contexts of a custom field.
- **Advanced Security Features**:

  - You can now set expiration dates for API tokens and Organization API Keys and use them for temporary administrative scripted maintenance. After the specified time, the tokens are automatically removed.
  - Added hmacSHA1 and hmacSHA256 routines to use for AMZ tokens or other secure integrations.

## Enhancements

- **Consistent Time Zone Handling**

  - The time zone is now considered across all datetime operations used in SIL.
  - Once you configure the time zone from the **General > Time** menu, all SIL scripts will use it consistently.
  - This enhancement eliminates the previous inconsistencies in datetime fields.

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed InlineCards display in paragraph custom fields.
- toJson() did not treat primitive int array values correctly. Resolved JSON serialization issues with integer arrays.
- Eliminated duplicate persistent variables.
- Power Scripts admin pages sometimes needed a refresh if left open. To improve admin page loading and prevent refresh requirements, the loading of the page is now postponed until Jira’s AP function is loaded.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview&hosting=cloud).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews&hosting=cloud).

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We know we have the smartest customers & we appreciate your trust in Power Scripts for Jira Cloud!

|  |  |
| --- | --- |
| **Release date** | October 26, 2024 |
| **Highlights** | - **Major release**, runtime updated - Traces of executions - SIL Excel Connector in Cloud - Time-Zone is obeyed everywhere - Security was greatly improved |

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]