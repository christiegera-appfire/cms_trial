# CQL Search

## Overview

This gadget brings Confluence content to your team’s dashboard, displaying content based on a given Confluence Query Language (CQL) query. Introduce a CQL query to filter and return content (pages, posts, etc.) from a Confluence instance, and select the columns to show.

For example, to list all the pages (type = page) in the space *Teams in Space* (space = TIS) with the label, space\_mission (label = space\_mission), you would use the following CQL query:

`space = TIS and type=page and label = space_mission`.

Refer to the [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/) to learn more about writing queries in Confluence.

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where the Confluence instance is installed.
- The **columns** that will appear in the list to display the search results. The title is set by default as the minimum column to be displayed.
- The **CQL (Confluence Query Language) query** to filter the list of content (see the [CQL documentation](https://developer.atlassian.com/server/confluence/advanced-searching-using-cql/)). If you don’t add any, the gadget will not request any content, because it would fetch all the content in the source instance, causing performance issues. You have to add at least one clause, for example to list a space `space = TIS`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [confluence icon]

Confluence

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget is not included in any pre-defined dashboard.