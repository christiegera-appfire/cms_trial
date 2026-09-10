# Last Failed Pipeline

## Overview

Bitbucket Pipelines makes CI/CD easy right into Bitbucket. From automatic builds, to tests and deployments. Our dashboard hooks into your process giving the continuous visibility your team requires.

This gadget displays the last failed pipeline in real-time for any of the repositories you select to track. Gives broad and quick visibility to fails and takes actions accordingly.

Note: the failures have to be between the last 50 builds of a repository, the gadget won’t look for failed pipelines before.

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource** to connect to Bitbucket Pipelines. See [Integrations with Bitbucket](/cms_trial/space/RDD/2381316116/Integration+with+Bitbucket/) to learn more.
- The Bitbucket **repositories** where your pipelines are configured, you can select multiple repositories if needed.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration.

## Dashboards

This gadget appears in the following dashboard: [DevOps software team template](/cms_trial/space/RDD/146309250/DevOps+software+team+template/).