# Deploy a snapshot

### Overview

Snapshots let you package Jira project configurations and deploy them at a later time. Deploying a snapshot applies the configuration elements captured in the snapshot to a destination Jira Cloud site.

The deployment process is:

1. Select a snapshot.
2. Select a Jira Cloud instance.
3. Analyze the changes.
4. Resolve any conflicts.
5. Deploy.

Snapshots enable you to reuse the same configuration across multiple Cloud sites and safely test changes in a sandbox or staging site before deploying them to production.

---

### Prerequisites

Before deploying a snapshot:

- Install and license CMJ Cloud on both the source and destination Jira Cloud sites.
- Ensure you have **Site Admin** or **Organization Admin** permissions on both sites.
- Generate an Atlassian **API token** for authentication.
- Confirm that the destination site uses a supported Jira Cloud plan (Standard, Premium, or Enterprise).

---

### Deploy a snapshot

1. In your Jira Cloud site, go to **Apps > Configuration Manager > Deployments**.
2. Click **New deployment**.
3. Under the *Choose what to deploy* section, the **Snapshot** option will be selected by default.

   ![Screenshot 2025-11-07 at 10.06.34.png](/cms_trial/assets/37319039-a1e4-4937-960d-5de30abb8bc8.png)
4. Name your deployment and choose which Jira Cloud site you want to deploy to.
5. Choose the snapshot you want to deploy from the drop-down list and click **Next**.

   ![Select-snapshot.png](/cms_trial/assets/3bd54cbc-78b8-468f-b12d-fa9a4a2d690f.png)
6. Next, in the **Analyze**phase, review the report of the changes introduced to the destination Jira Cloud. CMJ shows you the project configurations, configuration elements, and users deployed to the destination.

   ![Screenshot 2025-11-07 at 10.23.12.png](/cms_trial/assets/838944c5-e85a-4f5c-bad8-1c1150800a9e.png)

   CMJ Cloud also detects and shows warnings and errors. Remember that warnings won't block deployments, but errors will.
7. After resolving the errors using the [inline](/cms_trial/space/CMJC/759529597/Inline+transformations/) or [bulk](/cms_trial/space/CMJC/1851621940/Bulk+transformations/) transformations, rerun the analysis to check for new conflicts.
8. If the new analysis detects no errors, click **Deploy** to run the deployment.
9. After the deployment is completed successfully, review a summary of the results in the Deployment summary table (see the screenshot below).

   ![Screenshot 2025-11-07 at 10.41.52.png](/cms_trial/assets/b0c372cd-7010-4074-aa7c-c2dba25f0a99.png)
10. Navigate to the destination Jira Cloud site to browse your new or updated projects, custom fields, workflows, etc.

---