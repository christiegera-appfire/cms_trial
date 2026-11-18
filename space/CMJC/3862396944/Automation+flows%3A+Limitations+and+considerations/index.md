# Automation flows: Limitations and considerations

When deploying automation flows between Jira Cloud sites, CMJ Cloud transfers supported flow configurations and updates references to the corresponding Jira objects on the destination site.

However, some components and settings cannot be migrated automatically. CMJ Cloud reports potential problems during analysis so you can review them before deployment and take any necessary action afterward.

## How automation flows are matched

CMJ Cloud identifies matching automation flows based on their names and labels.

Two flows are considered identical when their names (excluding leading and trailing spaces) and their sets of labels match. The order of the labels doesn't matter.

- If a matching flow exists on the destination, CMJ Cloud updates it.
- If no matching flow exists, CMJ Cloud creates a new flow.

Unlike some other configuration elements, automation flow mappings cannot be changed manually during analysis.

## Known limitations

Some automation flow components require additional configuration or manual intervention after deployment.

| Limitation | What happens | What you need to do |
| --- | --- | --- |
| **Actor without Jira access** | The flow isn’t deployed, and no error or warning is shown. | Grant the actor Jira access on the destination site and deploy again. After deployment, verify that all flows exist. |
| **Third-party app components** | CMJ Cloud transfers unsupported components, but connections for newly added components are cleared. | Reconnect the affected components on the destination site. |
| **Team references** | References to Atlassian Teams in newly created or added components are removed because teams are organization-scoped. | Reconfigure the affected team references. |
| **Hidden webhook values** | Secure values in *Send web request* actions cannot be transferred. | Re-enter the hidden values after deployment. |
| **Jira Service Management forms** | Form references in *Form submitted* triggers cannot be migrated because of a Jira API limitation. | Review the trigger and select the appropriate forms on the destination site. |
| **Unsupported automation components** | CMJ Cloud may transfer components it cannot fully process or validate. | Review and, if necessary, reconfigure the affected components. |

![Screenshot 2026-11-02 at 9.46.48 (1).png](/cms_trial/assets/b650ddc0-9ba1-4cfe-8943-22ac3d57b358.png)

## Why are some automation flows deployed as disabled?

CMJ Cloud generally preserves the enabled or disabled state of automation flows during deployment. However, certain situations may cause a flow to be deployed as disabled.

This can happen when:

- **Third-party app components are newly added.** CMJ Cloud clears their site-specific connections. Newly created flows containing these components are deployed as disabled. When updating an existing flow, this applies only if new third-party components are introduced.
- **Team references need to be removed.** CMJ Cloud removes unsupported team references from newly created flows or newly added components. If references are removed, the affected flow is disabled.
- **Jira rejects an enabled flow.** If Jira rejects the initial create or update request, CMJ Cloud retries the operation with the flow disabled. If that attempt also fails, the deployment operation reports the error.

Existing third-party connections and team references on the destination are preserved when their corresponding components aren't newly added.

## Review automation flows after deployment

After deploying a snapshot containing automation flows, review any warnings reported during analysis and check the affected flows on the destination Jira Cloud site.

Pay particular attention to flows that contain third-party app components, team references, forms, or secure values.

Once you've resolved any outstanding configuration issues, test the affected flows and enable them when they're ready to use.

For instructions on including automation flows in snapshots and deploying them, see [**Deploy automation flows with CMJ Cloud**](/cms_trial/space/CMJC/3862265880/Deploy+automation+flows+with+CMJ+Cloud/).