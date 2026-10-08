# Create a project template from an existing project

## Overview

When teams need multiple Jira projects with the same configuration, recreating each project and its settings manually can be time-consuming and prone to inconsistencies.

With Configuration Manager for Jira (CMJ) Cloud, you can use an existing project as a template. Create a snapshot of the project and its configuration, then reuse that snapshot whenever you need to create another project with the same setup.

This is useful when you have a standard project configuration that you want to reuse across teams, departments, or other parts of your organization.

<https://app.arcade.software/share/fyvze5pPs1Fpq7tjocNv>

## Create a snapshot of your template project

Start with a Jira project that has the configuration you want to use as your template.

1. In your Jira Cloud site, go to *Apps > Configuration Manager > Snapshots*.
2. Click **New snapshot**.
3. On the *New snapshot* page, select **Specific elements**.
4. Enter a name for the snapshot. Use a name that makes the template easy to identify later.
5. Click **Select**, then select the Jira project you want to use as your template.

   ℹ️ You only need to select the project. CMJ automatically includes the configuration elements required by the project as dependencies.
6. Click **Next**.
7. Enter a description for the snapshot. You can use the description to explain what the template is intended for or when it should be used.
8. Optionally, add a label to make the template easier to find in your snapshot list.
9. Click **Take snapshot**.

When snapshot creation is complete, CMJ opens the *Snapshot Summary* page.

Review the *Summary* and *Scope* tabs to confirm that the project and its required configuration elements are included. Your snapshot is now ready to be used as a project template.

## Use the template

When you need another project based on this configuration, deploy the template snapshot and configure the new project during the deployment.

See [Deploy a snapshot](/cms_trial/space/CMJC/2507112493/Deploy+a+snapshot/) for the complete deployment workflow.