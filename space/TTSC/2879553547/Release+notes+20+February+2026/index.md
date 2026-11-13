# Release notes 20 February 2026

**Release date**: February 20, 2026

Our team is thrilled to announce the latest release of Time to SLA for Jira Cloud.

---

## New features

This release introduces two new field types and a dedicated management area inside Time to SLA.

### Settings is now Administration

The **Settings** section has been renamed to **Administration**. You’ll now manage app-level settings from:

Image — asset pipeline pending  
Time to SLA home screen with the Administration menu highlighted in the top navigation bar.

This change is the first step in improving the structure and organization of Time to SLA configuration options.

### Introducing new SLA custom fields

SLA custom fields can now be created and managed from:

Image — asset pipeline pending  
Administration menu expanded in Time to SLA, showing the SLA Fields option selected in the dropdown.

The interface mirrors Jira’s native custom field experience for a familiar and consistent workflow.

Image — asset pipeline pending  
SLA Fields page in Time to SLA with the Create an SLA Field dialog open and SLA Indicator selected as the field type.

#### SLA Indicator field

This new field displays SLA status directly in the work item view. The SLA Indicator shows whether an SLA is:

- In progress
- Breached
- Completed

Users can click the information icon in the work item to see a detailed SLA breakdown. This makes SLA health immediately visible to agents without opening the SLA panel.

Documentation: [SLA Indicator field](/cms_trial/space/TTSC/2878930952/SLA+Indicator+field/)

#### SLA Date field

This new field stores SLA dates in a Jira custom field. You can configure the field to store:

- Start
- End
- Target

If multiple SLAs apply, you can define whether the field stores the earliest or latest date.

Documentation: [SLA Date field](/cms_trial/space/TTSC/2879160326/SLA+Date+field/)

#### Coming soon: SLA Duration field

We’re also preparing the SLA Duration custom field. This upcoming field will allow you to store calculated SLA duration values, making SLA reporting even more powerful. It’s coming in an upcoming release, so stay tuned!

## Bug fixes

This release fixes the following bugs:

- Resolved an issue where SLA IDs were set incorrectly when transferring work item SLAs via JCMA (Jira Cloud Migration Assistant). This could lead to mismatched or inconsistent SLA references after migration.
- After JCMA migration, the SLA scope JQL is appended to all goal JQLs because Time to SLA Cloud does not support SLA-level scope JQL. Previously, SLA recalculation did not validate the default goal JQL. As a result, SLAs could appear on work items that did not meet the intended scope criteria. This has been fixed. Recalculation now properly checks the default goal JQL to ensure SLAs are only applied to relevant work items.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=overview&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1211843/time-to-sla?tab=reviews&hosting=cloud&utm_source=appfire.com&utm_medium=solutions&utm_campaign=Time-to-SLA).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Time to SLA!

---