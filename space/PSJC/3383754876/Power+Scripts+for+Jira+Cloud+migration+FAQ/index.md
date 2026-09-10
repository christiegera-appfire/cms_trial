# Power Scripts for Jira Cloud migration FAQ

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

## Power Scripts for Jira: Cloud Migration FAQ

## Overview

This FAQ addresses common migration questions and known limitations when migrating Power Scripts for Jira from Jira Data Center to Jira Cloud.

Because Jira Cloud uses a different architecture and execution model than Jira Data Center, some SIL scripts, workflow automations, and advanced features may require manual review, remediation, or redesign after migration.

---

## Why do some custom field automation scripts require updates after migration?

Some Power Scripts functions that interact with Jira custom field contexts behave differently in Jira Cloud than they do in Jira Data Center.

For example, Jira Cloud custom field contexts may require specific project and issue type mappings when using functions such as **admUpdateCustomFieldOptions**. Customers have reported challenges when working with contexts that apply to all issue types, because Cloud functions may require issue type information that is not explicitly defined in the context.

As a result, scripts that update custom field options, retrieve context information, or manage field configurations can require review and testing after migration.

If your Data Center environment contains custom scripts that:

- Update custom field options
- Manage field contexts
- Retrieve issue type mappings
- Automate field configuration changes

Test those scripts in a sandbox environment before moving them to production.

For example, with the following Data Center SIL script:

```text
string cfName = "Environment";
string[] options = {"Development", "QA", "Production"};
admUpdateCustomFieldOptions(
    cfName,
    projectKey,
    issueTypes,
    options
);
```

Appfire recommends verifying the following components after migrating to the Cloud:

- The target custom field context exists in Cloud
- Issue type mappings are correctly identified
- Contexts that apply to all issue types are handled as expected
- The option updates complete successfully

### SIL aliases

If Data Center SIL scripts reference custom fields by their IDs, those references will stop working after migration because the fields will have different IDs in Jira Cloud.

After migration, all custom field script references should be modified and mapped to the correct Cloud field IDs.

Another method is to use SIL aliases instead of custom field IDs in Power Scripts for Jira Data Center. Implementing SIL aliases in your Data Center instance will simplify the Cloud migration process.

For more information on SIL aliases, please review this article:

- [Make your scripts more readable with SIL aliases](https://support.appfire.com/space/PSJ/15486340/Make+your+scripts+more+readable+with+field+aliases)

---

## Are all SIL routines supported in Jira Cloud?

No. Some SIL routines available in Jira Data Center are not available in Jira Cloud, or may behave differently.

Examples include:

- workflow automation routines
- custom field context handling
- Live Fields functionality
- direct server-side operations that are not supported in Atlassian Cloud

Before migration, review your existing SIL scripts and identify any routines that may require updates or redesign for Cloud compatibility.

[Learn more about SIL function differences between Data Center and Cloud.](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/1562869982)

---

## Do SIL scripts migrate automatically to Jira Cloud?

Scripts and configurations may migrate, but manual validation is often required.

Currently:

- There is no fully automated conversion process for all SIL functionality.
- Some scripts might need to be rewritten using Jira Expressions or JavaScript.
- Certain features might require alternative implementations in the Cloud.

After migration, administrators should test all workflows, validators, conditions, post-functions, and custom scripts.

For more information, please review these articles:

- [Jira DC to Cloud script migration reference](https://support.appfire.com/space/PSJC/1940488485/Jira+DC+to+Cloud+script+migration+reference)
- [Automated script migration](https://support.appfire.com/space/PSJC/1940488414/Automated+script+migration)

---

## Are Live Fields supported in Jira Cloud?

In Cloud, Power Scripts does not provide Live Fields functionality or configuration options. Live Fields is a separate Cloud application with its own configuration model, which differs significantly from the Live Fields functionality included in Power Scripts for Jira Data Center.

Live Fields for Jira Data Center is built using the SIL language, whereas Live Fields for Jira Cloud was developed using Atlassian-provided APIs and therefore uses JavaScript and TypeScript. As a result, existing Live Fields configurations cannot be migrated and must be recreated from scratch in Jira Cloud. Migration of Live Fields configurations from Jira Data Center to Jira Cloud is currently not supported.

For more information, please review this article:

- [Live Fields Cloud vs. Live Fields Data Center](https://support.appfire.com/space/LF/1497826781/Live+Fields+Cloud+vs.+Live+Fields+Data+Center)

---

## Is there a post-migration validation page for Power Scripts?

Currently, there is no centralized post-migration dashboard that identifies all scripts requiring remediation.

Administrators should manually:

- review migrated scripts
- validate workflow behavior
- test automation logic
- identify unsupported routines
- confirm field and context mappings

Appfire product teams are aware of this pain point and are considering future improvements.

---

## Why is manual testing required after migration?

Because Jira Cloud and Jira Data Center use different execution models and APIs, migrated scripts cannot always be validated automatically.

Manual testing helps identify:

- unsupported routines
- workflow failures
- permission issues
- context mapping problems
- performance or execution limitations

Testing should include both functional and workflow-level validation.

---

## Are there performance or memory considerations during migration?

Yes. Some customer instances can require additional memory allocation during migration activities or large-scale script validation.

Migration performance can be affected by:

- number of scripts
- workflow complexity
- custom field usage
- automation volume
- instance size

Support teams often review logs or environment statistics to help diagnose migration-related performance issues.

Power Scripts for Jira Cloud has a **Self Help** > **Engine Resize** feature that allows customers to request additional memory directly in the app when resource limits become a concern.

![Power Scripts Self Help Engine Resize feature.](/cms_trial/assets/a7b4998b-f7e7-4df5-a121-956691d5cd02.png)

For more information, please review this article:

- [Cloud performance and resources](https://support.appfire.com/space/PSJC/504004659/Cloud+Performance+and+Resources)

---

## Is there a fully automated migration solution for Power Scripts?

Not at this time.

While migration tools and processes can assist with moving configurations and scripts, customers should plan for:

- manual validation
- script remediation
- feature compatibility review
- Cloud-specific redesign where necessary

Migration readiness depends heavily on the extent to which Power Scripts features are used in the Data Center environment.

---

## What should customers do before migrating Power Scripts to the Cloud?

Before migration, Appfire recommends:

1. Inventory all SIL scripts and workflow automations.
2. Identify use of unsupported or Cloud-limited functionality.
3. Review Live Fields usage carefully.
4. Test migration in a staging or sandbox environment.
5. Plan time for post-migration validation and script updates.
6. Engage Appfire Support if large or complex environments are involved.