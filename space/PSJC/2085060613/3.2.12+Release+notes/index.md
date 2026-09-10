# 3.2.12 Release notes

**Release date**: June 9, 2025

Our team is thrilled to announce the latest release of Power Scripts for Jira Cloud.

This release adds configurable buttons to the Forms and Wizards feature, providing multiple entry points to different forms or wizards within Jira issues. It also introduces some bug fixes.

---

## Enhancements

### Configurable buttons for Forms and Wizards

The [Forms and Wizards](/cms_trial/space/PSJC/1839235096/Forms+and+Wizards/) feature now supports configurable buttons that provide multiple entry points to different forms or wizards within a single Jira issue panel. This enhancement enables administrators to organize complex actions into intuitive, purpose-specific options, enabling users to quickly access the right form for their specific needs.

Each button opens its own fully configured form or multi-step wizard, making it possible to present multiple related actions in an organized, user-friendly interface without overwhelming your Jira users with a single complex form.

---

## Bug fixes

The following bugs are fixed in this release:

- Resolved an issue with `autotransition()` function not accepting transition names as parameters when workflow conditions are present on the transition.
- Resolved an issue where the Power Scripts container became significantly slow, affecting page responses and script execution, when aliases were not properly detected after manual modifications to the `sil.aliases` file, causing the SIL Manager to become unresponsive. The fix improves overall system performance by replacing frequent automatic `sil.aliases` file refresh with manual reload options:

  - Added `admReloadCustomFieldAliases()` function;
  - Manual reload option by using the **Reload aliases** icon in SIL Manager > SIL Aliases panel.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-script-automation?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Power Scripts for Jira Cloud!

---