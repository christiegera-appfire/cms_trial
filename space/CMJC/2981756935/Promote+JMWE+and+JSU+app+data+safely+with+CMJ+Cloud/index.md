# Promote JMWE and JSU app data safely with CMJ Cloud

## Overview

Many Jira Cloud customers rely on powerful workflow apps like Jira Misc Workflow Extensions (JMWE) and Jira Suite Utilities (JSU) to automate processes, enforce governance, and reduce manual work. As Jira environments grow, teams often need to move these workflows between instances — for example, when promoting changes from test to production, consolidating instances, or supporting mergers and acquisitions.

CMJ Cloud makes it easy to move workflows that include JMWE and JSU configurations between Jira Cloud instances, helping teams standardize automation, reduce risk, and save time.

---

## The Challenge

Workflows that depend on JMWE or JSU are often complex. They can contain scripts, validators, conditions, post-functions, and deeply nested configuration data. These configurations frequently reference environment-specific Jira object IDs, such as custom fields, which differ between instances. Recreating this setup manually is time-consuming and increases the risk of configuration errors. At the same time, teams need to ensure that any intentional customizations in the target environment are not accidentally overwritten.

As a result, teams either avoid reusing proven automation or spend significant effort rebuilding workflows in each environment.

---

## The CMJ Cloud Solution

CMJ Cloud provides built-in support for deploying workflows that include JMWE and JSU app data as part of its standard migration and deployment process. When exporting configurations, CMJ Cloud captures the full workflow structure, including app-specific settings. During deployment, it intelligently remaps Jira object references so that workflows align with the target environment.

The following step-by-step guide shows just how easy the whole process is.

1. [Create a snapshot](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/) in the source Jira Cloud instance and include the projects that contain workflows modified by JMWE and/or JSU. CMJ Cloud automatically captures the associated workflow configurations and app data as part of the snapshot.
2. Review the snapshot to ensure all relevant configuration items are included. No additional app-specific adjustments are required.
3. [Deploy the snapshot](/cms_trial/space/CMJC/2507112493/Deploy+a+snapshot/) to the target Jira Cloud instance using the standard CMJ Cloud deployment process. During deployment, CMJ Cloud remaps object references and applies the workflow configuration while preserving protected target-side customizations.

---

## JMWE App Support

CMJ Cloud understands how JMWE builds workflow logic for conditions, validators, and post-functions.

During deployment, CMJ Cloud safely synchronizes JMWE-generated logic with the target environment while intentionally protecting any custom scripts or JQL already configured on the target. This ensures workflows behave consistently across environments without overwriting local customizations.

Post-functions are deployed as expected, allowing teams to reuse JMWE-driven automation with confidence.

**Benefits:**

- Reuse complex JMWE automation across environments
- Avoid manual script updates or reconfiguration
- Reduce risk when promoting workflows to production

---

## JSU App Support

JSU workflows often include deeply nested rules and multiple Jira object references. CMJ Cloud handles this complexity automatically.

When exporting JSU configurations, CMJ Cloud preserves the full structure of the workflow rules. During deployment, it intelligently updates Jira object references — such as custom fields — so the workflow functions correctly in the target environment.

This allows teams to migrate even advanced JSU automation without simplifying or rebuilding their rules.

**Benefits:**

- Deploy complex JSU workflows without manual effort
- Maintain workflow logic and structure across instances
- Ensure correct field and object mapping every time

---