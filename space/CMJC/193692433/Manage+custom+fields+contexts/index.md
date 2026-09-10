# Manage custom fields contexts

## Custom field context deletion

We aim to manage custom field contexts and their options with maximum precision as possible during the:

- **cloud-to-cloud** Jira configuration deployments, and
- **server-to-cloud** Jira migrations.

Yet, sometimes, you might face the following error in the **Analyze** phase of the migration/deployment wizard:

`'Custom field context with id 'context_id' and name 'context_name' will be deleted with its options from the destination. Deletion will cause a loss of the option values in issues. See how to resolve this case in our documentation.'`

In these cases, the migration stops with the error above. To prevent the deletion case and error from occurring, you’ll need to configure the contexts in your Jira systems.

This page explains how we evaluate the source and destination contexts to find out if they match. This will give you the tools to avoid such situations.

## How Configuration Manager evaluates and matches source and destination

For each custom field, Configuration Manager for Jira (CMJ) Cloud exports the contexts of the projects in the deployment/migration scope. These are either the global contexts or the contexts for the projects in the migration/deployment scope.

The contexts in the deployment/migration scope don't contain references to projects outside the scope. Even if such are present on the source Jira instance, CMJ Cloud won't include them in the deployment/migration.

### What happens if a context must be deleted from the destination?

More specific is the situation when a context with references to multiple projects needs to be deleted from the destination Jira Cloud during the deployment. In that case, CMJ Cloud removes only the references to the projects in the migration/deployment scope.

While comparing the source and target contexts, you identify them by the projects they are assigned to. Suppose we have a source context assigned to projects A, B, and C. On the destination, we have a context assigned to projects C, D, and E.

You start a migration/deployment, add projects to it, and that source context ends up inside the scope. CMJ Cloud compares the source and destination contexts in the analysis phase. It identifies that project C is assigned to both source and destination contexts. The app removes project C from the destination context and adds the source context as a new context for projects A, B, and C to the destination.

The problem comes when you have a destination context, and all its projects are present in a source context. Then, CMJ Cloud attempts to execute its logic from above to remove the source projects from the destination context. This leaves the destination context without any projects, and it automatically becomes a global context. CMJ Cloud can't let that happen on the destination, as a project can have only a single global context. That's why it stops the deployment on the Analyze changes phase and shows you the error about the potential consequences of deletion.

Global contexts are never deleted from the destination Jira sites, which may affect many projects.

## How to resolve the context deletion error

If the context deletion works for you, we recommend removing the context from the custom fields it's assigned to on the destination Jira Cloud manually.

Remember that deleting a context is an issue only for custom fields with options. It's a problem as the values of the options in issues will be gone together with the context.

If deleting the context isn't an option for you, we recommend making adjustments to the source Jira instance. You need to make sure the projects you're deploying/migrating won't cause such an error. Refer to the logic we explained in the previous section when making the changes to the source instance.