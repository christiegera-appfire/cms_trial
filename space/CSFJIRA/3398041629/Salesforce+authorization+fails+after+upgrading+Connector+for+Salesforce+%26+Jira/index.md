# Salesforce authorization fails after upgrading Connector for Salesforce & Jira

## Overview

Following an upgrade of the **Connector for Salesforce & Jira**, existing Salesforce connections may stop functioning correctly even though they continue to appear as **Authorized** in the plugin configuration.

This behavior has been observed when upgrading from **2.1.19-jira-10** to higherversions.

## What you can experience

After upgrading the plugin, all Salesforce integrations may initially continue to function as expected. However, after some period of time, Salesforce operations may begin to fail.

- Salesforce connections continue to display an **Authorized** status in the administration UI.
- Attempts to perform actions that require connection with Salesforce fail.
- Users receive the following error message:

Salesforce authorization failed, contact your administrator.

Although the connection appears to be authorized, the underlying Salesforce authorization is no longer valid.

## Why this happens

The exact trigger is currently unknown.

Based on our investigation, the behavior appears to be related to recent Salesforce security and authorization changes. After upgrading the Connector for Salesforce & Jira plugin, existing authorization tokens may eventually expire or become invalid.

When this occurs, the plugin may continue to display the connection as authorized, while Salesforce rejects requests that rely on the stored authorization.

The issue does not necessarily occur immediately after the upgrade. Connections may continue to work for some time before authorization failures begin to appear.

## Scope of the impact

This behavior can affect one or more Salesforce connections configured in the plugin.

For instances with multiple Salesforce connections, all existing connections may become affected around the same time. As a result, administrators may need to review and re-authorize each configured connection after the upgrade.

## Workaround

If a Salesforce connection shows **Authorized** but Salesforce operations fail with the message:

> Salesforce authorization failed, contact your administrator.

or similar;

perform the following steps:

1. In Jira, go to **Salesforce** > **Connections** from the top navigation bar.
2. Select **Revoke Access** for the affected connection.
3. Click **Authorize**.
4. Sign in with Salesforce credentials when prompted.
5. Verify that Salesforce operations are working correctly.

Repeat these steps for each affected Salesforce connection.

## Resolution status

As of **version 2.1.23**, we have **not been able to reproduce this issue** during our testing.

However, the underlying root cause has **not yet been identified**, so we cannot confirm that the issue has been fully resolved. If you are experiencing this behavior on an earlier version, we recommend upgrading to **version 2.1.23** or later and monitoring your Salesforce connections to determine whether the authorization failures reoccur.