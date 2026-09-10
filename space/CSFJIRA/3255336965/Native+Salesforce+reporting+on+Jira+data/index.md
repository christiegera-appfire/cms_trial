# Native Salesforce reporting on Jira data

**Connector for Salesforce & Jira | Sales Enablement**

---

**Connector for Salesforce & Jira syncs live Jira field values into native Salesforce custom fields.** Once the data lives in Salesforce, teams build aging reports, bottleneck dashboards, and SLA tracking using standard Report Builder.

**20**

minute  
setup

**10**

fields  
mapped

**0**

Jira licenses  
needed for Salesforce users

**Live sync**

on every Jira update

This guide walks you through how to bring Jira work items data into Salesforce using Connector for Salesforce & Jira. Once the data is there, you can build reports and dashboards with the standard Salesforce Report Builder, no additional tools or Jira licenses required.

By the end, you’ll have a working dashboard that shows work item status, aging, assignee workload, and stale item alerts, all from native Salesforce fields on the Case object types.

---

## Dashboard

The IT Responsiveness Tracker dashboard is a Salesforce dashboard built from five reports that use Jira work item data synced via Connector for Salesforce & Jira. It includes four KPI cards (total, blocked, resolved, and stale work items counts), a status donut chart, a stale work items table, a work item aging bar chart grouped by assignee, and an aging detail table. The data lives in custom fields on the Case object that update automatically when Jira changes. Salesforce users don’t need Jira licenses to see or interact with it.

The data tells a clear story: three High-priority, dealer-facing work items have been Blocked for 28–42 days with no recent activity. Workload skews heavily toward a few engineers, and four work items have gone stale with no Jira updates in over a week. Managers can see exactly which work items are stuck, who owns them, and how long they’ve been waiting, all without leaving Salesforce or sending a single follow-up email.

![image-20260610-074359.png](/cms_trial/assets/1f713604-bd3c-4836-ab31-2e73b1bf7b13.png)

## Reports

Reports feed the dashboard. Each report needs a Group By field to unlock chart widgets.

| **Report** | **Group By** | **Key Filter** | **Dashboard Widget** |
| --- | --- | --- | --- |
| Items by Jira Status | Jira Status | Issue Key not blank | Metric (total count) + Donut chart |
| Blocked Jira Work Items | Jira Status | Status = Blocked | Metric (blocked count) |
| Resolved Jira Work Items | Jira Status | Status = Done | Metric (resolved count) |
| Stale Jira Work Items | Jira Status | Last Updated > 7 days ago, Status ≠ Done | Metric (stale count) + Table |
| Jira Work Items Aging | Jira Assignee | Issue Key not blank | Horizontal bar chart + Table |
| Engineers Assigned to Work Items | Jira Assignee | Status ≠ Done | Horizontal bar chart + Table*)* |
| Every report must use **Add Group** in the *Outline* panel to enable Summary format. Without this, chart and metric widget types won't be available on the dashboard. |

All reports are built with standard Salesforce Report Builder. Data lives in native Salesforce custom fields. It works with every report, dashboard, and flow your team already uses.

BOTTLENECK

#### Work item aging

Group by Status, sort by work item age descending. Shows which work items have been sitting the longest.

ACCOUNTABILITY

#### Response time by assignee

Group by assignee, measure average work item age. Shows who is carrying the most aged work.

PAPER TRAIL

#### Stale work item alert

Filter: Last Updated older than 7 days, Status not Done. Flags work items with no recent Jira activity.

EXECUTIVE

#### SLA compliance

Compare Target End Date vs. today. Chart % on-time vs. overdue by team, project, or priority.

---

## Data

## **Jira → Connector Sync → Salesforce Custom Fields**

Every status change, comment, or field update in Jira flows into native Salesforce fields using automated field mapping and Auto Push. There are no manual steps once configured.

![image-20260515-203052.png](/cms_trial/assets/05de8342-74fc-4eeb-b276-4ff6c5627abe.png)

![image-20260514-162715.png](/cms_trial/assets/ce149a5d-29eb-484a-8513-c59e2100873d.png)

![image-20260514-162725.png](/cms_trial/assets/fe77f137-c7a4-4ab2-8090-a946326f8eff.png)

Comments sync separately from field mappings. When comment synchronization is enabled in the Connection settings, Jira comments appear as Case Comments on the linked Salesforce Case. Each comment includes the author name and timestamp. This is automatic, and no custom field is needed.

To report on comment activity, use the `Jira_Last_Updated__c` field as a proxy. Any new Jira comment triggers an update to this timestamp, so a “Stale work item” filter (Last Updated older than 7 days) catches work items with no recent comments, status changes, or other Jira activity.

**Reference**

