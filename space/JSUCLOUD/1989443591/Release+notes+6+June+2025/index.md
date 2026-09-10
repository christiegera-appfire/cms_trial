# Release notes 6 June 2025

**Release date**: June 6, 2025

Our team is pleased to announce the latest release of JSU Automation Suite for Jira Workflows.

---

## New features

## Introducing rule builders for conditions and validators

You now have a new way to add JSU conditions and validators to your project workflows in Jira Cloud. You can build, edit, and preview your condition or validator rules from one place without navigating back to the workflow editor in Jira.

The new rule builders include 11 new conditions and validators previously available only with our Data Center app. You can use these new features to add more complex workflow rules for better control and improved compliance.

![JSU-Rule-Builder-CV-Release.png](/cms_trial/assets/beec1973-5a26-4d83-a6fb-990c0e113c35.png)

See [JSU Rule Builder - Conditions](/cms_trial/space/JSUCLOUD/1958084925/JSU+Rule+Builder+-+Conditions/) and [JSU Rule Builder - Validators](/cms_trial/space/JSUCLOUD/1973288961/JSU+Rule+Builder+-+Validators/) to get started.

## New conditions and validators

Our Data Center conditions and validators are now available in JSU Cloud. You can add one or more of the following to your transitions for better control:

- Field value (Value Field in Data Center)
- Fields required
- Issue status changed
- Related issue status
- User in field
- User in project role
- User in group
- Only selected users (formerly User is in Any User)
- Regular expression
- Compare dates
- Date expression

See [Workflow conditions](/cms_trial/space/JSUCLOUD/12518591/Workflow+conditions/) and [Workflow validators](/cms_trial/space/JSUCLOUD/12518578/Workflow+validators/) to learn more.

### What happens to my existing rules?

Previously, there was one JSU condition available in the Jira workflow editor, **User is in Any User**. If you already have rules configured with this condition, your rules will not change. If you need to edit the rule, the new dedicated version of the rule builder is available. You can recreate the rule using the **Only selected users** condition in the new rule builder if you prefer.

### What hasn’t changed?

Post functions and preconditions for post functions remain unchanged. Preconditions apply to post functions, while conditions are added to a workflow transition.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/5048/jsu-automation-suite-for-jira-workflows?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers! You are the driving force behind why we create software. We appreciate your trust in JSU!