# Hedge risk matrix

## Overview

Implemented two versions of a risk matrix:

- Inefficient: requires only the JQL initial parameter.

  - Gets issues by JQL**,** explores their issue properties, and looks for hedge properties**;** retrieves hedge property content for each issue.
- Efficient: requires JQL and hedge template IDs.

  - Gets issues by JQL with the hedge property in just one call.

### Features

- Requires variables (JQL and templateId) to work VARIABLE required.
- Load data from jira api datasource required.
- Reuse styles using stylesheets.
- Render a complete, custom interface to display a matrix using flexbox and node views.
- Pipe data from api to matrix.

### Setup

1. Add a datasource. See:[Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/).
2. Click **Add Gadget**.
3. Select **Custom Reports** in the side navigation.
4. Select **Appfire Hedge risk matrix**.

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough of how to customize your report.

![Dashboard Hub Hedge risk matrix report example](/cms_trial/assets/5b354418-3b82-45d4-bc8a-69fe227df92d.png)