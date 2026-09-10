# Extension Conversion Mapping

When migrating from **JMWE for Jira Data Center** to **JMWE for Jira Cloud**, some Server extensions will be converted to native Jira Cloud extensions. The native Cloud extensions provide the same base functionality as the **JMWE Data Center** extensions, but do not include scripting support (for [**Conditional Execution**](/cms_trial/space/JMWEC/466256678/Conditional+Execution/), for example). It is possible that you could use a JMWE Cloud extension to achieve the same results, but during migration, JMWE Data Center extensions *will always be converted* to the listed Jira Cloud extensions.

Any **JMWE for Jira Data Center** extensions not listed in the table below will convert to their equivalent **JMWE for Jira Cloud** extensions.

Below is a list of extensions that are converted to native Jira extensions when migrating from **Jira Data Center** to **Jira Cloud**.

**Note:** Conversion of the listed extensions below is applicable to migrations using both [Jira Cloud Migration Assistant (JCMA)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458555803) and [Configuration Manager for Jira (CMJ)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/501219431).

| **Extension Type** | **Extension Name (Data Center)** | **Extension Name (Cloud)** |
| --- | --- | --- |
| Post-function | [Set issue security level based on current user’s project role (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458523134)  [Unmapped block: nestedExpand] | Set issue security level based on user’s project role  [Unmapped block: nestedExpand] |
| Condition | [Hide Transition (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458786763)  [Unmapped block: nestedExpand] | Hide From User Condition  [Unmapped block: nestedExpand] |
| Condition | [Previous Status Condition (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458687483)  [Unmapped block: nestedExpand] | Previous Status Condition  [Unmapped block: nestedExpand] |
| Condition | [Separation of Duties Condition (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458687543)  [Unmapped block: nestedExpand] | Separation of Duties condition  [Unmapped block: nestedExpand] |
| Validator | [Comment Required Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458687654)  [Unmapped block: nestedExpand] | Field has been modified Validator  [Unmapped block: nestedExpand] |
| Validator | [Field has been modified Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458163792)  [Unmapped block: nestedExpand] | Field has been modified Validator  [Unmapped block: nestedExpand] |
| Validator | [Field has single value Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458588733)  [Unmapped block: nestedExpand] | Field has single value Validator  [Unmapped block: nestedExpand] |
| Validator | [Fields Required Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458687582)  [Unmapped block: nestedExpand] | Field Required Validator  [Unmapped block: nestedExpand] |
| Validator | [Parent Status Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458523182)  [Unmapped block: nestedExpand] | Parent Status Validator  [Unmapped block: nestedExpand] |
| Validator | [Previous Status Validator (JMWE app)](https://appfire.atlassian.net/wiki/spaces/JMWES/pages/458818047)  [Unmapped block: nestedExpand] | Previous State Validator  [Unmapped block: nestedExpand] |