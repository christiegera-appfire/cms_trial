# Difference between Advanced Tables for Confluence Data Center and cloud version

## Why migrate to the Cloud?

The Advanced Table for Confluence, hosted on the cloud, is the future of Advanced Tables. The Cloud version is where active development is happening.

- On cloud, you get access to the **Advanced Table Viewer macro** – a new macro exclusive to the cloud, which represents the next generation of Advanced Tables functionality.
- The Advanced Table Viewer macro currently supports CSV, Excel, and JSON data sources. Support for Jira work items will be released soon.
- The Advanced Table Viewer macro provides an intuitive and responsive user interface.
- All core macros, Table Plus, CSV, JSON Table, and Attachment Table are supported except JQL Table.

| **Macro/Features** | **Cloud** | **Data Center** |
| --- | --- | --- |
| Advanced Table Viewer macro | ✅ | ❌ |
| Table Plus macro | ✅ | ✅ |
| CSV (Comma Separated values) macro | ✅ | ✅ |
| JSON Table macro | ✅ | ✅ |
| Attachment Table macro | ✅ | ✅ |
| JQL Table macro | ❌ | ✅ |
| Custom macro editor | ✅ | ✅ |
| New feature development | ✅ | ❌ |
| One macro for different data sources (Advanced Table Viewer macro currently supports CSV, Excel, and JSON data sources, and support for Jira work items will be released soon.) | ✅ | ❌ |

All parameters function the same in both Cloud and Data Center, except for a few, as listed in [Differences between the Data Center and cloud versions](#).

## What will be different?

This page describes what you need to consider:

- When migrating from Confluence Data Center (DC) to Cloud, and you are using the Advanced Tables for Confluence app on pages in your instance.

The macros involved are:

- [Advanced Table Viewer macro](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/)
- [Table Plus macro](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74812918)
- [CSV Table macro](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74813743)
- [JSON Table macro](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74813238)
- [JQL Table macro](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74811686)
- [Attachment Table macro](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74813451)

## Differences between the cloud and Data Center versions

The key differences in behavior are:

- Macros render in the background in the cloud version and then appear as the data becomes available.
- The performance of the macro rendering in the cloud version is mostly dependent on the performance of the user's client machine, as a majority of the processing is now done using the browser's JavaScript engine. The loading time is dependent on client JavaScript speed (some browsers can be better than others) and network connections.
- There can be differences in behavior when interacting with other page elements or macros. The Atlassian Confluence development team continues to improve the macro integration and interactions.
- There are some known issues and incompatibilities.

If your pages use macros nested inside other macros, these will need a small adjustment before migrating. Flattening your page layouts before migration ensures everything migrates smoothly to Confluence Cloud. Since the nested macros are not supported in the cloud version.

The following table lists the macro parameters and features that work differently in the cloud and the Data Center:

Last updated February 3, 2026

 ✅ – Available | ❌ – Unavailable | ⚠️ – Partially available

| **Categories** | **Feature/Parameter** | **Cloud** | **Data Center** | **Notes** |
| --- | --- | --- | --- | --- |
| Visual styling | Full screen view (Advanced Table Viewer macro) | ✅ | ❌ | The Advanced Table Viewer macro provides full screen view. |
|  | Using customized CSS for tables in macros | ⚠️ | ✅ | The Advanced Table Viewer macro includes a row styling feature that lets you apply custom styles to table headers and rows using a simple, intuitive interface.  Other cloud macros do not support this feature |
| Core functionality | Upload file (CSV, Excel, and JSON) | ✅ | ❌ | The Advanced Table Viewer macro lets you upload a CSV, Excel and JSON file. |
| Display data filter for each column | ✅  Flexibility to apply a data filter to the required column. | ✅  By default, the data filter is applied to all columns. | The Advanced Table Viewer macro provides the flexibility to apply a data filter only to the required column. |
| Preview in the macro editor | ⚠️ | ✅ | The Advanced Table Viewer macro provides a preview in the macro editor  For more information, refer to [CE-13](https://ecosystem.atlassian.net/browse/CE-13). |
| URL whitelisting | ❌ | ✅  Supported natively by Confluence and configured using the [Global Configuration](https://appfire.atlassian.net/wiki/x/qp51B) page | For more information, refer to [CLOUD-2636](https://jira.atlassian.com/browse/CLOUD-2636?_ga=2.132608974.1394606258.1569218293-232908448.1565943714). |
| Sorting inline tasks in macros | ❌ | ✅ | For more information, refer to [CONF-45450](https://jira.atlassian.com/browse/CONF-45450). |
| Export to PDF or Word | ❌ | ✅ | Due to certain technical issues, the app does not support this feature in the cloud. |
| Integrations | Interoperability between macros | ❌ | ✅ | Confluence Cloud does not support this. For more information, refer to [CONFCLOUD-41551](https://jira.atlassian.com/browse/CONFCLOUD-41551). |
| *Anchor* macros within *Advanced Tables* macros | ❌ | ✅ | Confluence Cloud does not support this. For more information, refer to [CE-886](https://ecosystem.atlassian.net/browse/CE-886). |
| *Excerpt include* macro in *Advanced Tables* macros | ❌ | ✅ | Confluence Cloud does not support this. For more information, refer to [CE-876](https://ecosystem.atlassian.net/browse/CE-876). |
| *Jira Issue/Filter* macro in *Advanced Tables* macros | ❌ | ✅ | Due to certain technical issues, the app does not support this feature in the cloud. For more information, refer to [CE-1047](https://ecosystem.atlassian.net/browse/CE-1047). |
| *Page Properties Report* macro in the *Advanced Tables* macros | ❌ | ✅ | Due to certain technical issues, the app does not support this feature in the cloud. |

Please note that all the other parameters function the same in both versions of the app.

## Related article

[Atlassian's Confluence migration instructions](https://confluence.atlassian.com/confcloud/migrate-from-confluence-server-to-cloud-724765529.html)

## Problem reporting

If you experience any unexpected problems or behavior changes, [create a support request](https://appf.re/support). This helps us identify and prioritize fixes and improvements.