# Project Stakeholders Workload

## Overview

Projectrak makes easy gaining control and managing your projects, and that’s why you can set who’s the project lead and the stakeholders of each project. One of the problems of many project-lead companies is that of over-commitment, where some stakeholders end involved in too many projects. This leads to work fatigue and other problems that need a quick reaction.

This gadget displays a leader board of the stakeholders of a set of projects, result of a PQL query. Only the top 10 are displayed. The stakeholders are extracted from the “Stakeholders” field, as provided by Projectrak.

Learn everything about Projectrak’s [Advanced search with PQL (Project query language)](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html)

Don’t let your mates drown in projects!

![Dashboard Hub Projectrak Custom Charts area chart](/cms_trial/assets/b0d17e74-b17c-44bb-8aae-47afb1a97268.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).
- The **PQL (****Project** **Query Language) query** to filter the list of projects (see the DEISER’s Projectrak [Advanced search with PQL](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html) documentation). If you don’t add a PQL query and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend to add at least one clause, for example to list all the projects that are “On track” and the lead of those projects is the current user, use the clause `Status = "On track" and lead = currentUser()`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- ![contentId-146311454](/cms_trial/assets/f1dea358-fbe9-422e-b749-1ef1bca695e9.png)

Projectrak

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Project Tracking Insights template](/cms_trial/space/RDD/146310779/Project+Tracking+Insights+template/). See:

Project Tracking Insights dashboard