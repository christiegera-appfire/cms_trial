# Release notes 3 March 2026

**Release date**: March 3, 2026

Our team is thrilled to announce the latest release of the Dashboard Hub family of apps for Jira and Confluence.

---

## New features

## Created vs Resolved Work Items gadget

We now offer a gadget that provides a clear view of issue creation and resolution over time using two debt metrics alongside a stacked area chart, helping stakeholders understand not just how many work items are being created, but whether overall technical or operational debt is growing or shrinking.

The gadget combines two key metrics using the number of items created and resolved within the defined date range:

- **Current Period Accumulated Debt**: This shows how many work items created in the current period remain unresolved.
- **Historical Debt**: This shows how many work items created in *previous* periods were resolved in the current one, highlighting the team’s effort in paying down existing backlog.

![Dashboard Hub release notes screenshot for March 2026](/cms_trial/assets/031bd2fb-a904-426e-8202-37c01e86f7dc.png)

See [Created vs Resolved Work Items](/cms_trial/space/RDD/2710011923/Created+vs+Resolved+Work+Items/) to learn more.

---

## Platform updates

### Forge L3

At Appfire, we’re committed to maintaining the highest standards of security, reliability, and performance across our solutions. As part of this commitment, Dashboard Hub has been developed and deployed on Atlassian Forge, Atlassian’s most advanced cloud development platform. This release meets Level 3 technical and security standards.

Moving to Forge ensures that your data is protected within Atlassian’s trusted infrastructure, leveraging its built-in security, compliance, and scalability capabilities. By embracing Forge, Appfire continues to deliver on its promise to offer secure, enterprise-grade apps that evolve with Atlassian’s platform.

---

## Improvements

### Time in Status gadget

Updated the Time in Status gadget to preserve the selected Measure and Group Date By values when a user changes the view type.

### Datasource icons

We added icons and improved tooltip information to the gadget configuration and the *Manage datasources* page to better distinguish the different datasource options and their permissions.

![Dashboard Hub Dashboard Hub datasource selector improvements](/cms_trial/assets/db439c47-814a-4a66-9c9e-72d57115906c.png)

### Optimized gadget preview for extra settings

To improve rendering on smaller screens, we display the *Charts extra settings* panel as an overlay when it’s expanded in the gadget preview.

---

## Bug fixes

The following bug fixes are included in this release summary:

- Resolved an issue where gadgets using a Jira Service Management datasource didn’t load successfully when the Restrict Owner View Mode was enabled in global settings.
- Resolved an issue where clicking bar chart segments did not open the related work items for users other than the dashboard owner on gadgets using a JQL query and *This Jira instance* datasource.

---