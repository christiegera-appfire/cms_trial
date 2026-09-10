# Power Scripts for Jira Cloud vs DC/Server functionality

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

## Overview

|  |  |  |  |
| --- | --- | --- | --- |
| **Feature** | **Server** | **Cloud** | **Notes** |
| Event Listeners | ✅ | ✅ |  |
| External Database Integration | ✅ | ✅ |  |
| Jira Agile Support | ✅ | ✅ | 🆕 - Support added 10/2023 |
| Jira Portfolio (Roadmaps) Support | ✅ | ℹ️ | Indirect support via REST is available. |
| Jira Service Desk Support | ✅ | ✅ | 🆕 - Support added 10/2023 |
| JQL Functions | ✅ | ✅ |  |
| JSD | ✅ | ✅ | Support added in Q4 2023 and Q1 2024 |
| Live Fields (Screens) | ✅ | ✅ | Currently in development. Expected release in November 2024. |
| Mail Handler | ✅ | ✅ | Added Q2 2024 |
| Remote LDAP Integration | ✅ | ✅ |  |
| Remote Systems | ✅ | ✅ |  |
| REST Service | ✅ | ✅ |  |
| Scheduled Services | ✅ | ✅ |  |
| Script Gadget | ✅ | ✅ |  |
| SIL Panel | ✅ | ✅ |  |
| SIL Template Language | ✅ | ✅ |  |
| Slack Support | ✅ | ✅ |  |
| Start/Stop Scripts | ✅ | [minus icon] | This functionality is not relevant in Cloud. |
| Switch User | ✅ | [minus icon] | This functionality is not permitted in Cloud. |
| Version Control | ✅ | ✅ |  |
| Webhooks | ✅ | ✅ |  |
| Workflow Viewer | ✅ | [minus icon] |  |
| Workflows Conditions/ Validators | ✅ | ✅\* | Available to the extent allowed by Cloud limitations. |
| Workflows Post Functions | ✅ | ✅ |  |

## JQL Keywords vs JQL Functions

A JQL **function** performs an evaluation of the issue in real-time during the JQL search. This search type is not possible in Jira Cloud because it is a very resource-intensive search.

A JQL **keyword** is meta-data for an issue that has been evaluated and saved prior to a JQL search. This search type is available in Jira Cloud. It is faster and more efficient than a traditional, functional search because the results can be indexed and it is less resource intensive.

## Live Fields (screen manipulation)

The solution is currently in development. It will be available soon with limited support and to the extent allowed by Cloud limitations.

## Conditions/Validators

The only solution available for custom workflow conditions and validators is through the Atlassian Expressions language which has limited functionality compared to SIL.

## Function Availability

No Cloud API support is available for all functions in Server. Some functions are currently in development and will soon be available in Cloud. The actions for the unavailable functions are still supported using the REST API.