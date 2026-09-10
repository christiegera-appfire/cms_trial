# API 2.1 Migration FAQ

API v2.1 was deprecated more than four years ago (see [API Important Information](https://appfire.atlassian.net/wiki/x/j4C3Sg)) and now, the process of finally retiring it is ongoing. Once this API v2.1 is retired, you can no longer obtain data via this version.

This article provides answers to the questions you may have and provides guidance with the migration process to the updated and supported API versions.

## Why is 7pace retiring API v2.1?

Software is constantly evolving and so are its APIs. The TimeExport endpoint found in API v2.1 does not support pagination and includes all attributes in the response by default. This makes the API less than effective, which leads to occasional performance issues.

7pace provides more recent APIs that can provide the same data, but in an optimized way.

## When will API v2.1 be shut down?

API v2.1 has been retired - stopped serving requests - on **1st December, 2023**. Optional prolongation period of limited length (several months) can be requested by an e-mail sent to [support@7pace.com](mailto:support@7pace.com).

## How can I tell if I am sending API v2.1 requests?

The API endpoint and version are a part of URL that your application calls, and can be seen in the example below.

`https://yourcompany.timehub.7pace.com/api/odata/TimeExport(StartDate='2019-06-14',EndDate='2023-06-14',PopulateTopParentColumns=null,GroupTimeByDateByUser=null,IncludeBillable=null)?api-version=2.1`

## What API should I use as replacement?

The safest way is to use the newest stable version of the API that is listed in our [API documentation](https://appfire.atlassian.net/wiki/x/j4C3Sg). Currently (Q3/2022) it is 3.2.

Note that the *TimeExport* endpoint no longer exists in the new APIs, you will therefore have to call different endpoints with a different structure of requests. We recommend reading the following documentation:

- [Reporting API v3 - user guide](https://appfire.atlassian.net/wiki/x/qoG3Sg)
- [API reference documentation](https://timehub.7pace.com/apireference/?urls.primaryName=7pace%20Timetracker%20API%20documentation%20v3.1)
- [Incremental refresh guide](https://appfire.atlassian.net/wiki/x/Q4C3Sg)

Choosing a specific endpoint of API v3.2 depends on your needs. The most frequent cases are listed below; the rest of the endpoints are described in the mentioned user guides.

- `workLogsOnly`endpoint is the most effective if you only need to obtain worklogs.
- Choose `workLogsWorkItems`endpoint if you also need to obtain workitems (and, optionally, information about their parent item).

## Will API v2.1 be shut down for on-prem too?

If you run Azure DevOps and Timetracker on your own servers, you can continue using API v2.1. However, there is no guarantee that future versions of Timetracker will work with this API properly, and, troubleshooting support and bug fixing for API v2.1 are not available.

## What are the differences?

|  |  |  |
| --- | --- | --- |
| **API version 2.1** | **API version 3.0 and higher** | **Comment** |
| Limited filtering (start date, end date, flags) | Advanced filtering of records (by any attribute) | We recommend obtaining only updated records for a certain time period using filtering by EditedTimestamp - see [Incremental refresh guide](https://appfire.atlassian.net/wiki/x/Q4C3Sg). |
| Not paginated | Paginated | Pagination is handled via `@odata.nextLink` property.  Certain tools like Excel or Power BI handle the pagination automatically. You have to choose **Odata feed** as data source. |
| API version in parameters Example: `?api-version=2.1` | API version in the base URL Example: [https://url.timehub.7pace.com/api/odata/v3.2/](https://time-plutus.timehub.7pace.com/api/odata/v3.1/workLogsWorkItems?$filter=EditedTimestamp%20ge%202018-01-01T00%3A00%3A00%2B01%3A00%20and%20EditedTimestamp%20lt%202022-06-08T00%3A00%3A00%2B02%3A00&$expand=ParentItem%28%24select%3DSystem_Id%29&$top=1000) |  |
| Returns all object attributes (properties) by default | Explicit selection of attributes is enforced due to a newer OData standard | See the [respective documentation](https://support.7pace.com/hc/en-us/articles/360053657211). |
| Single `TimeExport` endpoint to rule them all | Multiple endpoints suited for different use cases | See the preceding sections for more information about endpoints. |