# Share deployment data with the support team

## Consent for sharing deployment data with Appfire’s support team

At Appfire, we deeply care about our users' and partners’ success. To enhance your experience with CMJ Cloud, we’ve introduced a new feature for greater supportability. It lets you share selected deployment data with our support team, ensuring quicker resolution of issues. Also, you can turn this feature on and off at any deployment phase. Sharing deployment data is usually required by the support personnel after creating a support ticket.

CMJ Cloud **doesn’t log a support ticket** to Appfire’s support team when you enable deployment data sharing. Remember that you still need to choose the **Get support** option to create a ticket to let our team know you need help. By sharing your data first, however, you’ll get a much quicker resolution to your issue.

The data-sharing preferences are *enabled per deployment*. This means that you need to set them in each deployment you’re willing to share with our support team. Also, with this feature, you only grant our support team access to selected deployment data.

You can give consent for sharing data with the support team in the following cases:

- For **failed deployments,** look for the *help* icon ( [question mark icon] ) at the bottom-right corner of the page with the error.
- For **existing deployments**, open a selected deployment and find the *help* icon ( [question mark icon] ) at the bottom-right corner.
- For **new deployments,** look for the *help* icon ( [question mark icon] ) at the bottom-right corner of any page after providing a name and destination for your deployment.

Find more details in our [step-by-step guides below](#Step-by-step-guides-for-sharing-deployment-data).

We’ll keep the data you share with Appfire for **30 days**. However, you can **stop sharing** deployment data with support at any time. See how to stop sharing in our [step-by-step guide below](#Stop-sharing-deployment-data).

The image below shows you where to find the help and support options for a deployment.

![ShareDeploymnetDataButton.png](/cms_trial/assets/30e4c205-4ddd-4b41-b237-d318b5fabd07.png)

### What data you can share for your cloud-to-cloud deployments

You can share the following deployment data with Appfire’s support team:

- **Source configuration**  
  This option includes the **projects and boards added to the deployment** and all *configuration elements* and *users* associated with these projects.
- **Applied transformations**  
  This option includes all [transformations](/cms_trial/space/CMJC/759595150/Transformations/) applied to the projects and configuration elements in the deployment scope. Applying certain transformations can lead to deployment issues, so sharing that data with the support team is essential.
- **Destination configuration**  
  This option includes destination projects, configuration elements, and users affected by the source configuration being deployed.

  ![ShareDeploymentDataSteps.png](/cms_trial/assets/42288b8f-05b1-43ed-8d9c-2bcd4ca4a957.png)

### Last change time

CMJ Cloud remembers and shows when you’ve shared data or changed your sharing preferences. Each time you click **Confirm** in the *Share info with the support team* window, the**Last change**time is updated.

![ShareDeploymentDataTime.png](/cms_trial/assets/9ae1072d-e8ec-4bcd-985b-6563d790b037.png)

## Step-by-step guides for sharing deployment data

In the following sections, we’ve put together instructions on sharing data for failed, new, and existing deployments and how to stop sharing data.

### Share data for failed deployments

1. If the deployment fails, click the *help* icon ( [question mark icon] ) at the bottom right of the error page. Alternatively, if you have already closed the failed deployment, navigate to the **Apps > Configuration Manager > Deployments** page and click the deployment’s name under the **Deployment** column.
2. In the deployment wizard, click the *help* icon ( [question mark icon] ) in the bottom-right corner.
3. In the *Get help on this deployment* window, choose the **Share info with the support team** option.
4. In the *Share info with the support team* window, check the boxes of the information you would like to share and click **Confirm**.
5. Check that you see the **SHARED WITH SUPPORT** status at the bottom right of the page. It means you’ve successfully shared your data with our support team for this specific deployment.

The video below demonstrates how to enable data sharing for a failed deployment.

### Share data for new deployments

1. Navigate to the **Apps > Configuration Manager > Deployments** page.
2. Click the **New deployment** button**.**
3. Аdd a name and choose a destination Jira Cloud, then choose a snapshot you want to deploy and click **Next** to move to the next page
4. In the deployment wizard, click the *help* icon ( [question mark icon] ) in the bottom-right corner. The options for data sharing are especially useful when you encounter an error that causes a deployment to fail.
5. In the *Get help on this deployment* window, choose the **Share info with the support team** option.
6. In the *Share info with the support team* window, check the boxes of the information you would like to share and click **Confirm**.
7. Check if you see the **SHARED WITH SUPPORT** status at the bottom right of the page. It means you’ve successfully shared your data with our support team for this specific deployment.

The video below demonstrates how to enable data sharing for a new deployment.

### Share data for existing deployments

You can also share data from older deployments. All you need to do is open a previous deployment and enable data sharing.

1. Navigate to the **Apps > Configuration Manager > Deployments** page.
2. Click the deployment’s name under the **Deployment** column.
3. In the deployment wizard, click the *help* icon ( [question mark icon] ) in the bottom-right corner.
4. In the *Get help on this deployment* window, choose the **Share info with the support** option.
5. In the *Share info with the support team* window, check the boxes of the information you would like to share and click **Confirm**.
6. Check if you see the **SHARED WITH SUPPORT** status at the bottom right of the page. It means you’ve successfully shared your data with our support team for this specific deployment.

The video below demonstrates how to enable data sharing for an existing deployment.

### Stop sharing deployment data

1. Navigate to the **Apps > Configuration Manager > Deployments** page.
2. Click the deployment’s name under the **Deployment** column.
3. In the deployment wizard, click the **SHARED WITH SUPPORT** status in the bottom-right corner.
4. In the *Share info with the support team* window, click the **Stop sharing** button or uncheck the boxes of the information you had previously shared and click **Confirm**.
5. You’ll return to the *Get help on this deployment* window. You can again choose between the options or click **Close** to return to the deployment.
6. After you stop the data sharing, check if the **SHARED WITH SUPPORT** status has reverted to the initial *help* icon ( [question mark icon] ) at the bottom right of the page.

The video below demonstrates how to stop the deployment data sharing.