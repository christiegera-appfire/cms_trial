# Data Sharing Changes for Imported Dataplane Reports

## Overview

In the current setup, data is accessed by acting as the Dashboard owner when configuring a connector or dashboard-based datasource. We aim to prioritize data integrity and security. As part of this initiative, we have implemented more restrictive access controls to determine who can view specific information.

**API-based datasources retrieve data solely based on API Key permissions,** ensuring that data is only accessible by users with appropriate access rights.

Dashboard Hub also works as a connector app, this means that you do NOT need a connector app if Dashboard Hub is already installed in the instance.

### Difference Between Connector-Based and Dashboard-Based Datasources

- **Connector-Based**: This type of datasource retrieves data by impersonating the dashboard owner, so viewers see data as if they were the owner. This potentially exposes sensitive information to viewers without permissions, since they see the data with the eyes (permissions) of the dashboard owner. Connector-based datasources retrieve data from external systems.

Read more about connectors: [Dashboard Hub Connector apps](/cms_trial/space/RDD/146309882/Dashboard+Hub+Connector+apps/)

- **Dashboard-Based**: Grants data access based on the dashboard owner’s permissions. It also displays data as if viewed by the owner, with a similar risk of exposing sensitive information. The dashboard-based datasource retrieves data from the actual instance where Dashboard Hub is installed.

### Impact of JCMA on Dataplane Reports

With the introduction of the **JCMA process** to import Dataplane reports into **Dashboard Hub**, data-sharing behavior has changed. Dataplane reports are generated based on the permissions of the user running them, which could expose sensitive data when shared with users who don’t have the same access rights.

### New Behavior for Imported Reports

To reduce the risk of exposing sensitive data, **Dataplane reports imported into Dashboard Hub will no longer be automatically shared** with other users.

- **Manual sharing** will be required for each report.
- By default, reports will only be accessible to the user who imported them.

### Why This Change?

This change is made to ensure that sensitive data is not inadvertently exposed. Reviewing and adjusting sharing settings for each imported Dataplane report is important to ensure only authorized users have access.