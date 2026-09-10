# AQL Search

## Overview

IT Service Management teams frequently handle corporate assets to provide a smooth service or quickly troubleshoot incidents. Thus, having an easy access to the list of assets and their information is a must for high-performance teams.

This gadget lets ITSM teams gain visibility on the corporate assets and their information. The list of gadgets is presented in a table with all the objects' information, in a given object schema.

![Dashboard Hub Assets information](/cms_trial/assets/b89fa9b0-5022-42d0-a34b-cb937a9982b6.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where the Asset cloud instance is installed.
- The **object schema** of the objects you want to query is displayed in the gadget.
- The **AQL (Asset Query Language) query** to filter the list of objects (see the [AQL documentation](https://confluence.atlassian.com/servicemanagementserver/managing-your-assets-with-assets-1044784300.html)). Try with a query like `"Created" > now(-52w)` to display all the objects created in the last 52 weeks. If you don’t add any, you will see all objects of the previously selected object schema. If you select specific objects in the *AQL*, the gadget will be static, always displaying those objects. However, if you select all, the results could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- Assets in Jira Service Management (formerly, Insight)

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).