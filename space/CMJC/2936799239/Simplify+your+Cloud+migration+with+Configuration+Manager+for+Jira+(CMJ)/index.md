# Simplify your Cloud migration with Configuration Manager for Jira (CMJ)

## Overview

Migrating from Jira Data Center to Jira Cloud is not a single technical event. It is a structured process that starts with understanding your current environment, continues through careful preparation and validation, and extends into long-term Cloud governance.

![Cloud Ready.png](/cms_trial/assets/d86c3438-978a-41c0-8630-993013347e71.png)

This guide brings together all migration-related use cases where **Configuration Manager for Jira**, **Power Admin for Jira**, and **Integrity Check for Jira** add value. It is intended to act as a single reference point for customers, partners, and support teams involved in the Cloud Ready program.

Rather than treating each app in isolation, this page explains how they support specific phases of the migration journey, from early assessment through to ongoing Cloud management.

## 1. Assessment and inventory

Every successful migration starts with a clear understanding of the existing Jira Data Center environment. This phase focuses on uncovering configuration complexity, identifying risks, and assessing overall readiness for Cloud.

Power Admin for Jira [provides visibility into projects, schemes, and shared configurations](https://appfire.atlassian.net/wiki/spaces/PA/pages/197822530), making it easier to understand where configuration sprawl exists and which elements are no longer in active use. This insight helps teams identify early candidates for cleanup or consolidation.

As part of the assessment process, Configuration Manager for Jira can also be utilized. It can capture a configuration snapshot of the current Jira Data Center instance before any cleanup truly begins. This snapshot serves as a fixed reference point that allows teams to confidently review and measure the impact of their assessment and preparation work, such as removing unused configurations or standardizing schemes.

By preserving a clear “before” state, teams can make informed cleanup decisions, demonstrate progress to stakeholders, and carry a trusted baseline forward into later migration and validation phases.

**Which app helps here?**

[Power Admin for Jira](https://marketplace.atlassian.com/apps/1219634/power-admin-for-jira?hosting=datacenter&tab=overview) supports inventory and analysis of projects and configurations.  
[Configuration Manager for Jira](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=datacenter&tab=overview) captures baseline configuration snapshots for assessment and comparison.

## 2. Migration planning

Migration planning is where teams decide how the move to Cloud will be executed, while remaining flexible enough to adapt as new information emerges.

At this stage, organizations typically define ownership, scope, milestones, and communication paths. The goal is not to document every technical detail, but to ensure alignment between stakeholders and to set realistic expectations.

Configuration Manager for Jira supports planning by encouraging a configuration-first mindset. Instead of focusing only on projects, teams can determine which configurations should move to Cloud, which should be redesigned, and [which can be retired entirely](https://appfire.atlassian.net/wiki/spaces/CMJ/pages/198116356). This helps reduce unnecessary migration effort before work begins.

**Which app helps here?**

[Configuration Manager for Jira](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=datacenter&tab=overview) helps teams decide what configuration should move, change, or be retired as part of the migration plan.

## 3. Migration preparation

Migration preparation is where the majority of migration risk is removed. Before any data is moved, Jira Data Center should be cleaned, standardized, and stabilized.

Integrity Check for Jira [identifies configuration errors](https://appfire.atlassian.net/wiki/spaces/ICJ/pages/198475963) and invalid references that may not be immediately visible but can cause migration failures or incomplete results. Resolving these issues early ensures the environment is technically safe to migrate.

Power Admin for Jira enables [bulk cleanup and standardization](https://appfire.atlassian.net/wiki/spaces/PA/pages/2623602849), allowing teams to remove unused configurations and align projects to shared schemes. This simplifies the migration itself and improves the long-term health of the Jira instance.

Once preparation is complete, Configuration Manager for Jira can be used to capture [clean and approved configuration snapshots](https://appfire.atlassian.net/wiki/spaces/CMJ/pages/197857347). These snapshots act as authoritative references for later validation.

**Which app helps here?**

[Integrity Check for Jira](https://marketplace.atlassian.com/apps/1212168/integrity-check-for-jira?hosting=datacenter&tab=overview) detects and helps resolve configuration errors on Data Center.  
[Power Admin for Jira](https://marketplace.atlassian.com/apps/1219634/power-admin-for-jira?hosting=datacenter&tab=overview) supports cleanup, consolidation, and standardization.  
[Configuration Manager for Jira](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=datacenter&tab=overview) captures approved configuration states before migration.

## 4. Test migration

A test migration allows teams to validate assumptions and identify issues before production users are affected. It turns migration from a one-time event into a repeatable, controlled process.

Using the Jira Cloud Migration Assistant (JCMA) or the Configuration Manager Cloud Migration Tool (CMT), teams can perform trial migrations and surface warnings or errors early. By transferring Data Center configurations to a Test Jira Cloud site, teams gain clear visibility into what migrated successfully, what changed due to Cloud differences, and where gaps or adjustments are required.

Issues discovered during the test migration are significantly easier and safer to resolve than those found after go-live.

**Which app helps here?**

[Configuration Manager Cloud Migration Tool](https://marketplace.atlassian.com/apps/1224900/configuration-manager-cloud-migration-tool?hosting=datacenter&tab=overview) can transfer your Data Center configurations to your Test Jira Cloud site to validate these test migrations.

## 5. Production migration

The production migration is the execution of everything planned, prepared, and validated in the earlier phases. At this stage, the primary focus is on minimizing disruption for end users while ensuring that configuration and data are migrated accurately and completely.

There are two common ways to approach the production migration. The first is to follow the same process used during [Test migration](#Test-migration), but target the Production Jira Cloud site instead of the Test site. This approach is preferred if teams want to repeat a known, validated process end-to-end and are comfortable running the migration steps again in production.

Alternatively, teams can use Configuration Manager for Jira Cloud to promote configuration changes that were already applied and validated in the Test Cloud environment into the Production Cloud environment. This approach allows teams to [deploy known fixes and adjustments without reintroducing unnecessary variability](/cms_trial/space/CMJC/2890924061/Test+and+deploy+Jira+configuration+changes+safely/), reducing both risk and manual effort.

**Which app helps here?**

[Configuration Manager Cloud Migration Tool](https://marketplace.atlassian.com/apps/1224900/configuration-manager-cloud-migration-tool?hosting=datacenter&tab=overview) can be used to migrate configurations from Data Center to a Production Jira Cloud site.

[Configuration Manager for Jira Cloud](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) supports production migration by promoting validated configuration changes to production and verifying post-migration results.

## 6. Cloud management after migration

Migration is done, but maintaining your new Jira Cloud site is an ongoing effort. Cloud environments evolve continuously, and without governance, configuration drift can quickly reintroduce risk.

Configuration Manager for Jira Cloud enables teams to [manage configuration changes between two Cloud sites](/cms_trial/space/CMJC/2890924061/Test+and+deploy+Jira+configuration+changes+safely/) safely after migration. It supports controlled updates, automation, and auditability, helping organizations maintain a stable and scalable Cloud environment as usage grows.

This phase ensures that the benefits of migration are sustained over time.

**Which app helps here?**

[Configuration Manager for Jira Cloud](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) supports ongoing configuration management and change control in Cloud.

## Support

Want more guidance with your migration to Cloud? Learn how we can support you [here](https://appfire.com/atlassian-cloud-migration-guidance).

Request a demo / [Request support](https://appfire.atlassian.net/servicedesk/customer/portal/11/group/1236/create/1918)