# Release notes April 2026

**Release date**: April 29, 2026

Our team is pleased to announce the latest release of JSU Automation Suite for Jira Workflows.

This release note covers JSU Cloud version `7.0.0`.

---

## New Features

## Team-managed spaces support!

![image-20260402-130712.png](/cms_trial/assets/f395368a-de92-489b-84f8-bea5a97326ad.png)

**JSU** now supports Team-managed spaces! Space managers can now create JSU automations - including post functions, conditions, and validators - without the assistance of a Jira administrator. All features of JSU are available in team-managed spaces, and the process for adding an automation is no different from that of working with Company-managed projects.

## JSU migrations now support Jira 11 using JCMA

Atlassian now supports **Jira Cloud Migration Assistant (JCMA)** on Jira 11 (see the [release notes for version 1.12.55-jira-11](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant/version-history?versionHistoryHosting=dataCenter)). This update includes support for using JCMA to migrate JSU from a Data Center instance running Jira 11 to a Jira Cloud instance.

## Enhancements

## JSU now entirely on Forge

Starting with version 7.0.0, JSU has completed its migration to Forge and now runs entirely on that platform. The overall look and feel of JSU, as well as the way it works, remains largely unchanged.

**Note**: This version of JSU is Forge-compatible, but it does include data actions on remote systems. It does not qualify as Runs on Atlassian. Additionally, JSU does not support data residency with this release.

This upgrade was required as part of Atlassian’s transition away from Connect. Because Atlassian is ending support for Connect apps within a defined timeframe, JSU needed to migrate to Forge to remain supported and aligned with Atlassian platform requirements.

There are a few minor differences between the previous Connect version and the new Forge version:

- The **Hints & Tips** help banner will no longer appear on Jira workflow pages.
- JSU will no longer display reminders to publish workflows after changes have been made. You’ll need to use Jira’s native process to publish updated workflows.

**Important:** If you are currently in the middle of a migration and already tested JSU using an earlier version before this Forge release, retest your migration with version 7.0.0. This helps ensure your validation reflects the current Forge-based version of JSU. You can also [contact Appfire Support](https://appfire.atlassian.net/servicedesk/customer/portal/11/group/1236) so we can help you review the best approach for your migration.

Please review your [Settings](/cms_trial/space/JSUCLOUD/12519472/Navigation+basics/) in JSU to verify that they are correct! The **Hints & Tips** setting has been removed, and all other settings have been cleared. This was necessary because of an infrastructure change in how JSU installations are identified in Forge.

After the upgrade, review and reconfigure your JSU settings before continuing with workflow changes or migration testing.

We’re making every effort to keep this transition smooth, but we recommend thorough testing before completing your production migration.

## ‘Field Required’ validator now supports Linked Issues field

The Field Required validator now supports validations against the Linked Issues field; previously, this field was not available for validation due to platform constraints. Administrators can now ensure that at least one linked issue exists before enabling a transition!

## Number of logs display option in Execution Logs

The Execution logs page has been updated to include a dropdown to select the number of logs to display at one time. The option is displayed at the bottom of the list of logs.

## Bug fixes

The following fix is included in this release summary:

- **‘Related Issue Status’ Conditions and Validators do not recognize when there are no children present:** Resolved an issue where some configurations of the ‘Related Issue Status’ conditions and validators prevented transitions for work items that have no child issues.
- **‘Update Any Issue Field’ panel disappears**: Resolved an issue where the Information panel describing JSU behavior disappears when specific special characters are entered in **Field Value**.
- **Universal Rule Builder tooltips continue to display**: Resolved an issue where the tooltips for the Universal Rule Builder continue to display when creating a new rule, even after they have been dismissed.
- **Incorrect issue relation values in rule configuration**: Resolved a display issue in the **Related issue status** rule where configuration of one row under Issue relation would change the displayed configuration of all other rows.
- **Various UI fixes:** Several minor display issues, including incorrect links on the **Get Started** page, spacing between components, and incorrect labels in the Universal Rule Builder, have been resolved.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JSU!

|  |  |
| --- | --- |
| **Release date** | February 5, 2026 |
| **Highlights** | - Improved related issue relations for conditions and validators |