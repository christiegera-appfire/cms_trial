# Safely deploy JSU workflow automation across Jira Cloud instances with CMJ Cloud

---

|  |  |
| --- | --- |
| **Goal** | Copy workflow automations from one Cloud instance to another Cloud instance. |
| **Scenario** | You want to migrate **Jira Suite Utilities (JSU)** automations from one Jira Cloud instance to another Cloud instance without manually copying the configurations. |
| **Components** | **Configuration Manager for Jira (CMJ)**, JSU workflow post functions, conditions, or validators.  **Note**: Migration of JMWE Actions (Event-based, Scheduled, or Shared) is not currently supported using CMJ. |
| **Scope** | - Configuration Manager for Jira is installed on both instances. - The workflows containing the JSU automations exist on both the source and target instances. |

Picture this: you are using **Jira Suite Utilities (JSU)** and already rely on it to build powerful workflow automations in Jira Cloud. As those workflows evolve and their functionality is requested in other projects, your team needs a reliable way to move them between environments, such as promoting tested changes to production, standardizing automation across multiple Jira sites, or even supporting larger platform migrations.

**Configuration Manager for Jira (CMJ) Cloud** provides a safe and easy way to move workflows that include **JSU** configurations between Jira Cloud instances. Instead of manually recreating automation or risking configuration drift between environments, teams can package and deploy their workflows in a controlled and repeatable way.

---

## Why CMJ Cloud

**CMJ Cloud** is designed to safely move Jira configuration between environments, including workflows enhanced by popular marketplace apps such as **JMWE** and **JSU**. By understanding how these apps structure their configuration, **CMJ Cloud** can deploy workflows without breaking references, overwriting important scripts, or requiring manual fixes after deployment.

For customers already using **JSU**, **CMJ Cloud** unlocks a faster, safer, and more scalable way to manage Jira Cloud changes across environments.

---

## JSU App Support

**JSU** workflows often include deeply nested rules and multiple Jira object references. CMJ Cloud handles this complexity automatically.

When exporting **JSU** configurations, **CMJ Cloud** preserves the full structure of the workflow rules. During deployment, it intelligently updates Jira object references — such as custom fields — so the workflow functions correctly in the target environment.

This allows teams to migrate even advanced **JSU** automation without simplifying or rebuilding their rules.

**Benefits:**

- Deploy complex **JSU** workflows without manual effort
- Maintain workflow logic and structure across instances
- Ensure correct field and object mapping every time

---

## Step-by-step guide

**CMJ Cloud** provides built-in support for deploying workflows that include **JSU** app data as part of its standard migration and deployment process. When exporting configurations, **CMJ Cloud** captures the full workflow structure, including app-specific settings. During deployment, it intelligently remaps Jira object references so that workflows align with the target environment.

The following step-by-step guide shows just how easy the whole process is.

1. [Install](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/194183182) and [license](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) [**CMJ Cloud**](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on your Jira Cloud instances. You’ll need a valid license for both sites you want to move data between.
2. [Create a snapshot](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/2506522887) in the source Jira Cloud instance and include the projects that contain workflows modified by **JSU**. **CMJ Cloud** automatically captures the associated workflow configurations and app data as part of the snapshot.
3. Review the snapshot to ensure all relevant configuration items are included. No additional app-specific adjustments are required.
4. [Deploy the snapshot](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/2507112493) to the target Jira Cloud instance using the standard **CMJ Cloud** deployment process. During deployment, **CMJ Cloud** remaps object references and applies the workflow configuration while preserving protected target-side customizations.

<https://appfire.wistia.com/medias/e3u7xci8jl>