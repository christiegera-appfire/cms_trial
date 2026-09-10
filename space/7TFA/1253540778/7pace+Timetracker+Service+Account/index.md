# 7pace Timetracker Service Account

7pace Timetracker requires a **Service Account user** to access your organization’s ADO data. If a Service Account is not configured, all of the features in Timetracker Reporting are not available, including the Times Explorer page, search, and API. Therefore, to use 7pace Timetracker to its fullest, configure one licensed user as a **Service Account user**.

## Requirements

The **Service Account user** must be an ADO user who is part of the ***DevOps Project Collection Administrator group***. This allows 7pace Timetracker to obtain ADO data about work items from across your organization through the user’s authorization token.

## Configuration

To configure the Timetracker Service Account, the user who serves as the Service Account must log into 7pace Timetracker, navigate to**Timetracker Settings** > **Reporting and API** > **Service Account** and click ***Set Myself as Service Account***:

![Service Account Settings page with the Set Myself as Service Account button.](/cms_trial/assets/05fa1c9f-fafd-4ef6-b6ef-04bb7e8b25a4.png)

## Optional Privacy Setting

You can enable 7pace Timetracker to display ADO data in Timetracker Reporting and Times Explorer to users who normally do not have access to those projects by enabling the ***Allow access to DevOps data from restricted projects in Reporting*** setting. With this setting activated, users can see work item details (title and basic information) for tracked time across your organization, even if their ADO user permissions don’t allow it.

## Service Account Personal Access Token (PAT)

Users can authorize 7pace Timetracker for use with ADO through OAuth authorization or a DevOps-issued Personal Access Token (PAT).

The user serving as the Timetracker Service Account user must authorize Timetracker with ADO with [a DevOps-issued PAT](/cms_trial/space/7TFA/1253540459/Use+a+Personal+Access+Token+to+authorize+7pace+Timetracker+for+ADO+Cloud/). Timetracker uses the PAT to access work item information from your organization and displays the data in Timetracker Reporting and Times Explorer.

Since ADO limits the lifespan of a Personal Access Token to a maximum of one year, we recommend creating a PAT that expires after a year. This way, you are forced to renew only once per year.

To see common errors related to an expired Service Account PAT or misconfigured Service account, see:

- [7pace Timetracker Reporting and API common errors and states. Why is my Reporting or API not working?](/cms_trial/space/7TFA/1253539973/7pace+Timetracker+Reporting+and+API+common+errors+and+states.+Why+is+my+Reporting+or+API+not+working%3F/)

## Service Account Personal Access Token (PAT) Requirements

There are no unique requirements for the Service Account user's PAT compared to regular users. The Personal Access token used for 7pace Timetracker must have the following scopes enabled:

| **Scope** | **Access Level** |
| --- | --- |
| User profile | Read |
| Work Item | Read & Write |
| Identity | Read |

Instructions on generating a Personal Access Token in ADO are found in this Microsoft article guide:

- [Use personal access tokens](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)