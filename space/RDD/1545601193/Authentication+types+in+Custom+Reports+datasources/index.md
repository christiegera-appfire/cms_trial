# Authentication types in Custom Reports datasources

## Overview

Custom Reports supports multiple authentication methods to securely connect to your REST APIs. Choose the required authentication for your API and enter the necessary credentials during datasource creation.

![Dashboard Hub authentication types](/cms_trial/assets/c115789c-e2dc-4f18-9980-170b9a2e6549.png)

## No Auth

This authentication type is utilized when the endpoint you are accessing does not require authentication. It lets you define the URL of your endpoints and modify it in a single location, eliminating the need to edit the report’s descriptor.

## API Key

In this scenario, you will be prompted to provide a key-value pair, which will be used as either a query parameter or a header in requests to API endpoints that necessitate this authentication format.

## Bearer Token

This authentication mechanism is widely recognized among developers. Your token will be included as part of the authorization header in each request.

## Basic Authentication

The basic authentication requires users to send a username and password to authenticate your request. However, in the Atlassian ecosystem, you are required to provide your email address and an API token as the password.

To add a Jira or Confluence Cloud datasource for Custom Reports, you need to use Basic Auth with your email and an [API Token](https://id.atlassian.com/manage-profile/security/api-tokens).

If you want to use any other Jira or Confluence gadget from the catalog, use the [default datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/).

![Dashboard Hub basic authentication](/cms_trial/assets/6b1681f9-d47f-4951-96f0-c6ebba7c5cec.png)

## Query parameters

Parameters allow you to define specific query details to refine the data fetched from the API.

Examples:

- ?status=active&dateRange=last30days
- ?limit=50&page=2

![Dashboard Hub query parameters](/cms_trial/assets/1d6baf9e-5eeb-48a7-b253-9fca7a9234d6.png)

## Headers

Headers are used to send additional information with your API requests, such as authentication details or content types.

Examples:

- Authorization: Bearer <token>
- Content-Type: application/json

![Dashboard Hub headers](/cms_trial/assets/742436bd-6246-4808-bcdb-4045c81371f8.png)