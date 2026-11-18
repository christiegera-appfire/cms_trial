# Deploy automation flows with CMJ Cloud

Jira automation flows help you automate repetitive tasks, such as updating work items, sending notifications, or triggering actions based on specific events. When managing multiple Jira Cloud sites, recreating these flows manually can be time-consuming, especially when they reference other Jira configuration elements.

Configuration Manager for Jira (CMJ) Cloud lets you include automation flows in your configuration snapshots and deploy them alongside their related configuration elements.

**Known issue:** Automation flows may be skipped during deployment if their actors don't have Jira access on the destination site. For details, see [Automation flows: Limitations and considerations](/cms_trial/space/CMJC/3862396944/Automation+flows%3A+Limitations+and+considerations/).

## Include automation flows in a snapshot

Automation flows are automatically included in your snapshot based on the scope you select during snapshot creation.

- **Everything supported**: CMJ Cloud includes all automation flows from the source Jira Cloud site, including global, project-type-scoped, and project-scoped flows.
- **Specific elements**: CMJ Cloud includes only the project-scoped automation flows associated with the selected projects. Global and project-type-scoped flows are not included.

You cannot select or exclude individual automation flows. CMJ Cloud determines which flows to include based on your snapshot scope.

For more information about creating snapshots, see [**Create a snapshot**](/cms_trial/space/CMJC/2506522887/Create+and+manage+snapshots/).

## Analyze automation flows before deployment

Automation flows are deployed using the regular snapshot deployment workflow. No additional configuration is required.

During analysis, CMJ Cloud compares the automation flows in the snapshot with those on the destination Jira Cloud site.

To review the changes, open the **Detailed View** and go to the **Changes** tab. Here, you can inspect which automation flows will be added or modified on the destination site.

![Screenshot 2026-11-02 at 10.28.19 (1).png](/cms_trial/assets/100dad6b-d56a-4d95-9d0d-01ff144d0613.png)

If CMJ Cloud detects problems with an automation flow, review the reported warnings or errors before proceeding with the deployment.

## Deploy automation flows

Automation flows are deployed together with the other configuration elements included in your snapshot.

CMJ Cloud creates new flows on the destination site and updates existing flows that match those in the snapshot. References to supported Jira configuration elements are updated to use the corresponding objects on the destination site.

Some flows may require additional attention after deployment. For example, flows containing third-party app components, team references, or configuration that Jira cannot validate may be deployed as **disabled**.

Before enabling a disabled flow, review its configuration, resolve any outstanding issues, and test that it works as expected.

For more information, see [Automation flows: Limitations and considerations](/cms_trial/space/CMJC/3862396944/Automation+flows%3A+Limitations+and+considerations/).