# Third-Party app support

The Rich Filters for Jira Dashboards app supports custom fields introduced by certain Jira apps that are available on the Atlassian Marketplace. The table below lists these third-party apps and describes their integration.

### Integration notice

The integration with these third-party apps is provided on a best-effort basis. We cannot guarantee that the integration will continue to function properly when the apps are modified by their editors.

| **Vendor** | **Jira App** | **Integration description** |
| --- | --- | --- |
| codecentric AG | Issue Picker for Jira | Custom fields of type *Issue Picker*can be used:   - as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets; - as *Statistic type* in the statistics and flexi charts gadgets; - as a [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/). |
| STAGIL | STAGIL Traffic Lights | Custom fields of type *STAGIL Traffic Light* can be used:   - as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets; - as *Statistic type* in the statistics and flexi charts gadgets; - as a [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/). |
| Tempo Software | Timesheets by Tempo - Jira Time Tracking | The custom fields *Account* and *Tempo Team* can be used:   - as column in [views](/cms_trial/space/RFCDOC/783941729/Configure+views/), to be displayed in [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadgets; - as *Statistic type* in the statistics and flexi charts gadgets; - as a [dynamic filter](/cms_trial/space/RFCDOC/783941707/Configure+dynamic+filters/).   Moreover, the following sub-fields can be used as *Statistic types*:   - *Account category* - *Account Category type* - *Account Customer* |
| Sourcesense | Multi-Level Cascading Select | Rich Filters supports custom fields created with [Multi-Level Cascading Select](https://marketplace.atlassian.com/apps/5008/multi-level-cascading-select?hosting=datacenter&tab=overview) in **Dynamic filters**. |
| Appfire | Jira Misc Custom Fields | Rich Filters supports custom fields created with [Jira Misc Custom Fields](https://marketplace.atlassian.com/apps/27136/jira-misc-custom-fields-jmcf?hosting=cloud&tab=overview):   - **Dynamic filters** - Filter issues dynamically with JMCF fields - **Statistics and charts** - Use JMCF fields as a statistic type to enhance reporting capabilities - **Views** - Display JMCF fields as columns in Rich Filter Results gadgets   In the [JMCF fields support](/cms_trial/space/RFCDOC/783942998/Third-Party+app+support/) table, you can find detailed fields that are supported for dynamic filters and statistic values. |

## JMCF fields support

| **JMCF field** | **Type** | **Column in views** | **Dynamic filter** | **Statistic type** | **Statistic value** |
| --- | --- | --- | --- | --- | --- |
| Last Field Change Time | datetime | ✅ | ✅ | ✅ | ❌ |
| Last field changed by user | user | ✅ | ✅ | ✅ | ❌ |
| Parent status | string | ✅ | ✅ | ✅ | ❌ |
| Status entered time | datetime | ✅ | ✅ | ✅ | ❌ |
| Status entered by user | user | ✅ | ✅ | ✅ | ❌ |
| Transition time | datetime | ✅ | ✅ | ✅ | ❌ |
| Transitioned by user | user | ✅ | ✅ | ✅ | ❌ |
| Transitioned by users | user | ✅ | ✅ | ❌ | ❌ |
| Transition count | number | ✅ | ✅ | ✅ | ✅ |
| Time in status | duration | ✅ | ❌ | ❌ | ❌ |
| Time in status table | duration | ✅ | ❌ | ❌ | ❌ |
| Scripted string | string | ✅ | ✅ | ✅ | ❌ |
| Scripted date | date | ✅ | ✅ | ✅ | ❌ |
| Scripted datetime | datetime | ✅ | ✅ | ✅ | ❌ |
| Scripted number | number | ✅ | ✅ | ✅ | ✅ |
| Scripted user | user | ✅ | ✅ | ✅ | ❌ |
| Scripted group | group | ✅ | ✅ | ✅ | ❌ |
| Scripted string collection | string | ✅ | ✅ | ❌ | ❌ |
| Scripted user collection | user | ✅ | ✅ | ❌ | ❌ |
| Scripted group collection | group | ✅ | ✅ | ❌ | ❌ |
| Scripted duration | duration | ✅ | ❌ | ❌ | ❌ |