# Integration with Bitbucket

To connect Bitbucket data with your dashboard gadget, you need to set up your Bitbucket datasource using an API token.

As of October 1st, 2025, we will no longer support the Bitbucket Connector app. If you have already set up your datasource with the connector app, follow the [steps](/cms_trial/space/RDD/2381316116/Integration+with+Bitbucket/) [below](/cms_trial/space/RDD/2381316116/Integration+with+Bitbucket/) to reconfigure it.

## How to add a new Bitbucket datasource with an API token

## Prerequisites

- API token from Atlassian. See the Atlassian support [documentation](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/) to learn how to create the API Token. Keep a note of the token details; you will need them to set up the datasource.

API tokens created to access Bitbucket APIs must have scopes (permissions). Atlassian's documentation provides a [list of available scopes](https://support.atlassian.com/bitbucket-cloud/docs/api-token-permissions/).   
When selecting the scopes for Bitbucket, select all the *Read* scopes. This integration doesn’t require *Manage*, *Admin*, *Delete*, or *Write* scopes.

**To add a new Bitbucket datasource:**

1. In Jira, go to **Apps** > **Dashboard Hub**.
2. Click **More actions** (**…**) > **Add datasource**.
3. Select **Bitbucket** in the *Add datasource* page.
4. Follow the instructions on the Cloud tab and add the API token in the *App password* field.
5. Click **Add**.

## How to update an existing Bitbucket datasource

### Update a Bitbucket Connector App datasource

If you have configured a gadget using a datasource from the Bitbucket Connecter app, you will need to create a new datasource.

1. Follow the instructions for how to add a new Bitbucket datasource with an API token.
2. Open the dashboard that contains the gadget you want to update, then click **Edit**.
3. In the gadget panel, select **More actions (…)** > **Configure**.
4. Make a note or screenshot of the current configuration details.
5. Select the datasource you created in step 1. This will clear the current configuration settings.
6. Update the configuration with the details you saved in step 4.
7. Click **Save**, then save the dashboard.

### Update a Bitbucket app password with an API token

FromSeptember 9, 2025, Atlassian has replaced App Passwords with API tokens. If your Bitbucket datasources use an app password, follow the instructions below to update it. See Atlassian’s support [documentation](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/) to learn more about this change.

1. Create the API token following the Atlassian support documentation, then make a note of the token. You will need it in the next steps.
2. In Dashboard Hub, select **More actions (…)** > **Manage datasources**.
3. On the *Manage datasources* page, select **More actions (…)** > **Edit** for the Bitbucket datasource.
4. Replace the username with your email address.
5. Replace the app password with the new API token.
6. Click **Save**. The gadgets that use this datasource will be updated automatically.

## Gadgets for Bitbucket

You can use a connection with Bitbucket to display data with the following gadgets:

- [Deployments](/cms_trial/space/RDD/146309688/Deployments/)
- [Hall of Fame](/cms_trial/space/RDD/146309449/Hall+of+Fame/)
- [Hall of Shame](/cms_trial/space/RDD/146309596/Hall+of+Shame/)
- [Pull Requests Team Workload](/cms_trial/space/RDD/146309582/Pull+Requests+Team+Workload/)
- [Open Pull Requests](/cms_trial/space/RDD/146309643/Open+Pull+Requests/)
- [Last Failed Pipeline](/cms_trial/space/RDD/146309787/Last+Failed+Pipeline/)
- [State of the Dev Union](/cms_trial/space/RDD/146310307/State+of+the+Dev+Union/)
- [Pipelines History](/cms_trial/space/RDD/146310238/Pipelines+History/)
- [Open Pull Requests by Author](/cms_trial/space/RDD/146310563/Open+Pull+Requests+by+Author/)