- [Work with comments](https://support.appfire.com/space/477986818/2560559505/Work+with+comments)
- [View Jira comments in Salesforce](https://support.appfire.com/space/477986818/2560559636/View+Jira+comments+in+Salesforce)
- [Filter Jira comments in Salesforce](https://support.appfire.com/space/477986818/2560919017/Filter+Jira+comments+in+Salesforce+Cases)

---

## Setup

[Unmapped macro: refined-stepper-item — no content to fall back on]

In Salesforce, add the Jira fields to the Case object. Add them to the page layout.

**Reference**

- [Create Custom Fields](https://help.salesforce.com/s/articleView?id=platform.adding_fields.htm&type=5&language=en_US)
- [Customize Page Layouts](https://help.salesforce.com/s/articleView?id=sfdo.ssh_setup_contact_case_layouts.htm&language=en_US&type=5)

[Unmapped macro: refined-stepper-item — no content to fall back on]

In Jira, open your Connector binding. Add a field mapping for each Jira field to its Salesforce custom field. Configure value mappings for picklists.

**Reference**

- [Configure entity, field and value mappings](https://support.appfire.com/space/477986818/2560917994/Configure+entity,+field+and+value+mappings)
- [Jira field type to Salesforce field type compatibility](https://support.appfire.com/space/477986818/2560918568/Jira+field+type+to+Salesforce+field+type+compatibility)
- [Import value mappings](https://support.appfire.com/space/477986818/2560918414/Import+value+mappings) (for picklists like Status, Resolution, Priority)

[Unmapped macro: refined-stepper-item — no content to fall back on]

Turn on Auto Pull in the Connection settings and deploy the Apex trigger. Jira updates sync into Salesforce automatically.

**Reference**

- [Configure automatic pull from Salesforce](https://support.appfire.com/space/477986818/2560919837/Configure+automatic+pull+from+Salesforce)
- [Configure workflow post functions in Jira](https://support.appfire.com/space/477986818/2560919948/Configure+workflow+post+functions+in+Jira)
- [Configure automatic Jira issue creation from Salesforce](https://support.appfire.com/space/477986818/2560920216/Configure+automatic+Jira+issue+creation+from+Salesforce)

[Unmapped macro: refined-stepper-item — no content to fall back on]

Create reports in Salesforce Report Builder. Group by Status or Assignee to unlock chart widgets on dashboards.

**Reference**

- [Build a Report](https://help.salesforce.com/s/articleView?id=analytics.rd_reports_build.htm&language=en_US&type=5)
- [Group Your Report Data](https://help.salesforce.com/s/articleView?id=analytics.reports_builder_fields_groupings.htm&language=en_US&type=5)

[Unmapped macro: refined-stepper-item — no content to fall back on]

Add KPI metrics, donut chart, assignee bar chart, and aging table to a single dashboard view.

**Reference**

- [Create a Dashboard](https://help.salesforce.com/s/articleView?id=analytics.dashboards_create_lex.htm&language=en_US&type=5)
- [Add Dashboard Components](https://help.salesforce.com/s/articleView?id=analytics.bi_dashboard_components_create.htm&language=en_US&type=5)

[Unmapped macro: refined-stepper-item — no content to fall back on]

- [Subscribe to Dashboards](https://help.salesforce.com/s/articleView?id=analytics.dashboards_subscribe_lex.htm&language=en_US&type=5)
- [Subscribe to Reports](https://help.salesforce.com/s/articleView?id=analytics.reports_subscribe_overview.htm&language=en_US&type=5)

**Video reference**

---

## Reference

### Field mapping reference

Create the following custom fields on the Salesforce Case object, then map each one in the Connector's binding configuration in Jira.

| **Jira field** | **Sync** | **Salesforce field** | **Data type** |
| --- | --- | --- | --- |
| Status | → | `Jira_Status__c` | Picklist |
| Resolution | ↔ | `Jira_Resolution__c` | Picklist |
| Priority | ↔ | `Jira_Priority__c` | Picklist |
| Updated | → | `Jira_Last_Updated__c` | Date/Time |
| Issue Key | → | `Jira_Issue_Key__c` | Text |
| Summary | ↔ | `Jira_Summary__c` | Long Text |
| Assignee | → | `Jira_Assignee__c` | Text |
| Created | → | `Jira_Created_Date__c` | Date/Time |
| Due Date | ↔ | `Jira_Target_End_Date__c` | Date |

**Work item Age formula:** Add one more field - `Jira_work item_Age__c` (Formula, Number): `TODAY() - DATEVALUE(Jira_Created_Date__c)`. This field provides a real-time aging metric to sort, filter, and chart.

---

## FAQ

[Unmapped macro: refined-tab — no content to fall back on]

No. Data lives in native custom fields. Sortable, filterable, chartable in any standard Salesforce report.

[Unmapped macro: refined-tab — no content to fall back on]

No. They see Jira data in native fields. They never need to open Jira.

[Unmapped macro: refined-tab — no content to fall back on]

Near real-time. Syncs on every Jira status change, comment, or field update.

[Unmapped macro: refined-tab — no content to fall back on]

Yes, using standard Salesforce report subscriptions, scheduled for daily or weekly delivery.