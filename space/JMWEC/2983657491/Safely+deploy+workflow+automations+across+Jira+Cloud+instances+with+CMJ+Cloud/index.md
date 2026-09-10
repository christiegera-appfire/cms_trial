# Safely deploy workflow automations across Jira Cloud instances with CMJ Cloud

| **Goal** | Copy workflow automations from one Cloud instance to another Cloud instance. |
| --- | --- |
| **Scenario** | You want to migrate Jira Misc Workflow Extension (JMWE) automations from one Jira Cloud instance to another Cloud instance without manually copying the configurations. |
| **Components** | Configuration Manager for Jira (CMJ), JMWE workflow post functions, conditions, or validators.  **Note**: Migration of JMWE Actions (Event-based, Scheduled, or Shared) is not currently supported using CMJ. |
| **Baseline** | - Configuration Manager for Jira is installed on both instances. |

Picture this: you are using **Jira Misc Workflow Extensions (JMWE)** and already rely on it to build powerful workflow automations in Jira Cloud. As those workflows evolve and their functionality is requested in other projects, your team needs a reliable way to move them between environments, such as promoting tested changes to production, standardizing automation across multiple Jira sites, or even supporting larger platform migrations.

**Configuration Manager for Jira (CMJ) Cloud** provides a safe and easy way to move workflows that include **JMWE** configurations between Jira Cloud instances. Instead of manually recreating automation or risking configuration drift between environments, teams can package and deploy their workflows in a controlled and repeatable way.

---

## Why CMJ Cloud

**CMJ Cloud** is designed to safely move Jira configuration between environments, including workflows enhanced by popular marketplace apps such as **JMWE** and **JSU**. By understanding how these apps structure their configuration, CMJ Cloud can deploy workflows without breaking references, overwriting important scripts, or requiring manual fixes after deployment.

For those already using JMWE, CMJ Cloud unlocks a faster, safer, and more scalable way to manage Jira Cloud changes across environments.

---

## JMWE App Support

CMJ Cloud understands how JMWE builds workflow logic for conditions, validators, and post functions.

During deployment, CMJ Cloud safely synchronizes JMWE-generated logic with the target environment while intentionally protecting any custom scripts or JQL already configured on the target. This ensures workflows behave consistently across environments without overwriting local customizations.

Post functions are deployed as expected, allowing teams to reuse JMWE-driven automation with confidence.

**Benefits:**

- Reuse complex JMWE automation across environments
- Avoid manual script updates or reconfiguration
- Reduce risk when promoting workflows to production

---

## Step-by-step guide

**CMJ Cloud** provides built-in support for deploying workflows that include **JMWE** app data as part of its standard migration and deployment process. When exporting configurations, **CMJ Cloud** captures the full workflow structure, including app-specific settings. During deployment, it intelligently remaps Jira object references so that workflows align with the target environment.

The following step-by-step guide shows just how easy the whole process is.

1. [Install](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/194183182) and [license CMJ Cloud](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on your Jira Cloud instances. You’ll need a valid license for both the source and target sites.
2. [Create a snapshot](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/2506522887) in the source Jira Cloud instance and include the projects that contain workflows enhanced by **JMWE**. **CMJ Cloud** automatically captures the associated workflow configurations and app data as a part of the snapshot.
3. Review the snapshot to ensure all relevant configuration items are included. No additional app-specific adjustments are required.
4. [Deploy the snapshot](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/2507112493) to the target Jira Cloud instance using the standard CMJ Cloud deployment process. During deployment, CMJ Cloud remaps object references and applies the workflow configuration while preserving protected target-side customizations.

<https://appfire.wistia.com/medias/e3u7xci8jl>