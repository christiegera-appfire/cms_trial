# Compass table

## Overview

Display a Compass components table for demo purposes, showing the information found for each component.

## Features

- Requires a variable **cloudId** VARIABLE required with the compass cloudId to retrieve the components, but as this is an internal ID from Atlassian, we have provided a way to get it from the variable **hostname (ex.** [**mysite.atlassian.net**](http://mysite.atlassian.net)**)**: this will launch a query to retrieve the cloudId to fill
- Load from a Compass datasource datasource required of type **POST** as it’s a GraphQL query.
- Renders the components table.
- Customize certain cells to render some flexible representation (name column).

## Setup

1. Add a datasource. See: [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/) (remember it’s a POST datasource as compass API is graphql).
2. Click **Add gadget**.
3. In the side navigation, click **Custom Reports**.
4. Select **Compass Table**.
5. Fill the cloudId variable (you may need to find it out using the hostname variable first

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough on how to customize your report.

See also:

[Custom Reports - REST API integration](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/)

[Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)