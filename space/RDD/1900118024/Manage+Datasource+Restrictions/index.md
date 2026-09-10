# Manage Datasource Restrictions

## Overview

Learn how to fine-tune your instance to have the best performance, based on your unique way of working.

## Allowlist

Control where your data comes from with three levels of restriction: **Disabled** (no restrictions), **Internal Only** (block all external sources), and **Allowlist** (permit only approved domains).  
Ideal for securing data access in environments that require strict control over external connections.

![Dashboard Hub datasource allowlist setting](/cms_trial/assets/419a9a4b-b44a-445b-b203-1cd87c440dd0.png)

Read everything you need to know in the dedicated page: [Configure Datasource Allowlist Settings](/cms_trial/space/RDD/1687716085/Configure+Datasource+Allowlist+Settings/)

## Restrict Datasource Creation

Control who can create datasources across your organization. Restrict creation to specific users or groups to prevent unauthorized connections. Ideal for maintaining **governance and reducing the risk of exposing sensitive data.**

![Dashboard Hub restrict datasource creation setting](/cms_trial/assets/16e7d854-5167-4b30-a883-a37975eda0c5.png)

Read everything you need to know in the dedicated page: [Manage Restrictions on Datasource Creation](/cms_trial/space/RDD/1798045983/Manage+Restrictions+on+Datasource+Creation/)

## Restrict Owner View Mode

By default, datasources like “This Jira Instance” use the Owner view mode, where the gadget uses the dashboard owner’s permissions to load data, ensuring a consistent view for all users viewing the dashboard. If you enable this restriction, the **Owner view mode will be replaced by the Viewer mode**.

Then, gadgets will display data according to the permissions of the person viewing the dashboard. Users without access to certain fields/projects **will not see restricted data**. Read more about [Viewing Modes here](/cms_trial/space/RDD/146309943/Learn+about+datasources/).

This configuration reduces the risk of unauthorized visibility. And it’s important to note that it does **not** apply to datasources using credentials (e.g., password or token).

## See also