# Hedge risk pie chart

## Overview

Display the risk pie chart from Hedge’s data.

## Features

- Requires variables (JQL and template Id) to work.
- Load data from the Jira API.
- Process data to render a custom pie chart.
- Render a custom legend.

## Setup

datasource required VARS required

1. Add a datasource. See, [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/).
2. Provide access to a Jira instance using a Custom Reports datasource with a valid access token.
3. Generate an access token at [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).

   - For more details, see: <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>.
4. Once you have obtained your token, create a Dashboard Hub datasource using basic authentication, specifying your email as the username and the access token as the password.

![Dashboard Hub Custom Report datasource setup for Hedge risk pie chart](/cms_trial/assets/99a85b1d-c5d5-4898-bcad-c60d652e0092.png)

## Configure

1. Configure the report with the Jira datasource.
2. Set the required variables:

   - JQL: the query to request issues from jira, a valid JQL request (ex. project=XXX).
   - templateid: the id for the hedge template you want to gather data.

You should now see your data.

See, [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video demonstration on how to configure your report.

![An example Portfolio risk register graph.](/cms_trial/assets/6bb01c8f-8208-47d0-9b27-6eb4b43830a2.png)