# Release notes 10 April 2023

### April 10, 2023

We are excited to announce the release of **Configuration Manager for Jira Cloud 2.0.0**!

Upgrading to Configuration Manager for Jira Cloud 2.0.0 is free for all customers.

## Highlights

- [Cloud-to-cloud is live now! Deploy project configurations between Jira Cloud](#FEATURES) [sites](#FEATURES)

![contentId-258408524](/cms_trial/assets/a397b50f-e48e-4a0a-92b2-128898a35b6d.png)

[**Installation instructions**](/cms_trial/space/CMJC/194183182/Installation+guide/)

## Updates and Resolved Issues

![contentId-258408524](/cms_trial/assets/f8b41aeb-8671-4ce8-af2b-805b5c359176.png)

#### FEATURES

- Use [Configuration Manager for Jira (CMJ) Cloud](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) to deploy project configurations and the configuration elements associated with them from one Jira Cloud site to another (a.k.a. **cloud-to-cloud** deployments).

[Overview](#Deploy-project-configurations-between-Jira-Cloud-sites)

Previous Releases...

[1.1.2 Release Notes](/cms_trial/space/CMJC/193593962/Release+notes+11+October+2021/)

[1.0.0 Release Notes](/cms_trial/space/CMJC/193855942/Release+notes+1+October+2021/)

---

## Deploy project configurations between Jira Cloud sites

### Configuration & change management

Now, you can use CMJ Cloud also to:

- **deploy new project configurations** from one Jira Cloud site to another, and
- **deploy changes** from a source Jira Cloud to projects and configuration elements in a destination Jira Cloud.

**Projects' issues** **can't be deployed** from one Jira Cloud site to another yet.

Deploying project configurations also affects Jira configuration elements referring to them. The configuration elements referring to a project can be custom fields, workflows, screens, users, etc.

To ensure the project's proper functioning at the destination, CMJ Cloud will also:

- add configuration elements to the destination, and
- modify configuration elements in the destination

if they refer to project configurations that will be deployed.

[View full documentation](/cms_trial/space/CMJC/193725041/Overview/)

**Service Management** projects can't be added to a deployment as they aren’t supported yet.

![contentId-258408524](/cms_trial/assets/4cedf9b6-e43a-4789-9477-3f6900c3b7ad.PNG)

### Installation & prerequisites

You need to install CMJ Cloud on **both Jira Cloud sites** to be able to perform configuration deployments. After the installation, you need to provide one license token for the source Jira Cloud site and another one for the destination Jira Cloud site. If your source Jira Cloud site is a production instance, you’ll need a production license for it too.

After the installation, you need to:

- have **two separate license tokens**, one token for the source and another token for the destination,
- have **site-admin permissions** on both Jira Cloud sites, and
- authorize your administrative credentials using an Atlassian account [API token](/cms_trial/space/CMJC/193594026/Authorize+with+API+token/) in CMJ Cloud’s UI.

For more information, please check out the detailed [prerequisites](/cms_trial/space/CMJC/193659801/Prerequisites/), [installation,](/cms_trial/space/CMJC/194183182/Installation+guide/)and [licensing](/cms_trial/space/CMJC/194150417/Licensing/) instructions.

### Intuitive UI to deploy configuration

After installing the app, you can configure your deployment by selecting projects and boards to upload. The deployment will automatically include the workflows, custom fields, screens, and other configuration elements associated with the projects in the scope.

See the [complete list](/cms_trial/space/CMJC/193855959/Supported+configuration+elements/) of configuration elements we’re able to deploy currently.

### Deep configuration analysis

CMJ Cloud performs a deep configuration analysis by comparing the configuration elements in the source and destination Jira Cloud sites. This analysis detects errors, warnings, and conflicts between the two sites.

Errors and conflicts stop a deployment, whereas warnings don’t. You need to resolve the reported errors and conflicts to continue a blocked deployment.

Errors are major problems with the configuration. Conflicts are problems between source and destination configuration elements. If unresolved, they would break the project configurations in the destination. Warnings are minor issues detected that won’t introduce breaking changes.

### Transformations during deployment

CMJ Cloud allows you to rename the projects, workflows, workflow schemes, and filters added to the deployment scope. You can also change project keys during deployment.

The app adds the edited source projects, workflows, and filters as new configurations on the destination. This way, the destination configuration elements matching source elements by type, name, or id won't be modified.

---

More improvements and bug fixes will be coming soon! Thanks! Please submit your suggestions for improvements to Appfire’s [**Support Portal**](https://apps.appf.re/support). We value your feedback!