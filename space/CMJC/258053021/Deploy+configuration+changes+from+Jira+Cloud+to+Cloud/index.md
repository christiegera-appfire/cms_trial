# Deploy configuration changes from Jira Cloud to Cloud

## Deploy project configuration changes from Jira Cloud to Cloud

[**Configuration Manager for Jira (CMJ) Cloud**](/cms_trial/space/CMJC/193725041/Overview/) helps you deploy project configuration changes from one **Jira** **Cloud site to another**. This article will refer to this use case as *"Cloud-to-Cloud"*.

For this use case, you need to create a temporary Jira Cloud site. It can be either a Jira Cloud site or a sandbox provided by Atlassian for testing purposes. The sandbox will act as a test environment where you can make changes safely, and when ready, deploy them to your production environment. [Learn more about setting up Atlassian sandboxes](https://support.atlassian.com/organization-administration/docs/manage-product-sandboxes/).

![contentId-258053021](/cms_trial/assets/d1c61f67-2eae-4eaa-b1e4-0bafe15ccd7a.png)

CMJ Cloud is built to protect the integrity of the destination Jira Cloud site by blocking breaking changes. The app analyzes each change that will be introduced. It then identifies the ones that aren't compatible with the destination Jira Cloud's project configurations.

<https://fast.wistia.com/embed/medias/ykgkuwnuds.jsonp>

## Use case steps

This section will guide you through the *Cloud-to-Cloud* use case's prerequisites and implementation phases.

### Prerequisites

---

- **Destination Jira Cloud site**
- **Source Jira Cloud site**: a standard Jira Cloud site or an Atlassian sandbox, which is a replica of the destination Jira Cloud site. [Learn more about setting up a sandbox](https://support.atlassian.com/organization-administration/docs/manage-product-sandboxes/).
- **Licenses:** You need a [valid license](/cms_trial/space/CMJC/194150417/Licensing/) for both the CMJ Cloud app on the destination Jira Cloud site and on the source Jira Cloud site/sandbox.
- **Supported objects:** Make sureCMJ Cloud supports the configuration elements you want to deploy to the destination Jira site, along with your projects. See the [Supported Configuration Elements](/cms_trial/space/CMJC/193855959/Supported+configuration+elements/) document.

---

### High-level process

This section lists the high-level phases of implementing the *Cloud-to-Cloud* use case. To learn more about each phase, read our [Detail process](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/255819777/Deploy+configuration+changes+from+Jira+Cloud+to+Cloud#Detailed-process) guide below.

- **Setup:** Prepare a temporary Jira Cloud site or Atlassian sandbox that mirrors the destination site.
- **Phase 1:** Bring the destination site’s configuration into the source site so you start from an identical baseline.
- **Phase 2:** Modify projects and configuration elements as needed.
- **Phase 3:** Conduct user acceptance testing (UAT) to validate that changes behave as expected.
- **Phase 4:** Export a CMJ Cloud snapshot from the source site and deploy it to the destination Jira Cloud site. [**Use CMJ Cloud for this purpose**](/cms_trial/space/CMJC/2507112493/Deploy+a+snapshot/)**.**

---

### Detailed process

**Setup**

- **Set up** a source Jira Cloud site or [**sandbox**](https://support.atlassian.com/organization-administration/docs/manage-product-sandboxes/) that mirrors the destination site.
- **Install** [**CMJ Cloud**](/cms_trial/space/CMJC/194183182/Installation+guide/) on both the source and destination sites.
- **License CMJ Cloud** and use a [valid license](/cms_trial/space/CMJC/194150417/Licensing/) for both the destination Jira Cloud site and the source Jira Cloud site/sandbox.

  **Phase 1:** **Replicate the destination Jira Cloud’s configuration to the source Jira Cloud site/sandbox**

1. Restore the destination site's configuration to the source Jira Cloud site or copy the destination site's data into a sandbox. [Learn more about copying data to the sandbox](https://support.atlassian.com/organization-administration/docs/manage-product-sandboxes/).
2. Validate that both environments are aligned.

   **Phase 2: Make configuration changes to the source Jira Cloud site/sandbox**
3. Apply all planned project and configuration updates in the source site.

   **Phase 3: Test the configuration changes on the source Jira Cloud site/sandbox**
4. Conduct UAT with stakeholders.
5. Confirm that the updated configuration behaves as expected.

If issues are found:

- Update the configuration in the source site.
- Create a new snapshot and restart the process from Phase 1 if necessary.

1. When ready, create a CMJ Cloud snapshot from the source site. [Follow the snapshot creation process described here](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/).

**Phase 4**: **Deploy projects to the destination Jira Cloud site**

1. Upload the snapshot from the source site to CMJ Cloud on the destination Jira Cloud site.
2. Proceed with the deployment. [Follow the deployment process described here](/cms_trial/space/CMJC/2507112493/Deploy+a+snapshot/).
3. Review CMJ Cloud’s [analysis](/cms_trial/space/CMJC/193626781/Analyze+changes/).
4. Finalize deployment.
5. (Optional) Retire or reset the temporary source site or sandbox.