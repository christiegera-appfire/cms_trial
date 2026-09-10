# Overview

Configuration Manager for Jira (CMJ) Cloud helps you manage and deploy Jira configuration changes between Jira Cloud sites. Whether you're promoting tested changes between environments, keeping multiple Jira Cloud sites aligned, or rolling out configuration updates across teams, CMJ Cloud helps you review, validate, and deploy configuration changes with confidence.

Configuration changes are packaged into **snapshots** before they're deployed. A snapshot captures a project's configuration at a specific point in time, allowing you to review the proposed changes, analyze their impact on the destination site, and resolve potential conflicts before deployment.

## Why use CMJ Cloud?

Configuration deployments support a range of day-to-day Jira administration scenarios.

You can use CMJ Cloud to:

- promote tested changes from development or staging to production;
- standardize project configurations across multiple Jira Cloud sites;
- create new projects from a project template;
- roll out approved workflows, fields, schemes, and other settings across teams or environments to keep related Jira sites aligned as their configurations evolve.

The goal may differ, but the underlying need is the same: introduce configuration changes without rebuilding them manually or applying them without first understanding their impact.

## How deployments work

Whether you're introducing new project configurations, promoting tested changes, or keeping multiple Jira Cloud sites synchronized, CMJ Cloud helps you review and deploy configuration changes in a controlled, reliable way.

A typical deployment workflow consists of three steps:

1. **Create a snapshot** of the project whose configuration you want to deploy.
2. **Review and analyze** the snapshot to understand what will change and identify any potential conflicts.
3. **Deploy** **the snapshot** to the destination Jira Cloud site.

## Where to go next

To begin your first deployment, continue with [**Create a snapshot**](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/).

To explore the different reasons for deploying configurations and find the workflow that best matches your situation, visit [**Use Cases**](/cms_trial/space/CMJC/194117717/Use+Cases/).

To see which Jira Cloud configuration elements CMJ Cloud can deploy, refer to [**Supported configuration elements**](/cms_trial/space/CMJC/193855959/Supported+configuration+elements/).

**Migrating from Jira Server/Data Center?** If you're moving your existing Jira configuration to Jira Cloud, see the [full migration use case](/cms_trial/space/CMJC/258085727/Migrate+projects+and+issues+from+Jira+Server%2FDC+to+Jira+Cloud/) or the [snapshot upload](/cms_trial/space/CMJC/2506391642/Upload+a+snapshot/) feature.