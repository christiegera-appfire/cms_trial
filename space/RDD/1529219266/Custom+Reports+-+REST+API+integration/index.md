# Custom Reports - REST API integration

## Overview

The **Custom Reports** gadget in Dashboard Hub that lets you integrate data from any product with a REST API into your dashboards. Unlike traditional gadgets tied to predefined [datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/), Custom Reports lets you create highly tailored reports by fetching data from virtually any external API and presenting it in a unified, interactive dashboard

![An example the Custom Reports gadget configuration and descriptor file.](/cms_trial/assets/2abccc8c-2a25-414e-8d79-6e4bacbd3ffe.png)

## What is a REST API-based report?

REST API-based reports retrieve data directly from external systems using REST APIs. You define the API endpoints, parameters, and filters to retrieve specific data, which is then transformed into visual reports such as charts or tables within the dashboard. REST API-based reports are ideal for integrating data from products like monday.com, Jira, Bitbucket, 7pace GitHub, GitLab, Zendesk, custom CRM or ERP systems, or other platforms, enabling centralized analysis and reporting.

Custom Reports uses industry standards like **JSON** and **JSONata** for data transformation and visualization, giving you powerful, flexible control over how your data is queried and displayed.

## Key features

### **Flexible data integration**

Connect to APIs beyond the existing integrations provided by Dashboard Hub. Retrieve data from external systems, such as open APIs or private services, using REST API calls.

### **Customizable gadgets**

Define every detail of the gadget's user interface with a descriptor file in JSON5 format. This includes layout, colors, and data presentation (text, tables, charts).

### **Advanced security**

Authenticate securely using methods such as Basic Authentication, Bearer Tokens, or API Keys, ensuring reliable and secure data access while maintaining best practices.

### **Powerful data contexts**

Combine data from multiple endpoints into a unified context. Query, filter, and visualize this data within the gadget using [JSONata](https://jsonata.org/).

### **Reusable** **reports**

Save and export reports as JSON files, to share designs, integrations, or collaborate on custom new visualizations.

### Custom Reports templates

To help you get started, we offer a catalog of [Custom Reports templates](/cms_trial/space/RDD/1568374878/Custom+Reports+templates/) that suit a variety of scenarios and integrations.

## Example use cases

- **Simple reports**: Display data from public APIs, such as weather or news updates, and display it on your dashboard.
- **Advanced reports**: Connect to authenticated APIs and create reports with combined data from multiple endpoints, using variables and filters for granular insights.

Use Custom Reports to break data silos, creating dashboards that integrate information from any source with full control over presentation and functionality. See the [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) to learn more.

## Related pages

- [Custom Reports templates](/cms_trial/space/RDD/1568374878/Custom+Reports+templates/)
- [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/)
- [Query and transform your data with JSONata](/cms_trial/space/RDD/1549304032/Query+and+transform+your+data+with+JSONata/)
- [Nodes as building blocks for Custom Reports](/cms_trial/space/RDD/1548747137/Nodes+as+building+blocks+for+Custom+Reports/)