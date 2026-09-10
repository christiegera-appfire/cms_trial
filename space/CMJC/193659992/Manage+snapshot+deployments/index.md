# Manage snapshot deployments

## How to manage my deployments

The **Deployments**page lists essential information for each deployment. It allows you to view the status and details of all created deployments at first glance. In addition, you can return to deployments in progress to continue or return to completed and failed deployments to review their result once again.

### Deployment status

Each deployment you create can be in one of the following statuses:

- CREated Your deployment is created. Use the View action to resume and complete the deployment.
- Analysis Your deployment is being analyzed. Use the View action for progress and details of the analysis.
- deploying Your deployment is currently in progress. Use the View action to watch the deployment progress.
- completed Your deployment completed successfully. Use the View action to open the deployment details.
- failed Your deployment failed. You can open a support request and send us the deployment ID.

### Review or return to deployments

**To return to deployments in progress or review completed deployments:**

1. Log in as a user with **site admin** permissions on the source and destination Jira Cloud sites.
2. Choose the **cog icon**at the top right of the screen, then choose **Apps > Configuration Manager.**
3. Select **Deployments** and review the list of deployments.
4. Choose a deployment in any state and click its name under the **Deployment** column.

   ![contentId-193659992](/cms_trial/assets/1648b350-c245-4dfb-9aed-d55d461570b9.png)
5. For deployments in CREATED, ANALYSIS, and DEPLOYING states, you will be able to return to the reached phase in the deployment wizard.  
   For COMPLETED deployments, you will be able to review the deployment result, as shown in the screenshot below.  
   For FAILED deployments, you will see an error page that suggests opening a support ticket with the deployment ID.

   ![Screenshot 2025-11-07 at 10.41.52.png](/cms_trial/assets/855f8fa2-396a-44fc-a3d0-c8fb67289dc3.png)