# Issue Type & IT Screen Scheme Administration Functions

This section contains functions that enable users to handle issue type administration.

## Functions Summary

- [admAddIssueTypeToScheme](/cms_trial/space/PSJC/986120241/admAddIssueTypeToScheme/)
- [admAppendITSSMapping](/cms_trial/space/PSJC/806158387/admAppendITSSMapping/)
- [admAssignITSSToProject](/cms_trial/space/PSJC/805667045/admAssignITSSToProject/)
- [admCreateIssueTypeScheme](/cms_trial/space/PSJC/986218517/admCreateIssueTypeScheme/)
- [admDeleteIssueTypeScheme](/cms_trial/space/PSJC/985989163/admDeleteIssueTypeScheme/)
- [admGetAllIssueTypeSchemes](/cms_trial/space/PSJC/514786551/admGetAllIssueTypeSchemes/)
- [admGetAllIssueTypeScreenSchemes](/cms_trial/space/PSJC/518324501/admGetAllIssueTypeScreenSchemes/)
- [admGetIssueTypeScheme](/cms_trial/space/PSJC/515211665/admGetIssueTypeScheme/)
- [admGetIssueTypeSchemeForProject](/cms_trial/space/PSJC/985989182/admGetIssueTypeSchemeForProject/)
- [admGetIssueTypeScreenScheme](/cms_trial/space/PSJC/518291809/admGetIssueTypeScreenScheme/)
- [admGetIssueTypesFromScheme](/cms_trial/space/PSJC/985727038/admGetIssueTypesFromScheme/)
- [admGetITSSMappings](/cms_trial/space/PSJC/805961911/admGetITSSMappings/)
- [admGetITSSProjects](/cms_trial/space/PSJC/806158401/admGetITSSProjects/)
- [admRemoveIssueTypeFromScheme](/cms_trial/space/PSJC/985956387/admRemoveIssueTypeFromScheme/)
- [admRemoveITSSMapping](/cms_trial/space/PSJC/806322241/admRemoveITSSMapping/)
- [admSetIssueTypeScheme](/cms_trial/space/PSJC/986382403/admSetIssueTypeScheme/)
- [admUpdateIssueTypeScheme](/cms_trial/space/PSJC/985923668/admUpdateIssueTypeScheme/)
- [admUpdateIssueTypeScreenScheme](/cms_trial/space/PSJC/806125616/admUpdateIssueTypeScreenScheme/)

Structures used:

### JIssueTypeScheme

```text
int id;
string name;
string description;
int defaultIssueTypeId; //the default issue type
```

### JIssueTypeScreenScheme

```text
int id;
string name;
string description;
```

### JIssueTypeScreenMapping

```text
int issueTypeId;
int screenSchemeId;
```