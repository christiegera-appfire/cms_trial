# Jira joins financial data

## Overview

Display Jira issue table linking issues with financial data taken from <https://www.npoint.io/docs/5a3a149160b561c7b868>.

## Prerequisites

- Connect **the** Jira datasource to a valid Jira instance.
- Set up an initial variable project to an existing project key.
- Clone point financial data and fill in some info for existing issue keys.
- Connect the financial data datasource to your endpoint.

## Features

- Load data from two different datasources and process it to be consumed (join data). datasource required

![Dashboard Hub Jira joins financial data custom report preview](/cms_trial/assets/dd02756e-458b-420e-9732-b67199cbcae8.png)![Dashboard Hub report setup using Jira and financial data sources](/cms_trial/assets/41d365f0-a9b5-4f01-b5f8-933c84006d66.png)

- Render a table.
- Reuse styles using stylesheets.
- Render columns from a different data set using `$root`.
- Shape data calculating aggregation for rendering purposes.
- Render a line/area chart showing multiple data series.
- Render a progress circular bar.

## Setup

1. Add a datasource. See: [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/).
2. Click **Add Gadget**.
3. Select **Custom Reports** in the side navigation.
4. Select the **Appfire Hedge risk matrix**.

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough of how to customize your report.

![Dashboard Hub custom report combining Jira and financial data sources](/cms_trial/assets/9e72d333-8f30-429e-b84a-9bb58626aa26.png)