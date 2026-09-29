# Mapping templates reference

Each template comes with ready entity and field mappings. This page lists the mappings included in each of the five templates:

- Bug escalation
- Feature requests
- Deal enablement
- Deal & feature sync
- Support requests

For instructions on applying a template, see [Configure entity and field mappings from templates](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/) :

## Bug escalation

Tracks unresolved bugs and brings cases from Salesforce to your engineering team in Jira. The template maps the Jira Bug work item type to the Salesforce Case object type.

| **Jira work item type** | **Salesforce object type** |
| --- | --- |
| Bug | Case |

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Subject |
| Status | ← → Bidirectional | Status |
| Priority | ← → Bidirectional | Priority |
| Decription | ← → Bidirectional | Description |

![image-20260929-111215.png](/cms_trial/assets/3a84a2dc-20f9-4ff0-8659-5e3fc15dce48.png)

## **Feature requests**

Sends customer feature requests from Salesforce into Jira and tracks them as they move through development in both platforms. The template maps Jira Story work item type to Salesforce Case object type.

| **Jira work item type** | **Salesforce object type** |
| --- | --- |
| Story | Case |

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Subject |
| Description | ← → Bidirectional | Description |
| Priority | ← → Bidirectional | Priority |
| Status | ← → Bidirectional | Status |

![image-20260929-111427.png](/cms_trial/assets/be2ec6a5-c717-4812-af95-50db27770c6e.png)

## **Deal enablement**

Connects Salesforce opportunities to Jira work items. The template maps the Jira Epic work item type to the Salesforce Opportunity object type.

| **Jira work item type** | **Salesforce object type** |
| --- | --- |
| Epic | Opportunity |

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Name |
| Description | ← → Bidirectional | Description |

![image-20260929-111805.png](/cms_trial/assets/7ad43834-fa24-4a7c-8ef5-de83ca36a081.png)

## **Deal & feature sync**

Brings sales, product, and engineering into one workflow by sending Salesforce opportunities and customer requests to Jira, so every team stays aligned. The template maps the Jira Epic work item type to the Salesforce Opportunity object type, Jira Story and Bug work item types to the Salesforce Case object type.

| **Jira work item type** | **Salesforce object type** |
| --- | --- |
| Epic | Opportunity |
| Story | Case |
| Bug | Case |

**Epic** → **Opportunity**

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Name |
| Description | ← → Bidirectional | Description |

**Story** → **Case** and **Bug** → **Case**

Both entity mappings use the same field mappings.

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Subject |
| Description | ← → Bidirectional | Description |
| Priority | ← → Bidirectional | Priority |
| Status | ← → Bidirectional | Status |

## **Support requests**

The support requests template converts customer-reported issues into Jira Service Management (JSM) incidents or change requests. The template maps Jira (System) Incident and (System) Change work item types to Salesforce Case object type. The template works only with JSM Premium spaces.

| **Jira work item type** | **Salesforce object type** |
| --- | --- |
| Incident | Case |
| Change | Case |

**Incident** → **Case** and **Change** → **Case**

Both entity mappings use the same field mappings.

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Subject |
| Description | ← → Bidirectional | Description |
| Priority | ← → Bidirectional | Priority |