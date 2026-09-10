# 3.1.0 Release Notes

![Release Notes.png](/cms_trial/assets/f74a5ac5-60e3-40b9-a4f3-c9c56170aee5.png)

**Release date**: August 10, 2024

Our team is thrilled to announce the 3.1.0 release of Power Scripts for Jira Cloud. This release is a foundational release, adding support for Jira Cloud Migration Assistant (JCMA) and Configuration Manager for Jira (CMJ) while introducing script templates for cloud, too.

---

| **Contents** |
| --- |
| - [New features](#new-features) - [Enhancements](#enhancements) - [Bug fixes](#bug-fixes) |

---

## New features

- Basic support for Jira Cloud Migration Assistant (JCMA) and Configuration Manager for Jira (CMJ). For now, only workflow postfunctions may be migrated but the foundation is there.
- Script templates were introduced in cloud. BETA feature, there’s more to come
- Support for Jira Premium field 'Team'
- Organization-wide token integration
- New functions to manage your Jira. Administrative support for:

  1. Project Issue Security levels
  2. Permission schemes
  3. Priority schemes
- currentSilScript() routine to determine the current script being executed
- lastActiveDates() to determine a user’s active date

---

## Enhancements

- Minor performance enhancements.
- for security, internal libraries were upgraded

---

## Bug fixes

The following bugs are fixed in this release:

- Fixed listener on user created/updated/deleted events
- Description parameter was ignored when we used the longer signature of createCustomerRequest()
- One minor security bug on the gadget

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=overview&hosting=cloud).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?tab=reviews&hosting=cloud).

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in Power Scripts for Jira Cloud!

|  |  |
| --- | --- |
| **Release date** | August 10, 2024 |
| **Highlights** | - Basic support for CMJ and JCMA. - Script templates (BETA) - 'Team' field support - Tens of administrative routines added |

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]