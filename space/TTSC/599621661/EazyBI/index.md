# EazyBI

The EazyBI - Time to SLA integration is now available in its beta version for EazyBI Cloud. This integration lets you incorporate Time to SLA information into your EazyBI reports, providing additional insights into your Jira data.

This document outlines the steps to enable the integration.

## Step 1: Enable the integration

To enable the Time to SLA integration, follow these steps:

1. Navigate to your EazyBI settings in the Atlassian Cloud environment. To learn how to navigate site settings, refer to [this documentation](https://docs.eazybi.com/eazybi/set-up-and-administer/atlassian-cloud/site-settings-for-cloud).
2. Add the following lines to the EazyBI settings:

```text
[jira.time_to_sla]
enable = true
```

1. Save the settings.

## Step 2: Configure the TTS API Token

After enabling the integration, you need to provide the Time to SLA (TTS) API token within the Jira import Add-ons tab. Follow these steps:

1. Navigate to the Jira import **Add-ons** tab in EazyBI.
2. Provide the TTS API token. If you don't know how to create a TTS API token, refer to [this documentation](/cms_trial/space/TTSC/36209134/REST+APIs/).
3. Click **Show available custom fields** after providing the token.

   ![Time to SLA Add-ons tab in EazyBI with API token field and custom fields button](/cms_trial/assets/593ff3f7-08e6-4053-89af-9122f82de1e6.png)

EazyBI will then query SLA information and present the available options for selection.

## Import

After configuring the integration and providing the TTS API token, you can proceed to import SLA information into EazyBI.

After data import, a separate set of dimensions and measures will be created for each SLA metric.

**Dimensions**

- **SLA State** – Displays whether the SLA is *Running*, *Paused*, or *Completed*.
- **SLA Breached** – Indicates if the SLA cycle was *Breached* or *Not breached*.

![Time to SLA dimensions in EazyBI showing SLA State and SLA Breached fields](/cms_trial/assets/24a4730e-bff5-410f-b6fe-80da76a6cf50.png)

**Measures**

- **SLA Issues** – Total number of issues with SLA data.
- **SLA Elapsed hours** – Total hours elapsed for completed SLA cycles.
- **SLA Remaining hours** – Hours remaining until SLA breach.
- **SLA Paused hours** – Total time the SLA was paused.
- **SLA Breached hours** – Duration the SLA spent in a breached state.
- **SLA Completed cycles issues count** – Number of issues with completed SLA cycles.
- **SLA - Met / Breached / Met % / Breached %** – Counts and percentages of met or breached SLAs.
- **SLA - Average hours** – Average elapsed time for completed SLA cycles.

![Time to SLA measures list in EazyBI showing SLA Issues, Elapsed hours, and other metrics](/cms_trial/assets/cd594642-a6a9-40dc-a946-51812510be3a.png)

The import process will also create a set of sample reports, which can be utilized to understand how SLA data can be utilized in EazyBI.

![Time to SLA sample reports created in EazyBI after data import](/cms_trial/assets/0a0adf09-9db0-466f-b0d4-798df0a096bf.png)

For a complete list of dimensions, measures, properties, and sample reports, refer to  
[EazyBI's documentation](https://docs.eazybi.com/eazybi/data-import/data-from-jira-apps/time-to-sla#TimetoSLA-DataimportinCloud).