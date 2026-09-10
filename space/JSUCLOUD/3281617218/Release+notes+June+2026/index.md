# Release notes June 2026

**Release date**: June 3, 2026

This release includes updates to JSU Automation Suite for Jira Workflows.

This release note covers JSU Cloud version `8.0.0`.

---

## Enhancements

## In-progress executions on the execution log

The [Execution log](https://support.appfire.com/space/JSUCLOUD/138149902/Execution+Log) now shows rule executions that are still in progress, in addition to successful and failed runs. Use this view on **Reporting** > **Execution log** to spot stuck automations and investigate workflows that did not complete.

## Clearer execution log messages

Execution log entries now include clearer messages for rate limiting and common configuration mistakes. Check the [Execution log](https://support.appfire.com/space/JSUCLOUD/138149902/Execution+Log) when a rule fails without an obvious cause.

## %%CURRENT\_USER%% in comments with other text

In the [Update Any Issue Field post function](https://support.appfire.com/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function), you can combine `%%CURRENT_USER%%` with other text when adding a comment (for example, to mention the user who triggered the transition). Enter the parameter alongside your comment text in **Field value**.

## Workflow editor links use the new Jira editor

Create and edit links in the JSU interface now open the new Jira workflow editor instead of the legacy editor, matching Atlassian's direction for workflow management.

## Simplified conditions and validators builder

The conditions and validators builder no longer shows an unneeded ELSE branch or the Condition passes/fails message, reducing confusion when you configure rules in the Universal Rule Builder or classic configuration screens.

## Space admin access to dedicated company-managed workflows

Space admins can now add and change JSU rules on a company-managed space when they are Space administrator for that space and that space's workflow is not shared with other projects. Open [My workflows](https://support.appfire.com/space/JSUCLOUD/195821774/View+and+manage+workflow+rules) to manage rules for spaces you administer.

## Realtime in-app notifications

JSU now uses realtime APIs for in-app notifications instead of polling, so status updates appear without delay.

## Infinite loop detection counter

JSU uses an updated counter for [infinite loop detection](https://support.appfire.com/space/JSUCLOUD/256770940/Infinite+loop+detection), improving reliability when post functions trigger each other repeatedly.

---

## Bug fixes

The following fixes are included in this release:

- **Universal Rule Builder:** Resolved issues where the builder sometimes got stuck showing a loading state, did not display the transition destination, did not show custom validator messages, listed no statuses for Trigger a Linked Transition, and flickered when opening post function configuration for the first time in a session. See the [Universal Rule Builder](https://support.appfire.com/space/JSUCLOUD/12517805/Universal+Rule+Builder) documentation.
- **Copy Value From Other Field:** Resolved issues where ‘create version if necessary’ option did not work, watchers could not be copied to another field, and Perform as User reverted to the JSU Add-On User when you reopened the configuration. See [Copy Value From Other Field post function](https://support.appfire.com/space/JSUCLOUD/12518474/Copy+Value+From+Other+Field+post+function) and [Perform As User](https://support.appfire.com/space/JSUCLOUD/12518776/Perform+As+User).
- **Update Any Issue Field:** Resolved an issue where the Organization field was not updated correctly. See the [Update Any Issue Field post function](https://support.appfire.com/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function).
- **Related issue status (conditions and validators):** Resolved an issue where IS NOT, AND NOT, and OR NOT operators were evaluated against each related issue individually instead of as a group.
- **Field value (conditions and validators):** Resolved issues with empty and not empty operators not saving or displaying correctly, not empty checks failing in some cases, inability to clear Assignee/Approvers/Reviewers values, the Ignore time of day checkbox resetting when you reopened Date expression rules, and the Validate each line separately option not applying for Regular expression rules.
- **Create linked issue:** Resolved an issue where creating a linked issue with the Epic issue type did not work.
- **Priorities:** Resolved a permissions issue that blocked access to the priorities endpoint in some configurations.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JSU!