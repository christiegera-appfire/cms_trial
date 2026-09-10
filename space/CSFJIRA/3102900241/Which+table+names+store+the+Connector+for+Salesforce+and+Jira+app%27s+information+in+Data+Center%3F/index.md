# Which table names store the Connector for Salesforce and Jira app's information in Data Center?

## Purpose

At times, it is beneficial to identify the specific tables that house the connector's data and the location where the associations are stored. This article is to answer the question, "Which are the table names that store the Connector's information?"

## Answer

Your Connector data is stored in these three tables:

- `entity_property`
- `AO_142EFA_CONNECTION_AO`
- `AO_142EFA_BINDING_AO`

The Connector's associations are stored within the `entity_property` table. You can access this information with the following SQL command:

```text
select concat(jp.pkey, '-', ji.issuenum) as PKEY, ep.entity_id, jp.pkey, ji.issuenum, ep.property_key, ep.json_value
from project jp, jiraissue ji, entity_property ep
where jp.id = ji.project
and ep.entity_id = ji.id
and ep.property_key = 'com.servicerocket.jira.cloud.issue.salesforce.associations'
order by jp.pkey, ji.issuenum;
```

Here's an example of what your results will look like:

```text
 pkey  | entity_id | pkey | issuenum |                        property_key                        |                                                                     json_value                                                                      
-------+-----------+------+----------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------
 TAB-1 |     10000 | TAB  |        1 | com.servicerocket.jira.cloud.issue.salesforce.associations | {"associations":{"5004x00000i3Wu9AAE":{"son":"Case","viewOnly":false,"autoPush":true,"autoPull":true}},"ids":"5004x00000i3Wu9AAE","types":"Case"}
 TAB-2 |     10001 | TAB  |        2 | com.servicerocket.jira.cloud.issue.salesforce.associations | {"associations":{"5004x00000i3WvVAAU":{"son":"Case","viewOnly":false,"autoPush":false,"autoPull":false}},"ids":"5004x00000i3WvVAAU","types":"Case"}
 TAB-3 |     10002 | TAB  |        3 | com.servicerocket.jira.cloud.issue.salesforce.associations | {"associations":{"5004x00000i3WZMAA2":{"son":"Case","viewOnly":false,"autoPush":false,"autoPull":false}},"ids":"5004x00000i3WZMAA2","types":"Case"}
```